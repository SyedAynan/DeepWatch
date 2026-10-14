# APPFLOW.md — Application Flow (DeepWatch)

**Status:** Defined for DeepWatch
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. Entry points & user roles
- **Primary:** local web UI at `http://localhost:8000` — a user uploads media
  in a browser; all analysis stays on the machine.
- **Secondary:** CLI (`uv run deepwatch analyze <file>`) for batch/dev use and
  the evaluation harness (`uv run eval --benchmark <name>`).
- Roles: single local user (no auth in v1 — localhost binding only).

## 2. Screen / surface inventory
- `upload` — drag-drop/file picker, media-type detection, consent note
- `run_status` — live progress of the analysis pipeline (per-channel steps)
- `results` — fused verdict + per-channel scores + calibrated confidence
- `evidence` — attribution label/abstention + explanation heatmaps + reasons
- `report` — PDF download + report hash + optional anchor status
- `history` — past runs listed by evidence hash (audit view)

## 3. Primary flows

**Flow: analyse a suspicious video**
1. User drops a video onto `upload`; UI shows the file's SHA-256 being computed
2. System preserves the original, logs ingest, splits frames + audio
3. `run_status` streams progress: visual → audio → sync → attribution → fuse
4. `results` shows fused verdict with confidence and per-channel scores
5. `evidence` shows heatmaps, region callouts, plain-language reasons, and the
   attribution result (method label or explicit `unseen`)
6. `report` offers the forensic PDF; optional blockchain hash anchor shown
7. Run appears in `history` keyed by evidence hash

**Flow: evaluate against a benchmark**
1. Developer runs `uv run eval --benchmark ff++`
2. Harness iterates the split, aggregates AUC/EER, prints FP/FN separately
3. Results written to `eval/results.md` for the docs

## 4. Alternate & error paths
- **Unreadable/corrupt media:** ingest fails → clear "unsupported file" state,
  no score fabricated (RULES: never invent results)
- **No audio track (or no face):** channel returns NULL; verdict is computed
  from available channels and the UI states which channels were analysed
- **Model failure mid-run:** run marked `failed` with the step that errored;
  UI never shows a confident default score
- **Attribution low-confidence:** explicit `unseen` abstention shown, not a
  guessed label
- **Duplicate upload:** same SHA-256 → option to reuse the existing run

## 5. Navigation map
```
upload ──→ run_status ──→ results ──→ evidence ──→ report
   └────────────── history ──────────┘  (revisit any past run by hash)
```

## 6. Session & state behavior
- Stateless frontend; run state lives in `analysis_run` (SCHEMA.md)
- Refresh-safe: `run_status`/`results` reload from the API by run id
- No login; localhost-only binding; uploads persist until the user deletes them
- Audit log is append-only — closing the app never loses traceability
