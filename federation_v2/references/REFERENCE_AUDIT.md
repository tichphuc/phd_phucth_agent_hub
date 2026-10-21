# REFERENCE_AUDIT.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive`

---

## 1. Mục đích

File này ghi lại kết quả audit Reference Track của Meow v2 sau khi Phase 0-4 đã có draft.

Audit này dùng trạng thái hiện có trong repo. Nó không thay thế một freshness check web trực tiếp, nên các kết luận được ghi theo mức độ chắc chắn phù hợp:

* `confirmed`
* `likely`
* `monitor`

---

## 2. Audit scope

Audit bao phủ:

* `references/REFERENCES.md`
* `references/SOURCE_MAPPING.md`
* `references/READ_ORDER.md`
* `references/DESIGN_DECISIONS_FROM_REFERENCES.md`

Mục tiêu:

* kiểm tra reference nào còn phù hợp cho Phase 5 và Phase 6;
* kiểm tra reference nào chỉ nên giữ ở mức watchlist/defer;
* kiểm tra mapping giữa source và module/phase có còn nhất quán không;
* kiểm tra design decision nào cần giữ, trì hoãn hoặc không đổi.

---

## 3. Audit summary

Kết luận tổng quát:

* chưa có nguồn nào trong catalog hiện tại bị xác nhận stale trong audit nội bộ này;
* bộ reference hiện tại đủ để hỗ trợ Phase 5;
* các nguồn `watchlist` vẫn nên giữ ở mức theo dõi, không nâng lên làm nền thiết kế sớm;
* các source chính cho Constitution, Oversight, Coordinator, Memory, Tool Safety và Experiment Steward đang có coverage tốt.

Nguồn quan trọng cần giữ nguyên:

* `INT-MEOW-V1`
* `INT-NVT-NCKH`
* `EXT-AGT`
* `EXT-MCP`
* `EXT-OWASP-AGENTIC`
* `EXT-NIST-AI-RMF`
* `EXT-OPENAI-AGENTS`
* `EXT-DEEPAGENTS`
* `INT-MEOW-MEMO`
* `INT-CODING`
* `INT-MIMO-NOTE`
* `INT-MEMORY-PAPERS`

---

## 4. Reference health by group

### 4.1. Keep active

Những nguồn này còn phù hợp cho ngữ cảnh hiện tại:

* `INT-MEOW-V1`
* `INT-MEOW-MEMO`
* `INT-CODING`
* `INT-MIMO-NOTE`
* `INT-MEMORY-PAPERS`
* `INT-NVT-NCKH`
* `EXT-AGT`
* `EXT-MIMOCODE`
* `EXT-LANGGRAPH`
* `EXT-DEEPAGENTS`
* `EXT-OPENAI-AGENTS`
* `EXT-MCP`
* `EXT-OWASP-AGENTIC`
* `EXT-NIST-AI-RMF`

Lý do:

* chúng khớp với architecture v2 đã được ghi nhận;
* chúng hỗ trợ trực tiếp Phase 0-4;
* chưa có dấu hiệu nội bộ nào buộc phải loại bỏ.

### 4.2. Keep support / watch

Những nguồn này vẫn hữu ích nhưng không nên nâng thành nền cứng quá sớm:

* `INT-EXP01`
* `INT-RESEARCH-PROTOCOL`
* `EXT-CREWAI`
* `EXT-AUTOGEN`
* `EXT-METAGPT`
* `EXT-A2A`
* `EXT-CAMEL`
* `EXT-AGENTGIT`

Lý do:

* một số là hỗ trợ khái niệm tốt nhưng dễ kéo v2 lệch hướng nếu dùng sớm;
* một số là watchlist nên chỉ đọc sâu khi phase thật sự cần;
* một số phù hợp để pilot/compatibility hơn là governance kernel.

### 4.3. No confirmed stale sources

Trong audit nội bộ này:

* không có source nào được đánh dấu `stale` một cách xác nhận;
* không có source nào bị yêu cầu remove khỏi catalog;
* chưa có đủ căn cứ để demote bất kỳ reference active nào thành reject-for-now.

---

## 5. Coverage check

### Constitution

Coverage tốt từ:

* `INT-MEOW-V1`
* `INT-NVT-NCKH`
* `INT-RESEARCH-PROTOCOL`
* `EXT-NIST-AI-RMF`
* `EXT-OWASP-AGENTIC`

### Governance / Oversight

Coverage tốt từ:

* `EXT-AGT`
* `EXT-OPENAI-AGENTS`
* `EXT-OWASP-AGENTIC`
* `EXT-NIST-AI-RMF`
* `INT-MEOW-V1`
* `INT-NVT-NCKH` cho scientific critique

### Coordinator / routing

Coverage tốt từ:

* `EXT-OPENAI-AGENTS`
* `EXT-DEEPAGENTS`
* `EXT-CREWAI`
* `EXT-AUTOGEN`
* `INT-MEOW-V1`

### Memory / knowledge / evidence

Coverage tốt từ:

* `INT-MEOW-MEMO`
* `INT-MIMO-NOTE`
* `INT-MEMORY-PAPERS`
* `EXT-DEEPAGENTS`
* `EXT-MCP`

### Experiment / coding / safety

Coverage tốt từ:

* `INT-CODING`
* `INT-EXP01`
* `INT-RESEARCH-PROTOCOL`
* `EXT-MIMOCODE`
* `EXT-METAGPT`
* `EXT-MCP`
* `EXT-OWASP-AGENTIC`

---

## 6. Audit findings

### Finding 1: Reference coverage is sufficient for Phase 5

Phase 5 có thể bắt đầu mà không cần thêm nguồn mới ngay.

### Finding 2: Watchlist sources should stay deferred

`EXT-A2A`, `EXT-CAMEL`, `EXT-AGENTGIT` nên giữ ở watchlist/defer. Chúng hữu ích cho phase sau nhưng chưa phải nền cho Phase 5.

### Finding 3: No source removal is justified now

Không có lý do đủ mạnh để xóa reference nào khỏi catalog hiện tại.

### Finding 4: External sources should be refreshed later

Các external docs/spec/papers sẽ cần refresh lại trước pilot/activation. Audit này chưa làm freshness check web trực tiếp, nên Phase 6/7 nên có bước revalidation.

---

## 7. Recommendations

* giữ nguyên active-reference hiện tại;
* giữ watchlist/defer cho A2A, CAMEL, AgentGit;
* không promote source support thành active rule;
* trước Phase 6, chạy một vòng freshness check cho external docs quan trọng;
* nếu source mới xuất hiện trong pilot, cập nhật audit này thay vì sửa source track tùy tiện.

