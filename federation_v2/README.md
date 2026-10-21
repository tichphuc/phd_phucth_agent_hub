# Meow v2 - Agent Federation

Version: `v0.1-draft`

Status: `active`

Activation: `scoped-by-user`

Language policy: nội dung chung viết bằng tiếng Việt; thuật ngữ English được giữ khi cần chính xác.

---

## 1. Meow v2 là gì?

Meow v2 là một thiết kế **Agent Federation** độc lập cho workflow nghiên cứu khoa học.

Meow v2 được xây trong folder:

```text
agent_hub/federation_v2/
```

Mục tiêu của v2 là tách Meow thành một hệ gồm:

* `Meow Central Coordinator` - điều phối chung;
* `Constitution` - hiến pháp và nguyên tắc bất biến;
* `Governance Core` - cơ chế quản trị luật, conflict và decision records;
* `Oversight Layer` - kiểm tra vận hành và phản biện khoa học;
* `Functional Agencies` - các agency chuyên môn như research, coding, memo, knowledge, librarian, experiment, data/output, tool safety.

Meow v2 là hệ **self-contained**: khi foundation hoàn thiện, một agent phải có thể đọc các file canonical trong folder này để hiểu cách vận hành v2 mà không cần phụ thuộc Meow v1.

Nếu muốn dùng ngay theo kiểu người dùng cuối hoặc người mới vào hệ, đọc thêm:

```text
USAGE_GUIDE.md
```

---

## 2. Trạng thái hiện tại

Hiện tại Meow v2 ở trạng thái:

```text
active
scoped-by-user
```

Điều này có nghĩa:

* v2 là default entry của Meow; v1 đã được archive trong `agent_hub/version/v1/`;
* v2 là default entry và foundation kernel đã active trong scope do User duyệt;
* v2 chưa tự động áp dụng cho code, notebook, data, experiment hoặc pipeline;
* v2 là foundation kernel active trong folder riêng, còn các phase sau vẫn được xây dần theo trạng thái riêng.

Không file nào trong folder này tự cấp quyền sửa, tạo, xóa, di chuyển, rename hoặc ghi đè file khác.

---

## 3. Quan hệ với Meow v1

Meow v1 là nguồn tham khảo thiết kế và di sản workflow hiện có.

Meow v2 không phụ thuộc Meow v1 để vận hành.

Nguyên tắc:

* không sửa Meow v1 trong quá trình xây v2 nếu User chưa yêu cầu rõ;
* không update registry v1 nếu User chưa yêu cầu rõ;
* không dùng v1 như dependency bắt buộc của v2;
* có thể học ý tưởng từ v1, nhưng nội dung vận hành của v2 phải nằm trong folder v2.

---

## 4. File canonical Phase 0

Foundation kernel của Phase 0 gồm:

```text
README.md
FEDERATION_MANIFEST.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
VERSIONING_POLICY.md
REGISTRY.md
```

Thứ tự đọc khuyến nghị:

```text
1. README.md
2. VERSIONING_POLICY.md
3. CONSTITUTION.md
4. AUTHORITY_MODEL.md
5. OPERATING_PROTOCOL.md
6. FEDERATION_MANIFEST.md
7. REGISTRY.md
```

---

## 5. Nguyên tắc nền

Meow v2 phải ưu tiên:

* tính đúng đắn khoa học;
* minh bạch;
* truy vết;
* khả năng kiểm chứng;
* phân quyền rõ;
* không tự ý mutate file;
* không biến proposal thành decision;
* không biến exploratory result thành validated result.

---

## 6. Khi nào được mở rộng?

Mọi mở rộng Meow v2 phải đi theo phase và có User confirmation.

Trước khi tạo thêm module, agency, schema hoặc reference file, Meow phải trình bày:

* phase-specific Operating Contract;
* file sẽ tạo hoặc sửa;
* nội dung dự kiến;
* risk và impact;
* gate cần qua;
* yêu cầu xác nhận của User.

---

## 7. Trạng thái Phase 0

Phase 0 tạo foundation kernel độc lập.

Phase 0 không tạo:

* agency module chi tiết;
* schema layer;
* pilot report;
* compatibility/migration file;
* runtime framework;
* YAML/JSON policy.

Reference Track R0 đã được tạo như support layer cho quá trình build v2, nhưng không phải active governance.

Các phần còn lại thuộc phase sau.

---

Ngoai foundation kernel, v2 con co `memo/` support layer de giu project state, session state va routing quick layer. Lop nay chi phuc vu dinh tuyen/nhu nho trang thai, khong thay the canonical files.

## 8. Phase 8 partial activation

Phase 8 cho phép xác nhận hẹp theo `activation/PARTIAL_ACTIVATION.md`.

Scope hiện tại:

* `QUERY + LOW` -> `FAST`;
* `QUERY + MEDIUM` -> `GUIDED`;
* `ANALYSIS + LOW` -> `FAST`;
* `ANALYSIS + MEDIUM` -> `GUIDED`.

Ngoài scope trên, Meow v2 vẫn chạy full gate.

Runtime layer `runtime/` đã được khởi tạo cho Phase 8 như một enforcement layer tối thiểu. Hiện tại nó đã compile và smoke-test được, bao gồm phân tầng `intent` và `topic` riêng nhau. Runtime chưa thế chân active governance toàn phân và chưa gắn executor thật.




## 9. Default entry update

After explicit User confirmation, `Meow` now starts from the v2 federation entry point.

Legacy v1 material is preserved in:

```text
agent_hub/version/v1/
```

v2 remains internally phased, but it is now the default runtime route for `Meow`.
