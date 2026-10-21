# MEOW_MEMO_MANIFEST.md

## 1. Mục đích

`agent_hub/memo/` là module bộ nhớ vận hành cho Meow.

Module này giúp Meow khởi động nhanh hơn, giữ trạng thái làm việc có truy vết,
và giảm nhu cầu quét lại toàn bộ project khi người dùng hỏi tình trạng hiện tại.

Memo module không thay thế:

* `AGENTS.md`;
* `agent_hub/MEOW_AGENT.md`;
* governance files;
* experiment active rules;
* experiment context index;
* research memo/report trong `doc/`;
* notebook, data hoặc output thật.

Memo chỉ là lớp định tuyến và tóm tắt có nguồn trỏ ngược.

---

## 2. Cơ sở thiết kế

Module này dựa trên ba ý tưởng chính:

1. Long-term memory cần ổn định, có nguồn, có cơ chế cập nhật và invalidation.
2. Short-term memory cần phục vụ phiên/task hiện tại, có thể thay đổi nhanh.
3. Log memory cần append-only để giữ trace của episode, audit, decision và thay đổi.

Tài liệu tham khảo đã lưu tại:

```text
doc/memo/2501.13956_Zep_Temporal_Knowledge_Graph_Agent_Memory.pdf
doc/memo/2504.19413_Mem0_Scalable_Long_Term_Memory.pdf
doc/memo/2404.16130_GraphRAG_Query_Focused_Summarization.pdf
```

Rút gọn thiết kế:

```text
Zep/Graphiti  -> episode / semantic / community memory + temporal validity
Mem0          -> extract / update / retrieve + ADD / UPDATE / DELETE / NOOP
GraphRAG      -> local-to-global summaries for project-level sensemaking
```

---

## 3. Cấu trúc

```text
agent_hub/memo/
├── MEOW_MEMO_MANIFEST.md
├── long_term/
│   ├── PROJECT_STATE.md
│   ├── DECISION_MEMORY.md
│   ├── ISSUE_MEMORY.md
│   └── ROUTING_MEMORY.md
├── short_term/
│   ├── SESSION_STATE.md
│   ├── TASK_CONTEXT.md
│   └── WORKING_SET.md
└── log/
    └── MEMO_LOG_2026.md
```

---

## 4. Ba tầng memo

### 4.1. Long-Term MEMO

Vai trò:

* lưu trạng thái bền của project;
* lưu decision đã xác nhận;
* lưu issue/risk còn mở;
* lưu routing ổn định;
* giúp Meow trả lời nhanh câu hỏi tổng quan.

Không dùng để lưu:

* log từng phiên;
* suy đoán tạm thời;
* kết luận khoa học chưa validated;
* nội dung thay thế research memo/report.

### 4.2. Short-Term MEMO

Vai trò:

* lưu trạng thái phiên/task hiện tại;
* lưu Operating Contract đang mở;
* lưu file đã đọc;
* lưu giả định tạm thời;
* lưu pending decision.

Short-term memory có thể stale nhanh và phải được kiểm tra trước khi dùng lại.

### 4.3. Log MEMO

Vai trò:

* append-only episode trace;
* ghi request, action, file đọc/sửa/tạo;
* ghi conflict/progress report;
* ghi decision được xác nhận;
* giúp truy vết vì sao long-term/short-term memory được cập nhật.

Không rewrite log cũ nếu không có yêu cầu rõ.

---

## 5. Lifecycle

Mọi cập nhật memo nên đi qua lifecycle:

```text
INGEST    -> ghi nhận sự kiện hoặc audit mới
EXTRACT   -> rút ra candidate issue/decision/routing/state
UPDATE    -> ADD / UPDATE / DELETE / NOOP
VALIDATE  -> đối chiếu source canonical trước khi nâng lên long-term
RETRIEVE  -> đọc đúng tầng memory theo task
INVALIDATE -> đánh dấu stale khi source canonical đổi
```

---

## 6. Startup routing đề xuất

Khi Meow khởi động nhanh:

```text
1. AGENTS.md
2. agent_hub/MEOW_AGENT.md
3. agent_hub/memo/MEOW_MEMO_MANIFEST.md
4. agent_hub/memo/long_term/ROUTING_MEMORY.md
5. agent_hub/memo/long_term/PROJECT_STATE.md
6. agent_hub/memo/short_term/SESSION_STATE.md nếu task nối tiếp phiên trước
```

Nếu task liên quan experiment, vẫn phải đọc:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
active rules của experiment
context index của experiment
```

Nếu task liên quan kết quả nghiên cứu, vẫn phải đọc research memo/report hoặc
output liên quan trong `doc/` và experiment folder.

---

## 7. Quy tắc an toàn

* Memo không được biến proposal thành decision.
* Memo không được biến exploratory result thành validated result.
* Memo không được override governance hoặc experiment rules.
* Mọi long-term memory item phải có source hoặc ghi rõ `source: pending`.
* Nếu memo mâu thuẫn với source canonical, source canonical thắng và memo phải được đánh dấu stale.
* Nếu không chắc memo còn đúng, phải đọc lại source canonical.

---

## 8. Trạng thái

Phiên bản: `v0.2`

Trạng thái: active initialized.

Cập nhật lần đầu: `2026-06-09`

Cập nhật gần nhất: `2026-06-09`
