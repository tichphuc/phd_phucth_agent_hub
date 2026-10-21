# PROJECT_STATE.md

## 1. Mục đích

File này lưu trạng thái bền cấp project cho Meow.

Đây là long-term memory, chỉ chứa thông tin tương đối ổn định và có source trỏ
ngược. Không dùng file này để thay thế audit thật hoặc research memo/report.

---

## 2. Project snapshot

```text
Memory status: initialized from project audit
Last verified: 2026-06-09
Source:
- agent_hub/experiments/EXPERIMENT_REGISTRY.md
- agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md
- agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md
- doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md
- doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md
- data/cygnss/df_cyg_vinhlong_phase10_smapl3_truth_input_audit.csv
- data/cygnss/df_cyg_vinhlong_phase10_smapl3_truth_stats_compact.csv
```

### Active project identity

```text
Project type: research repository
Default agent: Meow
Default mode: read -> analyze -> propose -> wait for confirmation
Primary governance layer: agent_hub/
Memo module: agent_hub/memo/
```

### Active experiment

```text
Active experiment: exp_01
Canonical experiment folder: Experiment_01/
Agent-hub folder: agent_hub/experiments/exp_01/
Active rules: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md
Context index: agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md
Primary domain: EC_CYG - GNSS-R salinity estimation via CYGNSS
AOI: Vietnam; Vinh Long bbox primary, Mekong Delta region
```

### Research status

```text
Current research state:
- EC_CYG pipeline has outputs through Phase 9.
- Phase 10 exploratory truth matching output exists for SMAP L3 / SoilGrids branch.
- SMAP L2 3 km / 1 km branches exist as sensitivity branches.

Current blocker:
- Phase 8 dielectric-domain collapse:
  epsilon_real_dobson > epsilon_magnitude
  which makes epsilon_imag = sqrt(epsilon_magnitude^2 - epsilon_real_dobson^2)
  non-real for many samples.

Validated result status:
- No output is currently marked as Validated.
- Phase 9 and Phase 10 are exploratory unless a later validation memo/report says otherwise.
```

### Notebook state

```text
Experiment_01/01_CYGNSS_extraction.ipynb:
  Status: completed / basically stable
  Role: CYGNSS netCDF extraction and point tabulation

Experiment_01/02_Data_Querying.ipynb:
  Status: completed / basically stable
  Role: collocation and ancillary data querying

Experiment_01/03.0_EC_CYG_SMAPL3.ipynb:
  Status: active / needs update
  Role: closest current baseline branch for SMAP L3 9 km

Experiment_01/03.0_EC_CYG_SMAPL2.ipynb:
  Status: active / sensitivity branch
  Role: SMAP L2_SM_SP 3 km / 1 km branch

Experiment_01/03.1_SMAP_L3SMPE_Process.ipynb:
  Status: active / support
  Role: SMAP L3 Enhanced processing

Root notebook/:
  Status: legacy / reference only
  Rule: do not use as active pipeline unless user explicitly asks
```

### Output state

```text
Phase 9 EC-ready rows:
- 9 km SoilGrids: A = 161, AB = 317
- L2 3 km SoilGrids: A = 213, AB = 454
- L2 1 km SoilGrids: A = 266, AB = 667

Phase 10 exploratory truth matching:
- field_truth_cleaned rows = 428
- truth date range = 2021-01-01 to 2022-03-20
- smap_l3_phase9s_soilgrids rows: A = 161, AB = 317
- rows inside truth date range: A = 47, AB = 103
- rows inside truth Jan-Mar: A = 18, AB = 45

Phase 10 compact stats:
- A, point_nearest_station, all: n = 18, Pearson = -0.0688, Spearman = -0.0445
- AB, point_nearest_station, all: n = 45, Pearson = -0.1710, Spearman = -0.2026
- A, point_nearest_station, distance <= 10 km: n = 5, Pearson = 0.7935, Spearman = 0.7826
- AB, grid_time_0p1deg, same_or_neighbor_1cell: n = 22, Pearson = 0.1210, Spearman = -0.0544

Safe interpretation:
- Phase 10 is useful as exploratory diagnostic.
- The high A <= 10 km correlation is too small-sample to be treated as validation.
```

### Repo/governance status

```text
Governance status:
- agent_hub governance active.
- Meow Memo Module integrated into MEOW_AGENT.md and AGENT_HUB_MANIFEST.md.
- RULE_REGISTRY.md registers agent_hub/memo/.
- DOC_INDEX.md registers doc/memo/ references.

Git/data status from 2026-06-09 audit:
- Worktree has many untracked project folders/files.
- No .gitignore detected during audit.
- data/cygnss is very large, about 195.77 GB.
- data/SMAP_L2_SM_SP is about 13.53 GB.
- data/SMAP_L3_SM_P_E_subsetted is about 10.69 GB.

Known hygiene gaps:
- agent_hub/experiments/EXPERIMENT_TEMPLATE.md is 0 bytes.
- Experiment_01/AGENTS.md is legacy and points to old doc paths.
- KRU_AGENT.md appeared in IDE tabs but was not found in workspace during audit.
- sources/ is missing while sources_old/ exists.
- several __pycache__ folders exist.
- hwt_gd docs say raster data not included, but sample folder contains GeoTIFFs.
```

---

## 3. Staleness rule

File này phải được xem là stale nếu:

* `EXPERIMENT_REGISTRY.md` thay đổi;
* active rules hoặc context index của experiment thay đổi;
* research memo/report mới được cập nhật;
* notebook canonical đổi;
* user xác nhận một decision mới ảnh hưởng project state;
* git/data layout thay đổi lớn.
