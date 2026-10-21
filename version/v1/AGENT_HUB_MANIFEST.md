# AGENT_HUB_MANIFEST.md

## 1. Mục đích

`AGENT_HUB_MANIFEST.md` là file điều hướng chính của `agent_hub/`.

File này giúp agent biết:

* cần đọc file nào trước;
* rule nào quản lý tác vụ hiện tại;
* khi nào cần đọc memo module để định tuyến nhanh;
* khi nào cần tra governance;
* khi nào cần tra experiment registry;
* khi nào cần đọc rule riêng của experiment;
* khi nào phải tạo `Operating Contract`;
* khi nào phải tạo `Conflict Report`.

File này chỉ đóng vai trò **điều hướng và kích hoạt quy trình**, không chứa chi tiết riêng của một experiment cụ thể.

---

## 2. Nguyên tắc chung

`AGENT_HUB_MANIFEST.md` phải giữ tính tổng quát.

Không được hard-code chi tiết riêng của một experiment, ví dụ:

* tên pipeline cụ thể;
* tên notebook cụ thể;
* công thức cụ thể;
* phase/step cụ thể;
* quyết định khoa học cụ thể;
* issue riêng của một experiment.

Các nội dung riêng đó phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

hoặc trong tài liệu nghiên cứu được index bởi experiment tương ứng.

---

## 3. Luồng đọc bắt buộc cho tác vụ không đơn giản

Với mọi tác vụ không đơn giản, agent phải đọc theo thứ tự:

```text
1. AGENTS.md
2. agent_hub/AGENT_HUB_MANIFEST.md
3. agent_hub/governance/RULE_GOVERNANCE.md
4. agent_hub/governance/RULE_REGISTRY.md
```

Nếu `agent_hub/memo/` tồn tại, agent có thể đọc memo sau governance để định tuyến nhanh:

```text
5. agent_hub/memo/MEOW_MEMO_MANIFEST.md
6. agent_hub/memo/long_term/ROUTING_MEMORY.md
7. agent_hub/memo/long_term/PROJECT_STATE.md
8. agent_hub/memo/short_term/SESSION_STATE.md nếu task nối tiếp phiên trước
```

Memo module không thay thế rule, registry, experiment context, tài liệu nghiên cứu,
notebook hoặc output thật. Nếu memo mâu thuẫn với source canonical, source canonical thắng.

Nếu tác vụ liên quan đến một experiment, agent phải đọc thêm:

```text
9. agent_hub/experiments/EXPERIMENT_REGISTRY.md
10. rule/context riêng của experiment tương ứng
```

Nếu tác vụ liên quan đến tài liệu nghiên cứu, nguồn, memo, report hoặc setup tool, agent phải tra thêm:

```text
doc/DOC_INDEX.md
```

nếu file này đã tồn tại.

---

## 4. Khi nào là tác vụ không đơn giản?

Một tác vụ được xem là không đơn giản nếu liên quan đến một trong các nhóm sau:

* code;
* notebook;
* dữ liệu;
* output thực nghiệm;
* công thức;
* mô hình vật lý;
* mô hình học máy;
* pipeline;
* validation;
* citation;
* tài liệu khoa học;
* refactor;
* tạo file mới;
* sửa file;
* di chuyển file;
* thay đổi cấu trúc project;
* thay đổi rule hoặc protocol;
* làm việc trong một experiment cụ thể.

Với các tác vụ này, agent phải tạo `Operating Contract` trước khi làm.

---

## 5. Chế độ làm việc mặc định

Trừ khi người dùng cho phép rõ ràng, agent phải hoạt động ở chế độ:

```text
chỉ đọc → phân tích → đề xuất → chờ xác nhận
```

Agent được phép:

* đọc file;
* kiểm tra cấu trúc project;
* tra registry;
* phân tích rule;
* phân tích tài liệu;
* đề xuất hướng xử lý;
* đề xuất nội dung file;
* đề xuất code;
* báo cáo rủi ro;
* báo cáo xung đột.

Agent không được tự ý:

* sửa code;
* sửa notebook;
* tạo file mới;
* ghi đè file;
* di chuyển file;
* đổi tên file/thư mục;
* refactor project;
* đổi công thức;
* đổi giả định;
* đổi pipeline;
* tạo experiment mới;
* cập nhật rule;
* biến đề xuất thành quyết định.

---

## 6. Điều hướng theo loại tác vụ

### 6.1. Tác vụ liên quan rule hoặc governance

Nếu task liên quan đến rule, governance, manifest, registry, conflict hoặc operating contract, agent phải đọc:

```text
agent_hub/governance/RULE_GOVERNANCE.md
agent_hub/governance/RULE_REGISTRY.md
```

Nếu cần thêm rule mới hoặc sửa rule cũ, agent phải tạo đề xuất trước và chờ người dùng xác nhận.

---

### 6.2. Tác vụ liên quan experiment

Nếu task liên quan đến một experiment, agent phải tra:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
```

Sau đó xác định:

* experiment ID;
* thư mục thật của experiment;
* file active rules;
* file context index;
* trạng thái experiment;
* các tài liệu bắt buộc phải đọc.

Agent không được tự đoán rule của experiment nếu registry chưa chỉ rõ.

Nếu experiment chưa có trong registry, agent phải báo:

```text
Experiment chưa được đăng ký trong EXPERIMENT_REGISTRY.md.
```

và đề xuất cách đăng ký, không tự tạo nếu chưa được phép.

---

### 6.3. Tác vụ liên quan tài liệu nghiên cứu

Nếu task liên quan đến tài liệu, memo, report, paper, user guide hoặc source/reference, agent phải tra:

```text
doc/DOC_INDEX.md
```

nếu đã tồn tại.

Nếu `DOC_INDEX.md` chưa tồn tại, agent phải đề xuất tạo index thay vì tự suy đoán vai trò của từng file.

---

### 6.4. Tác vụ liên quan setup tool

Nếu task liên quan đến setup công cụ, ví dụ NotebookLM MCP, Antigravity, Codex, GitHub MCP hoặc môi trường phát triển, tài liệu hướng dẫn phải được đặt trong:

```text
doc/tools/
```

Không đặt setup/tool notes trong `agent_hub/`, trừ khi đó là rule vận hành agent.

---

### 6.5. Tác vụ liên quan code/notebook

Nếu task liên quan đến code hoặc notebook, agent phải:

1. xác định experiment hoặc module liên quan;
2. tra rule tương ứng;
3. xác định file có thể bị ảnh hưởng;
4. tạo `Operating Contract`;
5. chỉ đề xuất code hoặc thay đổi;
6. chờ người dùng xác nhận trước khi sửa file.

---

### 6.6. Tác vụ liên quan memo module

Nếu task liên quan đến Meow memory, session memory, project state cache hoặc memo lifecycle, agent phải đọc:

```text
agent_hub/memo/MEOW_MEMO_MANIFEST.md
agent_hub/memo/long_term/ROUTING_MEMORY.md
agent_hub/memo/long_term/PROJECT_STATE.md
agent_hub/memo/short_term/SESSION_STATE.md
agent_hub/memo/log/MEMO_LOG_2026.md nếu cần truy vết
```

Memo module có ba tầng:

```text
Long-Term MEMO  -> state/decision/issue/routing bền
Short-Term MEMO -> task/session context
Log MEMO        -> append-only episode trace
```

Khi cập nhật memo, agent phải phân biệt:

```text
ADD
UPDATE
DELETE
NOOP
```

Không được nâng thông tin lên long-term memo nếu chưa có source canonical hoặc xác nhận rõ.

---

## 7. Operating Contract

Trước mọi tác vụ không đơn giản, agent phải tạo `Operating Contract`.

Mẫu tối thiểu:

```text
OPERATING CONTRACT

Task:
...

Task type:
...

Scope:
...

Applicable rules:
...

Allowed actions:
...

Forbidden actions:
...

Required files to read:
...

Required gates:
...

Potential conflicts:
...

Need user confirmation before file edits:
Yes / No
```

Nếu task có nhiều cách hiểu, agent phải nêu rõ các cách hiểu trước khi chọn hướng xử lý.

Nếu phải chọn một cách hiểu tạm thời, agent phải ghi rõ đó là giả định.

---

## 8. Conflict Report

Nếu phát hiện xung đột rule, agent phải dừng và tạo `Conflict Report`.

Mẫu tối thiểu:

```text
CONFLICT REPORT

Conflict ID:
...

Conflict type:
...

Related files/rules:
...

Description:
...

Why this matters:
...

Severity:
BLOCKER / MAJOR / MINOR

Recommended resolution:
...

Need user decision:
Yes / No
```

Agent không được âm thầm chọn rule tiện lợi hơn nếu xung đột chưa được xử lý.

---

## 9. Priority routing

Thứ tự ưu tiên tổng quát:

```text
P0 — System/tool constraints
P1 — Lệnh trực tiếp hiện tại của người dùng
P2 — Root AGENTS.md
P3 — Governance rules trong agent_hub/governance/
P4 — Experiment-level rules trong agent_hub/experiments/
P5 — Domain knowledge, memo, report, protocol trong doc/
P6 — Task-specific prompt
P7 — Model default behavior
```

`agent_hub/memo/` là operational memory/cache. Nó hỗ trợ routing và recall, nhưng không có priority cao hơn governance, experiment rules hoặc source canonical.

Nếu không chắc priority nào áp dụng, agent phải hỏi người dùng.

---

## 10. Quan hệ với experiment-specific rules

File chung chỉ điều hướng đến experiment-specific rules.

Rule riêng của experiment phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

Ví dụ cấu trúc chung:

```text
agent_hub/experiments/<experiment_id>/
├── <EXPERIMENT_ID>_ACTIVE_RULES.md
└── <EXPERIMENT_ID>_CONTEXT_INDEX.md
```

Trong đó:

* `*_ACTIVE_RULES.md`: quy tắc active cho experiment;
* `*_CONTEXT_INDEX.md`: bản đồ notebook, data, output, memo, report, source liên quan.

File chung không được copy chi tiết của các file này.

---

## 11. Quan hệ với `doc/`

`doc/` là kho tài liệu nghiên cứu.

Định hướng chung:

```text
doc/
├── README.md
├── DOC_INDEX.md
├── sources/
├── tools/
├── <domain>/
└── archive/
```

Trong đó:

* `doc/sources/`: paper, PDF, user guide, tài liệu gốc;
* `doc/tools/`: hướng dẫn setup công cụ;
* `doc/<domain>/`: knowledge, memo, report, formula audit theo domain;
* `doc/archive/`: tài liệu cũ hoặc legacy.

`agent_hub/` có thể trỏ tới file trong `doc/`, nhưng không nên sao chép toàn bộ nội dung nghiên cứu vào rule file.

---

## 12. Stop conditions

Agent phải dừng và hỏi người dùng nếu gặp một trong các điều kiện sau:

* task yêu cầu sửa file nhưng chưa có xác nhận rõ;
* task yêu cầu thay đổi pipeline, công thức hoặc giả định;
* task yêu cầu diễn giải kết quả chưa validated như kết luận khoa học;
* task yêu cầu tạo experiment mới nhưng chưa có registry entry;
* task yêu cầu dùng tài liệu/công thức chưa có nguồn rõ;
* rule giữa các file mâu thuẫn nhau;
* memo module mâu thuẫn với source canonical;
* agent không xác định được experiment hoặc domain liên quan;
* agent không chắc file nào là canonical.

---

## 13. Trạng thái

Phiên bản: `v0.2`

Trạng thái: manifest generic cho agent hub with memo-module routing.

Nguyên tắc chính:

* file chung chỉ chứa luật chung;
* experiment-specific logic nằm trong thư mục experiment tương ứng;
* tài liệu nghiên cứu nằm trong `doc/`;
* setup/tool notes nằm trong `doc/tools/`;
* memo module nằm trong `agent_hub/memo/` và chỉ là operational memory/cache;
* mọi tác vụ không đơn giản phải có `Operating Contract`;
* mọi xung đột rule phải có `Conflict Report`.

Cập nhật lần cuối: `2026-06-09`
