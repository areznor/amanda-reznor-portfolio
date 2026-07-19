# -*- coding: utf-8 -*-
import os
from content import PROFILES, LABELS, CONTACT, PHONE, MAIL, LOCATION_L, CERTS, LANGS, EDU

TPL = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<style>
  *{{margin:0;padding:0;box-sizing:border-box;}}
  html,body{{width:210mm;}}
  body{{font-family:'Carlito',sans-serif;font-size:9.6pt;line-height:1.42;color:#26262e;background:#fff;}}
  .page{{width:210mm;height:296.6mm;overflow:hidden;position:relative;background:#fff;}}
  .pb{{page-break-before:always;}}
  .hd{{position:relative;z-index:1;background:#f4f5f7;border-bottom:1.4pt solid #c9cdd4;padding:10mm 14mm 6.4mm 14mm;}}
  .hd .name{{font-family:'TeX Gyre Pagella',serif;font-size:25pt;letter-spacing:5.5pt;color:#26262e;}}
  .hd .name .dot{{color:#6a5b9e;}}
  .hd .role{{font-family:'TeX Gyre Heros',sans-serif;font-size:10.5pt;letter-spacing:3.2pt;color:#6a5b9e;text-transform:uppercase;margin-top:2.2mm;}}
  .hd .tag{{font-size:9.4pt;color:#7a7f89;margin-top:1.2mm;letter-spacing:.4pt;}}
  table.cols{{width:100%;border-collapse:collapse;position:relative;z-index:1;}}
  .sidebg{{position:absolute;left:0;top:0;bottom:0;width:60mm;background:#f4f5f7;border-right:.6pt solid #d7dade;z-index:0;}}
  td.side{{width:60mm;vertical-align:top;background:#f4f5f7;padding:6mm 6mm 6mm 14mm;border-right:.6pt solid #d7dade;}}
  td.main{{vertical-align:top;padding:7mm 14mm 6mm 8mm;}}
  h2{{font-family:'TeX Gyre Heros',sans-serif;font-size:8.6pt;letter-spacing:2.6pt;text-transform:uppercase;color:#26262e;margin:0 0 2.6mm 0;border-bottom:.7pt solid #c9cdd4;padding-bottom:1.4mm;}}
  h2 .tick{{color:#6a5b9e;}}
  .sec{{margin-bottom:6mm;}}
  .side .sec{{margin-bottom:4.4mm;}}
  .side h2{{font-size:8pt;}}
  .kv{{margin-bottom:1.2mm;}}
  .kv .k{{font-size:7.4pt;letter-spacing:1.6pt;color:#9ba1ab;text-transform:uppercase;}}
  .kv .v{{color:#26262e;}}
  ul.plain{{list-style:none;}}
  ul.plain li{{padding-left:3.6mm;position:relative;margin-bottom:.9mm;}}
  ul.plain li:before{{content:"—";position:absolute;left:0;color:#6a5b9e;font-size:7.5pt;top:.2mm;}}
  .lang{{margin-bottom:1.6mm;}}
  .lang .dots{{color:#6a5b9e;letter-spacing:1.5pt;font-size:8pt;}}
  .lang .dots .off{{color:#c9cdd4;}}
  .job{{margin-bottom:4.6mm;}}
  .job .t{{font-family:'TeX Gyre Heros',sans-serif;font-size:10.3pt;color:#26262e;}}
  .job .t .at{{color:#6a5b9e;}}
  .job .meta{{font-size:8.4pt;color:#7a7f89;letter-spacing:.5pt;margin:.4mm 0 1.2mm 0;}}
  .job ul{{list-style:none;}}
  .job ul li{{padding-left:4mm;position:relative;margin-bottom:1mm;}}
  .job ul li:before{{content:"›";position:absolute;left:.6mm;color:#6a5b9e;}}
  .prof{{color:#33333b;}}
  .edu{{margin-bottom:2.6mm;}}
  .edu .d{{font-family:'TeX Gyre Heros',sans-serif;font-size:9.8pt;}}
  .edu .i{{font-size:8.6pt;color:#7a7f89;}}
  .ft{{position:absolute;left:14mm;right:14mm;bottom:8mm;border-top:.6pt solid #d7dade;padding-top:2mm;font-size:7.6pt;color:#9ba1ab;letter-spacing:1.2pt;}}
  .ft .r{{float:right;}}
  .ft .v{{color:#6a5b9e;}}
</style>
</head>
<body>
<div class="page">
  <div class="sidebg"></div>
  <div class="hd">
    <div class="name">AMANDA<span class="dot"> · </span>BRITTO</div>
    <div class="role">{role}</div>
    <div class="tag">{tag}</div>
  </div>
  <table class="cols"><tr>
    <td class="side">
      <div class="sec"><h2><span class="tick">/</span> {L[contact]}</h2>
        <div class="kv"><div class="k">{L[loc]}</div><div class="v">{location}</div></div>
        <div class="kv"><div class="k">{L[phone]}</div><div class="v">{phone}</div></div>
        <div class="kv"><div class="k">{L[mail]}</div><div class="v">{mail}</div></div>
        {contact_kv}
      </div>
      <div class="sec"><h2><span class="tick">/</span> {core_title}</h2><ul class="plain">{core}</ul></div>
      <div class="sec"><h2><span class="tick">/</span> {L[tech]}</h2><ul class="plain">{tech}</ul></div>
      <div class="sec"><h2><span class="tick">/</span> {L[langs]}</h2>{langs}</div>
    </td>
    <td class="main">
      <div class="sec"><h2><span class="tick">/</span> {L[profile]}</h2><p class="prof">{prof}</p></div>
      <div class="sec"><h2><span class="tick">/</span> {L[exp]}</h2>{jobs1}</div>
    </td>
  </tr></table>
  <div class="ft">AMANDA · BRITTO <span class="r">{foot} · <span class="v">{LG}</span> · {L[page]} 1 / 2</span></div>
</div>
<div class="page pb">
  <div class="sidebg"></div>
  <table class="cols"><tr>
    <td class="side">
      <div class="sec"><h2><span class="tick">/</span> {L[certs]}</h2><ul class="plain">{certs}</ul></div>
      <div class="sec"><h2><span class="tick">/</span> {L[awards]}</h2><ul class="plain">{awards}</ul></div>
      <div class="sec"><h2><span class="tick">/</span> {L[online]}</h2>{online}</div>
    </td>
    <td class="main">
      <div class="sec"><h2><span class="tick">/</span> {L[cont]}</h2>{jobs2}</div>
      <div class="sec"><h2><span class="tick">/</span> {L[edu]}</h2>{edu}</div>
      {qual}
    </td>
  </tr></table>
  <div class="ft">AMANDA · BRITTO <span class="r">{foot} · <span class="v">{LG}</span> · {L[page]} 2 / 2</span></div>
</div>
</body>
</html>"""

def li(items):    return "".join(f"<li>{x}</li>" for x in items)
def kv(pairs):    return "".join(f'<div class="kv"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in pairs)
def langs_html(lang):
    return "".join(f'<div class="lang">{n}<br><span class="dots">{d}</span></div>' for n, d in LANGS(lang))
def jobs_html(jobs):
    out = []
    for j in jobs:
        bl = "".join(f"<li>{b}</li>" for b in j["b"])
        out.append(f'<div class="job"><div class="t"><b>{j["t"]}</b> <span class="at">— {j["at"]}</span></div>'
                   f'<div class="meta">{j["meta"]}</div><ul>{bl}</ul></div>')
    return "".join(out)
def edu_html(entries):
    return "".join(f'<div class="edu"><div class="d">{d}</div><div class="i">{i}</div></div>' for d, i in entries)

os.makedirs("out", exist_ok=True)
TASKS = []
for pkey, langs in PROFILES.items():
    for lg, d in langs.items():
        L = LABELS[lg]
        core_title = L["general"] if d.get("core_label") == "general" else L["core"]
        qual = ""
        if d.get("qual"):
            qual = (f'<div class="sec"><h2><span class="tick">/</span> {L["qual"]}</h2>'
                    f'<div class="edu"><div class="d">{d["qual"][0]}</div><div class="i">{d["qual"][1]}</div></div></div>')
        html = TPL.format(lang=lg, L=L, LG=lg.upper(), role=d["role"], tag=d["tag"], foot=d["foot"],
                          location=LOCATION_L[lg], phone=PHONE, mail=MAIL, contact_kv=kv(CONTACT),
                          core_title=core_title, core=li(d["core"]), tech=li(d["tech"]),
                          langs=langs_html(lg), certs=li(CERTS[lg]), prof=d["prof"],
                          jobs1=jobs_html(d["jobs1"]), jobs2=jobs_html(d["jobs2"]),
                          awards=li(d["awards"]), online=kv(d["online"]),
                          edu=edu_html(EDU(lg, d["edu_keys"])), qual=qual)
        hpath, ppath = f"out/cv-{pkey}-{lg}.html", f"out/cv-{pkey}-{lg}.pdf"
        with open(hpath, "w", encoding="utf-8") as f:
            f.write(html)
        TASKS.append((hpath, ppath))

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for hpath, ppath in TASKS:
        pg.goto("file://" + os.path.abspath(hpath))
        pg.pdf(path=ppath, width="210mm", height="297mm", print_background=True,
               margin={"top":"0","bottom":"0","left":"0","right":"0"})
        print("OK", ppath)
    b.close()
