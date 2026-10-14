# Deepfake Forensics: A Research-Led Selection of a Mini-Project Direction

**Prepared and researched by: Syed**
**Date: 14 October 2026**

---

## Executive Summary

This report documents a structured research exercise to select a computer-science mini-project that is technically strong, novel, and relevant to a real-world problem. Seven candidate domains were considered — artificial intelligence, neural networks, computer vision, cybersecurity, blockchain/cryptography, and computer networks. A systematic literature scan of recent (2022–2026) publications, including verified IEEE venues, led to a clear conclusion: the most pressing and under-served problem of the current technology era is the detection and forensic attribution of deepfakes. The selected direction is **DeepWatch**, an AI deepfake forensics and attribution platform that unifies detection, attribution, explanation, and report generation — a combination not present in any single published system reviewed.

## 1. Introduction

Generative AI can now produce synthetic voices, faces, and videos that are difficult for humans to identify as fake. This capability is being misused for financial scams, misinformation, and identity fraud, affecting ordinary citizens worldwide. For a student project to matter in this era, it should address a problem people actually face. This report explains how that reasoning, combined with evidence from current research, produced the chosen project direction.

## 2. Research Objectives

The exercise had four objectives: (1) survey candidate technology domains and identify which offer fresh, demonstrable project opportunities; (2) locate credible, recent base papers — preferably in IEEE venues — to anchor the project; (3) identify concrete gaps in those papers that a student project can realistically close; and (4) define a project whose improvement over prior work is measurable, not cosmetic.

## 3. Methodology

The research proceeded in four stages. First, broad domain scans were run against the arXiv open repository (export.arxiv.org API) across AI, computer vision, cybersecurity, blockchain, networks, and medical technology, covering 2023–2026 publications. Second, candidate topics repeatedly found to be saturated (for example, plant disease classification and basic disease prediction, both reporting accuracies above 99% in 2026 papers) were eliminated because they leave no room for improvement claims. Third, IEEE-venue verification was performed through the OpenAlex and Crossref scholarly APIs, after direct access to IEEE Xplore was found to be restricted by anti-automation controls. Fourth, the surviving base papers were read in detail to extract their methods, datasets, reported results, and limitations.

## 4. Background

Deepfake detection is an active research area, but it is fragmented. Detection (deciding whether media is fake), attribution (identifying which generation method produced it), and explanation (showing evidence a non-expert can understand) are treated as separate problems in separate papers. Meanwhile, the misuse of synthetic media has moved from laboratories into everyday crime, including voice-clone scam calls and fake video evidence. A tool that combines the full forensic chain — detect, attribute, explain, report — does not currently exist in the reviewed literature.

*(Page 1 of 2)*

---

## 5. Key Research Findings

The literature scan produced three verified IEEE/CVF findings of direct relevance. First, Yan et al. (ICCV 2023) proposed UCF, a generalizable detector that separates "common forgery features" from method-specific ones; it achieves 0.996 AUC within its training dataset but only 0.828 average AUC on unseen datasets — a large, openly visible generalization gap [1]. Second, Sun et al. (ICCV 2023) introduced open-world deepfake attribution (OW-DFA), showing that identifying the forgery method is possible even for attacks unseen during training, but only for face forgeries and with limited accuracy [2]. Third, the attribution field is young: the two leading IEEE attribution papers (IEEE ICIP 2022; ICCV 2023) have roughly 27–29 citations each, compared with 200+ for detection papers — indicating that attribution is an open frontier where a student contribution is realistic [2][3]. On the audio side, the ASVspoof 2021 benchmark (IEEE/ACM TASLP) confirms that speech spoofing is treated separately from video, leaving cross-modal video-call forensics unaddressed [4].

## 6. Analysis

These findings expose five exploitable gaps: (a) detectors trained on GAN-era fakes generalize poorly to newer diffusion-based generators; (b) audio and video detection are never fused, although real fake video calls contain both; (c) no reviewed system produces human-readable evidence reports suitable for police or legal use; (d) detectors output bare scores without explanation; and (e) attribution is accurate only within narrow, face-only settings. A project that closes even two or three of these gaps, while standing on published IEEE methods, can claim measurable novelty rather than a re-implementation.

## 7. Challenges

Three challenges are anticipated. Generalization remains the hardest open problem in the field, so improvement targets must be modest and honestly measured. Diffusion-generated fakes require suitable public datasets, which are newer and less standardized than FaceForensics++. Finally, IEEE full texts are paywalled; the project relies on authors' open arXiv versions, which carry identical technical content.

## 8. Recommendations

It is recommended to (1) adopt UCF [1] and the OW-DFA attribution framework [2] as the twin base papers; (2) target diffusion-aware detection and audio–video fusion as the primary innovations; (3) add an explainability layer and one-click forensic report generation as differentiating features; and (4) evaluate against the base papers' published numbers so the improvement is verifiable.

## 9. Conclusion

The research confirms that deepfake forensics — specifically the unification of detection, attribution, explanation, and reporting — is a fresh, high-impact, and feasible direction for a mini-project. It addresses a real-world problem affecting ordinary people today, rests on credible IEEE/CVF foundations, and offers clearly identifiable gaps that a focused student project can close. The direction, named **DeepWatch**, is therefore selected for implementation.

## References

[1] Z. Yan, Y. Zhang, Y. Fan, B. Wu, "UCF: Uncovering Common Features for Generalizable Deepfake Detection," IEEE/CVF ICCV 2023. DOI: 10.1109/ICCV51070.2023.02048 · https://arxiv.org/abs/2304.13949

[2] Z. Sun et al., "Contrastive Pseudo Learning for Open-World DeepFake Attribution," IEEE/CVF ICCV 2023. https://arxiv.org/abs/2309.11132

[3] S. Jia, X. Li, S. Lyu, "Model Attribution of Face-Swap Deepfake Videos," IEEE ICIP 2022. (Indexed via OpenAlex: https://api.openalex.org)

[4] X. Liu et al., "ASVspoof 2021: Towards Spoofed and Deepfake Speech Detection in the Wild," IEEE/ACM Trans. Audio, Speech, and Language Processing, 2023. (Indexed via OpenAlex: https://api.openalex.org)

[5] arXiv open repository, domain scans Oct 2026: https://export.arxiv.org/api/query

*(Page 2 of 2)*
