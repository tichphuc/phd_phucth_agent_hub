# STALE_SOURCE_REPORT.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive`

---

## 1. Mục đích

File này ghi những nguồn có dấu hiệu stale, weak, outdated hoặc không còn phù hợp cho Meow v2.

Kết quả audit hiện tại là conservative: chỉ gọi là stale khi có cơ sở đủ rõ.

---

## 2. Summary

Kết luận hiện tại:

```text
No confirmed stale sources
```

Không có nguồn nào trong catalog hiện tại bị xác nhận stale trong audit nội bộ này.

---

## 3. Monitor list

Các nguồn sau chưa stale, nhưng cần re-check trước pilot/activation:

| ID | Reason to monitor | Priority |
| --- | --- | --- |
| `EXT-A2A` | watchlist, chưa cần early implementation | monitor |
| `EXT-CAMEL` | role-play pattern hữu ích nhưng dễ lệch governance core | monitor |
| `EXT-AGENTGIT` | rollback/trajectory idea còn mới với local workflow | monitor |
| `EXT-CREWAI` | hữu ích như analogy, không nên đẩy thành core loop | monitor |
| `EXT-AUTOGEN` | group chat có nguy cơ debate loop và đồng thuận giả | monitor |
| `EXT-METAGPT` | SOP pattern tốt nhưng cần tránh automatic software-factory framing | monitor |

Lưu ý:

* đây là monitor list, không phải stale list;
* các nguồn này vẫn có giá trị tham khảo;
* chúng chỉ không nên được xem là nền cứng cho Phase 5.

---

## 4. Not stale, but phase-gated

Một số nguồn có giá trị rõ ràng nhưng nên đọc đúng phase:

* `EXT-AGT`
* `EXT-OPENAI-AGENTS`
* `EXT-DEEPAGENTS`
* `EXT-MCP`
* `EXT-NIST-AI-RMF`
* `EXT-OWASP-AGENTIC`

Các nguồn này không stale. Tuy nhiên, nếu đưa vào phase sai hoặc đọc ngoài ngữ cảnh, chúng có thể gây overscope hoặc runtime dependency illusion.

---

## 5. Decision

Không có source nào bị đánh dấu stale.

Không có source nào bị loại khỏi catalog.

Không có source nào cần remove ngay ở Phase 5.

---

## 6. Next check

Trước Phase 6 - Dry-run Pilots, cần:

* refresh external docs quan trọng;
* rà lại watchlist sources;
* kiểm tra xem pilot có làm thay đổi status của bất kỳ reference nào không.

