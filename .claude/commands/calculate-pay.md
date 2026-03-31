---
description: Calculate DJ payments for a period
allowed-tools: Read, Write, Glob
argument-hint: [month]
context: fork
model: claude-3-5-haiku-20241022
---

Calculate payments for: $1 (e.g., "2026-02")

## Payment Rates

**DJ Rate:** ฿750/hour (฿3,000 per 4-hour evening)
**Withholding Tax:** 5%

| Slot | Hours | Gross | WHT (5%) | Net |
|------|-------|-------|----------|-----|
| Horizon | 4 | ฿3,000 | ฿150 | ฿2,850 |

## Instructions

1. Read schedule from `schedules/[month]/schedule.md`
2. Count shifts per DJ
3. Calculate:
   - Total hours per DJ
   - Gross pay (shifts × ฿3,000)
   - WHT deduction (5%)
   - Net pay

## Output Format

### DJ Payment Summary - [Month]

| DJ | Shifts | Hours | Gross | WHT (5%) | Net |
|---|---|---|---|---|---|

### Bright Ears Invoice to Client
- Days worked: X
- Rate: TBD/day
- Total: TBD

Save to `payments/[month]-summary.md`
