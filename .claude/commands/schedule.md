---
description: Create or view monthly DJ schedule
allowed-tools: Read, Write, Edit, Glob
argument-hint: [month] [action]
---

Work on the DJ schedule for: $1 (e.g., "2026-02")
Action: $2 (view/create/edit, default: view)

## Schedule Requirements

**Daily slot to fill:**
- Horizon 18:30-22:30 (1 DJ, 4 hours)

**Total:** 1 DJ slot per day, 7 days/week = 7 slots/week

## Rules
- Match DJ genres to venue requirements (see CLAUDE.md)
- Check DJ availability notes in profiles
- Consider DJ preferences
- Balance workload across DJs

## Schedule Format
```
| Date | Day | Horizon DJ (18:30-22:30) |
|------|-----|--------------------------|
| 2026-02-01 | Sun | DJ Name |
```

## File Location
`schedules/[month]/schedule.md`
