#!/usr/bin/env python3
"""Shore NYE 2026 DJ quotation — Hilton Pattaya. On-brand (Bright Ears logo + cyan).
Shows 1-unit and 2-unit options for price comparison (Hilton's request)."""
from decimal import Decimal, ROUND_HALF_UP
import json
OUT="/home/brightears/horizon"   # Horizon repo covers Hilton Pattaya venue docs
q=lambda x:x.quantize(Decimal("0.01"),ROUND_HALF_UP)
def money(x): return f"{x:,.2f}"

DATE="21 July 2026"; VALID="20 August 2026"
DJ=Decimal("20000"); EQUIP=Decimal("5000")           # per unit (Norbert 2026-07-21)
# 1 unit
u1_sub=DJ+EQUIP; u1_vat=q(u1_sub*Decimal("0.07")); u1_tot=u1_sub+u1_vat
# 2 units
u2_dj=DJ*2; u2_eq=EQUIP*2; u2_sub=u2_dj+u2_eq; u2_vat=q(u2_sub*Decimal("0.07")); u2_tot=u2_sub+u2_vat
assert u1_tot==Decimal("26750.00") and u2_tot==Decimal("53500.00"), (u1_tot,u2_tot)

fonts=json.load(open("/home/brightears/BrightEars-Ops/data/brand/inter-fonts-base64.json"))
LOGO_B64=open("/home/brightears/BrightEars-Ops/data/brand/logo-png-base64.txt").read().strip()

INK="#131313"; CYAN="#00bbe4"; CYAN_BRIGHT="#4fd6ff"; OFFWHITE="#e5e2e1"
TEXT="#1c1c1c"; MUTED="#6a6a6a"; FAINT="#9a9a9a"; LINE="#e6e6e6"; WASH="#f4fbfd"

FONTFACE=f"""
@font-face{{font-family:'Inter';font-weight:400;font-style:normal;src:url(data:font/woff2;base64,{fonts['inter400']}) format('woff2');}}
@font-face{{font-family:'Inter';font-weight:600;font-style:normal;src:url(data:font/woff2;base64,{fonts['inter600']}) format('woff2');}}
"""

CSS=f"""
{FONTFACE}
@page{{ size:A4; margin:0; }}
*{{ margin:0; padding:0; box-sizing:border-box; }}
body{{ font-family:'Inter',system-ui,Arial,sans-serif; color:{TEXT}; font-size:11px; line-height:1.55; }}
.page{{ width:210mm; min-height:297mm; background:#fff; }}
.body{{ padding:9mm 20mm 10mm; }}
.brandbar{{ background:{INK}; color:#fff; padding:7mm 20mm 6mm; display:flex; justify-content:space-between; align-items:center; border-bottom:3px solid {CYAN}; }}
.brandbar .left{{ display:flex; align-items:center; gap:16px; }}
.brandbar .logo{{ width:56px; height:56px; flex-shrink:0; display:block; }}
.wordmark{{ font-family:Georgia,serif; font-size:22px; letter-spacing:2px; color:#fff; }}
.wordmark .be{{ color:{CYAN_BRIGHT}; }}
.tagline{{ font-size:8.5px; letter-spacing:3px; text-transform:uppercase; color:{CYAN_BRIGHT}; margin-top:4px; }}
.brandbar .right{{ text-align:right; font-size:10px; color:{OFFWHITE}; line-height:1.6; }}
.brandbar .right .d{{ color:#fff; font-weight:600; }}
.meta{{ display:flex; justify-content:space-between; margin-top:6px; }}
.recipient .nm{{ font-weight:600; }} .recipient p{{ color:#333; }}
.qmeta{{ text-align:right; font-size:10px; }}
.qmeta .k{{ color:{MUTED}; text-transform:uppercase; letter-spacing:1px; font-size:8.5px; }}
.qmeta .v{{ font-weight:600; }}
.subject{{ margin-top:15px; font-family:Georgia,serif; font-size:18px; color:{CYAN}; }}
.dear{{ margin-top:12px; }} .intro{{ margin-top:7px; color:#333; }}
.event{{ margin-top:14px; display:flex; gap:26px; padding:11px 16px; background:{WASH}; border-left:3px solid {CYAN}; }}
.event .ei .k{{ font-size:8.5px; letter-spacing:1.5px; text-transform:uppercase; color:{MUTED}; }}
.event .ei .v{{ font-weight:600; font-size:12px; }}
.opts{{ display:flex; gap:20px; margin-top:18px; }}
.opt{{ flex:1; border:1px solid {LINE}; border-radius:4px; overflow:hidden; }}
.opt .oh{{ background:{INK}; color:#fff; padding:9px 16px; font-size:11px; font-weight:600; letter-spacing:1px; border-left:3px solid {CYAN}; }}
.opt .oh span{{ color:{CYAN_BRIGHT}; font-size:9px; letter-spacing:2px; text-transform:uppercase; display:block; margin-top:2px; }}
.opt table{{ width:100%; border-collapse:collapse; }}
.opt td{{ padding:8px 16px; font-size:11px; border-bottom:1px solid #eef2f3; }}
.opt td.r{{ text-align:right; font-variant-numeric:tabular-nums; }}
.opt td .sub2{{ color:{MUTED}; font-size:9.5px; }}
.opt tr.sub td{{ font-weight:600; background:#fbfdfe; }}
.opt tr.total td{{ font-weight:600; font-size:13.5px; color:{CYAN}; background:{WASH}; border-bottom:none; }}
.terms{{ margin-top:20px; }}
.terms h3{{ font-size:10px; letter-spacing:2px; text-transform:uppercase; color:{CYAN}; font-weight:600; border-bottom:2px solid {CYAN}; padding-bottom:5px; margin-bottom:9px; }}
ul.perks{{ list-style:none; }}
ul.perks li{{ position:relative; padding-left:20px; margin-bottom:5px; color:#333; }}
ul.perks li::before{{ content:""; position:absolute; left:2px; top:6px; width:7px; height:7px; border-radius:50%; background:{CYAN}; }}
.close{{ margin-top:16px; color:#333; }}
.sign{{ margin-top:20px; }} .sign .nm{{ font-weight:600; font-size:12px; }} .sign .role{{ color:{MUTED}; font-size:10.5px; }}
.foot{{ margin-top:20px; border-top:1px solid {LINE}; padding-top:10px; display:flex; align-items:center; justify-content:center; gap:9px; font-size:8.5px; letter-spacing:2px; text-transform:uppercase; color:{FAINT}; }}
.foot .dot{{ width:8px; height:8px; border-radius:50%; border:2px solid {CYAN}; display:inline-block; }}
"""

HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
  <div class="brandbar">
    <div class="left">
      <img class="logo" src="data:image/png;base64,{LOGO_B64}" alt="Bright Ears"/>
      <div><div class="wordmark">BRIGHT <span class="be">EARS</span></div>
      <div class="tagline">DJ Booking · Scheduling · Management</div></div>
    </div>
    <div class="right"><div class="d">{DATE}</div><div>+66 (0) 85 664 4142</div><div>office@brightears.com</div></div>
  </div>
  <div class="body">
    <div class="meta">
      <div class="recipient"><p class="nm">Khun Jittima Ruttitham</p><p>Purchasing Manager · Finance · Hilton Pattaya</p></div>
      <div class="qmeta"><div class="k">Quotation No.</div><div class="v">QT-HILTON-NYE-2026</div>
        <div class="k" style="margin-top:5px;">Valid Until</div><div class="v">{VALID}</div></div>
    </div>

    <div class="subject">DJ Entertainment — New Year's Eve 2026 at Shore</div>
    <div class="dear">Dear Khun Jittima,</div>
    <div class="intro">Thank you for your enquiry. We are pleased to provide the following quotation for DJ entertainment services at Shore for New Year's Eve. As requested, both a single-unit and a two-unit option are shown below for your comparison.</div>

    <div class="event">
      <div class="ei"><div class="k">Event</div><div class="v">New Year's Eve</div></div>
      <div class="ei"><div class="k">Date</div><div class="v">31 December 2026</div></div>
      <div class="ei"><div class="k">Venue</div><div class="v">Shore · Hilton Pattaya</div></div>
    </div>

    <div class="opts">
      <div class="opt">
        <div class="oh">Option A<span>One DJ Unit</span></div>
        <table>
          <tr><td>DJ Performance<div class="sub2">1 in-house DJ</div></td><td class="r">THB {money(DJ)}</td></tr>
          <tr><td>Equipment<div class="sub2">DJ mixer</div></td><td class="r">THB {money(EQUIP)}</td></tr>
          <tr class="sub"><td>Sub Total</td><td class="r">THB {money(u1_sub)}</td></tr>
          <tr><td>VAT 7%</td><td class="r">THB {money(u1_vat)}</td></tr>
          <tr class="total"><td>Total</td><td class="r">THB {money(u1_tot)}</td></tr>
        </table>
      </div>
      <div class="opt">
        <div class="oh">Option B<span>Two DJ Units</span></div>
        <table>
          <tr><td>DJ Performance<div class="sub2">2 in-house DJs · 2 &times; {money(DJ)}</div></td><td class="r">THB {money(u2_dj)}</td></tr>
          <tr><td>Equipment<div class="sub2">2 DJ mixers · 2 &times; {money(EQUIP)}</div></td><td class="r">THB {money(u2_eq)}</td></tr>
          <tr class="sub"><td>Sub Total</td><td class="r">THB {money(u2_sub)}</td></tr>
          <tr><td>VAT 7%</td><td class="r">THB {money(u2_vat)}</td></tr>
          <tr class="total"><td>Total</td><td class="r">THB {money(u2_tot)}</td></tr>
        </table>
      </div>
    </div>

    <div class="terms">
      <h3>Notes</h3>
      <ul class="perks">
        <li>Rates are exclusive of VAT; 7% VAT is added as shown.</li>
        <li>Performance timing to be confirmed with the venue for the New Year's Eve programme.</li>
        <li>Saxophone / live band, if required, can be arranged separately on request.</li>
        <li>This quotation is valid until {VALID}.</li>
      </ul>
    </div>

    <div class="close">I look forward to your questions on the proposal. Should you like me to clarify any of the points above, I will be delighted to assist further.</div>
    <div class="sign"><p class="nm">Norbert Platzer</p><p class="role">Music Experience Manager · Bright Ears</p></div>
    <div class="foot"><span class="dot"></span> Bright Ears — DJ Booking, Scheduling &amp; Management · Bangkok</div>
  </div>
</div></body></html>"""

open(f"{OUT}/QT-Hilton-Shore-NYE-2026.html","w").write(HTML)
print("1 unit:", u1_sub, u1_vat, u1_tot, "| 2 units:", u2_sub, u2_vat, u2_tot)
