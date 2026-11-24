-- Render each distinct named note once.
--
-- Pandoc expands every reference to a named footnote into a separate Note
-- element, so a key used three times becomes three printed notes. This filter
-- keeps the first Note and replaces later copies with a link back to it.
-- Note content is used as the identity because the named key is not retained
-- in the AST after parsing. Keep note bodies distinct: two different keys with
-- identical bodies in different chapters would be merged. The Chapters 36 and
-- 37 editorial notes were made chapter-specific for this reason.

local seen = {}

function Note(el)
  local key = pandoc.write(pandoc.Pandoc(el.content), "markdown")
  local number = seen[key]
  if number == nil then
    number = #seen + 1
    seen[key] = number
    return nil
  end
  local link = pandoc.Link({ pandoc.Str(tostring(number)) }, "#fn" .. number)
  return pandoc.Span({ link }, { class = "footnote-ref" })
end
