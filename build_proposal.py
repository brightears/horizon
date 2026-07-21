#!/usr/bin/env python3
"""Horizon DJ Proposal 2026-27 — faithful update of the 2025-26 doc, same price.
Clean A4 proposal in the elevated Bright Ears style."""
from decimal import Decimal, ROUND_HALF_UP
OUT="/home/brightears/horizon"
q=lambda x:x.quantize(Decimal("0.01"),ROUND_HALF_UP)
def money(x): return f"{x:,.2f}"

DATE="21 July 2026"
# pricing (unchanged per Norbert)
MONTHLY=Decimal("117180.00"); VAT=q(MONTHLY*Decimal("0.07")); GRAND=MONTHLY+VAT
assert VAT==Decimal("8202.60") and GRAND==Decimal("125382.60"), (VAT,GRAND)

CSS="""
@page{ size:A4; margin:0; }
*{ margin:0; padding:0; box-sizing:border-box; }
:root{ --ink:#1c1a17; --muted:#6b6558; --faint:#938c7e; --line:#e4dfd5; --accent:#9c7a2e; --wash:#faf8f3; }
body{ font-family:'Helvetica Neue',Arial,sans-serif; color:var(--ink); font-size:11px; line-height:1.55; }
.page{ width:210mm; min-height:297mm; padding:14mm 20mm 12mm; }
.head{ display:flex; justify-content:space-between; align-items:flex-start; }
.co-name{ font-weight:700; font-size:14px; letter-spacing:.3px; }
.co .tag{ font-size:9px; letter-spacing:3px; text-transform:uppercase; color:var(--accent); margin-top:3px; }
.co .contact{ color:var(--muted); margin-top:8px; font-size:10px; }
.date{ text-align:right; color:var(--muted); font-size:10.5px; padding-top:4px; }
.rule{ height:2px; background:var(--accent); margin:13px 0 0; }
.recipient{ margin-top:18px; }
.recipient .nm{ font-weight:600; }
.recipient p{ color:#2c2924; line-height:1.5; }
.subject{ margin-top:16px; font-family:Georgia,serif; font-size:17px; color:var(--accent); }
.dear{ margin-top:14px; }
.intro{ margin-top:8px; color:#33302a; }
.section{ margin-top:16px; }
.section h3{ font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--accent); font-weight:700;
             border-bottom:1px solid var(--line); padding-bottom:5px; margin-bottom:8px; }
.grid{ display:grid; grid-template-columns:150px 1fr; gap:5px 14px; }
.grid .k{ color:var(--muted); }
.grid .v{ color:#2c2924; }
.theme-row{ display:grid; grid-template-columns:190px 1fr; gap:14px; padding:5px 0; border-bottom:1px solid #f0ebe1; }
.theme-row:last-child{ border-bottom:none; }
.theme-row .t{ font-weight:600; }
.theme-row .t span{ display:block; color:var(--muted); font-weight:400; font-size:10px; }
.theme-row .d{ color:#33302a; }
ul.perks{ list-style:none; }
ul.perks li{ position:relative; padding-left:18px; margin-bottom:6px; color:#33302a; }
ul.perks li::before{ content:"✦"; position:absolute; left:0; color:var(--accent); font-size:10px; top:1px; }
.fee{ margin-top:16px; border:1px solid var(--line); border-radius:2px; overflow:hidden; }
.fee .fh{ background:var(--ink); color:#f3efe6; font-size:10px; letter-spacing:2px; text-transform:uppercase; padding:8px 16px; font-weight:600; }
.fee table{ width:100%; border-collapse:collapse; }
.fee td{ padding:8px 16px; font-size:12px; border-bottom:1px solid #efeadf; }
.fee td.r{ text-align:right; font-variant-numeric:tabular-nums; }
.fee tr:last-child td{ border-bottom:none; }
.fee tr.grand td{ font-weight:700; font-size:13.5px; color:var(--accent); background:var(--wash); }
.note{ margin-top:10px; color:var(--muted); font-size:10px; font-style:italic; }
.close{ margin-top:16px; color:#33302a; }
.sign{ margin-top:26px; }
.sign .nm{ font-weight:700; }
.sign .role{ color:var(--muted); font-size:10.5px; }
.foot{ margin-top:20px; border-top:1px solid var(--line); padding-top:10px; text-align:center; font-size:9px;
       letter-spacing:2px; text-transform:uppercase; color:var(--faint); }
.flag{ color:#9a3b3b; }
"""

HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
  <div class="head">
    <div class="co">
      <div class="co-name">Bright Ears Co., Ltd.</div>
      <div class="tag">DJ Booking · Scheduling · Management</div>
      <div class="contact">11/10 Soi Panjit 3, Phaholyothin Road, Lum Luk Ka, Pathum Thani · +66 (0) 85 664 4142 · office@brightears.com</div>
    </div>
    <div class="date">{DATE}</div>
  </div>
  <div class="rule"></div>

  <div class="recipient">
    <p class="nm">Khun Jittima Ruttitham</p>
    <p>Purchasing Manager · Finance</p>
    <p>Hilton Pattaya</p>
  </div>

  <div class="subject">Tailored DJ Experience by Bright Ears &mdash; 2026&ndash;27</div>
  <div class="dear">Dear Khun Jittima,</div>
  <div class="intro">We are delighted to present our DJ proposal for the coming year &mdash; a vibrant and immersive musical experience at the Horizon Rooftop Bar, renewed for the 2026&ndash;27 term.</div>

  <div class="section">
    <h3>Performance Details</h3>
    <div class="grid">
      <div class="k">Duration</div><div class="v">8.00 PM &ndash; 12.00 AM (4 hours)</div>
      <div class="k">Artists</div><div class="v">2 to 3 local DJs</div>
      <div class="k">Theme</div><div class="v">Customizable as per your preference</div>
    </div>
  </div>

  <div class="section">
    <h3>Music Programme</h3>
    <div class="theme-row"><div class="t">Background Music<span>5 PM &ndash; 8 PM</span></div><div class="d">Relaxed sunset ambiance · house remixes, fresh yet familiar</div></div>
    <div class="theme-row"><div class="t">Early DJ Set<span>8 PM &ndash; 9 PM</span></div><div class="d">A smooth transition into a vibrant evening</div></div>
    <div class="theme-row"><div class="t">Main DJ Set<span>9 PM onwards</span></div><div class="d">Lively night grooves · nu disco &amp; indie dance, dynamic</div></div>
  </div>

  <div class="section">
    <h3>What's Included</h3>
    <ul class="perks">
      <li>Complimentary subscription to Soundtrack Your Brand at Horizon (approved by Hilton Corporate).</li>
      <li>No extra charges on special event days (e.g. NYE party).</li>
      <li>Performance by DJ Norbert for 4 special theme nights per year, free of charge (e.g. Firework Festival, NYE).</li>
      <li>DJs with MC experience available at no extra charge.</li>
      <li>Hassle-free DJ replacement &mdash; a suitable replacement within a week's notice.</li>
    </ul>
  </div>

  <div class="fee">
    <div class="fh">Fee Structure</div>
    <table>
      <tr><td>Monthly Fee</td><td class="r">THB {money(MONTHLY)}</td></tr>
      <tr><td>VAT (7%)</td><td class="r">THB {money(VAT)}</td></tr>
      <tr class="grand"><td>Grand Total (31 days)</td><td class="r">THB {money(GRAND)}</td></tr>
    </table>
  </div>
  <div class="note">The invoiced amount will align with the actual performance days and hours. DJs are required to log in and out.</div>

  <div class="close">Looking forward to enhancing the Horizon Rooftop Bar experience for another year with our curated music selection.</div>
  <div class="sign">
    <p class="nm">Norbert Platzer</p>
    <p class="role">Music Experience Manager · Bright Ears</p>
  </div>

  <div class="foot">Bright Ears — DJ Booking, Scheduling &amp; Management · Bangkok</div>
</div></body></html>"""

open(f"{OUT}/Horizon-DJ-Proposal-2026-27.html","w").write(HTML)
print("Monthly", MONTHLY, "VAT", VAT, "Grand", GRAND)
print("wrote", f"{OUT}/Horizon-DJ-Proposal-2026-27.html")
