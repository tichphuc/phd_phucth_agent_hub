# SOURCE_MAPPING.md

Version: `v0.1-draft`

Status: `reference-only`

Activation: `inactive`

---

## 1. Mục đích

File này map nguồn tham khảo vào module/phase của Meow v2.

Mục tiêu là bảo đảm mỗi module mới đều có `GATE-REFERENCE` trước khi implement.

---

## 2. Mapping theo module

| Meow v2 area | Primary references | Secondary references | Design focus |
| --- | --- | --- | --- |
| Constitution | INT-MEOW-V1, INT-NVT-NCKH, INT-RESEARCH-PROTOCOL | EXT-NIST-AI-RMF, EXT-OWASP-AGENTIC | scientific integrity, transparency, traceability, research standards, risk discipline |
| Authority Model | INT-MEOW-V1, EXT-AGT, EXT-MCP | EXT-A2A | user authority, execution authority, consent, permission states |
| Operating Protocol | INT-MEOW-V1, EXT-DEEPAGENTS, EXT-OPENAI-AGENTS | EXT-LANGGRAPH | gates, task routing, human-in-loop, context control |
| Registry | INT-MEOW-V1, EXT-AGT, EXT-A2A | EXT-METAGPT | inventory, status, agent/module cards later |
| Lawmaker Agent | INT-MEOW-V1, EXT-AGT | EXT-NIST-AI-RMF | rule proposal, policy lifecycle, approval |
| Operational Inspector | EXT-AGT, EXT-OWASP-AGENTIC, INT-MEOW-V1 | EXT-OPENAI-AGENTS | fail-closed, inspection report, guardrails, operational risk categories |
| Scientific Critic | INT-NVT-NCKH, INT-RESEARCH-PROTOCOL, INT-MEOW-V1 | EXT-NIST-AI-RMF | research question, evidence/method/data critique, overclaim control, scientific integrity |
| Conflict Court | INT-MEOW-V1, EXT-NIST-AI-RMF | EXT-AUTOGEN | conflict classification, escalation, human decision |
| Decision Records | EXT-AGT, INT-MEOW-V1, EXT-A2A | EXT-OPENAI-AGENTS | audit, decision record, task/message trace |
| Meow Coordinator | EXT-OPENAI-AGENTS, EXT-CREWAI, EXT-DEEPAGENTS | EXT-AUTOGEN, EXT-METAGPT | handoff, manager pattern, role routing |
| Research Agency | INT-NVT-NCKH, INT-RESEARCH-PROTOCOL, INT-EXP01, INT-MEOW-V1 | EXT-NIST-AI-RMF | evidence classification, scientific claim control, method/data/source discipline |
| Coding Agency | INT-CODING, EXT-MIMOCODE, EXT-DEEPAGENTS | EXT-METAGPT | Sprint Contract, generator-evaluator, compose/checkpoint |
| Memo Agency | INT-MEOW-MEMO, INT-MIMO-NOTE, INT-MEMORY-PAPERS | EXT-MIMOCODE, EXT-DEEPAGENTS | memory lifecycle, checkpoint, search, context rebuild |
| Document Librarian Agency | doc/DOC_INDEX.md, INT-MEOW-MEMO, INT-MIMO-NOTE | EXT-MCP, EXT-DEEPAGENTS, EXT-OPENAI-AGENTS | source access, catalog, path resolution, adapters |
| Knowledge / Evidence Agency | INT-NVT-NCKH, INT-MEMORY-PAPERS, EXT-DEEPAGENTS | EXT-MCP | progressive disclosure, source routing, claim-source mapping, evidence sufficiency |
| Tool Safety Agency | EXT-AGT, EXT-MCP, EXT-OWASP-AGENTIC | EXT-DEEPAGENTS | action policy, consent, untrusted tool descriptions, sandboxing |
| Experiment Steward | INT-EXP01, INT-RESEARCH-PROTOCOL | EXT-METAGPT | SOP/phase/step control, baseline protection |
| Data / Output Agency | INT-EXP01, INT-RESEARCH-PROTOCOL | EXT-NIST-AI-RMF | provenance, output status, validation discipline |
| Schema Layer | EXT-AGT, EXT-A2A, EXT-OPENAI-AGENTS | EXT-MCP | structured reports, trace fields, task/decision object shapes |

---

## 3. Mapping theo phase

| Phase | Reference pass cần làm |
| --- | --- |
| Phase 0 | Meow v1 + project decisions already used; no external dependency |
| R0 | Initialize reference track and design decisions |
| C0 Scientific Constitution/Oversight | Nguyễn Văn Tuấn, Meow v1, Research Protocol |
| Phase 1 Governance and Oversight Core | AGT, OWASP, NIST, Meow v1, OpenAI guardrails, Nguyễn Văn Tuấn |
| Phase 2 Coordinator | OpenAI Agents SDK, CrewAI, Deep Agents, AutoGen |
| Phase 3 Schema Layer | AGT specs, A2A task/message model, OpenAI tracing/results, MCP |
| Phase 4 Functional Agencies | MiMoCode, Deep Agents, memory papers, Research Protocol, exp_01 |
| Phase 5 Reference Consolidation | audit all sources, update decisions, remove stale mappings |
| Phase 6 Pilot | NIST/OWASP risk checks, AGT audit concepts, Meow v1 comparison if needed |

---

## 4. Reference status for immediate next phase

Before Phase 1, read/check:

```text
EXT-AGT
EXT-OWASP-AGENTIC
EXT-NIST-AI-RMF
EXT-OPENAI-AGENTS
INT-MEOW-V1
INT-NVT-NCKH
```

Expected outputs for Phase 1:

* Lawmaker should adopt rule lifecycle and proposal-only behavior.
* Operational Inspector should adapt fail-closed and guardrail concepts.
* Scientific Critic should adapt research-question discipline, evidence/method/data critique and proportionate conclusions.
* Conflict Court should adapt conflict escalation and human decision requirements.
* Decision Records should adapt audit/decision trace concepts.

---

## 5. Doc real mapping from `doc/`

These are the concrete project docs that should be mapped into v2 module reading:

| Doc source | Primary v2 area | Secondary v2 area | Design focus |
| --- | --- | --- | --- |
| `doc/DOC_INDEX.md` | Knowledge / Evidence Agency | Meow Coordinator | document inventory, routing, artifact discovery |
| `doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md` | Research Agency | Experiment Steward | baseline pipeline, phase/step structure, validation discipline |
| `doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md` | Research Agency | Memo Agency, Scientific Critic | exploratory vs validated separation, issue/decision log, next-direction tracking |
| `doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md` | Data / Output Agency | Research Agency, Experiment Steward | snapshot results, limitation framing, report-style evidence |
| `doc/ec_cyg/knowledge/studying_CYGNSS_note_v03_SMAPL2_SM_SP.md` | Experiment Steward | Research Agency, Knowledge Agency | L2 collocation, roughness/tau handling, notebook phase logic |
| `doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md` | Research Agency | Coding Agency, Operating Protocol | notebook/code discipline, traceability, phase/step rigor |

Use this map when deciding which doc to read before which v2 module.
