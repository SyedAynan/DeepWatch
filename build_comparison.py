import json, html
from collections import Counter

papers = json.load(open('.research/papers_raw.json', encoding='utf-8'))

AREA_LIMIT = {
 "A_cnn_vit_detection":  ("Single-frame visual detection only; degrades cross-dataset; no explanation, no audio, no attribution, no evidence output.","Adds audio fusion, attribution, explainable evidence, integrity logging, calibrated abstention."),
 "B_face_swap":          ("Generator/detector for face swaps only; no audio channel, no source attribution, no forensic report.","Adds multimodal fusion + open-set attribution + tamper-evident reporting."),
 "C_ai_generated_image": ("Detects AI images but is generator-bound; no video/audio; no provenance or evidence layer.","Adds cross-generator robustness eval + AV fusion + forensic report."),
 "C2_synthetic_image":   ("Artifact/fingerprint-bound detection; fails on unseen generators; no explanation for users.","Adds diffusion-aware detection + explainable evidence + integrity ledger."),
 "D_video_temporal":     ("Temporal/frame analysis only; no audio channel, no attribution, no evidence preservation.","Adds audio-video fusion + attribution + forensic reporting."),
 "E_audio_deepfake":     ("Audio-only detection; degrades cross-corpus; never fused with visual channel.","Adds audio-video fusion + visual detection + explainable evidence."),
 "E2_antispoofing":      ("Face/voice anti-spoofing alone; not deepfake forensics; no AV consistency or report.","Adds unified AV forensics + attribution + evidence ledger."),
 "F_multimodal_av":      ("AV fusion exists but mostly unimodal benchmarks; no attribution, no forensic report, no abstention.","Adds calibrated fusion + open-set attribution + integrity reporting."),
 "G_frequency_domain":   ("Frequency/spatial artifact detection only; artifact-bound; no fusion/attribution/report.","Adds multimodal fusion + explainable evidence + forensic ledger."),
 "H_explainable_xai":    ("Produces explanations/heatmaps but rarely validates faithfulness; no detection+attribution+report unity.","Adds faithfulness-measured explanations + fused verdict + forensic PDF."),
 "I_attribution":        ("Attribution alone - no detection fusion, no explainability for users, no evidence output.","Adds detection+fusion+explain+report around attribution, with abstention."),
 "I2_model_attr":        ("Generator/model attribution only; narrow scope; no full forensic pipeline.","Adds open-set abstaining attribution inside a full pipeline."),
 "K_adversarial_robust": ("Shows detectors are attackable, or defends narrowly; no unified forensic platform.","Adds robustness evaluation + honest FP/FN + integrity logging."),
 "L_uncertainty_calib":  ("Sparse dedicated work; detectors mostly uncalibrated, no abstention.","Adds calibrated confidence + explicit 'inconclusive' verdict."),
 "M_provenance":         ("Provenance/watermark/C2PA focus - verifies origin metadata, not AI-manipulation analysis.","Adds analysis-driven detection+attribution+explain, optionally hash-anchored."),
 "N_efficient":          ("Lightweight/edge detectors trade accuracy for speed; no forensic features.","Adds full forensic pipeline; efficiency handled as deployment constraint."),
 "O_benchmarks":         ("Provides datasets/eval protocols, not an end-user forensic tool.","We consume these benchmarks to evaluate DeepWatch honestly."),
}
AREA_LABEL = {
 "A_cnn_vit_detection":"A. CNN/ViT deepfake detection","B_face_swap":"B. Face swap / manipulation",
 "C_ai_generated_image":"C. AI-generated image detection","C2_synthetic_image":"C2. Synthetic-image fingerprints",
 "D_video_temporal":"D. Video temporal analysis","E_audio_deepfake":"E. Audio deepfake detection",
 "E2_antispoofing":"E2. Face/voice anti-spoofing","F_multimodal_av":"F. Multimodal audio-video",
 "G_frequency_domain":"G. Frequency-domain analysis","H_explainable_xai":"H. Explainable AI",
 "I_attribution":"I. Source/generator attribution","I2_model_attr":"I2. Model attribution",
 "J_generalization":"J. Generalization","K_adversarial_robust":"K. Adversarial robustness",
 "L_uncertainty_calib":"L. Uncertainty/calibration","M_provenance":"M. Provenance & authenticity",
 "N_efficient":"N. Efficient/lightweight","O_benchmarks":"O. Benchmarks & eval",
}

def doi_link(p):
    d = p.get('doi') or ''
    if d.startswith('http'): return d
    if d.startswith('10.'): return 'https://doi.org/'+d
    return ''

areas_legend = "".join(
    "<li><b>"+AREA_LABEL.get(k,k)+"</b> — "+str(v)+" papers</li>"
    for k,v in Counter(p['q'] for p in papers).items())

rows = []
for i,p in enumerate(papers,1):
    q = p['q']; lim,adds = AREA_LIMIT.get(q,("-","-"))
    authors = ', '.join(p.get('authors',[])[:3]) + (' et al.' if len(p.get('authors',[]))>3 else '')
    link = doi_link(p) or (p.get('arxiv') or '')
    ieee = '&#9733;' if p['ieee'] else ''
    row = ("<tr><td class='num'>"+str(i)+"</td>"
           "<td><b>"+html.escape(p['title'])+"</b><br>"
           "<span class='meta'>"+html.escape(authors)+" &middot; "+str(p['year'])+" &middot; "+html.escape((p['venue'] or '')[:60])+" "+ieee+"</span><br>"
           "<span class='doi'>"+html.escape(link)+"</span></td>"
           "<td class='lim'>"+html.escape(lim)+"</td>"
           "<td class='add'>"+html.escape(adds)+"</td></tr>")
    rows.append(row)

html_doc = """<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
@page { size: A4 landscape; margin: 12mm; }
*{box-sizing:border-box}
body{font-family:"Helvetica Neue",Arial,sans-serif;font-size:8pt;color:#1a1a1a;margin:0}
h1{font-size:15pt;color:#0b3d66;margin:0 0 2pt}
h2{font-size:10.5pt;color:#0b3d66;border-bottom:1px solid #0b3d66;margin:8pt 0 3pt;padding-bottom:1pt}
.sub{font-size:9pt;color:#555;margin-bottom:4pt}
table{width:100%;border-collapse:collapse}
th{background:#0b3d66;color:#fff;text-align:left;padding:2.5pt 3.5pt;font-size:7.8pt}
td{border-bottom:0.5pt solid #cfd8e0;padding:2.5pt 3.5pt;vertical-align:top}
tr:nth-child(even){background:#f6f9fc}
.num{width:14pt;color:#666} .meta{color:#555;font-size:7.4pt} .doi{color:#0b3d66;font-size:7pt}
.lim{width:34%} .add{width:34%}
ul{margin:2pt 0;padding-left:14pt} li{margin-bottom:1pt}
.note{background:#f2f6fa;border-left:3pt solid #0b3d66;padding:5pt 8pt;margin:5pt 0;font-size:8.4pt}
</style></head><body>
<h1>DeepWatch - Complete Literature Corpus vs Project Comparison</h1>
<div class="sub">Prepared and researched by: <b>Syed</b> &middot; 14 October 2026 &middot; """ + str(len(papers)) + """ verified papers (OpenAlex/Crossref-verified, DOIs included)</div>
<div class="note"><b>How to read this table.</b> Column "Limitation vs this project" states what each paper <i>does not cover</i> relative to DeepWatch's unified scope (detection + audio-video fusion + attribution + explainability + forensic integrity). It is a <b>scope/capability comparison</b>, not a criticism of the papers' quality - the base papers are the foundation we build on. &#9733; = IEEE-flagged venue.</div>
<h2>Research-area distribution</h2><ul>""" + areas_legend + """</ul>
<h2>Full paper-by-paper comparison</h2>
<table><tr><th>#</th><th>Paper (title &middot; authors &middot; year &middot; venue &middot; DOI/link)</th><th>Limitation vs this project</th><th>What DeepWatch adds</th></tr>""" + "".join(rows) + """</table>
<div class="note"><b>Honest note:</b> this comparison reflects each paper's <i>scope</i> relative to DeepWatch's integrated goal. Detection papers are not "worse" - they are the components we reproduce and measure against. DeepWatch's claim is <b>integration + integrity + honest evaluation</b>, not a novel detection algorithm.</div>
</body></html>"""

with open('docs/LITERATURE_COMPARISON.html','w',encoding='utf-8') as f:
    f.write(html_doc)
print("Wrote docs/LITERATURE_COMPARISON.html with", len(papers), "papers")
