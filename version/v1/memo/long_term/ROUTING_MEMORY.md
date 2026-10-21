# ROUTING_MEMORY.md

## 1. Mục đích

File này là routing memory ổn định cho Meow.

Nó giúp Meow quyết định cần đọc file nào trước theo từng loại task, nhưng không
thay thế rule đọc bắt buộc trong governance hoặc experiment active rules.

---

## 2. Routing table

| Task type | First memory file | Canonical files still required | Notes |
| --------- | ----------------- | ------------------------------ | ----- |
| Project status | `PROJECT_STATE.md` | `EXPERIMENT_REGISTRY.md`, active context index, relevant memo/report | Memo chỉ dùng để định hướng nhanh |
| Current session | `short_term/SESSION_STATE.md` | User prompt hiện tại | Short-term có thể stale |
| Experiment task | `PROJECT_STATE.md` | `EXPERIMENT_REGISTRY.md`, active rules, context index | Không tự đoán experiment |
| Research result | `ISSUE_MEMORY.md` | `doc/DOC_INDEX.md`, research memo/report, output liên quan | Không gọi exploratory là validated |
| Code/notebook change | `ROUTING_MEMORY.md` | coding rules, active rules, file code/notebook liên quan | Cần Sprint/Operating Contract |
| Governance change | `MEOW_MEMO_MANIFEST.md` | `RULE_GOVERNANCE.md`, `RULE_REGISTRY.md` | Cần conflict check |

---

## 3. Fast startup route for Meow

```text
Always read first for non-simple project tasks:
1. AGENTS.md
2. agent_hub/MEOW_AGENT.md
3. agent_hub/AGENT_HUB_MANIFEST.md
4. agent_hub/governance/RULE_GOVERNANCE.md
5. agent_hub/governance/RULE_REGISTRY.md

Then read memo quick layer:
6. agent_hub/memo/MEOW_MEMO_MANIFEST.md
7. agent_hub/memo/long_term/ROUTING_MEMORY.md
8. agent_hub/memo/long_term/PROJECT_STATE.md
9. agent_hub/memo/short_term/SESSION_STATE.md nếu nối tiếp task hiện tại
```

Memo quick layer can reduce repo-wide scanning, but cannot replace canonical reads when task touches experiment, code, notebook, data, formula, validation, or research conclusion.

---

## 4. EC_CYG / exp_01 route

For exp_01 / EC_CYG tasks, read:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md
agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md
```

If task touches EC_CYG method, formula, pipeline, or validation, also read:

```text
doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md
doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md
doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md
doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md
```

If task touches Phase 10 status, also inspect current Phase 10 CSV/report outputs in `data/cygnss/`.

---

## 5. Memo-update route

When updating memo:

```text
1. Identify target layer:
   - long_term for stable state/decision/issue/routing
   - short_term for current task/session
   - log for append-only event trace

2. Classify operation:
   ADD / UPDATE / DELETE / NOOP

3. Validate source:
   - source canonical required for long_term
   - user prompt/session source enough for short_term
   - action trace enough for log

4. Apply update.

5. Append log entry.

6. Report conflict/progress if requested or if any source mismatch exists.
```

---

## 6. Staleness rule

Routing memory phải được kiểm tra lại nếu:

* startup flow trong `MEOW_AGENT.md` đổi;
* `AGENT_HUB_MANIFEST.md` đổi;
* registry hoặc experiment routing đổi;
* memo module được nâng version.
