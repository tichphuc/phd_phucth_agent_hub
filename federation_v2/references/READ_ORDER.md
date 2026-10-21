# READ_ORDER.md

Version: `v0.1-draft`

Status: `reference-only`

Activation: `inactive`

---

## 1. Mục đích

File này quy định thứ tự đọc nguồn tham khảo trước khi implement từng phần của Meow v2.

Reference read order không thay thế Constitution hoặc Operating Protocol.

---

## 2. General rule

Trước khi build module mới:

```text
1. Đọc foundation kernel v2
2. Xác định module/phase
3. Đọc references trong file này
4. Ghi hoặc cập nhật design decision nếu có
5. Chỉ sau đó mới viết module
```

---

## 3. Foundation startup

Luôn đọc trước:

```text
agent_hub/federation_v2/README.md
agent_hub/federation_v2/VERSIONING_POLICY.md
agent_hub/federation_v2/CONSTITUTION.md
agent_hub/federation_v2/AUTHORITY_MODEL.md
agent_hub/federation_v2/OPERATING_PROTOCOL.md
agent_hub/federation_v2/FEDERATION_MANIFEST.md
agent_hub/federation_v2/REGISTRY.md
```

Sau đó đọc:

```text
agent_hub/federation_v2/references/REFERENCES.md
agent_hub/federation_v2/references/SOURCE_MAPPING.md
agent_hub/federation_v2/references/DESIGN_DECISIONS_FROM_REFERENCES.md
```

---

## 4. Read order by phase

### R0 - Reference Track

Read:

```text
doc/memo/MIMO_CODE_MEMORY_IDEAS_20260614.md
doc/DOC_INDEX.md
agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
```

External check:

```text
Microsoft AGT README / limitations
Xiaomi MiMoCode README
LangGraph overview
Deep Agents overview
OpenAI Agents SDK agents / handoffs / guardrails / tracing
MCP specification
A2A specification
OWASP Agentic AI threats
NIST AI RMF
MetaGPT / CAMEL / AgentGit abstracts
```

### Phase 1 - Governance and Oversight Core

Read:

```text
EXT-AGT
EXT-OWASP-AGENTIC
EXT-NIST-AI-RMF
EXT-OPENAI-AGENTS guardrails/tracing
INT-MEOW-V1 governance
INT-NVT-NCKH
agent_hub/federation_v2/governance/LAWMAKER_AGENT.md
agent_hub/federation_v2/governance/CONFLICT_COURT.md
agent_hub/federation_v2/governance/DECISION_RECORDS.md
agent_hub/federation_v2/oversight/OPERATIONAL_INSPECTOR.md
agent_hub/federation_v2/oversight/SCIENTIFIC_CRITIC.md
```

Need deeper reading:

* AGT policy engine spec;
* AGT audit/compliance spec;
* AGT limitations;
* OWASP Agentic AI mitigation categories;
* NIST GOVERN/MAP/MEASURE/MANAGE framing;
* Nguyễn Văn Tuấn: câu hỏi nghiên cứu, FINER, cơ sở khoa học, đạo đức, dữ liệu, plagiarism, phản biện và đánh giá khoa học.
* Lawmaker/Conflict Court/Decision Records/Operational Inspector/Scientific Critic charters after they are drafted.

### C0 - Scientific Constitution and Oversight

Read:

```text
INT-NVT-NCKH
INT-MEOW-V1 governance
INT-RESEARCH-PROTOCOL
agent_hub/federation_v2/CONSTITUTION.md
agent_hub/federation_v2/AUTHORITY_MODEL.md
agent_hub/federation_v2/OPERATING_PROTOCOL.md
agent_hub/federation_v2/FEDERATION_MANIFEST.md
```

Need deeper reading:

* research question as the kernel of a study;
* FINER as a question-quality check;
* scientific basis: evidence, method, theory/mechanism, checkability and proportionate conclusions;
* data integrity, plagiarism, authorship/credit and conflict-of-interest issues;
* scientific critique as quality control, not execution authority.

### Phase 2 - Coordinator

Read:

```text
EXT-OPENAI-AGENTS agents/handoffs/orchestration
EXT-DEEPAGENTS subagents/context/human-in-loop
EXT-CREWAI crews/processes
EXT-AUTOGEN group chat
agent_hub/federation_v2/core/MEOW_COORDINATOR.md
agent_hub/federation_v2/core/TASK_ROUTING.md
agent_hub/federation_v2/core/GATE_PROTOCOL.md
```

Need deeper reading:

* manager vs handoff pattern;
* subagent isolation;
* lifecycle hooks;
* termination conditions;
* route decision boundaries between Coordinator, Oversight Layer and agencies.

### Phase 3 - Schema Layer

Read:

```text
EXT-AGT audit/compliance specs
EXT-A2A task/message/artifact model
EXT-OPENAI-AGENTS tracing/results
EXT-MCP protocol objects and logging
```

Need deeper reading:

* decision records;
* task states;
* trace/span fields;
* audit event schema.

### Phase 4 - Functional Agencies

Read:

```text
INT-MEOW-MEMO
INT-MIMO-NOTE
INT-MEMORY-PAPERS
EXT-MIMOCODE
EXT-DEEPAGENTS memory/skills/subagents/permissions
INT-CODING
INT-RESEARCH-PROTOCOL
INT-EXP01
doc/DOC_INDEX.md
doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md
doc/ec_cyg/knowledge/studying_CYGNSS_note_v03_SMAPL2_SM_SP.md
doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md
doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md
```

Need deeper reading:

* MiMo memory service;
* MiMo checkpoint service;
* EC_CYG baseline pipeline and report discipline;
* CYGNSS L2 collocation and tau/roughness handling;
* Zep/Mem0/GraphRAG details;
* Deep Agents permissions and context engineering;
* Research protocol source discipline.

### Phase 5 - Reference Consolidation

Read:

```text
agent_hub/federation_v2/references/REFERENCE_AUDIT.md
agent_hub/federation_v2/references/STALE_SOURCE_REPORT.md
agent_hub/federation_v2/references/DESIGN_DECISION_REVIEW.md
agent_hub/federation_v2/references/REFERENCES.md
agent_hub/federation_v2/references/SOURCE_MAPPING.md
agent_hub/federation_v2/references/DESIGN_DECISIONS_FROM_REFERENCES.md
```

Need deeper reading:

* coverage gaps and watchlist items;
* stale / monitor decision basis;
* decision reclassification rationale if any;
* pilot-readiness implications for Phase 6.

### Phase 6 - Dry-run Pilots

Read:

```text
agent_hub/federation_v2/pilot/PILOT_PLAN.md
agent_hub/federation_v2/pilot/PILOT_001_REPORT.md
agent_hub/federation_v2/pilot/PILOT_002_REPORT.md
agent_hub/federation_v2/pilot/PILOT_003_REPORT.md
agent_hub/federation_v2/pilot/PILOT_004_REPORT.md
agent_hub/federation_v2/pilot/PILOT_005_REPORT.md
agent_hub/federation_v2/pilot/PILOT_RESULTS.md
```

Need deeper reading:

* confirm no real mutation happened during pilot;
* compare route correctness, gate behavior and role separation;
* decide whether wording needs tightening before Phase 7;
* compare pilot readout with v1 only after v2 dry-run is stable.

### Pilot / activation support

Read:

```text
EXT-AGT limitations
EXT-OWASP-AGENTIC
EXT-NIST-AI-RMF
DESIGN_DECISIONS_FROM_REFERENCES.md
```

Need deeper reading:

* risk/mitigation checklists;
* fail-closed behavior;
* rollback/deactivation pattern.

### Phase 7 - Compatibility Review

Read:

```text
agent_hub/federation_v2/compatibility/MEOW_V1_COMPARISON.md
agent_hub/federation_v2/compatibility/MIGRATION_NOTES.md
agent_hub/federation_v2/pilot/PILOT_RESULTS.md
agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
```

Need deeper reading:

* confirm comparison is advisory, not migration;
* identify what should stay reference-only from v1;
* identify what must remain independent in v2;
* decide whether any later migration sprint is warranted.


### Experiment overlay

Read the v2 experiment overlay directly when task routing involves exp_01 or any future experiment:

```text
agent_hub/federation_v2/experiments/EXPERIMENT_REGISTRY.md
agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md
agent_hub/federation_v2/experiments/exp_01/EXP01_CONTEXT_INDEX.md
```
