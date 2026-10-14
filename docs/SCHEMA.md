# SCHEMA.md — Data Schema (DeepWatch)

**Status:** Defined for DeepWatch
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. Storage
**SQLite** (`data/analysis_log.db`) for the append-only audit trail, plus the
filesystem for evidence and run artifacts. No cloud database — local-first per
PRD NFR-04. Files live under `data/evidence/` (immutable originals) and
`data/runs/` (per-run artifacts).

## 2. Entities

### `evidence_item`
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| id | INTEGER PK | autoincrement | |
| sha256 | TEXT | UNIQUE, NOT NULL | hash computed at ingest |
| original_path | TEXT | NOT NULL | immutable copy location |
| media_type | TEXT | NOT NULL | `image` \| `video` \| `audio` |
| filename | TEXT | nullable | pseudonymised in logs if needed |
| byte_size | INTEGER | NOT NULL | |
| ingested_at | TEXT (ISO-8601) | NOT NULL | |

### `analysis_run`
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| id | TEXT PK | UUID | run identifier |
| evidence_id | INTEGER FK → evidence_item | NOT NULL | |
| status | TEXT | NOT NULL | `queued`/`running`/`done`/`failed` |
| visual_score | REAL | 0.0–1.0 or NULL | manipulation probability |
| audio_score | REAL | 0.0–1.0 or NULL | NULL for non-audio media |
| sync_score | REAL | 0.0–1.0 or NULL | lip–speech consistency |
| fused_score | REAL | 0.0–1.0 or NULL | fused verdict |
| confidence | REAL | 0.0–1.0 | calibrated |
| attribution | TEXT | nullable | method label or `UNSEEN` |
| model_versions | TEXT (JSON) | NOT NULL | {detector, audio, attrib, sync} |
| started_at / finished_at | TEXT (ISO-8601) | NOT NULL | |
| error | TEXT | nullable | failure detail if status=`failed` |

### `analysis_log` (append-only)
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| id | INTEGER PK | autoincrement | never UPDATE/DELETE |
| run_id | TEXT FK → analysis_run | NOT NULL | |
| step | TEXT | NOT NULL | ingest/detect/audio/sync/attribute/fuse/report |
| detail | TEXT (JSON) | | step parameters and outputs |
| logged_at | TEXT (ISO-8601) | NOT NULL | |

### `explanation_map`
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| id | INTEGER PK | autoincrement | |
| run_id | TEXT FK → analysis_run | NOT NULL | |
| kind | TEXT | NOT NULL | `heatmap`/`artifact_region`/`reason` |
| artifact_path | TEXT | | image/text artifact path |
| region | TEXT (JSON) | nullable | bounding region if applicable |

### `report`
| Field | Type | Constraints | Notes |
| --- | --- | --- | --- |
| id | INTEGER PK | autoincrement | |
| run_id | TEXT FK → analysis_run | UNIQUE, NOT NULL | one report per run |
| pdf_path | TEXT | NOT NULL | |
| report_hash | TEXT | NOT NULL | SHA-256 of the PDF |
| anchor_tx | TEXT | nullable | optional test-blockchain tx id |
| generated_at | TEXT (ISO-8601) | NOT NULL | |

## 3. Relationships
- `evidence_item` 1:N `analysis_run` (same evidence can be re-analysed)
- `analysis_run` 1:N `analysis_log`, 1:N `explanation_map`, 1:1 `report`
- No cascades/deletes — the audit trail is immutable by design.

## 4. Migrations & versioning
Schema evolves via versioned SQL migration files in `src/deepwatch/db/migrations/`
applied at startup; recorded in a `schema_version` table.

## 5. Data rules
- `evidence_item.sha256` unique — duplicate uploads deduplicate to the same item.
- Scores constrained to [0.0, 1.0]; NULL where a channel doesn't apply.
- `analysis_log` and `evidence_item.original_path` are write-once — immutability
  is a forensic requirement, not an optimisation.
- Retention: user-controlled deletion of uploads; log entries persist.

> Schema matches ARCHITECTURE §3; changes go through migrations, never manual edits.
