# DECISION_MEMORY.md

## 1. Mục đích

File này lưu các decision dài hạn đã được người dùng hoặc rule active xác nhận.

Không ghi `IDEA`, `RISK`, hoặc proposal chưa được chốt vào đây như decision.

---

## 2. Decision schema

```text
Decision ID:
Status:
Date confirmed:
Scope:
Decision:
Source:
Evidence:
Does not imply:
Staleness rule:
```

---

## 3. Decisions

### EXP01-DEC-01

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: EC_CYG baseline
Decision: Baseline follows STEP 0 -> STEP 7.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-02
Evidence: Active rule explicitly defines STEP 0 through STEP 7 as baseline order.
Does not imply: Baseline is scientifically validated.
Staleness rule: stale if EXP01_ACTIVE_RULES.md or baseline skeleton changes.
```

### EXP01-DEC-02

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: DDM quality / LES-TES
Decision: LES/TES are DDM quality and waveform-shape indicators, not direct salinity predictors.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-04
Evidence: Active rule forbids using LES/TES as direct salinity predictors without new scientific basis and decision.
Does not imply: LES/TES cannot be used for uncertainty or QC.
Staleness rule: stale if user confirms a new LES/TES role.
```

### EXP01-DEC-03

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: EC_CYG baseline correction
Decision: Do not replace SMAP roughness/vegetation in the baseline with DeltaDTM, optical variables, L2_SM_SP, terrain, or proxy variables without a new confirmed decision.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-05
Evidence: Active rule limits these variables to diagnostic, uncertainty, sensitivity, comparison, or support roles.
Does not imply: These variables cannot be tested in sensitivity branches.
Staleness rule: stale if user confirms a baseline pipeline change.
```

### EXP01-DEC-04

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: SMAP L2 branch
Decision: SMAP L2_SM_SP 3 km / 1 km is a sensitivity branch, not the baseline replacement.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-06; EXP01_CONTEXT_INDEX.md §5
Evidence: Context index marks SMAPL2 as active/sensitivity and SMAPL3 as closest baseline branch.
Does not imply: SMAP L2 results are invalid.
Staleness rule: stale if user designates SMAP L2 as baseline.
```

### EXP01-DEC-05

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: Phase 8 red gate
Decision: Do not loosen or remove the Phase 8 red gate epsilon_real_dobson > epsilon_magnitude without a new decision.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-08; doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md
Evidence: The gate is mathematical; otherwise epsilon_imag becomes non-real under the current formula.
Does not imply: No sensitivity analysis can be proposed.
Staleness rule: stale if formula/model changes are confirmed and documented.
```

### EXP01-DEC-06

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: result interpretation
Decision: Phase 9 and current Phase 10 outputs are exploratory unless later validation/local calibration is confirmed.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-09; EXP01_CONTEXT_INDEX.md §7; Phase 10 compact stats CSV
Evidence: Context index marks outputs exploratory; Phase 10 correlations are weak/unstable except tiny n filters.
Does not imply: Outputs are useless; they can support diagnostics and exploratory maps.
Staleness rule: stale if a new validation report marks outputs as validated.
```

### EXP01-DEC-07

```text
Status: Active
Date confirmed: source-backed as of 2026-06-09
Scope: notebook routing
Decision: Root notebook/ folder is legacy/reference only; active EC_CYG pipeline belongs in Experiment_01/.
Source: agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md §EXP01-EC-10; EXP01_CONTEXT_INDEX.md §5.1
Evidence: Active rules define DECISION-NOTEBOOK-LEGACY-01.
Does not imply: legacy notebooks cannot be read for historical reference.
Staleness rule: stale if user reactivates root notebook/ explicitly.
```

### EXP01-DEC-08

```text
Status: Research memo decision
Date confirmed: source-backed as of 2026-06-09
Scope: experiment branches
Decision: Keep three experiment branches: SMAP 9 km, SMAP L2 3 km, SMAP L2 1 km.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §5
Evidence: Memo says all three show the Phase 8 pattern and help argue the issue is not only spatial resolution.
Does not imply: all three are equally baseline.
Staleness rule: stale if experiment design changes.
```

### EXP01-DEC-09

```text
Status: Research memo decision
Date confirmed: source-backed as of 2026-06-09
Scope: soil ancillary data
Decision: SoilGrids is the main static soil input for current Phase 8/9 snapshot.
Source: doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md §5; EC_CYG_TECHNICAL_REPORT_20260602.md §2
Evidence: SoilGrids has sand, clay, and bulk density with checked unit conversions.
Does not imply: SoilGrids resolves Phase 8.
Staleness rule: stale if a new soil-data decision is documented.
```
