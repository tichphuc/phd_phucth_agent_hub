# VERSIONING_POLICY.md

Version: `v0.1-draft`

Status: `active`

Activation: `scoped-by-user`

---

## 1. Mục đích

File này quy định cách quản lý version, trạng thái và activation của Meow v2.

Mục tiêu là tránh việc một file planning hoặc draft bị hiểu nhầm là active governance.

---

## 2. Version states

Meow v2 dùng các trạng thái sau:

| State | Ý nghĩa |
| --- | --- |
| `planned` | Đã có trong roadmap, chưa tạo file |
| `draft` | Đã tạo bản nháp, chưa ổn định |
| `planning-only` | Chỉ dùng để thiết kế, chưa vận hành task thật |
| `pilot-only` | Chỉ dùng trong dry-run/pilot, không mutate file thật |
| `advisory` | Được dùng để tham khảo trong task thật, chưa có quyền active governance |
| `partial-active` | Chỉ được dùng trong scope hẹp do User duyệt, chưa phải active governance toàn phần |
| `active` | Được User xác nhận là rule/protocol active |
| `deprecated` | Không dùng cho task mới, giữ để truy vết |
| `archived` | Lưu trữ, không còn là workflow active |

Phase 0 mặc định là:

```text
active
scoped-by-user
```

---

## 3. Activation rule

Không file nào trong Meow v2 tự động trở thành active chỉ vì file đó tồn tại.

Activation cần:

1. User decision rõ ràng;
2. scope activation rõ ràng;
3. registry update trong `REGISTRY.md`;
4. risk/conflict review;
5. rollback hoặc deactivation path nếu cần.

Không được viết:

```text
v2 is now active
```

nếu User chưa xác nhận rõ.

---

### 3.1. Partial activation

`partial-active` là trạng thái cho scope kích hoạt hợp.

Trong Phase 8, scope kích hoạt hợp phải được ghi rõ trong:

```text
activation/PARTIAL_ACTIVATION.md
```

Nguyên tắc:

* chỉ các task năm trong scope được xử lý theo partial activation;
* task ngoài scope và task có mutation/governance/science/risk phải quay về FULL gate;
* partial activation không được diễn giải thành active governance toàn phân.

## 4. Independence rule

Meow v2 phải tự vận hành trong folder riêng.

Nguyên tắc:

* v2 không phụ thuộc Meow v1 để hiểu luật nền;
* v2 có thể tham khảo v1 như historical/design reference;
* nội dung vận hành của v2 phải được ghi trong folder v2;
* nếu cần so sánh v1/v2, việc đó thuộc phase compatibility sau này.

---

## 5. No silent mutation

Mọi thay đổi file trong v2 phải có:

* mục tiêu rõ;
* file path rõ;
* lý do rõ;
* risk/impact rõ;
* User confirmation nếu tạo/sửa/xóa/di chuyển file.

Không được âm thầm:

* sửa file v2;
* sửa file v1;
* update registry;
* rename folder;
* xóa draft cũ;
* promote draft thành active.

---

## 6. Phase policy

Meow v2 được xây theo phase.

Không phase nào được tự động nhảy sang phase tiếp theo.

Workflow chuẩn:

```text
Phase proposal
-> Sprint Contract
-> User confirmation
-> implementation
-> review
-> report
-> next gate
```

Phase 0 chỉ tạo foundation kernel.

Agency, schema, reference, pilot và compatibility thuộc phase sau.

---

## 7. Registry policy

Mọi file v2 canonical phải được ghi trong:

```text
REGISTRY.md
```

Registry v2 phải ghi tối thiểu:

* file path;
* role;
* phase;
* status;
* canonical hay support;
* ghi chú activation.

Không update registry v1 nếu User chưa yêu cầu rõ.

---

## 8. Language policy

Nội dung chung của agent dùng tiếng Việt.

Thuật ngữ English được giữ nếu:

* là thuật ngữ kỹ thuật phổ biến;
* giúp tránh dịch sai;
* cần giữ tương thích với reference ngoài.

Nếu thuật ngữ English quan trọng, file nên giải thích ngắn bằng tiếng Việt.



## 9. Default entry update

The root `Meow` entry now points to `agent_hub/federation_v2/`.

This does not mean every v2 phase is fully active. It means the default start route is v2, while v1 is archived under `agent_hub/version/v1/` for legacy reference.
