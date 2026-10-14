-- DeepWatch append-only analysis log schema (see docs/SCHEMA.md)
CREATE TABLE IF NOT EXISTS evidence_item (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  sha256        TEXT UNIQUE NOT NULL,
  original_path TEXT NOT NULL,
  media_type    TEXT NOT NULL,
  filename      TEXT,
  byte_size     INTEGER NOT NULL,
  ingested_at   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS analysis_run (
  id            TEXT PRIMARY KEY,
  evidence_id   INTEGER NOT NULL REFERENCES evidence_item(id),
  status        TEXT NOT NULL CHECK(status IN ('queued','running','done','failed')),
  visual_score  REAL,
  audio_score   REAL,
  sync_score    REAL,
  fused_score   REAL,
  confidence    REAL,
  attribution   TEXT,
  model_versions TEXT NOT NULL,           -- JSON: {detector, audio, attrib, sync}
  started_at    TEXT NOT NULL,
  finished_at   TEXT,
  error         TEXT
);

CREATE TABLE IF NOT EXISTS analysis_log (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id     TEXT NOT NULL REFERENCES analysis_run(id),
  step       TEXT NOT NULL,               -- ingest/detect/audio/sync/attribute/fuse/report
  detail     TEXT,                        -- JSON: step parameters + outputs
  logged_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS explanation_map (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id       TEXT NOT NULL REFERENCES analysis_run(id),
  kind         TEXT NOT NULL,             -- heatmap | artifact_region | reason
  artifact_path TEXT,
  region       TEXT                       -- JSON bounding region
);

CREATE TABLE IF NOT EXISTS report (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  run_id       TEXT UNIQUE NOT NULL REFERENCES analysis_run(id),
  pdf_path     TEXT NOT NULL,
  report_hash  TEXT NOT NULL,
  anchor_tx    TEXT,                      -- optional test-blockchain tx id
  generated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS schema_version (
  version INTEGER PRIMARY KEY,
  applied_at TEXT NOT NULL
);
