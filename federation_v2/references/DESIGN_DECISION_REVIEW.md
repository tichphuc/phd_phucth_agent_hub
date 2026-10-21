# DESIGN_DECISION_REVIEW.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive`

---

## 1. Mục đích

File này rà lại các `REF-DEC-*` hiện có sau khi Phase 0-4 đã có draft.

Mục tiêu là xác định:

* quyết định nào giữ nguyên;
* quyết định nào chỉ nên dùng đúng phase;
* quyết định nào vẫn để watch/defer;
* quyết định nào cần sửa wording sau pilot.

---

## 2. Review summary

Kết luận tổng quát:

* không cần reclassify lớn nào ở Phase 5;
* bộ decisions hiện tại đủ để support Phase 6 pilot planning;
* early-core decisions vẫn là backbone cho governance/coordinator/oversight;
* phase-specific và defer/watch decisions vẫn nên giữ nguyên, không ép sớm.

---

## 3. Keep as-is

### 3.1. EARLY-CORE

Giữ nguyên là early-core:

* `REF-DEC-003`
* `REF-DEC-005`
* `REF-DEC-008`
* `REF-DEC-010`
* `REF-DEC-012`
* `REF-DEC-014`
* `REF-DEC-019`
* `REF-DEC-024`
* `REF-DEC-025`
* `REF-DEC-026`
* `REF-DEC-028`
* `REF-DEC-029`

Lý do:

* đây là các quyết định trực tiếp sửa điểm yếu nền của v1;
* chúng phù hợp với governance kernel, oversight và research integrity;
* chưa có xung đột đủ mạnh để đổi priority.

### 3.2. PHASE-SPECIFIC

Giữ nguyên là phase-specific:

* `REF-DEC-001`
* `REF-DEC-002`
* `REF-DEC-006`
* `REF-DEC-007`
* `REF-DEC-009`
* `REF-DEC-011`
* `REF-DEC-013`
* `REF-DEC-015`
* `REF-DEC-020`
* `REF-DEC-021`
* `REF-DEC-027`
* `REF-DEC-030`

Lý do:

* các decision này hữu ích nhưng chỉ nên dùng đúng module/phase;
* nếu đẩy sớm, v2 sẽ nặng hơn cần thiết;
* chúng nên được đọc sâu đúng phase chứ không phải nâng toàn cục.

### 3.3. DEFER / WATCH

Giữ nguyên defer/watch:

* `REF-DEC-004`
* `REF-DEC-016`
* `REF-DEC-017`
* `REF-DEC-018`
* `REF-DEC-022`
* `REF-DEC-023`

Lý do:

* các ý tưởng này có giá trị tham khảo;
* chúng dễ kéo v2 sang framework/debate/rollback complexity sớm;
* nên giữ cho pilot hoặc phase tương lai.

---

## 4. What changes after Phase 5

### 4.1. Stronger boundary for Scientific Critic

`REF-DEC-026`, `REF-DEC-028`, `REF-DEC-029`, `REF-DEC-030` đã được dùng để khóa lại:

* research question as kernel;
* scientific basis;
* data integrity / plagiarism / credit integrity;
* multidimensional science evaluation.

Kết quả:

* scientific critique không còn là ý tưởng mơ hồ;
* nó đã có role boundary rõ với Research Agency và Operational Inspector.

### 4.2. Stronger boundary for Coordinator

`REF-DEC-007`, `REF-DEC-010`, `REF-DEC-011`, `REF-DEC-024` đã cung cấp khung đủ để Coordinator:

* route;
* synthesize;
* handoff;
* không ôm quyền quyết cuối.

### 4.3. Stronger boundary for Tool Safety

`REF-DEC-001`, `REF-DEC-003`, `REF-DEC-005`, `REF-DEC-009`, `REF-DEC-019`, `REF-DEC-020` đã đủ cho tool/action governance ở mức markdown/protocol.

---

## 5. No reclassification needed

Phase 5 review không tạo ra lý do đủ mạnh để:

* đổi ADOPT thành REJECT;
* đổi DEFER thành EARLY-CORE;
* đổi PHASE-SPECIFIC thành global core.

Nói ngắn:

```text
keep the current classification
```

---

## 6. Minor wording notes for future phases

Một số decision sẽ cần wording chặt hơn khi pilot:

* `REF-DEC-002` nếu sau này cần tamper-evident audit;
* `REF-DEC-007` nếu Coordinator harness bị hiểu quá framework-heavy;
* `REF-DEC-020` nếu risk lifecycle bị diễn giải quá enterprise;
* `REF-DEC-030` nếu evaluation đa chiều bị dùng như bureaucratic gate cho task thường ngày.

Đây là wording note, không phải reclassification.

---

## 7. Recommendation

Giữ nguyên decision map hiện tại.

Trước Phase 6:

* audit lại external sources một lần nữa;
* xác nhận watchlist source nào cần kéo vào pilot;
* chỉ cập nhật `REF-DEC-*` nếu pilot thật sự cho thấy cần đổi.
