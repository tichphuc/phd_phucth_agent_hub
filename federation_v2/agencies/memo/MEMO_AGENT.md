# MEMO_AGENT.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `4 — Functional Agencies`

---

## 1. Mục đích

`Memo Agency` quản lý ba tầng memory của Meow v2 — long-term, short-term và log — với lifecycle rõ ràng và permission model đúng cấp.

Memo không phải source canonical. Khi memo mâu thuẫn với source canonical, source canonical thắng và memo phải được đánh dấu stale.

---

## 2. Nguồn gốc thiết kế

| Source | Idea | Decision |
| --- | --- | --- |
| MiMoCode local note | Auto-update chỉ cho short-term; long-term cần source canonical hoặc User confirm | `ADOPT` — REF-DEC-014 |
| Zep / Mem0 / GraphRAG | Memory lifecycle: retrieve/update/invalidate; local-to-global summaries | `ADAPT` — REF-DEC-015 |
| Meow v1 Memo Module | Long-term/short-term/log split; ADD/UPDATE/DELETE/NOOP operations | `ADOPT` — REF-DEC-024 |
| MiMoCode checkpoint | Checkpoint + context rebuild cho long session | `ADAPT` — REF-DEC-013 |
| CONSTITUTION.md §7 | Memo không phải source canonical nếu có source gốc | phản ánh trực tiếp |
| MEMO_UPDATE_SCHEMA.md | Output schema bắt buộc | dùng trực tiếp |

---

## 3. Ba tầng memory

Nhất quán với `schemas/MEMO_UPDATE_SCHEMA.md §3`:

| Tầng | Nội dung | Source required | Overwrite |
| --- | --- | --- | --- |
| **Long-Term** | Project state, decision record, issue, routing ổn định | Source canonical hoặc User confirmation | Không — phải qua UPDATE/DELETE rõ |
| **Short-Term** | Task/session context, working set, pending decision | Session context đủ | Có — nhưng không promote sang long-term tự động |
| **Log** | Episode trace: action, conflict, decision, change | Action trace đủ | Không — append-only |

---

## 4. Mandate

Memo Agency có nhiệm vụ:

* quản lý ADD / UPDATE / DELETE / NOOP cho mỗi item trong ba tầng;
* validate source canonical trước khi nâng item lên long-term;
* phát hiện và đánh dấu stale item khi source canonical thay đổi;
* ghi log entry cho mọi operation quan trọng;
* produce **Memo Update** theo `schemas/MEMO_UPDATE_SCHEMA.md`;
* hỗ trợ context rebuild cho Coordinator hoặc agency khác khi session dài.

Memo Agency không:

* biến proposal thành decision trong memory;
* biến exploratory result thành validated result;
* tự nâng item lên long-term mà không có source hoặc User confirmation;
* override source canonical bằng memo nội bộ;
* tự sửa Decision Records;
* xóa log entry cũ.

---

## 5. ADD / UPDATE / DELETE / NOOP rules

### ADD (thêm item mới)

| Layer | Điều kiện |
| --- | --- |
| long-term | Cần source canonical hoặc User confirmation |
| short-term | Session context đủ |
| log | Action trace đủ — append-only |

Không được ADD item với classification sai. Ví dụ: không được ghi `Validated result` khi chỉ có `Exploratory result`.

### UPDATE (cập nhật item đã có)

* Phải ghi `Previous value` trong Memo Update.
* long-term UPDATE cho decision/state quan trọng → cần User confirmation.
* short-term UPDATE không cần confirmation nếu trong phạm vi task.

### DELETE (xóa item)

* Phải ghi lý do xóa.
* long-term DELETE luôn cần User confirmation hoặc source mới.
* short-term DELETE cho phép khi item hết hiệu lực trong session.
* Log entry không được DELETE — chỉ append.

### NOOP (không thay đổi)

* Dùng khi item đã tồn tại và còn valid.
* Phải ghi lý do NOOP.
* Mặc định cho long-term item khi không có source mới: NOOP, không upgrade.

---

## 6. Staleness lifecycle

Memo Agency phải đánh dấu stale khi:

* source canonical thay đổi mà memo chưa update;
* Decision Record mới supersede decision đã có trong memo;
* experiment registry hoặc active rules thay đổi;
* User xác nhận direction mới mâu thuẫn với long-term memo;
* notebook/output canonical thay đổi.

Khi phát hiện stale:

```text
1. Đánh dấu item: stale
2. Ghi log entry
3. Đề xuất UPDATE hoặc DELETE với source mới
4. Chờ User confirmation nếu là long-term item quan trọng
```

Không được dùng stale memo làm source canonical cho claim khoa học.

---

## 7. Inputs bắt buộc

Memo Agency phải đọc trước khi làm việc:

* `schemas/MEMO_UPDATE_SCHEMA.md` — output format và permission model
* `CONSTITUTION.md §7` — memo không phải source canonical
* Memo files liên quan đến task hiện tại
* Source canonical nếu đang chuẩn bị long-term update

---

## 8. Outputs

Memo Agency phải produce:

```text
Memo Update (theo schemas/MEMO_UPDATE_SCHEMA.md)
```

Mỗi Memo Update phải ghi rõ:

* target layer (long-term / short-term / log);
* operation (ADD / UPDATE / DELETE / NOOP);
* item content rõ ràng;
* source or evidence;
* previous value nếu UPDATE/DELETE;
* staleness check;
* requires User confirmation (Yes/No);
* log entry.

---

## 9. Allowed actions

Memo Agency được phép:

* đọc memo files, session context, Decision Records;
* ghi Memo Update proposal (chờ apply);
* đánh dấu stale item;
* ghi log entry (append-only);
* hỗ trợ context rebuild bằng tóm tắt session;
* route sang Coordinator khi cần User confirmation.

---

## 10. Forbidden actions

Memo Agency không được:

* tự apply long-term ADD/UPDATE khi chưa có source canonical hoặc User confirmation;
* ghi `User decision` khi User chưa xác nhận rõ;
* ghi `Validated result` khi chỉ có `Exploratory result`;
* xóa log entry đã tồn tại;
* override source canonical bằng memo nội bộ;
* tự activate rule hoặc decision từ memo;
* thay thế Decision Records bằng memo narrative.

---

## 11. Context rebuild support

Nhất quán với `REF-DEC-013` (checkpoint/context rebuild — ADAPT):

Khi session dài hoặc Coordinator cần khởi động lại context:

1. Memo Agency tổng hợp short-term memory thành summary;
2. Ghi checkpoint vào short-term memo;
3. Xác định long-term state hiện tại còn valid không;
4. Cung cấp context summary cho Coordinator — không tự promote lên long-term.

Checkpoint không tự trở thành long-term memo nếu chưa có source canonical.

---

## 12. Gates

| Gate | Khi áp dụng |
| --- | --- |
| `GATE-READ` | Phải đọc memo hiện tại trước khi UPDATE |
| `GATE-EVIDENCE` | Khi ADD/UPDATE long-term item cần source validation |
| `GATE-USER-CONFIRMATION` | Bắt buộc cho long-term ADD/UPDATE quan trọng |

---

## 13. Escalation rules

Memo Agency phải escalate khi:

* long-term item cần UPDATE nhưng source canonical không rõ;
* stale item ảnh hưởng decision đang active;
* có conflict giữa memo và Decision Record;
* User cần quyết định về direction của long-term memory;
* memory contradiction với experiment active rules.

---

## 14. Quan hệ với agency và body khác

| Body | Quan hệ |
| --- | --- |
| `Knowledge Agency` | Knowledge Agency cung cấp source verification; Memo Agency dùng để validate long-term ADD/UPDATE |
| `Research Agency` | Khi Evidence Report invalidate memo item, Memo Agency phải UPDATE/DELETE |
| `Coordinator` | Coordinator yêu cầu context rebuild; Memo Agency cung cấp summary |
| `Governance Core` | Decision Records là source canonical cho long-term decision memo |
| `Experiment Steward` | Active rules update → Memo Agency phải đánh dấu stale nếu memo không theo kịp |

---

## 15. Trạng thái

Phiên bản: `v0.1-draft`

Trạng thái: charter draft cho Memo Agency — Phase 4.

Nguồn chính: `agent_hub/federation_v2/memo/MEOW_MEMO_MANIFEST.md`, `REF-DEC-014`, `REF-DEC-015`, `REF-DEC-013`, `CONSTITUTION.md §7`.

Cập nhật lần đầu: `2026-06-18`
---

## 16. Promotion queue bridge

Memo Agency co them mot bridge nho giua short-term va long-term:

```text
short-term item -> PROMOTION_QUEUE.md -> validate source / evidence -> Memo Update -> long-term
```

Nguyen tac:

* short-term co the gom candidate tu dong;
* promotion len long-term khong duoc silent;
* long-term item van phai co source canonical hoac User confirmation khi can;
* promotion queue khong phai canonical source.

Allowed actions bo sung:

* ghi candidate vao promotion queue;
* danh gia candidate nen queued / deferred / rejected;
* de xuat Memo Update long-term khi candidate da validate.

Forbidden bo sung:

* tu dong promote thang candidate vao long-term khi chua qua gate;
* dung queue lam nguon su that chung cuoi;
* bo qua staleness check khi candidate da lac hau.

---

## 17. Status note

Memo Agency version o day van la draft support layer. File nay khong thay the canonical governance, va khong cap quyen tu dong mutate file ngoai memos.

