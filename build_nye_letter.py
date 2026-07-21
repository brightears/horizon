#!/usr/bin/env python3
"""Shore NYE 2026 DJ proposal — faithful revision of last year's letter (same rate,
1 unit), updated to 2026 + Bright Ears brand design (logo + cyan)."""
from decimal import Decimal, ROUND_HALF_UP
import json
OUT="/home/brightears/horizon"
q=lambda x:x.quantize(Decimal("0.01"),ROUND_HALF_UP)
def money(x): return f"{x:,.2f}"

DATE="21 July 2026"; VALID="20 August 2026"
DJ=Decimal("10000"); EQUIP=Decimal("5000")            # SAME as last year (Norbert 2026-07-21)
SUB=DJ+EQUIP; VAT=q(SUB*Decimal("0.07")); TOTAL=SUB+VAT
assert SUB==Decimal("15000") and VAT==Decimal("1050.00") and TOTAL==Decimal("16050.00")

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
body{{ font-family:'Inter',system-ui,Arial,sans-serif; color:{TEXT}; font-size:11px; line-height:1.6; }}
.page{{ width:210mm; min-height:297mm; background:#fff; display:flex; flex-direction:column; }}
.body{{ padding:10mm 20mm 8mm; flex:1; }}
.brandbar{{ background:{INK}; color:#fff; padding:7mm 20mm 6mm; display:flex; justify-content:space-between; align-items:center; border-bottom:3px solid {CYAN}; }}
.brandbar .left{{ display:flex; align-items:center; gap:16px; }}
.brandbar .logo{{ width:56px; height:56px; flex-shrink:0; display:block; }}
.wordmark{{ font-family:Georgia,serif; font-size:22px; letter-spacing:2px; color:#fff; }}
.wordmark .be{{ color:{CYAN_BRIGHT}; }}
.tagline{{ font-size:8.5px; letter-spacing:3px; text-transform:uppercase; color:{CYAN_BRIGHT}; margin-top:4px; }}
.brandbar .right{{ text-align:right; font-size:10px; color:{OFFWHITE}; line-height:1.6; }}
.brandbar .right .d{{ color:#fff; font-weight:600; }}
.meta{{ display:flex; justify-content:space-between; align-items:flex-start; }}
.recipient .nm{{ font-weight:600; }} .recipient p{{ color:#333; }}
.qmeta{{ text-align:right; font-size:9.5px; }}
.qmeta .k{{ color:{MUTED}; text-transform:uppercase; letter-spacing:1px; font-size:8px; }}
.qmeta .v{{ font-weight:600; }}
.subject{{ margin-top:16px; font-family:Georgia,serif; font-size:18px; color:{CYAN}; }}
.dear{{ margin-top:14px; }} .para{{ margin-top:8px; color:#333; }}
.detail{{ margin-top:16px; border:1px solid {LINE}; border-radius:4px; overflow:hidden; }}
.detail .dh{{ background:{INK}; color:#fff; padding:9px 16px; font-size:11px; font-weight:600; letter-spacing:.5px; border-left:3px solid {CYAN}; }}
.detail .dh span{{ display:block; font-size:8.5px; letter-spacing:2px; text-transform:uppercase; color:{CYAN_BRIGHT}; margin-top:2px; }}
.detail .rows{{ padding:4px 16px; }}
.detail .row{{ display:grid; grid-template-columns:150px 1fr; gap:12px; padding:5px 0; border-bottom:1px solid #f0f4f5; }}
.detail .row .k{{ color:{MUTED}; }} .detail .row .v{{ color:#2a2a2a; }}
.detail table{{ width:100%; border-collapse:collapse; }}
.detail td{{ padding:8px 16px; font-size:11.5px; border-top:1px solid #eef2f3; }}
.detail td.r{{ text-align:right; font-variant-numeric:tabular-nums; }}
.detail td .s{{ color:{MUTED}; font-size:9.5px; }}
.detail tr.sub td{{ font-weight:600; background:#fbfdfe; }}
.detail tr.total td{{ font-weight:600; font-size:14px; color:{CYAN}; background:{WASH}; }}
.close{{ margin-top:16px; color:#333; }}
.sign{{ margin-top:20px; }} .sign .kr{{ color:#333; }} .sign .nm{{ font-weight:600; font-size:12px; margin-top:10px; }} .sign .role{{ color:{MUTED}; font-size:10.5px; }}
.foot{{ background:#fafafa; border-top:1px solid {LINE}; padding:9px 20mm; display:flex; justify-content:space-between; align-items:center; font-size:8.5px; color:{FAINT}; line-height:1.5; }}
.foot .brandline{{ display:flex; align-items:center; gap:8px; letter-spacing:1.5px; text-transform:uppercase; }}
.foot .dot{{ width:8px; height:8px; border-radius:50%; border:2px solid {CYAN}; display:inline-block; }}
.foot .addr{{ text-align:right; }}
"""

HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="page">
  <div class="brandbar">
    <div class="left">
      <img class="logo" src="data:image/png;base64,{LOGO_B64}" alt="Bright Ears"/>
      <div><div class="wordmark">BRIGHT <span class="be">EARS</span></div>
      <div class="tagline">DJ Booking · Scheduling · Management</div></div>
    </div>
    <div class="right"><div class="d">{DATE}</div><div>+66 (0) 85 664 4142</div><div>info@brightears.com</div></div>
  </div>

  <div class="body">
    <div class="meta">
      <div class="recipient"><p class="nm">Khun Jittima Ruttitham</p><p>Purchasing Manager · Finance · Hilton Pattaya</p></div>
      <div class="qmeta"><div class="k">Quotation No.</div><div class="v">QT-HILTON-NYE-2026</div>
        <div class="k" style="margin-top:5px;">Valid Until</div><div class="v">{VALID}</div></div>
    </div>

    <div class="subject">DJ Proposal — New Year's Eve 2026 at Shore</div>
    <div class="dear">Dear Khun Jittima,</div>
    <div class="para">Further to your enquiry, I am pleased to provide the following DJ proposal for New Year's Eve, on the 31st of December 2026 at Shore, Hilton Pattaya — at the same rate as last year.</div>

    <div class="detail">
      <div class="dh">New Year's Eve 2026 at Shore<span>31 December 2026</span></div>
      <div class="rows">
        <div class="row"><div class="k">Performance time</div><div class="v">As required</div></div>
        <div class="row"><div class="k">Theme</div><div class="v">As required</div></div>
      </div>
      <table>
        <tr><td>Artist<div class="s">1 in-house DJ</div></td><td class="r">THB {money(DJ)}</td></tr>
        <tr><td>Equipment<div class="s">DJ mixer</div></td><td class="r">THB {money(EQUIP)}</td></tr>
        <tr class="sub"><td>Sub Total</td><td class="r">THB {money(SUB)}</td></tr>
        <tr><td>VAT 7%</td><td class="r">THB {money(VAT)}</td></tr>
        <tr class="total"><td>Total</td><td class="r">THB {money(TOTAL)}</td></tr>
      </table>
    </div>

    <div class="close">I look forward to your questions on the proposal. Should you like me to clarify any of the points above, I will be delighted to assist further.</div>
    <div class="sign"><p class="kr">Kind Regards,</p><p class="nm">Norbert Platzer</p><p class="role">Music Experience Manager · Bright Ears</p></div>
  </div>

  <div class="foot">
    <div class="brandline"><span class="dot"></span> Bright Ears — DJ Booking, Scheduling &amp; Management</div>
    <div class="addr">65/213 Chamnan Phenjati Business Center, 25th Fl, Rama 9 Rd., Huaykwang, Bangkok 10310 · info@brightears.com · www.brightears.com</div>
  </div>
</div></body></html>"""

open(f"{OUT}/QT-Hilton-Shore-NYE-2026.html","w").write(HTML)
print("rate:", DJ, "+", EQUIP, "=", SUB, "VAT", VAT, "Total", TOTAL)
