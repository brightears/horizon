# Bright Ears DJ Management - Horizon

## Project Overview

Bright Ears Co., Ltd. manages DJ entertainment at Horizon.

**Contract Period:** TBD
**Contract Duration:** TBD

---

## Venue & Schedule

### Horizon
- **Location:** TBD
- **Type:** TBD
- **Hours:** 18:30-22:30 (4 hours)
- **DJs per Night:** 1

**Total daily performance:** 4 hours (1 DJ per night)

---

## Music Guidelines

### Horizon
- **Style:** Elegant but flexible/open format preferred
- **Vibe:** High-end bar atmosphere, sophisticated but adaptable
- **Approach:** Follow the guest profile, which varies night to night. While sophisticated house music works, flexible DJs who can read the crowd are preferred.
- **Best Feedback:** Open format sets that adapt to the audience

---

## Key Contacts

| Name | Role |
|------|------|
| TBD | Manager |

---

## Payment Structure

### Bright Ears Invoices to Client

TBD — Invoice rates to be defined.

### Bright Ears Pays DJs

| Item | Amount |
|------|--------|
| Hourly rate | ฿750 |
| Per evening (4 hours) gross | ฿3,000 |
| Withholding tax (5%) | -฿150 |
| **Net per evening** | **฿2,850** |
| Net per hour | ฿712.50 |

### DJ Earnings per Shift

| Venue | Hours | Gross | WHT (5%) | Net |
|-------|-------|-------|----------|-----|
| Horizon | 4 hrs | ฿3,000 | ฿150 | ฿2,850 |

**Additional Hours:** Same hourly rate (฿750 gross / ฿712.50 net) for special bookings.

### Monthly Invoice Timeline

- **Submit invoice:** End of month
- **Payment received:** 3-4 weeks after submission
- **Pay DJs:** After receiving payment from client

---

## Operational Rules

- **Schedule changes:** Client may request changes for special bookings
- **Dress code:** TBD
- **Benefits:** TBD
- **Equipment:** TBD

---

## Current Weekly Schedule

| Day | Horizon (18:30-22:30) |
|-----|-----------------------|
| Mon | Pound |
| Tue | Pound |
| Wed | Eskay |
| Thu | Nun |
| Fri | Eskay |
| Sat | Ize |
| Sun | Ize |

---

## Current DJ Roster (4 DJs)

### Regular DJs
| DJ | Schedule | Style |
|---|---|---|
| DJ Pound | Mon, Tue | Open Format, Pop, R&B, Hip Hop, House |
| DJ Eskay | Wed, Fri | Hip Hop, R&B, Afro House, Latino |
| DJ Nun | Thu | Funky, Groovy, Disco House, Thai |
| DJ Ize | Sat, Sun | R&B, Hip-Hop, '80s/'90s |

### DJs Also at CRU/Cocoa XO
- Pound (CRU Thursday, Le Du Kaan Friday)
- Eskay Da Real (CRU Friday)

---

## Presentations Created

| Presentation | Location |
|-------------|----------|
| DJ Roster | `presentations/dj-roster-presentation.html` / `.pdf` |
| February 2026 Schedule | `presentations/february-2026-schedule.html` / `.pdf` |
| April 2026 Schedule | `presentations/april-2026-schedule.html` / `.pdf` |

---

## Schedules Created

| Month | Location |
|-------|----------|
| February 2026 | `schedules/2026-02/schedule.md` |
| April 2026 | `schedules/2026-04/schedule.md` |

---

## Payments Processed

None yet.

---

## File Organization

```
Horizon/
├── CLAUDE.md                # This file - project knowledge
├── contracts/               # Signed agreements
├── djs/
│   ├── profiles/           # DJ profiles (markdown)
│   │   ├── _TEMPLATE.md
│   │   ├── nun.md
│   │   ├── pound.md
│   │   ├── ize.md
│   │   └── eskay.md
│   └── images/             # DJ photos
│       ├── nun-1.png
│       ├── pound-photo1.jpg
│       ├── ize-1.jpg
│       └── eskay-photo1.jpg
├── schedules/              # Monthly schedules
│   ├── 2026-02/
│   │   └── schedule.md
│   └── 2026-04/
│       └── schedule.md
├── presentations/          # DJ roster & schedule presentations
│   ├── dj-roster-presentation.html
│   ├── dj-roster-presentation.pdf
│   ├── february-2026-schedule.html
│   ├── february-2026-schedule.pdf
│   ├── april-2026-schedule.html
│   └── april-2026-schedule.pdf
├── payments/
│   ├── templates/          # WHT form templates
│   ├── scripts/            # Automation scripts
│   │   └── fill_wht_form.py
│   └── venv/               # Python virtual environment
├── branding/               # Bright Ears logo & brand guide
│   ├── BE_Logo_Transparent.png
│   ├── BE_Logo_Dark.jpg
│   ├── BE_Logo_White.jpg
│   ├── BE_Logo_Mark.png
│   └── BRAND_GUIDE.md
└── .claude/
    ├── commands/           # Slash commands
    └── agents/             # Subagents
```

---

## Available Subagents

| Subagent | Model | Triggers On |
|----------|-------|-------------|
| `dj-profiler` | Sonnet | Processing DJ info, creating profiles |
| `schedule-builder` | Opus | Creating/managing monthly schedules |
| `presentation-builder` | Opus | Building DJ presentations for venues |
| `payment-calculator` | Sonnet | Calculating payments, generating summaries |

---

## Available Slash Commands

| Command | Purpose |
|---------|---------|
| `/add-dj [name]` | Quick DJ profile creation |
| `/list-djs` | Show roster |
| `/build-presentation` | Generate DJ presentation |
| `/schedule [month]` | View/create schedules |
| `/calculate-pay [month]` | Calculate DJ payments |
| `/project-status` | Quick status overview |

---

## DJ Profile Template

When adding a new DJ, create a markdown file in `djs/profiles/` with:
- Stage name / Real name
- Photo filename (stored in `djs/images/`)
- Music genres/specialties
- Brief bio
- Contact info
- Availability notes

---

## Bright Ears Branding

**Website:** https://brightears.io

### Logo
- **Primary:** `branding/BE_Logo_Transparent.png` - High-res with "BRIGHTEARS" text, transparent background
- **Icon only:** `branding/BE_Logo_White.jpg` - Circle mark only, for small uses
- **Style:** Circular "BE" monogram with cyan ring, white text on transparent/dark

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Brand Cyan | `#00bbe4` | Primary accent, highlights |
| Deep Teal | `#2f6364` | Secondary accent, headers |
| Soft Lavender | `#d59ec9` | Tertiary (use sparingly) |
| Earthy Brown | `#a47764` | Warm accent |
| Luxury Black | `#0a0a0a` | Dark backgrounds |
| Off-White | `#f7f7f7` | Light backgrounds |
| Dark Gray | `#333333` | Body text |

### Typography
- **Headlines:** Playfair (elegant serif)
- **Body:** Inter (modern sans-serif)

---

## Pending Items

- [ ] Add venue location and details
- [ ] Add contract details when signed
- [ ] Add key contact names
- [ ] Define invoice rates to client
- [ ] Define dress code and operational details

---

## Notes

- Sister projects: CRU/Cocoa XO and NOBU/Le Du Kaan
- CRU project at: `/Users/benorbe/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding Projects/CRU/`
- NOBU project at: `/Users/benorbe/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding Projects/NOBU/`
- Some DJs may work across multiple Bright Ears venues

### February 2026 Specific Notes

- Eskay guested Feb 18 (Wed, replaced Pound) and Feb 19 (Thu, replaced Nun)

### April 2026 Specific Notes

- New regular rotation: Pound Mon/Tue, Eskay Wed/Fri, Nun Thu, Ize Sat/Sun
- Eskay promoted from substitute to regular DJ
- Songkran (Apr 13-15): schedule unchanged pending venue guidance

---

## Technical Notes

### Presentations
- Generated via HTML → Chrome headless → PDF
- Command: `cd presentations && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="output.pdf" --no-margins --print-to-pdf-no-header "file://$(pwd)/source.html"`

### Withholding Tax Form Automation (ภ.ง.ด.3)

Automated system to fill Thai WHT forms for DJ payments.

**Templates saved:** `payments/templates/wht-{djname}.pdf` (none yet)

**Usage:**
```bash
cd payments && source venv/bin/activate
python3 scripts/fill_wht_form.py <dj_name> <amount> <tax> <output_folder> <month> <year> <venue>

# Example:
python3 scripts/fill_wht_form.py djname 3000 150 "2026-02/wht" feb 2026 "Horizon"
# Creates: djname-feb2026-horizon-wht.pdf
```

**Filename format:** `{dj}-{month}{year}-{venue}-wht.pdf`

**Fields updated automatically:**
- Amount (with comma formatting: 3,000.00)
- Tax withheld (with comma formatting: 150.00)
- Written amount in English (e.g., "ONE HUNDRED FIFTY BAHT")
- Date (current date)

**Cross-platform compatibility:**
- Script uses `auto_regenerate=True` to embed font appearances
- Removes `/NeedAppearances` flag to ensure embedded appearances are used
- This fixes comma/decimal rendering issues when opening PDFs on Windows after syncing via Google Cloud
