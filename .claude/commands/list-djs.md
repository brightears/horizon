---
description: List all DJs in the roster with their venue assignments
allowed-tools: Read, Glob, Grep
context: fork
model: claude-3-5-haiku-20241022
---

List all DJs currently in the roster.

## Instructions

1. Find all DJ profile files in `djs/profiles/` (exclude _TEMPLATE.md)
2. For each DJ, extract:
   - Stage name
   - Music genres
   - Schedule (if assigned)
3. Present as a summary table:

### Horizon DJs
| DJ | Genres | Schedule |
|---|---|---|
