# DESIGN_DECISIONS_FROM_REFERENCES.md

Version: `v0.1-draft`

Status: `reference-only`

Activation: `inactive`

---

## 1. Mục đích

File này ghi các quyết định thiết kế rút ra từ nguồn tham khảo cho Meow v2.

Mỗi item phải làm rõ:

```text
source -> idea/pattern -> ADOPT/ADAPT/REJECT/DEFER -> target module -> deeper reading
```

Các decision ở đây chưa phải active rule. Chúng là định hướng thiết kế để khi build module sau này, Meow biết cần cập nhật tiến bộ nào vào v2 và cần đọc sâu nguồn nào.

Nguyên tắc quan trọng:

```text
Reference is not a shopping list.
Không nhét mọi ý tưởng hay vào v2.
Chỉ adopt/adapt những gì giải quyết điểm yếu thật của Meow v1 hoặc giúp v2 vận hành chặt chẽ hơn.
```

---

## 2. Decision status

| Status | Ý nghĩa |
| --- | --- |
| `ADOPT` | Dùng gần như trực tiếp trong v2 |
| `ADAPT` | Dùng có điều chỉnh cho research governance |
| `REJECT` | Không dùng vì không phù hợp |
| `DEFER` | Chưa dùng ngay, giữ để xem xét sau |

---

## 3. Priority summary

30 decisions trong file này là **candidate design decisions**, không phải 30 việc cần implement ngay.

Meow v2 dùng ba mức ưu tiên:

| Priority | Ý nghĩa | Cách xử lý |
| --- | --- | --- |
| `EARLY-CORE` | Nên đưa vào sớm vì sửa điểm yếu nền của v1 và cần cho governance kernel/Phase 1-2 | implement hoặc phản ánh ngay trong Governance Core / Coordinator / early schema |
| `PHASE-SPECIFIC` | Có giá trị nhưng chỉ nên dùng khi đến đúng module/phase | giữ trong roadmap, đọc sâu khi implement module liên quan |
| `DEFER / WATCH` | Ý tưởng hay nhưng dễ làm v2 nặng, lệch hướng hoặc chưa cần | không implement sớm; chỉ dùng cho pilot hoặc phase tương lai |

### 3.1. EARLY-CORE decisions

Các decision này đáng ưu tiên trong Phase 1-2 vì trực tiếp cải thiện governance so với v1.

| ID | Lý do ưu tiên | Module nên cập nhật sớm |
| --- | --- | --- |
| `REF-DEC-003` | Formal hóa fail-closed khi thiếu permission/source/policy | Operational Inspector, Operating Protocol |
| `REF-DEC-005` | Tool/action cần explicit consent; không tin tool description tuyệt đối | Tool Safety, Authority Model |
| `REF-DEC-008` | Agency phải có report boundary, không tự mutate | Coordinator, Agency Charter |
| `REF-DEC-010` | Agency interface cần rõ instructions/input/output/guardrails | Coordinator, Agency Charter |
| `REF-DEC-012` | Guardrails + tracing là nền cho Operational Inspector và Decision Records | Operational Inspector, Decision Records |
| `REF-DEC-014` | Memo permission model: long-term cần source/User confirm | Memo Agency |
| `REF-DEC-019` | Risk taxonomy giúp Operational Inspector không đánh giá rủi ro cảm tính | Operational Inspector, Tool Safety |
| `REF-DEC-024` | Giữ xương sống tốt từ v1: Operating Contract, Conflict Report, read/analyze/propose/wait | Operating Protocol, Coordinator |
| `REF-DEC-025` | Pattern active rules + context index hữu ích cho Experiment Steward | Experiment Steward |
| `REF-DEC-026` | Research question là kernel giúp mọi claim/method có điểm neo rõ | Constitution, Scientific Critic |
| `REF-DEC-028` | Scientific basis cần evidence, method, theory/checkability và kết luận tương xứng | Constitution, Scientific Critic, Research Agency |
| `REF-DEC-029` | Data integrity, plagiarism và credit integrity là điều kiện nền của nghiên cứu khoa học | Constitution, Scientific Critic, Memo/Knowledge |

Nếu Phase 1 chỉ chọn vài ý chính, chọn theo thứ tự:

```text
1. REF-DEC-003 fail-closed
2. REF-DEC-012 guardrails/tracing
3. REF-DEC-019 risk taxonomy
4. REF-DEC-024 Operating Contract / Conflict Report
```

### 3.2. PHASE-SPECIFIC decisions

Các decision này có giá trị nhưng không nên đưa vào mọi nơi ngay.

| ID | Dùng khi nào | Ghi chú |
| --- | --- | --- |
| `REF-DEC-001` | Tool Safety / Action Policy Schema | chưa cần runtime policy engine |
| `REF-DEC-002` | Decision Records / Schema Layer | chuẩn hóa audit trước, tamper-evident để sau |
| `REF-DEC-006` | Knowledge Agency / Tool Safety | dùng khi phân loại resources/prompts/tools |
| `REF-DEC-007` | Coordinator / harness architecture | dùng như khung tư duy, không framework hóa |
| `REF-DEC-009` | Tool Safety / Action Policy | policy hóa permission sau khi có schema |
| `REF-DEC-011` | Coordinator | handoff-style routing |
| `REF-DEC-013` | Memo Agency | checkpoint/context rebuild nhưng cần kiểm soát |
| `REF-DEC-015` | Memo / Knowledge Agency | lifecycle và summary strategy |
| `REF-DEC-020` | Operational Inspector / Pilot | dùng vừa đủ risk lifecycle, tránh enterprise hóa |
| `REF-DEC-021` | Experiment Steward / Coding | SOP và intermediate verification |
| `REF-DEC-027` | Research Agency / Scientific Critic | FINER hữu ích khi đánh giá câu hỏi nghiên cứu, không cần áp vào mọi task nhỏ |
| `REF-DEC-030` | Research report / Evaluation | đánh giá khoa học đa chiều, dùng khi review output/report hơn là gate vận hành thường ngày |

### 3.3. DEFER / WATCH decisions

Các decision này giữ để tham khảo, không implement sớm.

| ID | Vì sao defer |
| --- | --- |
| `REF-DEC-004` | là limitation/warning cần ghi nhớ, không phải feature lớn |
| `REF-DEC-016` | CrewAI hữu ích cho role analogy nhưng dễ kéo sang business automation |
| `REF-DEC-017` | AutoGen group chat dễ tạo debate dài và đồng thuận giả |
| `REF-DEC-018` | A2A Agent Card hữu ích nhưng quá sớm |
| `REF-DEC-022` | CAMEL role-play không đủ strict cho governance core |
| `REF-DEC-023` | AgentGit rollback hay nhưng chưa cần trong local workflow |

### 3.4. Adoption filter

Trước khi đưa bất kỳ decision nào vào module v2, Meow phải hỏi:

```text
1. Nó sửa điểm yếu cụ thể nào của v1?
2. Nó có phục vụ research integrity không?
3. Nó có làm v2 nặng hoặc lệch hướng không?
4. Nó có cần implementation/runtime dependency không?
5. Nó có thể diễn đạt bằng Markdown/protocol trước không?
6. Nó có cần User decision, Operational Inspector review hoặc Scientific Critic review không?
```

Nếu không trả lời rõ được 1-3, decision phải `DEFER`.

---

## 4. Full decision inventory

| ID | Source | Idea / tiến bộ mới | Decision | Vì sao | Target v2 module | Cần đọc sâu khi implement | Ưu điểm so với v1 | Nhược điểm / rủi ro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REF-DEC-001 | Microsoft AGT | Deterministic policy gate trước tool/action | `ADAPT` | V2 cần action-aware governance, nhưng chưa cần runtime SDK | Operational Inspector, Tool Safety, Action Policy Schema | AGT Policy Engine spec, AGT limitations, MCP Gateway spec | V1 chủ yếu dựa vào protocol; v2 có thể tiến tới fail-closed rõ hơn | Nếu bê nguyên sẽ quá nặng và lệch research workflow |
| REF-DEC-002 | Microsoft AGT | Audit/Decision Record cho mỗi allow/deny | `ADAPT` | V2 cần trace action/decision tốt hơn memo narrative | Decision Records, Registry, Inspection Report Schema | AGT Audit and Compliance spec | V1 log còn thủ công; v2 có thể chuẩn hóa decision trace | Tamper-evident/Merkle audit chưa cần ngay |
| REF-DEC-003 | Microsoft AGT | Fail-closed khi policy/permission không rõ | `ADOPT` | Phù hợp với nghiên cứu khoa học và file mutation safety | Operational Inspector, Operating Protocol | AGT policy examples, limitations | V1 có stop condition nhưng chưa luôn biểu đạt như fail-closed | Có thể làm workflow chậm hơn |
| REF-DEC-004 | AGT limitations | Governance middleware không thay thế OS/kernel isolation hoặc reasoning validation | `ADOPT` | V2 phải ghi rõ giới hạn của Tool Safety | Tool Safety, Constitution, Versioning | AGT limitations/security boundaries | Tránh ảo tưởng governance | Cần nhắc lại trong module runtime sau này |
| REF-DEC-005 | MCP spec | Tool descriptions/annotations không mặc nhiên đáng tin; tool use cần explicit consent | `ADOPT` | Cực kỳ phù hợp với Tool Safety và User authority | Tool Safety, Authority Model, Operating Protocol | MCP Security and Trust & Safety | V1 chưa có tool-trust model rõ | Có thể tăng số lần hỏi User khi dùng tools |
| REF-DEC-006 | MCP spec | Resources/Prompts/Tools là ba loại capability khác nhau | `ADAPT` | V2 nên phân loại tool/context/source interface rõ | Knowledge Agency, Tool Safety, Manifest | MCP server features/tools/resources/prompts | Giảm lẫn lộn source, prompt và action | Chưa cần MCP implementation |
| REF-DEC-007 | Deep Agents | Harness gồm execution environment, context management, delegation, steering | `ADAPT` | Đây là blueprint tốt cho v2 federation nhưng phải giữ research-first | Coordinator, Tool Safety, Memo, Agency design | Deep Agents overview, permissions, subagents, context engineering | V1 chưa có harness model rõ | Dễ bị framework hóa quá sớm |
| REF-DEC-008 | Deep Agents | Subagents chạy trong isolated context và trả về final report | `ADAPT` | Phù hợp cho agency model: agency trả report, không tự mutate | Coordinator, Agency Charter, Schema Layer | Deep Agents subagents docs | V1 role switching trong một agent; v2 có report boundary | Nếu quá nhiều subagents sẽ tốn token và rườm rà |
| REF-DEC-009 | Deep Agents | Declarative filesystem permissions | `ADAPT` | V2 nên có permission state và later Action Policy | Tool Safety, Action Policy Schema | Deep Agents permissions docs | V1 có cấm sửa nhưng chưa policy hóa | Cần tránh tạo policy giả không enforce được |
| REF-DEC-010 | OpenAI Agents SDK | Agent gồm instructions, tools, handoffs, guardrails, output type, hooks | `ADAPT` | Tốt cho thiết kế Agency Charter | Coordinator, Agency modules, Schema Layer | OpenAI Agents docs: agents, handoffs, guardrails | V1 thiếu formal agent interface | Không nên phụ thuộc SDK |
| REF-DEC-011 | OpenAI Agents SDK | Handoffs cho specialist agents | `ADAPT` | Meow Coordinator nên route task qua handoff-style protocol | Coordinator, Task Routing | OpenAI handoffs/orchestration docs | V1 routing chưa có agency handoff rõ | Handoff sai có thể mất context |
| REF-DEC-012 | OpenAI Agents SDK | Guardrails và tracing | `ADAPT` | Guardrail concept hợp với Operational Inspector; tracing hợp Decision Records | Operational Inspector, Decision Records, Schema Layer | OpenAI guardrails/tracing docs | V1 có review nhưng trace schema yếu | Need schema design trước khi implement |
| REF-DEC-013 | Xiaomi MiMoCode | Persistent project memory + checkpoint + context rebuild | `ADAPT` | Hữu ích cho Memo Agency, nhưng phải giữ source-confirmation rule | Memo Agency, Coordinator | MiMo README, memory service, checkpoint service, local note | V1 memo file-based, chưa có search/checkpoint tự động | Auto-memory dễ biến memo thành truth nếu không kiểm soát |
| REF-DEC-014 | MiMoCode local note | Auto-update chỉ nên cho short-term/task progress/log; long-term cần source/User confirm | `ADOPT` | Phù hợp trực tiếp với research safety | Memo Agency, Memo Update Schema | Local MiMo note, Mem0/Zep papers | Cải thiện v1 bằng permission model rõ | Cần implementation discipline |
| REF-DEC-015 | Zep/Mem0/GraphRAG | Memory lifecycle: retrieve/update/invalidate và local-to-global summaries | `ADAPT` | Memo v2 nên có lifecycle và summary strategy | Memo Agency, Knowledge Agency | local PDFs in `doc/memo/` | V1 đã có lifecycle sơ bộ; v2 có thể formal hóa hơn | Cần đọc sâu khi thiết kế Memo Agency |
| REF-DEC-016 | CrewAI | Crew/roles/tasks/process/manager pattern | `DEFER` | Hữu ích cho analogy, nhưng không nên dùng làm core governance | Coordinator, Agency design | CrewAI crews/process docs | Có thể giúp role clarity | Dễ kéo v2 sang business automation |
| REF-DEC-017 | AutoGen | Group chat + manager/selector + human proxy | `DEFER` | Hữu ích cho pilot debate/inspection, nhưng không dùng mặc định | Conflict Court, Pilot | AutoGen group chat docs | Có thể hỗ trợ multi-perspective review | Dễ sinh debate dài, tốn token, đồng thuận giả |
| REF-DEC-018 | A2A Protocol | Agent Card, Task, Message, Artifact, streaming task state | `DEFER` | Rất hữu ích nếu v2 sau này cần formal agent protocol | Registry, Agency interface, Schema Layer | A2A spec: Agent Card, Task, Message, Artifact | V1 không có agent interface chuẩn | Quá sớm cho Phase 1 |
| REF-DEC-019 | OWASP Agentic AI | Threat categories và mitigation language cho agentic systems | `ADAPT` | Dùng cho Operational Inspector risk taxonomy và Tool Safety | Operational Inspector, Tool Safety, Risk Register | OWASP Agentic AI threats/mitigations | V1 có risk nhưng chưa taxonomy hệ thống | Cần chọn subset phù hợp research repo |
| REF-DEC-020 | NIST AI RMF | GOVERN/MAP/MEASURE/MANAGE risk management framing | `ADAPT` | Dùng ngôn ngữ quản trị risk, không dùng như bureaucracy nặng | Governance Core, Operational Inspector, Pilot | NIST AI RMF overview/resources | V1 chưa có risk lifecycle formal | Có thể quá enterprise nếu dùng quá mức |
| REF-DEC-021 | MetaGPT | SOP + role decomposition + intermediate verification | `ADAPT` | Phù hợp với Experiment Steward và phase/step workflow | Experiment Steward, Coding Agency | MetaGPT paper | V1 có phase/step exp_01; v2 có thể generalize SOP | Không dùng automatic software company pattern |
| REF-DEC-022 | CAMEL | Role-playing agent cooperation | `DEFER` | Có thể hữu ích để test agency prompts, không là governance core | Pilot, examples | CAMEL paper | Hỗ trợ nghiên cứu multi-agent behavior | Không đủ strict cho research governance |
| REF-DEC-023 | AgentGit | Branch/rollback/trajectory comparison for multi-agent workflows | `DEFER` | Ý tưởng tốt cho future pilot/rollback, chưa cần ngay | Pilot, Versioning, Decision Records | AgentGit paper | V1 không có trajectory rollback | Chưa mature trong local workflow |
| REF-DEC-024 | Meow v1 | Operating Contract + Conflict Report + read/analyze/propose/wait | `ADOPT` | Đây là nền research governance đã phù hợp | Operating Protocol, Operational Inspector, Coordinator | v1 governance files | Giữ continuity và discipline | Cần viết lại self-contained trong v2 |
| REF-DEC-025 | Meow v1 exp_01 | Experiment active rules/context index | `ADAPT` | Mẫu tốt cho Experiment Steward: active rules + context map | Experiment Steward Agency | exp_01 active/context files | V1 đã bảo vệ baseline tốt | Không hard-code EC_CYG vào v2 global |
| REF-DEC-026 | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | Câu hỏi nghiên cứu là kernel của nghiên cứu | `ADOPT` | V2 phục vụ nghiên cứu nên mọi claim/method quan trọng cần neo vào câu hỏi rõ | Constitution, Scientific Critic, Research Agency | INT-NVT-NCKH phần câu hỏi nghiên cứu | V1 có scientific caution nhưng chưa buộc làm rõ research question | Nếu áp cứng vào mọi task nhỏ sẽ rườm rà |
| REF-DEC-027 | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | FINER: Feasible, Interesting, Novel, Ethical, Relevant | `ADAPT` | Hữu ích để đánh giá câu hỏi nghiên cứu, nhưng không phải checklist cho mọi phản hồi | Scientific Critic, Research Agency, Evidence Report Schema | INT-NVT-NCKH phần FINER | Giúp v2 hỏi đúng về chất lượng câu hỏi nghiên cứu | Có thể làm quá nặng nếu dùng như bureaucratic gate |
| REF-DEC-028 | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | Cơ sở khoa học cần dữ liệu, phương pháp, lý thuyết/cơ chế, kiểm tra được và kết luận tương xứng | `ADOPT` | Đây là chuẩn cốt lõi để chống overclaim và false validation | Constitution, Scientific Critic, Research Agency | INT-NVT-NCKH phần cơ sở khoa học/phương pháp | V1 đã cẩn trọng source nhưng chưa formal hóa đủ method/data/proportionate conclusion | Cần giữ ngắn trong Constitution, chi tiết để ở agency/schema |
| REF-DEC-029 | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | Data integrity, plagiarism, credit/authorship integrity và conflict disclosure | `ADOPT` | Đây là điều kiện đạo đức tối thiểu của nghiên cứu khoa học | Constitution, Scientific Critic, Memo Agency, Knowledge Agency | INT-NVT-NCKH phần đạo đức, plagiarism, tác giả, dữ liệu | V1 có source caution nhưng chưa nêu đầy đủ các dạng plagiarism/credit risk | Cần tránh biến thành luật xuất bản quá chi tiết ở Phase 0 |
| REF-DEC-030 | Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học | Đánh giá khoa học phải đa chiều, không chỉ dựa vào paper count, IF hoặc citation | `ADAPT` | Hữu ích khi review báo cáo/kết quả/nghiên cứu, nhưng không phải gate vận hành thường ngày | Scientific Critic, Research Agency, Pilot Review | INT-NVT-NCKH phần đánh giá khoa học | Giúp v2 tránh metric fetishism khi đánh giá chất lượng khoa học | Có thể ít liên quan tới coding/governance task hằng ngày |

---

## 5. Cập nhật mới nên đưa vào v2 so với v1

### 5.0. Scientific Constitution / Critic

Nên cập nhật:

* research question là điểm neo cho claim/method quan trọng;
* dùng FINER như checklist nhẹ khi đánh giá câu hỏi nghiên cứu;
* scientific basis phải gồm evidence, method, data/provenance, theory/mechanism hoặc rationale, checkability và kết luận tương xứng;
* data integrity, plagiarism, credit/authorship và conflict-of-interest risk phải được flag;
* Scientific Critic là oversight function ngang hàng với Operational Inspector, không phải Research Agency.

Cần đọc sâu:

* Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học;
* Meow v1 scientific caution;
* Research coding protocol;
* exp_01 active/context rules khi thiết kế Experiment Steward.

### 5.1. Governance / Operational Inspector

Nên cập nhật:

* fail-closed khi permission/source/policy không rõ;
* Inspection Report có `Can proceed`;
* risk taxonomy lấy cảm hứng từ OWASP/NIST;
* decision/audit records rõ hơn;
* phân biệt guardrail, operational inspection, scientific critique và conflict resolution.

Cần đọc sâu:

* AGT Policy Engine;
* AGT Audit and Compliance;
* AGT Limitations;
* OWASP Agentic AI threats;
* NIST AI RMF.

### 5.2. Tool Safety

Nên cập nhật:

* tool/action classification;
* explicit consent trước tool risk;
* coi tool descriptions là untrusted nếu không từ trusted source;
* action policy schema;
* future runtime enforcement path.

Cần đọc sâu:

* AGT MCP Security Gateway;
* MCP Security and Trust & Safety;
* Deep Agents permissions;
* OWASP Agentic AI.

### 5.3. Coordinator / Agency handoff

Nên cập nhật:

* handoff-style routing;
* agency report boundary;
* subagent isolation pattern;
* manager không override specialist/Operational Inspector/Scientific Critic;
* task state tracking.

Cần đọc sâu:

* OpenAI Agents SDK agents/handoffs/orchestration;
* Deep Agents subagents;
* CrewAI process/manager;
* AutoGen group chat.

### 5.4. Memo / Knowledge

Nên cập nhật:

* checkpointing long sessions;
* markdown memory search/index;
* short-term candidate queue va gated promotion sang long-term;
* source-confirmed long-term memory;
* context rebuild policy;
* staleness/invalidation lifecycle;
* local-to-global summaries.

Cần đọc sâu:

* MiMoCode memory/checkpoint files;
* local MiMo note;
* Zep, Mem0, GraphRAG papers;
* Deep Agents memory/skills/context engineering.

### 5.5. Coding / Experiment

Nên cập nhật:

* SOP-style phase/step workflow;
* generator-evaluator separation;
* intermediate verification;
* branch/sensitivity/proposal separation;
* future rollback/trajectory comparison idea.

Cần đọc sâu:

* Meow v1 coding rules;
* research coding protocol;
* MetaGPT paper;
* AgentGit paper later;
* exp_01 active/context as example only.

### 5.6. Short-term to long-term memo bridge

Nên cập nhật:

* short-term memo items co the gom candidate vao promotion queue;
* queue chi la bo dem trung gian, khong phai canonical memory;
* long-term promotion van phai qua validation gate va User confirmation khi can;
* candidate khong dat nguong thi giu `queued`, `deferred`, hoac `rejected`.

Cần đọc sâu:

* MiMoCode local note;
* Zep/Mem0 lifecycle material;
* current v2 memo support layer files;
* `REF-DEC-014` và `REF-DEC-015`.

---

## 6. Rejected or deferred ideas

Rejected for now:

* cài hoặc phụ thuộc framework bên ngoài ngay;
* biến AGT thành runtime dependency ở giai đoạn thiết kế;
* dùng CrewAI/AutoGen làm core execution loop;
* tự động cập nhật long-term research memory;
* group-chat mặc định cho mọi task.

Deferred:

* A2A Agent Card formalization;
* Git-like trajectory rollback;
* runtime policy engine;
* tamper-evident audit/Merkle log;
* automated memory indexing/search implementation.

---

## 7. Implementation rule

Trước khi implement module nào, Meow phải:

1. kiểm tra module đó trong `SOURCE_MAPPING.md`;
2. đọc `READ_ORDER.md` phần tương ứng;
3. kiểm tra các `REF-DEC-*` liên quan;
4. nếu cần thêm decision mới, update file này;
5. không biến reference thành active rule nếu chưa qua Constitution, Authority Model và User decision.
6. ưu tiên `EARLY-CORE` trước, chỉ dùng `PHASE-SPECIFIC` khi đúng module, và không implement `DEFER / WATCH` nếu chưa có decision mới.
