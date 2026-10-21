# ISSUE_MEMORY.md

## 1. Mục đích

File này lưu issue/risk dài hạn còn mở để Meow không phải quét lại toàn bộ
project khi người dùng hỏi tình trạng.

Issue trong file này phải trỏ về source canonical và không được thổi phồng thành
kết luận khoa học.

---

## 2. Issue schema

```text
Issue ID:
Status:
Severity:
Scope:
Summary:
Source:
Evidence:
Current safe interpretation:
Blocked actions:
Recommended next check:
Staleness rule:
```

---

## 3. Issues

### EXP01-ISSUE-P8-DOMAIN-COLLAPSE

```text
Status: Open
Severity: MAJOR / scientific blocker
Scope: EC_CYG Phase 8
Summary: Most samples fail because epsilon_real_dobson > epsilon_magnitude.
Source:
- agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-08
- doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-P8-DOMAIN-COLLAPSE
- doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md §4
Evidence:
- 9 km SoilGrids blocked rate: A 98.24%, AB 99.19%
- L2 3 km blocked rate: A 95.44%, AB 97.58%
- L2 1 km blocked rate: A 94.53%, AB 96.74%
Current safe interpretation: Phase 8 is the main scientific bottleneck; do not bypass the gate.
Blocked actions: no silent gate loosening, no calling Phase 9/10 validated.
Recommended next check: Dobson formula audit, soil moisture sensitivity, Phase 6 correction sensitivity, Fresnel model audit.
Staleness rule: stale if formula/correction baseline changes or new validation report supersedes it.
```

### EXP01-ISSUE-DOBSON-FORMULA-AUDIT

```text
Status: Open
Severity: MAJOR
Scope: EC_CYG Phase 8
Summary: Need to audit Dobson/Jundong real dielectric formula, especially possible -m_v term and unit handling.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-DOBSON-FORMULA-AUDIT
Evidence: Memo records formula uncertainty and says any change must be sensitivity, not silent baseline overwrite.
Current safe interpretation: formula issue is a candidate cause, not a confirmed fix.
Blocked actions: do not edit baseline formula without source audit and user confirmation.
Recommended next check: compare notebook formula against source notes/papers and run isolated sensitivity.
Staleness rule: stale after formula audit is documented.
```

### EXP01-ISSUE-SMAP-SOIL-MOISTURE-REPRESENTATIVENESS

```text
Status: Open hypothesis
Severity: MAJOR
Scope: SMAP / Dobson input
Summary: SMAP soil moisture may push epsilon_real_dobson too high, but this is not proven.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-SMAP-SOIL-MOISTURE-REPRESENTATIVENESS
Evidence: Memo notes L2 median soil moisture around 0.54 m3/m3 and L2 epsilon_real_dobson median around 34 while epsilon_magnitude median is around 4.8-4.9.
Current safe interpretation: plausible hypothesis; not a conclusion that SMAP is the cause.
Blocked actions: do not claim SMAP is the sole cause.
Recommended next check: soil moisture sensitivity with fixed epsilon_magnitude.
Staleness rule: stale after soil moisture sensitivity is documented.
```

### EXP01-ISSUE-L2-TAU-ROUGHNESS-CORRECTION

```text
Status: Open
Severity: MAJOR
Scope: Phase 6 correction
Summary: L2 tau/roughness correction uses an implementation choice that needs sensitivity.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-L2-TAU-ROUGHNESS-CORRECTION
Evidence: Memo says tau normalization with cos(40 deg) is a technical inference, not a directly sourced Wang formula.
Current safe interpretation: keep as implementation choice/sensitivity, not source-backed formula.
Blocked actions: do not present tau normalization as source-backed if not audited.
Recommended next check: no-correction, roughness-only, vegetation-only, full-correction sensitivity.
Staleness rule: stale after correction sensitivity or source audit.
```

### EXP01-ISSUE-FRESNEL-SCALAR-INVERSION

```text
Status: Open
Severity: MAJOR
Scope: Phase 7 Fresnel inversion
Summary: epsilon_magnitude is an effective scalar from power inversion, not a full complex dielectric retrieval.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-FRESNEL-SCALAR-INVERSION
Evidence: Memo records solver range and warns coherent/incoherent mixture, roughness, footprint heterogeneity, water/vegetation, or mismatch can lower scalar epsilon.
Current safe interpretation: audit model/correction before interpreting low epsilon_magnitude physically.
Blocked actions: do not over-interpret epsilon_magnitude as full dielectric constant.
Recommended next check: audit polarization equation, dB/linear units, theta units, solver residuals.
Staleness rule: stale after Fresnel model audit.
```

### EXP01-ISSUE-P9-WANG-TRANSFERABILITY

```text
Status: Open
Severity: MAJOR
Scope: Phase 9 EC conversion
Summary: Wang/YRD empirical conversion may not transfer directly to Vinh Long.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §ISSUE-P9-WANG-TRANSFERABILITY; EC_CYG_TECHNICAL_REPORT_20260602.md §5
Evidence: EC above Wang reference max remains high: 9 km SoilGrids A 87.58%, AB 84.23%; L2 1 km AB 54.72%.
Current safe interpretation: Phase 9 is exploratory and needs truth validation/local calibration.
Blocked actions: do not call Phase 9 a calibrated EC product.
Recommended next check: local calibration or robust Phase 10 validation.
Staleness rule: stale after calibration/validation report.
```

### EXP01-ISSUE-P10-VALIDATION-WEAK

```text
Status: Open
Severity: MAJOR
Scope: Phase 10 validation
Summary: Phase 10 matching exists but does not yet support validated-result status.
Source:
- data/cygnss/df_cyg_vinhlong_phase10_smapl3_truth_input_audit.csv
- data/cygnss/df_cyg_vinhlong_phase10_smapl3_truth_stats_compact.csv
Evidence:
- A point_nearest_station all: n = 18, Pearson = -0.0688, Spearman = -0.0445
- AB point_nearest_station all: n = 45, Pearson = -0.1710, Spearman = -0.2026
- A distance <= 10 km: n = 5, Pearson = 0.7935, Spearman = 0.7826, but sample size is too small
- AB grid same_or_neighbor_1cell: n = 22, Pearson = 0.1210, Spearman = -0.0544
Current safe interpretation: useful exploratory validation diagnostic; not validated result.
Blocked actions: do not use tiny-n positive correlation as final validation.
Recommended next check: expand truth matching, define acceptance criteria, report RMSE/MAE/bias with sufficient n.
Staleness rule: stale after Phase 10 report is updated.
```

### GOV-ISSUE-REPO-HYGIENE

```text
Status: Open
Severity: MINOR to MAJOR depending on commit/data plan
Scope: repo governance / data management
Summary: Worktree contains large untracked data and lacks .gitignore; several legacy/cache artifacts remain.
Source: project audit on 2026-06-09
Evidence:
- data/cygnss about 195.77 GB
- data/SMAP_L2_SM_SP about 13.53 GB
- data/SMAP_L3_SM_P_E_subsetted about 10.69 GB
- no .gitignore detected during audit
- multiple __pycache__ folders
Current safe interpretation: handle before any clean commit or packaging.
Blocked actions: do not mass-delete or move data without explicit user decision.
Recommended next check: create data/git hygiene plan and .gitignore proposal.
Staleness rule: stale after git hygiene cleanup.
```

### GOV-ISSUE-MISSING-TEMPLATE

```text
Status: Open
Severity: MINOR
Scope: agent_hub experiments
Summary: agent_hub/experiments/EXPERIMENT_TEMPLATE.md is empty but registered as template draft.
Source: project audit on 2026-06-09; RULE_REGISTRY.md
Evidence: file size was 0 bytes during audit.
Current safe interpretation: template needs content before future experiment onboarding.
Blocked actions: do not create new experiment from empty template.
Recommended next check: fill template after user approval.
Staleness rule: stale after template is populated.
```

### GOV-ISSUE-CANONICAL-NOTEBOOK-NAME

```text
Status: Open
Severity: MINOR
Scope: exp_01 routing
Summary: Active rules mention 03_EC_CYG.ipynb, but actual current notebooks are split into 03.0_EC_CYG_SMAPL3 and 03.0_EC_CYG_SMAPL2.
Source: EXP01_ACTIVE_RULES.md §5; EXP01_CONTEXT_INDEX.md §5
Evidence: Context index notes no plain 03_EC_CYG.ipynb exists and treats SMAPL3 as closest baseline.
Current safe interpretation: use SMAPL3 as closest baseline and SMAPL2 as sensitivity until user confirms canonical naming.
Blocked actions: do not assume a missing 03_EC_CYG.ipynb is active.
Recommended next check: update active rules/context or rename/canonicalize only after user decision.
Staleness rule: stale after canonical notebook is confirmed.
```
