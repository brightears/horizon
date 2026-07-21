#!/usr/bin/env python3
"""Two comparison quotes for the Horizon MONTHLY DJ proposal (DJ Pound + BMAsia),
matching last year's monthly templates. NOT Bright Ears. No signature (Norbert adds)."""
from decimal import Decimal, ROUND_HALF_UP
OUT="/home/brightears/horizon/comparison"
q=lambda x:x.quantize(Decimal("0.01"),ROUND_HALF_UP)
def m0(x): return f"{int(x):,}"

def brush(color):
    return f'''<svg class="brush" viewBox="0 0 420 150" xmlns="http://www.w3.org/2000/svg">
      <path d="M18,78 C70,40 150,34 235,54 C300,69 360,50 402,72 C372,104 300,112 210,96 C150,86 70,104 18,78 Z" fill="{color}"/>
      <path d="M40,112 C90,100 150,108 210,102 C160,124 90,128 44,120 Z" fill="{color}" opacity="0.9"/>
      <circle cx="14" cy="66" r="5" fill="{color}"/>
      <circle cx="30" cy="126" r="3.5" fill="{color}"/>
      <circle cx="235" cy="120" r="3" fill="{color}" opacity="0.85"/>
      <ellipse cx="392" cy="90" rx="9" ry="4" fill="{color}" opacity="0.8" transform="rotate(18 392 90)"/>
    </svg>'''

def css(accent):
    return f'''
@page{{ size:A4; margin:0; }}
*{{ margin:0; padding:0; box-sizing:border-box; }}
body{{ font-family:Georgia,'Times New Roman',serif; color:#222; font-size:12px; }}
.page{{ width:210mm; min-height:297mm; background:#fff; display:flex; flex-direction:column; }}
.hdr{{ position:relative; background:#e7e7e7; padding:16mm 16mm 14mm; }}
.logo-wm{{ font-family:'Trebuchet MS',Arial,sans-serif; font-size:34px; font-weight:700; letter-spacing:-1px; }}
.company{{ font-size:17px; font-weight:400; margin-top:6px; }}
.addr{{ color:#666; font-size:12.5px; line-height:1.55; margin-top:8px; }}
.brushwrap{{ position:absolute; top:12mm; right:12mm; width:300px; height:118px; }}
.brush{{ position:absolute; inset:0; width:100%; height:100%; }}
.qtitle{{ position:absolute; top:22px; right:24px; text-align:right; }}
.qtitle .t{{ font-family:'Trebuchet MS',Arial,sans-serif; font-size:26px; font-weight:700; color:#3a3a3a; }}
.qtitle .d{{ font-size:12px; color:#4a4a4a; line-height:1.55; margin-top:6px; }}
.body{{ padding:14mm 16mm 0; flex:1; }}
.two{{ display:flex; gap:40px; }}
.two .lbl{{ font-family:'Trebuchet MS',Arial,sans-serif; font-weight:700; font-size:13px; margin-bottom:7px; }}
.two p{{ line-height:1.5; }}
.tbl{{ width:100%; border-collapse:collapse; margin-top:26px; }}
.tbl th{{ font-family:'Trebuchet MS',Arial,sans-serif; font-size:12.5px; font-weight:700; text-align:center; padding:6px 4px; border-bottom:2px solid {accent}; line-height:1.2; }}
.tbl th.l{{ text-align:left; }} .tbl th.r{{ text-align:right; }}
.tbl td{{ padding:16px 4px; font-size:13px; text-align:center; border-top:2px solid {accent}; border-bottom:1px solid #ccc; }}
.tbl td.l{{ text-align:left; }} .tbl td.r{{ text-align:right; }}
.totals{{ text-align:right; margin-top:26px; }}
.totals .st{{ font-family:'Trebuchet MS',Arial,sans-serif; font-weight:700; font-size:14px; margin-bottom:8px; }}
.totals .grand{{ font-family:'Trebuchet MS',Arial,sans-serif; font-weight:700; font-size:22px; margin-top:16px; }}
.sigwrap{{ margin-top:44px; }}
.sig{{ font-size:30px; padding-left:8px; height:34px; }}
.sigline{{ border-bottom:1px solid {accent}; width:270px; margin-top:-2px; }}
.signame{{ font-size:12.5px; margin-top:6px; }}
.pay{{ text-align:center; font-family:'Trebuchet MS',Arial,sans-serif; font-weight:700; font-size:12.5px; padding:20mm 8mm 12mm; }}
'''

def doc(*, logo_html, company, addr_lines, accent, date_lines, project, price_hour, price_month, sub, vat, total, sig_name, sig_title, pay):
    addr = "<br>".join(addr_lines)
    dlines = "".join(f"<div>{d}</div>" for d in date_lines)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css(accent)}</style></head><body><div class="page">
  <div class="hdr">
    {logo_html}
    <div class="company">{company}</div>
    <div class="addr">{addr}</div>
    <div class="brushwrap">{brush(accent)}
      <div class="qtitle"><div class="t">DJ QUOTATION</div><div class="d">{dlines}</div></div>
    </div>
  </div>
  <div class="body">
    <div class="two">
      <div style="flex:1"><div class="lbl">CUSTOMER</div>
        <p>Khun Jittima Ruttitham<br>Purchasing Manager | Finance<br>Hilton Pattaya</p></div>
      <div style="flex:1"><div class="lbl">PROJECT DESCRIPTION:</div><p>{project}</p></div>
    </div>
    <table class="tbl">
      <tr><th class="l">DESCRIPTION</th><th>Hours/<br>Night</th><th>Days/<br>Week</th><th>PRICE/HOUR</th><th class="r">PRICE/MONTH</th></tr>
      <tr><td class="l">DJ Entertainment</td><td>4</td><td>7</td><td>THB {m0(price_hour)}</td><td class="r">THB {m0(price_month)}</td></tr>
    </table>
    <div class="totals">
      <div class="st">SUBTOTAL: THB {m0(sub)}</div>
      <div class="st">VAT (7%): THB {m0(vat)}</div>
      <div class="grand">TOTAL/MONTH : THB {m0(total)}</div>
    </div>
    <div class="sigwrap">
      <div class="sig">&nbsp;</div><div class="sigline"></div>
      <div class="signame">Name: {sig_name}<br>Title: {sig_title}</div>
    </div>
  </div>
  <div class="pay">Payment Terms: {pay}</div>
</div></body></html>'''

PAY="All payments shall be made at the end of each month in which the DJ performs."

# DJ Pound (purple) — 1,000/hr -> 124,000/month
ph1=Decimal("1000"); pm1=Decimal("124000"); vat1=q(pm1*Decimal("0.07")); tot1=pm1+vat1
assert vat1==Decimal("8680.00") and tot1==Decimal("132680.00")
open(f"{OUT}/QT-DJPound-Horizon-2026.html","w").write(doc(
  logo_html='', company="DJ Pound Entertainment",
  addr_lines=["460/8 M.9 Central Pattaya Rd., Nongprue,","Banglamoong, Chonburi 20260"],
  accent="#b45dc9", date_lines=["Date: 07/18/2026"], project="DJ Entertainment for Horizon",
  price_hour=ph1, price_month=pm1, sub=pm1, vat=vat1, total=tot1,
  sig_name="Ittiwat Thongsuk", sig_title="Head DJ", pay=PAY))

# BMAsia (orange) — 1,100/hr -> 136,400/month
ph2=Decimal("1100"); pm2=Decimal("136400"); vat2=q(pm2*Decimal("0.07")); tot2=pm2+vat2
assert vat2==Decimal("9548.00") and tot2==Decimal("145948.00")
bm_logo='<div class="logo-wm"><span style="color:#f0902f">bm</span><span style="color:#6a6a6a">asia</span></div>'
open(f"{OUT}/QT-BMAsia-Horizon-2026.html","w").write(doc(
  logo_html=bm_logo, company="BMAsia (Thailand) Co., Ltd. (Head Office)",
  addr_lines=["725 Metropolis Building, Suite 144,","Level 20, Sukhumvit Road, Klongtan Nuea","Watthana, Bangkok 10110 Thailand"],
  accent="#f0902f", date_lines=["Date: 07/17/2026","Valid Until: 08/17/2026","Tax No.: 0105548025073"],
  project="DJ Entertainment for Horizon",
  price_hour=ph2, price_month=pm2, sub=pm2, vat=vat2, total=tot2,
  sig_name="Chris Andrews", sig_title="Director", pay=PAY))

print("DJ Pound:", pm1, vat1, tot1, "| BMAsia:", pm2, vat2, tot2)
