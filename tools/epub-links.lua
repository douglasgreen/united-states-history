-- Strip parent-relative repository links from EPUB output.
--
-- The manuscript uses links such as [README](../README.md),
-- [AGENTS](../AGENTS.md), and [Chapter 1](../chapters/01-chapter-1.md)
-- for editorial navigation. Those targets are not part of the EPUB
-- package, and EPUBCheck correctly reports them as missing resources.
-- Keep the visible label and remove the link wrapper for EPUB only.

function Link(el)
  if el.target:match("^%.%./") then
    return el.content
  end
  return nil
end
