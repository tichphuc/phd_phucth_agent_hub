# REFERENCES.md

Version: `v0.1-draft`

Status: `reference-only`

Activation: `inactive`

---

## 1. Mục đích

File này là danh mục nguồn tham khảo cho quá trình xây dựng Meow v2 Agent Federation.

Các nguồn trong file này chỉ là **reference**. Chúng không tự động trở thành luật, protocol hoặc decision của Meow v2.

Khi dùng một nguồn để thiết kế module, phải ghi rõ:

```text
source -> idea -> adopt/adapt/reject/defer -> target module -> deeper reading
```

Quyết định thiết kế cụ thể được ghi trong:

```text
DESIGN_DECISIONS_FROM_REFERENCES.md
```

---

## 2. Source status scale

| Status | Ý nghĩa |
| --- | --- |
| `active-reference` | Nên dùng khi thiết kế v2 |
| `support-reference` | Dùng để hỗ trợ, không phải nguồn chính |
| `watchlist` | Theo dõi, đọc sâu khi cần |
| `defer` | Chưa dùng ở giai đoạn hiện tại |
| `reject-for-now` | Không phù hợp cho v2 hiện tại |

---

## 3. Internal references

| ID | Source | Location | Status | Use for | Do not use for |
| --- | --- | --- | --- | --- | --- |
| INT-MEOW-V1 | Meow v1 governance | `agent_hub/version/v1/` | `active-reference` | Operating Contract, Conflict Report, scientific caution, routing discipline | dependency bắt buộc của v2 |
| INT-MEOW-MEMO | Meow Memo Module | `agent_hub/federation_v2/memo/` | `active-reference` | memory lifecycle, long/short/log split, stale/source rule | source canonical cho research result |
| INT-CODING | Coding rules | `agent_hub/version/v1/CODING_RULES.md` | `active-reference` | Sprint Contract, Generator-Evaluator loop | tự động mutate code |
| INT-EXP01 | exp_01 active/context rules | `agent_hub/federation_v2/experiments/exp_01/` | `support-reference` | Experiment Steward model, baseline protection | rule chung cho mọi experiment |
| INT-MIMO-NOTE | MiMoCode local note | `doc/memo/MIMO_CODE_MEMORY_IDEAS_20260614.md` | `active-reference` | memory checkpoint, search, context rebuild idea | implementation decision |
| INT-MEMORY-PAPERS | Zep, Mem0, GraphRAG papers | `doc/memo/` | `active-reference` | memory architecture, retrieval, local-to-global summaries | governance rule trực tiếp |
| INT-RESEARCH-PROTOCOL | Research coding protocol | `doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md` | `support-reference` | scientific/coding discipline | v2 constitution dependency |
| INT-NVT-NCKH | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | `C:\Users\Administrator\Zotero\storage\GGFWV27B\DiVaoNCKH_NguyenVanTuan.md` | `active-reference` | câu hỏi nghiên cứu, FINER, cơ sở khoa học, đạo đức, dữ liệu, plagiarism, phản biện và đánh giá khoa học | luật chi tiết cứng nhắc hoặc domain-specific evidence |

---

## 4. External references

| ID | Source | Location | Status | Use for | Do not use for |
| --- | --- | --- | --- | --- | --- |
| EXT-AGT | Microsoft Agent Governance Toolkit | https://github.com/microsoft/agent-governance-toolkit | `active-reference` | policy engine, audit, fail-closed, MCP security, action governance | scientific validation |
| EXT-MIMOCODE | Xiaomi MiMoCode | https://github.com/XiaomiMiMo/MiMo-Code | `active-reference` | persistent memory, checkpoint, context rebuild, subagents, goal judge | uncontrolled automation |
| EXT-LANGGRAPH | LangGraph | https://docs.langchain.com/oss/python/langgraph/overview | `active-reference` | durable workflow, persistence, human-in-loop | required framework dependency |
| EXT-DEEPAGENTS | Deep Agents | https://docs.langchain.com/oss/python/deepagents/overview | `active-reference` | harness, subagents, permissions, context engineering, memory, skills | replacing Meow governance |
| EXT-OPENAI-AGENTS | OpenAI Agents SDK | https://openai.github.io/openai-agents-python/ | `active-reference` | agents, handoffs, guardrails, tracing, sessions, sandbox concepts | direct SDK migration |
| EXT-CREWAI | CrewAI | https://docs.crewai.com/en/concepts/crews | `support-reference` | crew/role/task/process design, manager pattern | autonomous business workflow assumptions |
| EXT-AUTOGEN | AutoGen | https://microsoft.github.io/autogen/stable/ | `support-reference` | group chat, manager/selector, human proxy idea | uncontrolled debate loop |
| EXT-MCP | Model Context Protocol | https://modelcontextprotocol.io/specification/2025-06-18 | `active-reference` | tool/resource/prompt boundary, user consent, tool safety | governance replacement |
| EXT-A2A | A2A Protocol | https://a2a-protocol.org/latest/specification/ | `watchlist` | agent card, task/message protocol, agent discovery | early implementation |
| EXT-OWASP-AGENTIC | OWASP Agentic AI Threats | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ | `active-reference` | threat taxonomy, mitigation language | scientific source |
| EXT-NIST-AI-RMF | NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | `active-reference` | risk governance vocabulary | module implementation detail |
| EXT-METAGPT | MetaGPT paper | https://arxiv.org/abs/2308.00352 | `support-reference` | SOP, role decomposition, intermediate verification | automatic software factory |
| EXT-CAMEL | CAMEL paper | https://arxiv.org/abs/2303.17760 | `watchlist` | role-playing, communicative agent cooperation | core governance model |
| EXT-AGENTGIT | AgentGit paper | https://arxiv.org/abs/2511.00628 | `watchlist` | branching, rollback, trajectory comparison | immediate dependency |

---

## 5. Current interpretation

Reference strategy for Meow v2:

* Meow v1 provides research-governance seed ideas.
* Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học provides the core scientific research discipline for Constitution and Scientific Critic.
* AGT provides action-governance and audit ideas.
* MiMoCode and memory papers provide memory/checkpoint ideas.
* Deep Agents and LangGraph provide harness and context-management ideas.
* OpenAI Agents SDK provides handoff/guardrail/tracing concepts.
* MCP and A2A provide protocol/interface ideas.
* OWASP and NIST provide risk language.
* MetaGPT, CAMEL and AgentGit provide research patterns to adapt carefully.

No external framework is required by Meow v2 at this stage.

### 4.1. Project docs from `doc/`

These are not source canonical for scientific claims by themselves, but they are the real project docs that v2 should map to its research and experiment modules:

| ID | Source | Location | Status | Use for | Do not use for |
| --- | --- | --- | --- | --- | --- |
| INT-DOC-INDEX | Document index | `doc/DOC_INDEX.md` | `active-reference` | doc inventory, routing, artifact discovery | canonical truth cho research claim |
| INT-EC-CYG-SKEL | EC_CYG baseline knowledge skeleton | `doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md` | `active-reference` | baseline pipeline, phase/step structure, validation discipline | replace general governance |
| INT-EC-CYG-RESEARCH-MEMO | EC_CYG research memo | `doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md` | `active-reference` | issue log, decision log, exploratory vs validated separation | source canonical |
| INT-EC-CYG-TECH-REPORT | EC_CYG technical report | `doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md` | `active-reference` | snapshot results, limitations, report-style evidence | final scientific conclusion without validation |
| INT-CYGNSS-L2-NOTE | CYGNSS / SMAP L2 note | `doc/ec_cyg/knowledge/studying_CYGNSS_note_v03_SMAPL2_SM_SP.md` | `active-reference` | L2 collocation, roughness/tau handling, phase workflow | baseline-independent conclusion |

Map usage:

* Research Agency should read the EC_CYG skeleton, memo and technical report before touching EC_CYG claim structure.
* Experiment Steward should read the EC_CYG skeleton and CYGNSS L2 note before changing notebook phase logic.
* Data / Output Agency should use the technical report as the output snapshot anchor.
* Knowledge / Evidence Agency should use `DOC_INDEX.md` as the project-wide doc router.

---

## 6. Update rule

When adding a new reference:

1. add it to this file;
2. classify status;
3. map it in `SOURCE_MAPPING.md`;
4. record adopted/adapted/rejected/deferred ideas in `DESIGN_DECISIONS_FROM_REFERENCES.md`;
5. update `READ_ORDER.md` if it affects a phase.



