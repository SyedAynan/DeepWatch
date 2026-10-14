import json, urllib.request, time

UA = {"User-Agent": "DeepWatchResearch/1.0 (mailto:research@example.com)"}

QUERIES = {
    "A_cnn_vit_detection": 'title.search:"deepfake detection"',
    "B_face_swap": 'title.search:"face swap"',
    "C_ai_generated_image": 'title.search:"AI-generated image"',
    "C2_synthetic_image": 'title.search:"generated image detection"',
    "D_video_temporal": 'title.search:"deepfake temporal"',
    "E_audio_deepfake": 'title.search:"audio deepfake"',
    "E2_antispoofing": 'title.search:"anti-spoofing"',
    "F_multimodal_av": 'title.search:"multimodal deepfake"',
    "G_frequency_domain": 'title.search:"frequency deepfake"',
    "H_explainable_xai": 'title.search:"explainable deepfake"',
    "I_attribution": 'title.search:"deepfake attribution"',
    "I2_model_attr": 'title.search:"generator attribution"',
    "J_generalization": 'title.search:"deepfake generalizable"',
    "K_adversarial_robust": 'title.search:"adversarial deepfake"',
    "L_uncertainty_calib": 'title.search:"uncertainty deepfake"',
    "M_provenance": 'title.search:"media provenance"',
    "M2_c2pa": 'title.search:"content authenticity"',
    "N_efficient": 'title.search:"lightweight deepfake"',
    "O_benchmarks": 'title.search:"deepfake benchmark"',
}

seen = {}
for key, filt in QUERIES.items():
    url = ("https://api.openalex.org/works?filter=" + filt +
           ",from_publication_date:2019-01-01&per-page=6"
           "&select=title,authorships,publication_year,doi,primary_location,cited_by_count,ids,type,abstract_inverted_index")
    url = url.replace(" ", "%20")
    try:
        req = urllib.request.Request(url, headers=UA)
        d = json.loads(urllib.request.urlopen(req, timeout=30).read())
        for w in d.get("results", []):
            t = (w.get("title") or "").strip()
            if not t or t.lower() in seen:
                continue
            src = (w.get("primary_location") or {}).get("source") or {}
            venue = src.get("display_name") or "?"
            pub = (src.get("host_organization_name") or "").lower()
            is_ieee = "ieee" in pub or "ieee" in venue.lower() or "ieeexplore" in venue.lower()
            auth = [a["author"]["display_name"] for a in (w.get("authorships") or [])][:8]
            seen[t.lower()] = {
                "title": t, "authors": auth, "year": w.get("publication_year"),
                "venue": venue, "ieee": is_ieee, "doi": w.get("doi"),
                "cites": w.get("cited_by_count"), "type": w.get("type"),
                "abs": bool(w.get("abstract_inverted_index")), "q": key,
            }
    except Exception as e:
        print("FAIL", key, e)
    time.sleep(1)

papers = sorted(seen.values(), key=lambda p: (p["q"], -(p["cites"] or 0)))
json.dump(papers, open(".research/papers_raw.json","w"), indent=1)
ieee = sum(1 for p in papers if p["ieee"])
print(f"TOTAL: {len(papers)} | IEEE-flagged: {ieee}")
for p in papers:
    m = "IEEE" if p["ieee"] else "    "
    print(f"{m} [{p['q'][:16]:16}] {p['year']} | {p['title'][:70]}")
