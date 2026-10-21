# DECISION_RECORDS.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

---

## 1. Mục đích

`Decision Records` là ledger ghi nhận các quyết định quan trọng của Meow v2.

Nó ghi quyết định.
Nó không thay thế source document, report, hay canonical rule.

---

## 2. Schema record

Mỗi record nên có:

* `record_id`
* timestamp
* trigger task hoặc proposal ID
* proposer
* authority involved
* scope
* source basis
* relevant rule references
* risk level
* decision state
* user decision
* next gate
* trace tới output hoặc report
* pre-state
* post-state

---

## 3. Loại record

Decision Records phải bao phủ tối thiểu:

* rule proposal;
* conflict resolution;
* approval hoặc rejection;
* inspection outcome;
* scientific critique outcome;
* registry-impacting change;
* activation hoặc deprecation decision.

---

## 4. Vòng đời

Record states:

* `draft`
* `reviewed`
* `approved`
* `rejected`
* `archived`

Quy tắc vòng đời:

* proposal không phải decision;
* review không phải approval;
* exploratory result không phải validated result;
* khi decision thay đổi, phải tạo record mới thay vì overwrite âm thầm.

---

## 5. Rubric vận hành tối thiểu

Một record chỉ hợp lệ khi trả lời được:

1. Record này được kích hoạt bởi cái gì?
2. Ai là người chịu trách nhiệm quyết định?
3. Source hoặc report nào làm căn cứ?
4. Trước và sau quyết định thay đổi gì?
5. Có truy vết ngược lại được không, không mơ hồ?

Decision Records là ledger của closure, không phải log kể chuyện.

---

## 6. Điều cấm

Decision Records không được:

* biến thành câu chuyện mơ hồ;
* thay thế canonical source khi source tồn tại;
* che uncertainty;
* nhập nhằng proposal với decision;
* nhập nhằng exploratory với validated;
* đóng vai trò scientific truth source.

---

## 7. Closure

Decision record đóng khi rơi vào một trong các trạng thái:

* approved;
* rejected;
* archived.

Nếu quyết định sau này supersede quyết định cũ, tạo record mới và link record cũ là superseded.
