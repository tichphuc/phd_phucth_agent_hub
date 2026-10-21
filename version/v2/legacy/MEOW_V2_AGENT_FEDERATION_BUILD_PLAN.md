# Kế hoạch xây dựng Meow v2 - Agent Federation

Version: `v0.2-draft`

Status: `planning-only`

Created: `2026-06-18`

Updated: `2026-06-19`

Owner: `User`

Coordinator: `Meow`

Activation state: `inactive-by-default`

Language policy: nội dung chung của agent viết bằng tiếng Việt; thuật ngữ kỹ thuật tiếng Anh được giữ khi giúp chính xác hơn.

---

## 1. Mục đích

File này ghi lại kế hoạch xây dựng **Meow v2 - Agent Federation**.

Meow v2 được định hướng là một phiên bản mới, độc lập và tự vận hành được trong folder riêng:

```text
agent_hub/federation_v2/
```

Meow v2 có thể lấy cảm hứng từ Meow v1 và các nguồn tham khảo bên ngoài, nhưng không phụ thuộc vào Meow v1 để vận hành. Khi nền tảng v2 hoàn chỉnh, một agent chỉ cần đọc các file canonical trong `federation_v2/` là phải hiểu được:

* Meow v2 là gì;
* quyền hạn của User, Meow Coordinator và các agency;
* luật nền cần tuân thủ;
* workflow xử lý task;
* gate bắt buộc;
* khi nào được tiếp tục;
* khi nào phải dừng;
* khi nào phải hỏi User;
* cách thêm hoặc mở rộng agency module.

File này là:

* roadmap xây dựng Meow v2;
* bản định hướng kiến trúc;
* tài liệu kiểm soát quá trình triển khai;
* guardrail để tránh refactor tùy tiện.

File này không phải:

* active rule thay thế Meow v1;
* constitution chính thức của v2;
* quyết định kích hoạt v2;
* quyền sửa code, notebook, data, pipeline, công thức hoặc experiment;
* quyền sửa, xóa, di chuyển hoặc rename bất kỳ file legacy nào.

---

## 2. Cách hiểu kiến trúc mới

### 2.1. Meow v2 là một hệ độc lập

Meow v2 không phải chỉ là overlay của Meow v1.

Cách hiểu đúng:

```text
Meow v2 = independent Agent Federation
Meow v1 = historical/design reference
```

Meow v1 có giá trị vì đã có nhiều thành phần tốt:

* root governance;
* Operating Contract;
* Conflict Report;
* priority routing;
* experiment routing;
* memo module;
* coding rules;
* scientific caution.

Tuy nhiên, Meow v2 phải tự chứa đủ luật và protocol của chính nó. V2 không được yêu cầu người vận hành phải đọc ngược về v1 mới hiểu cách làm việc.

### 2.2. Quan hệ với Meow v1

Trong giai đoạn xây dựng:

* Meow v1 vẫn giữ nguyên;
* Meow v2 nằm riêng trong `agent_hub/federation_v2/`;
* v2 không sửa v1;
* v2 không update registry v1;
* v2 không tự tuyên bố active;
* v1 chỉ được dùng như nguồn tham khảo thiết kế.

Nếu sau này cần so sánh hoặc migration, có thể tạo nhóm file riêng:

```text
agent_hub/federation_v2/compatibility/
```

Nhưng **legacy mapping không thuộc Phase 0**. Phase 0 tập trung xây khung vận hành độc lập cho v2.

---

## 3. User Intent

User muốn xây Meow v2 theo hướng **Agent Federation**.

Ý tưởng trung tâm:

```text
User
  -> Meow Central Coordinator
     -> Constitution / Governance Core
        -> Lawmaker
        -> Conflict Court
        -> Oversight Layer
           -> Operational Inspector
           -> Scientific Critic
        -> Functional Agencies
```

Các functional agency có thể gồm:

* Memo Agency;
* Research Agency;
* Coding Agency;
* Knowledge / Evidence Agency;
* Experiment Steward Agency;
* Data / Output Agency;
* Tool Safety Agency.

Mục tiêu không phải chỉ chia file cho gọn, mà là tách quyền và tách trách nhiệm:

* Coordinator điều phối;
* Lawmaker đề xuất luật;
* Operational Inspector kiểm tra vận hành và có quyền chặn task/action;
* Scientific Critic phản biện khoa học và có quyền yêu cầu revise/hạ cấp claim;
* Conflict Court xử lý xung đột;
* agency chuyên môn chỉ làm trong mandate của mình;
* User là cấp quyết định cao nhất.

---

## 4. Language Policy

Nội dung chung của Meow v2 nên viết bằng tiếng Việt để phù hợp với workflow của project.

Quy ước:

* Tiếng Việt là ngôn ngữ chính cho rule, protocol, mô tả trách nhiệm và gate.
* Thuật ngữ tiếng Anh được giữ khi cần chính xác hoặc đã phổ biến, ví dụ:
  * `Agent Federation`;
  * `Coordinator`;
  * `Operational Inspector`;
  * `Scientific Critic`;
  * `Lawmaker`;
  * `Conflict Court`;
  * `Operating Contract`;
  * `Sprint Contract`;
  * `Evidence Report`;
  * `Action Policy`;
  * `Source-backed`;
  * `Implementation choice`;
  * `Exploratory result`;
  * `Validated result`.
* Không trộn ngôn ngữ theo cách gây mơ hồ.
* Nếu thuật ngữ tiếng Anh có thể gây hiểu nhầm, file phải giải thích ngắn bằng tiếng Việt.

---

## 5. Authority Model - Nguyên tắc ban đầu

Meow v2 cần phân biệt hai trục quyền lực.

### 5.1. Decision Authority

Decision Authority là quyền quyết định project nên làm gì.

Thứ tự ban đầu:

```text
User
  > Constitution
  > Governance Core
  > Oversight Layer
  > Agency Charter
  > Experiment / Domain Rules
  > Task Procedure
```

Nguyên tắc:

* User là cấp quyết định cao nhất.
* Nếu User yêu cầu việc có rủi ro, Meow phải báo rủi ro rõ trước khi làm.
* Một quyết định của User phải được ghi là `USER_DECISION`.
* Không được trình bày `USER_DECISION` như thể đó là source-backed scientific fact.

### 5.2. Execution Authority

Execution Authority là quyền thực thi hành động.

Thứ tự ban đầu:

```text
System / tool constraints
  > User approval
  > Meow Central Coordinator
  > Agency mandate
  > Task-specific permission
```

Nguyên tắc:

* Không agency nào được hành động ngoài mandate.
* Không agency nào tự cấp quyền sửa, tạo, xóa, di chuyển, rename hoặc ghi đè file.
* Meow Coordinator được route và tổng hợp, nhưng không được âm thầm override Constitution, Operational Inspector, Scientific Critic hoặc User gate.

---

## 6. Constitutional Principles cho v2

Constitution của Meow v2 phải đủ chặt để phục vụ nghiên cứu khoa học.

### 6.1. Scientific Integrity

Meow v2 không được:

* bịa công thức;
* bịa tham số;
* bịa đơn vị;
* bịa citation;
* bịa nguồn;
* biến proposal thành decision;
* biến exploratory result thành validated result;
* che giấu uncertainty;
* suy diễn vượt quá bằng chứng.

### 6.2. Transparency

Task không đơn giản phải làm rõ:

* task;
* scope;
* applicable rules;
* allowed actions;
* forbidden actions;
* required sources;
* required gates;
* risks;
* conflicts;
* có cần User approval hay không.

### 6.3. Traceability

Mọi claim hoặc action quan trọng phải truy vết được về:

* User prompt;
* source file;
* rule file;
* agency report;
* decision record;
* memo/report;
* output hoặc log liên quan.

### 6.4. Separation of Powers

Meow v2 phải tránh để một module vừa đề xuất, vừa thực thi, vừa tự kiểm tra chính mình.

Nguyên tắc:

* Coordinator không phải chủ quyền tối cao.
* Lawmaker không tự activate luật.
* Coding Agency không tự duyệt patch của mình.
* Memo Agency không tạo ra sự thật.
* Research Agency không thay User quyết định.
* Operational Inspector có quyền chặn task/action hoặc yêu cầu User decision.
* Scientific Critic có quyền yêu cầu revise/hạ cấp claim khoa học hoặc yêu cầu User decision.
* Conflict Court không tự quyết vấn đề cần User quyết định.

### 6.5. Proposal before Mutation

Mọi thay đổi file hoặc workflow phải đi theo:

```text
proposal -> review -> user approval -> action -> verification -> report
```

Không được:

```text
idea -> silent patch
risk -> direct action
exploratory result -> conclusion
```

---

## 7. Reference Base

Reference base được dùng để học ý tưởng thiết kế. Reference không tự trở thành rule.

### 7.1. Internal references

| Source | Học gì |
| --- | --- |
| Meow v1 governance | Operating Contract, Conflict Report, priority, experiment routing |
| Meow memo module | memory lifecycle, long-term/short-term/log split |
| Coding rules | Sprint Contract, Generator-Evaluator loop |
| doc/DOC_INDEX.md | project document inventory and routing |
| EC_CYG baseline knowledge skeleton | baseline pipeline, phase/step structure, validation discipline |
| EC_CYG research memo | issue log, decision log, exploratory vs validated separation |
| EC_CYG technical report | snapshot results, limitations, report-style evidence |
| CYGNSS L2_SM_SP note | L2 collocation, roughness/tau handling, phase workflow |
| exp_01 active rules | scientific discipline, experiment steward model |
| Research protocol | source discipline, code/notebook caution |
| Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | câu hỏi nghiên cứu, FINER, cơ sở khoa học, đạo đức, dữ liệu, phản biện và đánh giá khoa học |

### 7.2. External references

| Source | Học gì | Không dùng để |
| --- | --- | --- |
| Microsoft AGT | policy engine, audit, fail-closed, MCP security | thay thế scientific validation |
| Xiaomi MiMoCode | checkpoint, persistent memory, context rebuild, goal judge | automation không kiểm soát |
| LangGraph | durable workflow, state, human-in-loop | ép v2 phụ thuộc framework |
| Deep Agents | harness, subagents, permissions, context engineering | thay thế Constitution |
| OpenAI Agents SDK | handoff, guardrails, tracing, sessions | migration trực tiếp |
| CrewAI | crews, roles, manager process | business automation assumptions |
| AutoGen | group chat, manager/selector | debate dài không kiểm soát |
| MCP | tool/resource/prompt interface, safety | thay thế governance |
| A2A | agent card, task/message protocol | bắt buộc triển khai sớm |
| OWASP Agentic AI | threat model, mitigation language | research-source authority |
| NIST AI RMF | risk management language | task implementation detail |
| MetaGPT | SOP, role decomposition | auto-code không inspection |
| CAMEL | role-playing agents | governance core |
| AgentGit | branching/rollback idea | dependency sớm |

Reference files nên đặt trong:

```text
agent_hub/federation_v2/references/
```

Không đặt reference ở root core nếu nó không phải file vận hành bắt buộc.

---

## 8. Target Architecture

### 8.1. High-level architecture

```text
User
  |
  v
Meow Central Coordinator
  |
  +-- Constitution / Authority Model / Operating Protocol
  |
  +-- Governance Agencies
  |     +-- Lawmaker
  |     +-- Conflict Court
  |     +-- Registry / Records
  |
  +-- Oversight Layer
  |     +-- Operational Inspector
  |     +-- Scientific Critic
  |
  +-- Functional Agencies
        +-- Memo Agency
        +-- Research Agency
        +-- Coding Agency
        +-- Knowledge / Evidence Agency
        +-- Experiment Steward Agency
        +-- Data / Output Agency
        +-- Tool Safety Agency
```

### 8.2. Target folder structure

```text
agent_hub/federation_v2/
├── README.md
├── FEDERATION_MANIFEST.md
├── CONSTITUTION.md
├── AUTHORITY_MODEL.md
├── OPERATING_PROTOCOL.md
├── VERSIONING_POLICY.md
├── REGISTRY.md
├── core/
│   ├── MEOW_COORDINATOR.md
│   ├── TASK_ROUTING.md
│   └── GATE_PROTOCOL.md
├── governance/
│   ├── LAWMAKER_AGENT.md
│   ├── CONFLICT_COURT.md
│   └── DECISION_RECORDS.md
├── oversight/
│   ├── OPERATIONAL_INSPECTOR.md
│   └── SCIENTIFIC_CRITIC.md
├── schemas/
│   ├── OPERATING_CONTRACT_SCHEMA.md
│   ├── INSPECTION_REPORT_SCHEMA.md
│   ├── RULE_PROPOSAL_SCHEMA.md
│   ├── DECISION_RECORD_SCHEMA.md
│   ├── EVIDENCE_REPORT_SCHEMA.md
│   ├── MEMO_UPDATE_SCHEMA.md
│   └── ACTION_POLICY_SCHEMA.md
├── agencies/
│   ├── memo/
│   │   └── MEMO_AGENT.md
│   ├── research/
│   │   └── RESEARCH_AGENT.md
│   ├── coding/
│   │   └── CODING_AGENT.md
│   ├── knowledge/
│   │   └── KNOWLEDGE_AGENT.md
│   ├── experiment/
│   │   └── EXPERIMENT_STEWARD_AGENT.md
│   ├── data_output/
│   │   └── DATA_OUTPUT_AGENT.md
│   └── tool_safety/
│       └── TOOL_SAFETY_AGENT.md
├── references/
│   ├── REFERENCES.md
│   ├── SOURCE_MAPPING.md
│   └── READ_ORDER.md
├── examples/
│   ├── TASK_ROUTING_EXAMPLE.md
│   ├── RULE_PROPOSAL_EXAMPLE.md
│   └── INSPECTION_REPORT_EXAMPLE.md
├── pilot/
│   ├── PILOT_PLAN.md
│   └── PILOT_RESULTS.md
└── compatibility/
    ├── MEOW_V1_COMPARISON.md
    └── MIGRATION_NOTES.md
```

Lưu ý:

* Không tạo toàn bộ cấu trúc cùng lúc nếu chưa có User approval cho phase tương ứng.
* `compatibility/` là tùy chọn sau này, không thuộc foundation.
* `references/` là knowledge support, không phải governance core.

---

## 9. Minimum Viable Governance Kernel

Trước khi mở rộng agency module, v2 cần một kernel tự vận hành.

Kernel tối thiểu gồm:

```text
README.md
FEDERATION_MANIFEST.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
VERSIONING_POLICY.md
REGISTRY.md
```

Kernel này phải trả lời đủ:

* Meow v2 là gì?
* v2 đang active hay planning-only?
* User có quyền gì?
* Meow Coordinator có quyền gì?
* Constitution quy định gì?
* Khi nhận task phải đọc file nào?
* Task không đơn giản là gì?
* Khi nào cần Operating Contract?
* Khi nào Operational Inspector phải chặn?
* Khi nào Scientific Critic phải yêu cầu revise/hạ cấp claim?
* Khi nào phải hỏi User?
* File nào là canonical trong v2?
* Cách thêm module mới như thế nào?

---

## 10. Agency Concepts

### 10.1. Meow Central Coordinator

Mandate:

* nhận task từ User;
* phân loại task;
* route đến agency phù hợp;
* yêu cầu report;
* tổng hợp report;
* hỏi User khi cần decision;
* bảo đảm task đi qua gate phù hợp.

Forbidden:

* override Operational Inspector;
* override Scientific Critic;
* override Constitution;
* tự sửa file nếu chưa có approval;
* biến proposal thành User decision.

### 10.2. Lawmaker Agent

Mandate:

* đề xuất rule mới;
* đề xuất sửa rule;
* đề xuất deprecate/archive rule;
* kiểm tra conflict rule;
* đề xuất cập nhật registry v2.

Forbidden:

* tự activate luật;
* tự sửa registry nếu chưa có approval;
* che giấu conflict.

### 10.3. Operational Inspector

Mandate:

* kiểm tra rule compliance;
* kiểm tra gate;
* kiểm tra permission và action safety;
* kiểm tra authority conflict;
* kiểm tra workflow/protocol compliance;
* tạo Inspection Report;
* chặn task/action nếu không an toàn về vận hành.

Required output:

```text
Can proceed: Yes / No
Need user decision: Yes / No
Severity: BLOCKER / MAJOR / MINOR
```

### 10.4. Scientific Critic

Mandate:

* đặt câu hỏi phản biện đúng lúc;
* kiểm tra câu hỏi nghiên cứu, evidence, phương pháp và dữ liệu;
* phát hiện overclaim, uncertainty bị che giấu, thiếu credit hoặc plagiarism risk;
* yêu cầu hạ cấp claim nếu chưa đủ cơ sở;
* tạo Scientific Critique Report.

Forbidden:

* tự làm thay Research Agency;
* tự sửa claim hoặc phương pháp nếu chưa được giao;
* tự quyết scientific truth khi thiếu source;
* cản trở task chỉ vì cầu toàn nếu claim đã được giới hạn đúng mức.

Required output:

```text
Can claim proceed: Yes / No / Revise
Need user decision: Yes / No
Main scientific concern:
```

### 10.5. Conflict Court

Mandate:

* xử lý conflict chưa resolve;
* phân loại conflict;
* đề xuất hướng giải quyết;
* escalate lên User nếu cần.

Forbidden:

* tự quyết scientific truth khi thiếu source;
* tự đoán User intent;
* override User confirmation gate.

### 10.6. Memo Agency

Mandate:

* quản lý memory;
* phân loại update: ADD / UPDATE / DELETE / NOOP;
* validate source trước khi update long-term;
* đánh dấu stale memory.

Forbidden:

* biến proposal thành decision;
* biến exploratory result thành validated result;
* override source canonical.

### 10.7. Research Agency

Mandate:

* kiểm tra scientific claim;
* map formula với source;
* phân loại evidence;
* bảo vệ research integrity.

Forbidden:

* bịa công thức/tham số/đơn vị/citation;
* claim validation khi chưa có validation source;
* đổi baseline hoặc giả định nếu chưa có decision.

### 10.8. Coding Agency

Mandate:

* chuẩn bị Sprint Contract;
* đề xuất patch;
* implement chỉ sau User approval;
* chạy test/check khi được phép;
* báo cáo validation và risk.

Forbidden:

* refactor ngoài scope;
* đổi công thức ngầm;
* mutate file khi chưa được phép.

### 10.9. Knowledge / Evidence Agency

Mandate:

* xác định canonical source;
* map claim -> source;
* kiểm tra missing/stale evidence;
* tạo Evidence Report.

Forbidden:

* coi memo là source canonical nếu có source gốc;
* gán source support khi chưa đọc source.

### 10.10. Experiment Steward Agency

Mandate:

* route task theo experiment;
* bảo vệ baseline experiment;
* xác định phase/step impact;
* phân biệt baseline, sensitivity, diagnostic, exploratory.

Forbidden:

* tạo experiment mới nếu chưa được phép;
* promote sensitivity branch thành baseline nếu chưa có decision;
* gọi exploratory output là validated.

### 10.11. Data / Output Agency

Mandate:

* kiểm tra data/output status;
* phân loại input, intermediate, output, truth, diagnostic;
* flag large-file risk;
* kiểm tra provenance.

Forbidden:

* overwrite output nếu chưa có approval;
* coi output tồn tại là validation.

### 10.12. Tool Safety Agency

Mandate:

* phân loại action: read, write, delete, move, run, install, network, notebook execute;
* kiểm tra approval needs;
* đề xuất Action Policy;
* xác định tool/MCP risk.

Forbidden:

* tự execute action;
* tự approve destructive action;
* tin tool description một cách tuyệt đối.

---

## 11. Implementation Phases

### Track R - Reference and Learning

Goal:

* duy trì một knowledge track chạy song song với quá trình build Meow v2;
* bảo đảm mỗi module mới có trace từ nguồn tham khảo;
* ghi rõ ý tưởng nào được `ADOPT`, `ADAPT`, `REJECT` hoặc `DEFER`;
* chỉ rõ khi implement cần đọc sâu nguồn nào.

Deliverables:

```text
references/REFERENCES.md
references/SOURCE_MAPPING.md
references/READ_ORDER.md
references/DESIGN_DECISIONS_FROM_REFERENCES.md
```

Gates:

* reference không tự trở thành rule;
* mỗi design decision phải có source và target module;
* trước khi build governance/agency/schema/protocol mới phải qua `GATE-REFERENCE`;
* nếu source ngoài mâu thuẫn Constitution, Constitution thắng.

Exit criteria:

* mọi phase sau có read order và source mapping rõ;
* design decision từ reference được ghi trước khi implement module liên quan.

### Sprint C0 - Scientific Constitution and Oversight Update

Goal:

* bổ sung chuẩn nghiên cứu khoa học cốt lõi vào foundation kernel;
* đưa tài liệu Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học vào Reference Track như nguồn quan trọng;
* tách oversight vận hành và oversight khoa học trước khi tạo Phase 1 modules.

Deliverables:

```text
README.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
FEDERATION_MANIFEST.md
MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
REGISTRY.md
references/REFERENCES.md
references/SOURCE_MAPPING.md
references/READ_ORDER.md
references/DESIGN_DECISIONS_FROM_REFERENCES.md
```

Gates:

* không tạo agency file mới trong C0;
* không biến tài liệu tham khảo thành luật chi tiết;
* chỉ đưa nguyên tắc khoa học cốt lõi vào Constitution;
* `Scientific Critic` là oversight function ngang hàng với `Operational Inspector`.

Exit criteria:

* source Nguyễn Văn Tuấn được đăng ký trong reference track;
* Constitution có chuẩn khoa học ngắn gọn;
* Operating Protocol có `GATE-SCIENTIFIC-CRITIQUE`;
* Phase 1 được định hướng lại thành Governance and Oversight Core.

### Phase 0 - Independent Foundation Kernel

Goal:

* tạo nền tự vận hành tối thiểu cho Meow v2;
* không cần đọc v1 để hiểu v2;
* chưa mở rộng agency module chi tiết.

Deliverables:

```text
README.md
FEDERATION_MANIFEST.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
VERSIONING_POLICY.md
REGISTRY.md
```

Required contents:

* định nghĩa Meow v2;
* trạng thái `planning-only` / `inactive-by-default`;
* authority hierarchy;
* constitutional principles;
* operating workflow;
* task classification;
* gate cơ bản;
* registry nội bộ của v2;
* quy tắc thêm file/module mới.

Gates:

* không sửa Meow v1;
* không tạo agency module chi tiết;
* không tạo compatibility/migration file;
* không update registry v1;
* không activate v2.

Exit criteria:

* v2 có foundation kernel self-contained;
* một agent đọc các file Phase 0 có thể hiểu cách vận hành nền của v2.

### Phase 1 - Governance and Oversight Core

Goal:

* tạo các cơ quan governance chính;
* tạo oversight layer gồm Operational Inspector và Scientific Critic;
* dùng Track R để cập nhật các tiến bộ về policy, audit, fail-closed, risk, guardrails và scientific critique trước khi viết governance/oversight files.

Deliverables:

```text
governance/LAWMAKER_AGENT.md
governance/CONFLICT_COURT.md
governance/DECISION_RECORDS.md
oversight/OPERATIONAL_INSPECTOR.md
oversight/SCIENTIFIC_CRITIC.md
```

Gates:

* phải qua `GATE-REFERENCE`;
* Lawmaker chỉ đề xuất, không activate;
* Operational Inspector phải có quyền report/chặn task/action;
* Scientific Critic phải có quyền yêu cầu revise/hạ cấp claim khoa học;
* Conflict Court phải escalate khi cần User decision.

Exit criteria:

* rule creation, operational inspection, scientific critique và conflict resolution được tách quyền.

### Phase 2 - Core Coordinator

Goal:

* định nghĩa Meow Coordinator v2.

Deliverables:

```text
core/MEOW_COORDINATOR.md
core/TASK_ROUTING.md
core/GATE_PROTOCOL.md
```

Gates:

* phải qua `GATE-REFERENCE`;
* Coordinator không được override Constitution;
* Coordinator không được override Operational Inspector hoặc Scientific Critic;
* Coordinator chỉ route và synthesize trong authority model.

Exit criteria:

* mọi task type chính có routing path.

### Phase 3 - Schema Layer

Goal:

* chuẩn hóa output giữa các agency.

Deliverables:

```text
schemas/OPERATING_CONTRACT_SCHEMA.md
schemas/INSPECTION_REPORT_SCHEMA.md
schemas/RULE_PROPOSAL_SCHEMA.md
schemas/DECISION_RECORD_SCHEMA.md
schemas/EVIDENCE_REPORT_SCHEMA.md
schemas/MEMO_UPDATE_SCHEMA.md
schemas/ACTION_POLICY_SCHEMA.md
```

Gates:

* phải qua `GATE-REFERENCE`;
* schema phải human-readable;
* schema không phụ thuộc framework runtime;
* schema phải phân biệt proposal, decision, evidence và action.

Exit criteria:

* agency có thể produce report nhất quán.

### Phase 4 - Functional Agencies

Goal:

* xây agency chuyên môn.

Deliverables:

```text
agencies/research/RESEARCH_AGENT.md
agencies/coding/CODING_AGENT.md
agencies/memo/MEMO_AGENT.md
agencies/knowledge/KNOWLEDGE_AGENT.md
agencies/tool_safety/TOOL_SAFETY_AGENT.md
agencies/experiment/EXPERIMENT_STEWARD_AGENT.md
agencies/data_output/DATA_OUTPUT_AGENT.md
```

Recommended order:

1. Research Agency;
2. Coding Agency;
3. Memo Agency;
4. Knowledge Agency;
5. Tool Safety Agency;
6. Experiment Steward Agency;
7. Data / Output Agency.

Gates:

* phải qua `GATE-REFERENCE`;
* mỗi agency phải có mandate, allowed actions, forbidden actions, inputs, outputs, gates, escalation;
* không agency nào self-authorize mutation.

Exit criteria:

* các agency chính có charter rõ.

Status:

* draft stage đã được harden và đồng bộ xong vào `2026-06-19`;
* phase này sẵn sàng cho review/iterate, chưa phải active governance.

### Phase 5 - Reference Consolidation

Goal:

* audit lại Reference Track sau khi governance, coordinator, schema và agency đã có bản đầu;
* cập nhật source mapping;
* phát hiện source stale hoặc design decision cần sửa.

Deliverables:

```text
references/REFERENCE_AUDIT.md
references/STALE_SOURCE_REPORT.md
references/DESIGN_DECISION_REVIEW.md
```

Gates:

* không xóa reference cũ nếu chưa có lý do rõ;
* không promote reference thành rule;
* nếu design decision đổi, phải ghi rationale.

Exit criteria:

* reference base được audit và đủ hỗ trợ pilot/activation.

### Phase 6 - Dry-run Pilots

Goal:

* test federation workflow bằng task giả định, không sửa file thật.

Pilot cases:

```text
PILOT-001: yêu cầu sửa notebook exp_01
PILOT-002: yêu cầu cập nhật memo
PILOT-003: yêu cầu thêm rule
PILOT-004: yêu cầu chạy risky tool/action
PILOT-005: yêu cầu diễn giải validation claim
```

Deliverables:

```text
pilot/PILOT_PLAN.md
pilot/PILOT_001_REPORT.md
pilot/PILOT_002_REPORT.md
pilot/PILOT_003_REPORT.md
pilot/PILOT_004_REPORT.md
pilot/PILOT_005_REPORT.md
pilot/PILOT_RESULTS.md
```

Gates:

* không mutate file thật trong pilot;
* pilot report không phải decision;
* ghi rõ v2 cải thiện gì và làm rườm rà gì.

Exit criteria:

* ít nhất 3 pilot hoàn tất;
* không còn blocker design conflict.

Status:

* 5 scenario dry-run đã hoàn tất và được tổng kết trong `pilot/PILOT_RESULTS.md`;
* phase này đã hoàn thành ở mức pilot artifact, nhưng vẫn là `dry-run-only` và không tạo activation.

### Phase 7 - Compatibility Review

Goal:

* chỉ sau khi v2 foundation và pilot đã ổn, mới so sánh với v1.

Deliverables:

```text
compatibility/MEOW_V1_COMPARISON.md
compatibility/MIGRATION_NOTES.md
```

Gates:

* compatibility review không được sửa v1;
* mapping không được dùng để làm v2 phụ thuộc v1;
* mọi migration đều cần plan riêng.

Exit criteria:

* hiểu rõ điểm giống/khác giữa v1 và v2.

Status:

* compatibility review đã hoàn tất ở mức advisory;
* hai file compatibility đã được chốt wording tối thiểu;
* phase này sẵn sàng cho review tiếp theo nếu User muốn tinh chỉnh thêm, nhưng hiện không cần mở rộng thêm.

### Phase 8 - Partial Activation

Goal:

* nếu User đồng ý, kích hoạt một phần v2.

Possible activation order:

1. dùng schema v2 trong response;
2. dùng Operational Inspector v2 để review vận hành;
3. dùng Scientific Critic v2 để review claim khoa học;
4. dùng Research/Coding agency charter;
5. dùng Memo Agency update protocol;
6. dùng Tool Safety action policy.

Gates:

* mỗi activation cần User decision rõ;
* activation scope phải hẹp;
* rollback path phải rõ.

Exit criteria:

* v2 hỗ trợ task thật mà không phá workflow hiện tại.

### Phase 9 - Migration / Integration

Goal:

* quyết định vai trò dài hạn của v2.

Options:

* giữ v2 như hệ độc lập;
* dùng v2 làm active governance mới;
* giữ v1 và v2 song song;
* migrate một số phần v1 sang v2;
* deprecate một số legacy file nếu thật sự cần.

Gates:

* migration plan bắt buộc;
* Conflict Report bắt buộc nếu v1/v2 mismatch;
* không xóa legacy nếu chưa có explicit approval;
* registry update chỉ làm khi User yêu cầu.

Exit criteria:

* User xác nhận vai trò cuối của v2.

---

## 12. Standard Workflow cho mỗi phase

Mỗi phase implementation phải đi theo:

```text
1. Tạo phase-specific Operating Contract
2. Liệt kê file sẽ tạo/sửa
3. Tóm tắt nội dung dự kiến
4. Nêu risk và impact
5. Hỏi User confirmation
6. Chỉ tạo/sửa file đã được duyệt
7. Review file đã tạo/sửa
8. Báo cáo kết quả và next gate
```

Không phase nào được tự động nhảy sang phase tiếp theo.

---

## 13. Risk Register

| Risk ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RISK-V2-001 | v2 quá phức tạp | MAJOR | build theo phase, tạo kernel trước, pilot trước activation |
| RISK-V2-002 | v2 vô tình phụ thuộc v1 | MAJOR | self-contained foundation, v1 chỉ là reference |
| RISK-V2-003 | agency trùng trách nhiệm | MINOR | mandate matrix và routing protocol |
| RISK-V2-004 | Operational Inspector chỉ mang tính biểu tượng | MAJOR | Operational Inspector có explicit veto/report authority |
| RISK-V2-005 | Lawmaker tự activate luật | MAJOR | Rule Proposal cần User decision |
| RISK-V2-006 | memo trở thành false canonical source | MAJOR | source validation và stale marking |
| RISK-V2-007 | mất discipline khoa học | MAJOR | Constitution + Research Agency + Evidence Report |
| RISK-V2-008 | Coding Agency mutate file quá tự do | MAJOR | Sprint Contract + approval gate |
| RISK-V2-009 | Tool Safety chỉ là prompt-level | MINOR ban đầu, MAJOR về sau | Action Policy schema, runtime layer nếu cần |
| RISK-V2-010 | pilot report bị hiểu là decision | MINOR | đánh dấu pilot là dry-run |
| RISK-V2-011 | file v2 dùng ngôn ngữ không nhất quán | MINOR | Language Policy: tiếng Việt là chính, thuật ngữ English khi cần |
| RISK-V2-012 | build module mới mà không trace reference | MAJOR | Track R + GATE-REFERENCE |
| RISK-V2-013 | Scientific Critic bị trộn với Research Agency hoặc Operational Inspector | MAJOR | tách Oversight Layer, dùng `GATE-SCIENTIFIC-CRITIQUE` và report riêng |
| RISK-V2-014 | phản biện khoa học trở thành cản trở quá mức | MINOR ban đầu, MAJOR nếu làm chậm workflow | Scientific Critic chỉ yêu cầu revise/hạ cấp claim khi có lý do rõ |
| RISK-V2-015 | nguồn sách nghiên cứu bị biến thành luật chi tiết cứng nhắc | MINOR | dùng sách làm `active-reference`, chỉ đưa nguyên tắc cốt lõi vào Constitution |

---

## 14. Initial Deliverable Priority

Recommended first implementation batch: **Phase 0 only**.

```text
1. README.md
2. FEDERATION_MANIFEST.md
3. CONSTITUTION.md
4. AUTHORITY_MODEL.md
5. OPERATING_PROTOCOL.md
6. VERSIONING_POLICY.md
7. REGISTRY.md
```

Reason:

* tạo foundation kernel độc lập;
* chưa mở rộng agency module quá sớm;
* Reference Track R0 được tạo ngay sau Phase 0 để tránh build module theo cảm tính;
* chưa cần compatibility mapping với v1;
* tránh tạo nhiều file đẹp nhưng chưa có governance core rõ.

---

## 15. Open Questions

Các câu hỏi cần giải quyết trước activation đầy đủ:

```text
Q1. Khi nào v2 được xem là đủ self-contained để pilot?
Q2. Registry nội bộ v2 nên ghi status theo Active/Draft/Planned hay Planning/Implemented/Activated?
Q3. Agency charter nên là active governance hay advisory protocol trong giai đoạn đầu?
Q4. V2 chỉ dùng Markdown hay sau này thêm YAML/JSON policy?
Q5. Có cho phép memo update tự động ở mức short-term không?
Q6. Tool Safety có cần runtime enforcement kiểu AGT ở giai đoạn sau không?
Q7. Mỗi experiment có cần một Experiment Steward Agent riêng không?
Q8. Pilot report có lưu trong v2/pilot/ không?
Q9. Cần bao nhiêu pilot thành công trước partial activation?
Q10. Rollback mechanism khi v2 gây confusion là gì?
Q11. Khi reference ngoài thay đổi, ai/phase nào đánh dấu stale?
Q12. Design decision nào bắt buộc phải có source trước khi implement?
```

---

## 16. Current Decision State

Đã xác nhận:

* xây Meow v2 theo hướng Agent Federation;
* v2 nằm trong folder riêng;
* v2 là hệ độc lập, self-contained, có thể vận hành không cần v1;
* v1 chỉ là nguồn tham khảo/di sản thiết kế;
* không cần legacy mapping trong Phase 0;
* xây khung hoàn chỉnh trước, mở rộng agency module sau;
* Reference Track phải chạy song song với quá trình build v2;
* trước khi build module mới phải có `GATE-REFERENCE`;
* User là cấp decision authority cao nhất;
* Constitution phải chặt chẽ, minh bạch, rõ ràng và được tuân thủ nghiêm;
* nội dung chung của agent dùng tiếng Việt, thuật ngữ English có thể giữ khi phù hợp;
* tài liệu Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học là nguồn tham khảo quan trọng cho chuẩn nghiên cứu khoa học;
* Constitution chỉ bổ sung nguyên tắc khoa học cốt lõi, không biến tài liệu tham khảo thành luật chi tiết nặng nề;
* Meow v2 cần Oversight Layer gồm `Operational Inspector` và `Scientific Critic`;
* `Scientific Critic` là cơ chế giám sát/phản biện khoa học ngang hàng với kiểm tra vận hành, không phải Research Agency và không tự can thiệp sâu vào execution;
* task có claim/kết luận/validation khoa học quan trọng phải qua `GATE-SCIENTIFIC-CRITIQUE`.
* Phase 1 governance and oversight charters đã hoàn thiện draft stage trong folder riêng, sẵn sàng cho review/iterate.
* Phase 2 core coordinator charter đã hoàn thiện draft stage trong folder riêng, sẵn sàng cho review/iterate.
* Phase 3 schema layer đã hoàn thiện draft stage trong folder riêng, sẵn sàng cho review/iterate.
* Phase 4 functional agencies đã hoàn thành draft stage trong folder riêng, sẵn sàng cho review/iterate.
* Phase 5 reference consolidation đã hoàn tất draft stage, các file audit/review đã có trong folder riêng.
* Phase 6 dry-run pilots đã hoàn tất trong `pilot/`, chỉ là dry-run artifacts và không mutate file thật.
* Memo support layer trong `memo/` đã được bootstrap từ khung v1, nhưng state bên trong là state của v2.

* Phase 8 partial activation đã được mở hẹp cho task QUERY/ANALYSIS mức FAST/GUIDED.
* Runtime package `runtime/` đã được khởi tạo như lớp enforcement tối thiểu; hiện compile-ok, smoke-test pass, và đã tách riêng `intent` với `topic`.
* Executor trong runtime vẫn là adapter-only, chưa gắn backend thực.

Chưa xác nhận:

* thời điểm v2 được pilot;
* thời điểm v2 được partial activation;
* mức độ mở rộng runtime sau Phase 8 smoke-test;
* mức độ mở rộng memo automation trong v2;
* có dùng YAML/JSON policy hay chỉ Markdown;
* exact content của từng file Phase 6;
* có đăng ký v2 vào registry v1 hay không trong tương lai.

---

## 17. Next Recommended Step

Bước tiếp theo sau pilot là **Phase 7 - Compatibility Review** để đối chiếu v2 với v1 trên nền tảng pilot đã hoàn tất.

Trọng tâm phase này:

1. so sánh v2 với v1 ở mức advisory;
2. ghi lại điểm reuse và điểm khác biệt;
3. giữ compatibility làm tài liệu tham khảo, không biến thành dependency;
4. chỉ sau đó mới cân nhắc các bước mở rộng tiếp theo.
---

## 19. Sprint Contract - Phase 5 Reference Consolidation

Task: audit và củng cố Reference Track sau khi Phase 0-4 đã có bản draft.

Scope:

* audit các nguồn tham khảo đã đăng ký;
* kiểm tra source nào stale, weak, outdated hoặc không còn phù hợp;
* rà lại design decisions từ reference để xem decision nào cần giữ, sửa, defer hoặc reject;
* chuẩn bị nền cho pilot và partial activation sau này;
* không biến reference thành active rule.

Files dự kiến:

* `agent_hub/federation_v2/references/REFERENCE_AUDIT.md`
* `agent_hub/federation_v2/references/STALE_SOURCE_REPORT.md`
* `agent_hub/federation_v2/references/DESIGN_DECISION_REVIEW.md`

Rules áp dụng:

* `AGENTS.md` root
* `agent_hub/MEOW_AGENT.md`
* `agent_hub/federation_v2/CONSTITUTION.md`
* `agent_hub/federation_v2/OPERATING_PROTOCOL.md`
* `agent_hub/federation_v2/FEDERATION_MANIFEST.md`
* `agent_hub/federation_v2/REGISTRY.md`
* `agent_hub/federation_v2/references/REFERENCES.md`
* `agent_hub/federation_v2/references/SOURCE_MAPPING.md`
* `agent_hub/federation_v2/references/READ_ORDER.md`
* `agent_hub/federation_v2/references/DESIGN_DECISIONS_FROM_REFERENCES.md`

Gates bắt buộc:

* `GATE-REFERENCE`
* `GATE-EVIDENCE`
* `GATE-SCIENTIFIC-CRITIQUE` nếu review source làm thay đổi claim khoa học
* `GATE-USER-CONFIRMATION` trước mọi file mutation

Allowed:

* audit source status;
* đề xuất stale / keep / update / defer;
* review design decision mapping;
* ghi nhận gap và risk;
* chuẩn bị roadmap cho pilot.

Forbidden:

* xóa source cũ khi chưa có lý do rõ;
* promote reference thành rule;
* đổi constitutional principle;
* tạo pilot/compatibility output trước phase của nó;
* âm thầm đổi meaning của source tham khảo.

Risks:

* stale source làm lệch decision;
* review quá rộng làm loãng trọng tâm;
* reference audit bị biến thành rule change;
* source ngoài mâu thuẫn Constitution.

Exit criteria:

* source map và design decision map được rà lại;
* stale/weak source được đánh dấu rõ;
* phase sau có nền tham khảo sạch hơn để xây pilot.

---

## 18. Status

File này là planning artifact cho Meow v2 Agent Federation.

File này không kích hoạt v2.

File này không sửa Meow v1.

Phase 6 dry-run pilots đã hoàn tất trong `pilot/` và chỉ được hiểu là dry-run, không phải activation.

Phase 7 compatibility review đã có artifact riêng trong `compatibility/` và chỉ là đối chiếu/advisory, không phải migration.

File này là roadmap để triển khai v2 theo hướng độc lập, self-contained và có kiểm soát.



## 20. Migration update

The default `Meow` entry has been switched to the v2 federation path, and the v1 snapshot is archived in `agent_hub/version/v1/`.

The v2 experiment overlay is now mirrored under `agent_hub/federation_v2/experiments/` so v2 can route experiments without depending on the root legacy path.

---

## 21. Chot lo trinh 5 buoc

Lo trinh hien tai cua Meow v2 duoc chot thanh 5 buoc, theo thu tu:

### Buoc 1 - Hoan thien Governance / Oversight

Muc tieu:

* chot wording cuoi cho `governance/LAWMAKER_AGENT.md`;
* chot wording cuoi cho `governance/CONFLICT_COURT.md`;
* chot wording cuoi cho `governance/DECISION_RECORDS.md`;
* chot wording cuoi cho `oversight/OPERATIONAL_INSPECTOR.md`;
* chot wording cuoi cho `oversight/SCIENTIFIC_CRITIC.md`.

Exit criteria:

* 5 charter phan quyen ro;
* escalation path ro;
* output schema va gate lien quan khong con mung mo;
* registry status dong bo voi thuc trang.

### Buoc 2 - Khoa Schema Layer

Muc tieu:

* hoan thien cac schema output/report;
* giu field bat buoc on dinh;
* fail-closed ro rang;
* khong chen logic van hanh vao schema.

Exit criteria:

* schema dung vai tro template + contract format;
* producer/consumer mapping ro;
* co the dung lam dau vao cho pilot va runtime.

### Buoc 3 - Hoan thien Functional Agencies

Muc tieu:

* chot cac agency chuyen mon theo mandate rieng;
* giam role bleed;
* chi moi agency mot output chinh va mot duong escalate.

Exit criteria:

* research, memo, knowledge, coding, tool safety, experiment, data/output co ranh gioi ro;
* routing khong con cham cheo.

### Buoc 4 - Chuan hoa Pilot

Muc tieu:

* dong bo lai report va ket luan pilot;
* sua registry status cho khop thuc trang;
* giu pilot la dry-run artifact, khong nang thanh decision.

Exit criteria:

* pilot report khop voi registry;
* khong co mismatch status lon;
* cac case chinh da duoc xac nhan hanh vi.

### Buoc 5 - Chot Compatibility

Muc tieu:

* giu `compatibility/MEOW_V1_COMPARISON.md` va `compatibility/MIGRATION_NOTES.md` o muc advisory;
* khong de compatibility keo runtime v2 quay ve phu thuoc v1;
* dung lam tai lieu doi chieu va migration note, khong phai co che van hanh.

Exit criteria:

* comparison ro rang;
* migration note chi mang tinh tham khao;
* v2 van self-contained.

Tham chieu uu tien khi thuc hien:

```text
1. Governance / Oversight
2. Schemas
3. Agencies
4. Pilot
5. Compatibility
```

Nguyen tac:

* khong dao nguoc dependency;
* khong mo rong agency truoc khi governance va schema on dinh;
* khong chuyen pilot thanh activation;
* khong chuyen compatibility thanh dependency moi.

---

## 22. Sprint Contract - Phase 2 Core Coordinator

Task: hoan thien lop dieu phoi trung tam cua Meow v2, bao gom Coordinator, routing va gate protocol.

Scope:

* chot wording cuoi cho `core/MEOW_COORDINATOR.md`;
* chot wording cuoi cho `core/TASK_ROUTING.md`;
* chot wording cuoi cho `core/GATE_PROTOCOL.md`;
* giu Coordinator chi la lop dieu phoi, khong the vuot len governance, oversight hay agency;
* khong mo rong sang schemas, agencies, runtime, hay pilot.

Files in scope:

* `core/MEOW_COORDINATOR.md`
* `core/TASK_ROUTING.md`
* `core/GATE_PROTOCOL.md`

Rules ap dung:

* `CONSTITUTION.md`
* `AUTHORITY_MODEL.md`
* `OPERATING_PROTOCOL.md`
* `FEDERATION_MANIFEST.md`
* `REGISTRY.md`
* `governance/LAWMAKER_AGENT.md`
* `governance/CONFLICT_COURT.md`
* `governance/DECISION_RECORDS.md`
* `oversight/OPERATIONAL_INSPECTOR.md`
* `oversight/SCIENTIFIC_CRITIC.md`
* `references/REFERENCES.md`
* `references/SOURCE_MAPPING.md`
* `references/DESIGN_DECISIONS_FROM_REFERENCES.md`

Reference basis:

* `REF-DEC-007` - harness / coordinator framing
* `REF-DEC-008` - subagent isolation and report boundary
* `REF-DEC-010` - agent instructions, tools, handoffs, guardrails
* `REF-DEC-011` - handoff-style routing
* `REF-DEC-012` - guardrails + tracing
* `REF-DEC-024` - Operating Contract / Conflict Report continuity from v1
* `REF-DEC-003` - fail-closed when source / permission / policy is unclear

Gates bat buoc:

* `GATE-REFERENCE`
* `GATE-READ`
* `GATE-SCOPE`
* `GATE-INSPECTION`
* `GATE-USER-CONFIRMATION` truoc moi file mutation
* `GATE-SCIENTIFIC-CRITIQUE` neu routing/coordination cham claim khoa hoc

Allowed:

* chot route decision;
* tao Coordination Report;
* chuan hoa task classification;
* chuan hoa handoff boundary;
* giu gate sequence ngan gon;
* dong bo wording giua Coordinator, TASK_ROUTING, va GATE_PROTOCOL.

Forbidden:

* overrule Constitution;
* thay User decision;
* mutate file khi chua co approval;
* bien Coordinator thanh body quyet dinh cuoi;
* route bo qua Inspector / Scientific Critic khi task can;
* de task nho bi full governance neu khong can.

Risks:

* Coordinator bi phinh thanh agent tong hop qua tay;
* routing matrix qua nhe lam mat gate;
* routing matrix qua nang lam phinh workflow;
* gate protocol bi trung voi Operating Protocol neu wording khong gon;
* handoff khong ro lam rot context giua body.

Exit criteria:

* Coordinator co mandate ngan gon, ro rang, khong vuot quyen;
* TASK_ROUTING co bang route day du cho INFO / GOVERNANCE / OVERSIGHT / AGENCY / MUTATION / SCIENCE / UNKNOWN;
* GATE_PROTOCOL co thu tu gate va stop rule khop voi Operating Protocol;
* Coordination Report, routing decision, va gate decision dung cung vocabulary;
* phase 2 sẵn sàng review/iterate ma khong lam phinh core.
