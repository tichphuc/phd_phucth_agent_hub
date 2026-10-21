# FEDERATION_MANIFEST.md

Version: `v0.1-draft`

Status: `active`

Activation: `scoped-by-user`

---

## 1. Mục đích

`FEDERATION_MANIFEST.md` là file điều hướng chính của Meow v2 Agent Federation.

File này cho biết:

* cần đọc file nào;
* thứ tự đọc;
* file nào là canonical;
* task type nào route đến đâu;
* khi nào cần Operating Contract;
* khi nào cần Operational Inspector;
* khi nào cần Scientific Critic;
* khi nào phải hỏi User.

---

## 2. Canonical Phase 0 files

Foundation kernel gồm:

```text
README.md
VERSIONING_POLICY.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
FEDERATION_MANIFEST.md
REGISTRY.md
```

---

## 3. Startup read order

Khi khởi động Meow v2, đọc theo thứ tự:

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

## 4. Task routing

| Task type | Required file(s) | Notes |
| --- | --- | --- |
| hoi truy xuat tai lieu / tim source | `agencies/librarian/LIBRARIAN_AGENT.md`, `doc/DOC_INDEX.md` | source access, catalog, path resolution, adapters |
| hỏi Meow v2 là gì | `README.md`, `FEDERATION_MANIFEST.md` | xác định status và scope |
| hỏi quyền hạn | `AUTHORITY_MODEL.md`, `CONSTITUTION.md` | phân biệt decision/execution authority |
| hỏi luật nền | `CONSTITUTION.md` | source of principles |
| hỏi workflow | `OPERATING_PROTOCOL.md` | task intake, gates, conflict |
| hỏi version/activation | `VERSIONING_POLICY.md` | inactive/default, phase states |
| hỏi file nào canonical | `REGISTRY.md`, `FEDERATION_MANIFEST.md` | inventory nội bộ |
| hỏi nguồn tham khảo | `references/REFERENCES.md`, `references/SOURCE_MAPPING.md` | reference-only, không phải active rule |
| hỏi design decision từ reference | `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | adopt/adapt/reject/defer |
| hỏi chuẩn nghiên cứu khoa học | `CONSTITUTION.md`, `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | dùng chuẩn cốt lõi, không biến sách thành luật chi tiết |
| phản biện claim/kết luận khoa học | `CONSTITUTION.md`, `OPERATING_PROTOCOL.md` | cần `GATE-SCIENTIFIC-CRITIQUE` |
| hỏi lawmaking | `governance/LAWMAKER_AGENT.md`, `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | proposal only, no activation |
| hỏi conflict resolution | `governance/CONFLICT_COURT.md`, `governance/DECISION_RECORDS.md` | conflict triage, escalation, resolution trace |
| hỏi operational inspection | `oversight/OPERATIONAL_INSPECTOR.md`, `OPERATING_PROTOCOL.md` | operational safety, fail-closed, inspection report |
| hỏi scientific critique | `oversight/SCIENTIFIC_CRITIC.md`, `CONSTITUTION.md` | question quality, evidence, method, overclaim control |
| hỏi experiment routing | `experiments/EXPERIMENT_REGISTRY.md` | `experiments/<experiment_id>/` |
| hỏi coordinator / routing / gate protocol | `core/MEOW_COORDINATOR.md`, `core/TASK_ROUTING.md`, `core/GATE_PROTOCOL.md` | route, synthesize, stop, escalate |
| phase implementation | `OPERATING_PROTOCOL.md`, `REGISTRY.md`, build plan | cần Sprint Contract |
| thêm module mới | `VERSIONING_POLICY.md`, `REGISTRY.md`, `OPERATING_PROTOCOL.md` | cần User confirmation |

---

## 5. Non-simple task rule

Task không đơn giản nếu liên quan đến:

* governance;
* authority;
* file mutation;
* rule/protocol;
* agency/module architecture;
* experiment;
* scientific claim;
* scientific critique;
* code/notebook/data/output;
* activation/deprecation;
* tool execution;
* reference-backed design decision.

Task không đơn giản phải có Operating Contract.

Nếu task tạo governance/agency/schema/protocol mới, phải qua `GATE-REFERENCE`.

Nếu task đưa ra hoặc nâng cấp claim khoa học quan trọng, phải qua `GATE-SCIENTIFIC-CRITIQUE`.

---

## 6. Oversight triggers

Meow v2 có hai chức năng oversight ngang hàng:

```text
Operational Inspector
Scientific Critic
```

`Operational Inspector` phải được gọi hoặc mô phỏng khi task:

* có conflict;
* có mutation;
* có activation;
* có deprecation/archive;
* có missing source;
* có authority ambiguity;
* chuẩn bị chuyển sang phase implementation quan trọng.

`Scientific Critic` phải được gọi hoặc mô phỏng khi task:

* có scientific claim rủi ro;
* có validation claim;
* có kết luận từ dữ liệu/output;
* có thay đổi giả thuyết, phương pháp, baseline hoặc scientific framing;
* có khả năng overclaim, thiếu evidence, thiếu credit, plagiarism hoặc bỏ qua uncertainty.

Trong Phase 0, hai oversight function chưa có file riêng. Từ Phase 1 trở đi, Coordinator ưu tiên route sang `oversight/OPERATIONAL_INSPECTOR.md` và `oversight/SCIENTIFIC_CRITIC.md`.

---

## 7. Required User confirmation

User confirmation bắt buộc trước:

* tạo file;
* sửa file;
* xóa file;
* di chuyển file;
* rename file/folder;
* update registry;
* activate v2;
* tạo agency module mới;
* tạo schema/reference/pilot/compatibility folder;
* thay đổi Constitution hoặc Authority Model.

### 7.1. Memo support layer

Memo support layer đã được bootstrap trong `memo/` để giữ project state, routing quick layer, và session context cho federation v2.

Memo support layer chỉ là operational memory, không thay thế canonical files, governance, hoặc reference track.

---

## 8. Current phase boundary

Phase hiện tại:

```text
Phase 0 - Independent Foundation Kernel
```

Phase 0 chỉ gồm foundation kernel.

Reference Track R0 đã được tạo như support track cho toàn bộ quá trình build v2.

Sprint C0 đã bổ sung scientific constitution và oversight concept vào foundation kernel. C0 chưa tạo agency file mới.

Không thuộc Phase 0:

* governance agency files;
* oversight agency files;
* functional agency files;
* schema files;
* pilot reports;
* compatibility/migration files.

---

## 9. Registry relation

`REGISTRY.md` là inventory nội bộ của v2.

Khi tạo file mới trong v2 ở phase sau, phải cập nhật `REGISTRY.md` nếu file đó là canonical hoặc support artifact có vai trò trong workflow.

Không update registry v1 nếu User chưa yêu cầu rõ.

Reference files trong `references/` là support artifacts. Chúng định hướng thiết kế nhưng không tự kích hoạt rule.


## 10. Usage guide routing

Nếu task là hỏi cách dùng Meow v2, prompt pattern, hoặc quy trình thao tác cơ bản, đọc:

```text
USAGE_GUIDE.md
```

Nếu task là hỏi luật nền hoặc quyền hạn, vẫn ưu tiên:

```text
README.md
VERSIONING_POLICY.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
```

