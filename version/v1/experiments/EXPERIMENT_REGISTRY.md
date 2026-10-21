# EXPERIMENT_REGISTRY.md

## 1. Mục đích

`EXPERIMENT_REGISTRY.md` là bảng đăng ký các experiment trong project.

File này giúp agent xác định:

* project hiện có những experiment nào;
* experiment ID là gì;
* thư mục thật của experiment nằm ở đâu;
* file rule active của experiment nằm ở đâu;
* file context index của experiment nằm ở đâu;
* trạng thái hiện tại của experiment;
* agent cần đọc file nào trước khi làm việc với experiment đó.

File này chỉ dùng để **điều hướng**.

Không viết rule chi tiết, công thức, phase/step, notebook status hoặc decision khoa học trực tiếp trong file này.
Các nội dung đó phải nằm trong thư mục riêng của từng experiment.

---

## 2. Nguyên tắc đăng ký experiment

Mỗi experiment nên có một ID ngắn, ổn định và dễ gọi lại.

Quy ước ID:

```text
exp_01
exp_02
exp_03
...
```

Mỗi experiment được quản lý bởi một thư mục riêng trong:

```text
agent_hub/experiments/<experiment_id>/
```

Mỗi experiment tối thiểu nên có:

```text
<EXPERIMENT_ID>_ACTIVE_RULES.md
<EXPERIMENT_ID>_CONTEXT_INDEX.md
```

Trong đó:

* `*_ACTIVE_RULES.md`: rule active riêng cho experiment;
* `*_CONTEXT_INDEX.md`: bản đồ notebook, data, output, doc, memo, report, source liên quan đến experiment.

---

## 3. Experiment registry

| Experiment ID | Project path     | Agent-hub path                  | Active rules                                         | Context index                                         | Status   | Notes                                                               |
| ------------- | ---------------- | ------------------------------- | ---------------------------------------------------- | ----------------------------------------------------- | -------- | ------------------------------------------------------------------- |
| `exp_01`      | `Experiment_01/` | `agent_hub/experiments/exp_01/` | `agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md` | `agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md` | Active   | Experiment hiện tại; rule chi tiết phải nằm trong thư mục `exp_01/` |
| `exp_02`      | Chưa xác định    | `agent_hub/experiments/exp_02/` | Chưa có                                              | Chưa có                                               | Reserved | Dự phòng cho experiment tiếp theo                                   |

---

## 4. Trạng thái experiment

| Status     | Ý nghĩa                                                  |
| ---------- | -------------------------------------------------------- |
| Active     | Đang được sử dụng hoặc phát triển                        |
| Draft      | Đang thiết lập, chưa ổn định                             |
| Reserved   | Đã giữ chỗ nhưng chưa có nội dung                        |
| Paused     | Tạm dừng                                                 |
| Completed  | Đã hoàn tất ở trạng thái hiện tại                        |
| Archived   | Đã lưu trữ, không dùng cho task mới nếu không có yêu cầu |
| Deprecated | Không nên dùng cho task mới                              |

---

## 5. Quy trình khi agent nhận task liên quan experiment

Khi task liên quan đến một experiment, agent phải làm theo thứ tự:

1. đọc `AGENTS.md`;
2. đọc `agent_hub/AGENT_HUB_MANIFEST.md`;
3. đọc `agent_hub/governance/RULE_GOVERNANCE.md`;
4. đọc `agent_hub/governance/RULE_REGISTRY.md`;
5. đọc `agent_hub/experiments/EXPERIMENT_REGISTRY.md`;
6. xác định experiment ID;
7. đọc active rules của experiment;
8. đọc context index của experiment nếu có;
9. tạo `Operating Contract`;
10. chỉ tiếp tục trong phạm vi được phép.

Agent không được tự đoán rule riêng của experiment nếu registry chưa chỉ rõ.

---

## 6. Nếu experiment chưa được đăng ký

Nếu task liên quan đến một experiment chưa có trong registry, agent phải dừng và báo:

```text
Experiment chưa được đăng ký trong EXPERIMENT_REGISTRY.md.
```

Sau đó agent chỉ được đề xuất cách đăng ký, bao gồm:

1. experiment ID đề xuất;
2. thư mục project tương ứng;
3. thư mục agent-hub tương ứng;
4. file active rules cần tạo;
5. file context index cần tạo;
6. rủi ro nếu đăng ký sai;
7. cần người dùng xác nhận trước khi tạo.

Agent không được tự tạo experiment mới nếu chưa có xác nhận rõ.

---

## 7. Nếu experiment đã có thư mục nhưng thiếu rule/context

Nếu một experiment đã có trong project nhưng thiếu file rule hoặc context index trong `agent_hub/`, agent phải báo cáo:

```text
Experiment đã tồn tại nhưng thiếu governance overlay.
```

Sau đó agent phải đề xuất tạo tối thiểu:

```text
agent_hub/experiments/<experiment_id>/<EXPERIMENT_ID>_ACTIVE_RULES.md
agent_hub/experiments/<experiment_id>/<EXPERIMENT_ID>_CONTEXT_INDEX.md
```

Không được tự tạo nếu người dùng chưa cho phép rõ.

---

## 8. Quan hệ với thư mục experiment thật

Thư mục experiment thật, ví dụ:

```text
Experiment_01/
```

chỉ nên chứa nội dung phục vụ thực nghiệm:

* notebook;
* data;
* output;
* script;
* tài liệu riêng của experiment nếu cần.

Rule, governance, agent protocol và active rule overlay phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

Nếu còn rule file cũ trong thư mục experiment thật, file đó cần được xem là legacy cho đến khi nội dung quan trọng được migrate sang `agent_hub/`.

Không xóa file legacy nếu người dùng chưa xác nhận rõ.

---

## 9. Quan hệ với tài liệu trong `doc/`

Tài liệu nghiên cứu, memo, report, source/reference và setup notes không được đăng ký chi tiết trong `EXPERIMENT_REGISTRY.md`.

Các tài liệu đó nên được index trong:

```text
doc/DOC_INDEX.md
```

hoặc trong context index riêng của experiment, ví dụ:

```text
agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md
```

`EXPERIMENT_REGISTRY.md` chỉ trỏ đến context index, không liệt kê toàn bộ tài liệu.

---

## 10. Khi nào phải cập nhật file này?

Agent phải đề xuất cập nhật `EXPERIMENT_REGISTRY.md` khi:

* thêm experiment mới;
* đổi trạng thái experiment;
* đổi project path của experiment;
* đổi active rule file của experiment;
* đổi context index của experiment;
* archive/deprecate experiment;
* phát hiện experiment đã tồn tại nhưng chưa được đăng ký;
* phát hiện registry mâu thuẫn với cấu trúc project thật.

Không được tự cập nhật nếu người dùng chưa xác nhận rõ.

---

## 11. Ghi chú cho `exp_01`

`exp_01` hiện là experiment active đầu tiên của project.

Chi tiết rule, context, notebook, domain knowledge và trạng thái nghiên cứu của `exp_01` không viết trong file registry này.

Các chi tiết đó phải nằm trong:

```text
agent_hub/experiments/exp_01/EXP01_ACTIVE_RULES.md
agent_hub/experiments/exp_01/EXP01_CONTEXT_INDEX.md
```

---

## 12. Trạng thái

Phiên bản: `v0.1`

Trạng thái: experiment registry generic.

Nguyên tắc chính:

* registry chỉ điều hướng;
* không hard-code rule riêng của experiment;
* experiment-specific logic nằm trong thư mục riêng;
* nếu experiment chưa đăng ký thì phải dừng và hỏi;
* không tự tạo hoặc sửa experiment nếu chưa được phép rõ.

Cập nhật lần cuối: `2026-06-09`
