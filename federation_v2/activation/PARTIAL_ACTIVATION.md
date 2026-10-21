# PARTIAL_ACTIVATION.md

Version: `v0.1-draft`

Status: `partial-active`

Activation: `scoped-by-user`

---

## 1. Mục đích

File này định nghĩa scope kích hoạt hẹp của Meow v2 trong Phase 8.

Mục tiêu là cho phép Meow v2 vận hành các task hỏi-đáp, tra cứu và phân tích nhẹ mà không mở full governance.

---

## 2. Phạm vi được phép

Chỉ các task sau được đi theo partial activation:

```text
QUERY + LOW       -> FAST
QUERY + MEDIUM    -> GUIDED
ANALYSIS + LOW    -> FAST
ANALYSIS + MEDIUM -> GUIDED
```

Trong scope này, Meow được phép:

* đọc file canonical trong `agent_hub/federation_v2/`;
* tra registry, plan và reference track;
* trả lời hỏi-đáp, tóm tắt, giải thích ngắn;
* phân tích nhẹ theo nguồn đã có;
* báo rủi ro và điểm chưa chắc chắn;
* đề xuất next step mà không tự mutate file.

---

## 3. Ngoài phạm vi

Các task sau không thuộc partial activation:

* `MUTATION`;
* `SCIENCE`;
* `GOVERNANCE`;
* `RISK`;
* bất kỳ task nào chạm tới file write, rename, move, delete, overwrite;
* thay đổi rule, baseline, formula, pipeline;
* claim khoa học cần validation mới;
* activation rộng hơn scope ghi trong file này.

Khi task rơi vào nhóm trên, Meow phải chuyển về full gate và hỏi User nếu cần.

---

## 4. Rollback path

Rollback path của Phase 8 là:

1. dừng partial activation cho task đang xử lý;
2. quay lại read-only / propose-only mode;
3. ghi rõ case nào đã bị chặn và vì sao;
4. nếu cần, đánh dấu scope mới là ngoài phạm vi.

Rollback không cần thay đổi toàn bộ v2.

---

## 5. Reporting

Mỗi task trong partial activation phải báo:

* task class;
* scope đã dùng;
* file đã đọc;
* điểm còn thiếu chắc chắn;
* có chạm ngưỡng full gate hay không;
* có cần User confirmation cho bước tiếp theo hay không.

