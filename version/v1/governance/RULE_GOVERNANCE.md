# RULE_GOVERNANCE.md

## 1. Mục đích

`RULE_GOVERNANCE.md` là bộ quy tắc quản trị các bộ luật trong project.

File này không thay thế các rule khác. Nó quy định cách agent phải:

* đọc luật;
* xác định luật nào đang áp dụng;
* đánh giá mức ưu tiên;
* phát hiện xung đột;
* báo cáo xung đột;
* dừng khi cần thiết;
* yêu cầu người dùng xác nhận;
* đề xuất thêm, sửa hoặc loại bỏ rule.

Mục tiêu là tránh tình trạng nhiều rule/prompt tồn tại rời rạc, trùng lặp hoặc mâu thuẫn nhau mà không có cơ chế quản lý rõ ràng.

---

## 2. Nguyên tắc thiết kế

`RULE_GOVERNANCE.md` phải giữ tính tổng quát.

File này không chứa:

* rule riêng của một experiment cụ thể;
* tên pipeline cụ thể;
* công thức cụ thể;
* phase/step cụ thể;
* trạng thái notebook cụ thể;
* quyết định khoa học riêng của một experiment;
* issue riêng của một domain nghiên cứu.

Các nội dung riêng đó phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

hoặc trong tài liệu nghiên cứu được experiment tương ứng trỏ tới.

---

## 3. Thứ tự ưu tiên luật

Agent phải áp dụng thứ tự ưu tiên sau:

| Priority | Nguồn luật                                            | Ý nghĩa                                                                       |
| -------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| P0       | System/tool constraints                               | Ràng buộc hệ thống và công cụ; không được override                            |
| P1       | Lệnh trực tiếp hiện tại của người dùng                | Áp dụng cho phiên hiện tại, nhưng không được vi phạm P0 hoặc các rule an toàn |
| P2       | Root `AGENTS.md`                                      | Luật nền toàn repo                                                            |
| P3       | Governance rules trong `agent_hub/governance/`        | Cơ chế quản trị luật, registry, conflict, operating contract                  |
| P4       | Experiment-level rules trong `agent_hub/experiments/` | Rule riêng cho từng experiment                                                |
| P5       | Domain knowledge, memo, report, protocol trong `doc/` | Cơ sở khoa học, trạng thái nghiên cứu, tri thức domain                        |
| P6       | Task-specific prompt                                  | Prompt cụ thể của tác vụ hiện tại                                             |
| P7       | Model default behavior                                | Chỉ dùng khi không có rule cụ thể                                             |

Nếu agent không chắc priority nào áp dụng, agent phải hỏi người dùng.

---

## 4. Nguyên tắc bất biến

Các nguyên tắc sau không được bỏ qua:

1. Không được vi phạm ràng buộc hệ thống hoặc công cụ.
2. Không được tự ý sửa file nếu người dùng chưa cho phép rõ.
3. Không được refactor project nếu chưa được yêu cầu rõ.
4. Không được bịa công thức, tham số, đơn vị, nguồn hoặc citation.
5. Không được thay đổi công thức, giả định, pipeline hoặc thiết kế thí nghiệm nếu chưa có xác nhận.
6. Không được biến đề xuất thành quyết định.
7. Không được biến kết quả exploratory thành kết luận khoa học.
8. Không được chuyển sang vấn đề mới khi vấn đề hiện tại chưa được xử lý, quyết định hoặc tạm gác.
9. Không được tự tạo experiment mới nếu experiment chưa được đăng ký hoặc người dùng chưa cho phép.
10. Không được âm thầm chọn rule thuận tiện hơn khi có xung đột.

---

## 5. Operating Contract

Trước mọi tác vụ không đơn giản, agent phải tạo `Operating Contract`.

Một tác vụ được xem là không đơn giản nếu liên quan đến:

* code;
* notebook;
* dữ liệu;
* output;
* công thức;
* mô hình;
* pipeline;
* validation;
* citation;
* tài liệu khoa học;
* rule/protocol;
* experiment;
* sửa file;
* tạo file;
* di chuyển file;
* thay đổi cấu trúc project.

### Mẫu Operating Contract

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

### Nguyên tắc

* Nếu task có nhiều cách hiểu, agent phải nêu rõ các cách hiểu trước khi chọn hướng xử lý.
* Nếu phải chọn một cách hiểu tạm thời, agent phải ghi rõ đó là giả định.
* Nếu chưa có đủ thông tin để tạo Operating Contract, agent phải hỏi người dùng hoặc đề xuất bước kiểm tra.
* Nếu task đơn giản, ví dụ chỉ hỏi nghĩa một thuật ngữ, có thể không cần Operating Contract.

---

## 6. Required Gates

Tùy loại task, agent phải đi qua các gate tương ứng.

### GATE-READ

Áp dụng cho mọi task không đơn giản.

Agent phải đọc đúng rule và tài liệu liên quan trước khi phân tích hoặc đề xuất.

### GATE-SCOPE

Agent phải xác định phạm vi task:

* global;
* governance;
* documentation;
* tool setup;
* experiment-specific;
* code/notebook;
* data/output;
* domain knowledge.

### GATE-EVIDENCE

Áp dụng khi task liên quan đến công thức, citation, nguồn tài liệu, cơ chế khoa học hoặc nhận định học thuật.

Agent phải xác định:

* nguồn nào hỗ trợ nhận định;
* phần nào là source-backed;
* phần nào là implementation choice;
* phần nào là inference/hypothesis;
* phần nào chưa đủ bằng chứng.

### GATE-PLAN

Áp dụng khi task có thể dẫn đến thay đổi file, code, notebook hoặc cấu trúc project.

Agent phải đề xuất plan trước khi sửa.

### GATE-USER-CONFIRMATION

Áp dụng trước mọi hành động sửa, tạo, xóa, di chuyển hoặc ghi đè file.

Nếu người dùng chưa xác nhận rõ, agent chỉ được đề xuất.

### GATE-REVIEW

Áp dụng sau khi có đề xuất thay đổi quan trọng.

Agent phải tự kiểm tra:

* có vi phạm rule không;
* có xung đột không;
* có thiếu nguồn không;
* có ảnh hưởng đến pipeline hoặc experiment không;
* có cần cập nhật registry không.

---

## 7. Conflict Detection

Agent phải kiểm tra xung đột trước khi thực hiện tác vụ.

Các loại xung đột thường gặp:

### CONFLICT-FILE-EDIT

Task yêu cầu sửa, tạo, xóa, ghi đè hoặc di chuyển file nhưng chưa có xác nhận rõ.

### CONFLICT-RULE-PRIORITY

Hai hoặc nhiều rule có yêu cầu khác nhau, nhưng priority chưa rõ hoặc chưa đủ để quyết định.

### CONFLICT-FORMULA-SOURCE

Một công thức, tham số, đơn vị, biến hoặc citation được yêu cầu sử dụng nhưng chưa có nguồn rõ.

### CONFLICT-PIPELINE-CHANGE

Task hoặc đề xuất làm thay đổi pipeline, baseline, giả định, công thức hoặc thiết kế thí nghiệm.

### CONFLICT-EXPERIMENT-SCOPE

Task liên quan một experiment nhưng experiment chưa được đăng ký, chưa có active rules hoặc chưa có context index.

### CONFLICT-DOC-LOCATION

Một file được đặt sai vùng trách nhiệm, ví dụ:

* rule nằm trong experiment folder;
* setup/tool note nằm trong `agent_hub/`;
* tài liệu nghiên cứu bị đưa vào governance file.

### CONFLICT-RESULT-INTERPRETATION

Một kết quả exploratory, sensitivity hoặc chưa validated bị yêu cầu trình bày như kết luận khoa học.

### CONFLICT-LEGACY-RULE

Một file rule cũ vẫn tồn tại và có thể mâu thuẫn với rule mới trong `agent_hub/`.

### CONFLICT-MISSING-CANONICAL-SOURCE

Agent không xác định được file nào là nguồn canonical cho task hiện tại.

---

## 8. Conflict Report

Nếu phát hiện xung đột, agent phải dừng và tạo `Conflict Report`.

### Mẫu Conflict Report

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

### Mức độ nghiêm trọng

| Severity | Ý nghĩa                                                  | Hành động                  |
| -------- | -------------------------------------------------------- | -------------------------- |
| BLOCKER  | Không được tiếp tục nếu chưa có quyết định               | Dừng và hỏi người dùng     |
| MAJOR    | Có thể phân tích tiếp nhưng không được sửa/chạy/thay đổi | Báo cáo rõ và chờ xác nhận |
| MINOR    | Có thể tiếp tục theo rule ưu tiên cao hơn                | Ghi chú trong response     |

---

## 9. Cơ chế thêm rule mới

Agent không được tự ý thêm rule mới nếu chưa được người dùng xác nhận.

Trước khi thêm rule mới, agent phải báo cáo:

1. tên rule đề xuất;
2. lý do cần thêm;
3. phạm vi áp dụng;
4. mức ưu tiên đề xuất;
5. file sẽ chứa rule;
6. rule là global hay experiment-specific;
7. rule có trùng rule cũ không;
8. rule có mâu thuẫn rule hiện hành không;
9. có cần cập nhật `RULE_REGISTRY.md` không;
10. có cần cập nhật `EXPERIMENT_REGISTRY.md` không.

Chỉ sau khi người dùng đồng ý, agent mới được thêm rule.

---

## 10. Cơ chế sửa rule cũ

Khi sửa rule cũ, agent phải báo cáo trước:

* rule nào sẽ được sửa;
* file nào sẽ được sửa;
* nội dung hiện tại;
* nội dung đề xuất;
* lý do sửa;
* ảnh hưởng đến workflow;
* ảnh hưởng đến experiment nếu có;
* có cần cập nhật registry không;
* có cần đánh dấu legacy không.

Không được âm thầm sửa rule.

---

## 11. Cơ chế loại bỏ hoặc archive rule

Khi muốn loại bỏ rule cũ, agent phải phân biệt:

```text
Remove:
Xóa khỏi hệ thống rule active.

Archive:
Giữ lại để truy vết nhưng đánh dấu không còn active.

Deprecate:
Không dùng cho task mới nhưng vẫn giữ để hiểu lịch sử.
```

Agent không được tự ý xóa rule hoặc file legacy nếu người dùng chưa xác nhận.

Nếu một rule bị thay thế bởi rule mới, agent phải ghi rõ:

* rule cũ;
* rule mới;
* lý do thay thế;
* ngày thay thế;
* tác động đến workflow.

---

## 12. Cơ chế cập nhật registry

Khi thêm, sửa, deprecate hoặc archive rule, agent phải kiểm tra có cần cập nhật:

```text
agent_hub/governance/RULE_REGISTRY.md
```

Nếu thay đổi liên quan đến experiment, agent cũng phải kiểm tra:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
```

Nếu thay đổi liên quan đến tài liệu, agent phải kiểm tra:

```text
doc/DOC_INDEX.md
```

nếu file này đã tồn tại.

---

## 13. Quan hệ với experiment-specific rules

`RULE_GOVERNANCE.md` chỉ quản lý cơ chế chung.

Rule riêng của experiment phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

File governance không được chứa chi tiết riêng của experiment.

Nếu một rule ban đầu chỉ áp dụng cho một experiment nhưng sau này cần áp dụng cho mọi experiment, agent phải đề xuất nâng cấp rule đó thành global rule và chờ người dùng xác nhận.

---

## 14. Quan hệ với tài liệu nghiên cứu

Tài liệu nghiên cứu nằm trong `doc/`.

Governance file không được sao chép dài nội dung khoa học từ `doc/`.

Nếu task cần thông tin khoa học, agent phải trỏ về tài liệu tương ứng trong `doc/` hoặc index của experiment.

Nếu tài liệu khoa học và rule workflow có vẻ mâu thuẫn, agent phải báo cáo xung đột thay vì tự diễn giải.

---

## 15. Quan hệ với setup/tool notes

Hướng dẫn setup công cụ phải đặt trong:

```text
doc/tools/
```

Ví dụ:

* NotebookLM MCP;
* Antigravity;
* Codex;
* GitHub MCP;
* môi trường Python;
* dependency setup;
* IDE setup.

`agent_hub/` chỉ chứa rule liên quan đến cách agent sử dụng công cụ, không chứa hướng dẫn setup chi tiết nếu đó là tài liệu thao tác kỹ thuật.

---

## 16. Stop Conditions

Agent phải dừng và hỏi người dùng nếu gặp một trong các điều kiện sau:

* task yêu cầu sửa file nhưng chưa có xác nhận rõ;
* task yêu cầu tạo file mới nhưng scope chưa rõ;
* task yêu cầu thay đổi pipeline, công thức hoặc giả định;
* task yêu cầu dùng công thức/tài liệu chưa có nguồn rõ;
* task yêu cầu tạo experiment mới nhưng chưa có registry entry;
* task liên quan experiment nhưng không xác định được active rules;
* task yêu cầu diễn giải kết quả chưa validated như kết luận khoa học;
* có xung đột giữa rule cũ và rule mới;
* agent không xác định được file canonical;
* agent không chắc mình được phép làm gì.

---

## 17. Trạng thái

Phiên bản: `v0.1`

Trạng thái: active governance file.

Nguyên tắc chính:

* quản lý rule ở mức generic;
* không hard-code experiment-specific logic;
* mọi tác vụ không đơn giản cần Operating Contract;
* mọi xung đột cần Conflict Report;
* mọi thay đổi rule cần cập nhật registry nếu được xác nhận;
* không sửa, tạo, xóa, di chuyển file nếu chưa có xác nhận rõ.

Cập nhật lần cuối: `2026-06-09`
