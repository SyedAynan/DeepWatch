# DESIGN.md — UI/UX Design System (DeepWatch)

**Status:** Defined for DeepWatch (applied in Phase 3 when the web UI is built)
**Created:** 2026-10-07
**Updated:** 2026-10-14

- **Visual direction:** forensic-lab aesthetic — clinical, precise, evidence-first.
  Dark navy base with cyan/teal accents (matches `assets/banner.png`).
- **Theme / colors:** `#0b3d66` primary, `#00F0FF` accent, `#00E676` authentic
  pass, `#FF5252` manipulated alert, `#161b22` surfaces, `#f2f6fa` light panels.
- **Typography:** system sans for UI (Segoe UI/Inter); monospace for hashes and
  model-version strings (JetBrains Mono / Consolas).
- **Spacing / layout:** single-column analysis flow (upload → status → results);
  8px spacing grid; max content width ~1100px.
- **Components:**
  - Drop zone (dashed border; SHA-256 hash computed on drop)
  - Channel score cards (visual / audio / sync) with verdict chips
  - Confidence meter with labelled bands (never a bare number)
  - Heatmap overlay viewer with region callouts
  - Verdict banner: `LIKELY AUTHENTIC` / `INDICATORS OF MANIPULATION` /
    `INCONCLUSIVE — needs human review` (never binary-only)
  - Report card (PDF download + report hash + optional anchor status)
  - History table keyed by evidence hash
- **Responsive behavior:** desktop-first (analysis tool); usable to tablet
  widths; no mobile-specific layout in v1.
- **Accessibility:** WCAG-AA contrast; verdict uses color + text (never
  color-only); keyboard-operable flow; alt text on all evidence images.
- **Loading / empty / error / success states:**
  - Loading: per-channel progress checklist (not a spinner alone)
  - Empty: "No analyses yet" with upload CTA
  - Error: the failed step is named explicitly; no fabricated scores
  - Success: verdict banner + evidence + report CTA
- **Animation guidelines:** subtle transitions only (< 200ms); heatmap fade-in;
  no decorative motion on forensic surfaces.
