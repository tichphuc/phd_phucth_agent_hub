# RULE_REGISTRY.md

## 1. Mục đích

`RULE_REGISTRY.md` là bảng kiểm kê các bộ luật và cơ chế quản trị đang được sử dụng trong project.

File này giúp agent biết:

* rule nào đang tồn tại;
* rule nằm ở file nào;
* rule áp dụng cho phạm vi nào;
* rule có mức ưu tiên nào;
* rule đang active, draft, proposed, legacy hay deprecated;
* rule nào cần được tra tiếp ở experiment registry;
* rule nào cần cập nhật khi có thay đổi workflow.

`RULE_REGISTRY.md` không phải nơi viết rule chi tiết.
Rule chi tiết phải nằm trong file rule tương ứng.

---

## 2. Nguyên tắc registry

Registry cấp chung chỉ ghi các rule hoặc nhóm rule có tính tổng quát.

Không ghi chi tiết riêng của một experiment cụ thể, ví dụ:

* tên pipeline cụ thể;
* tên notebook cụ thể;
* công thức cụ thể;
* phase/step cụ thể;
* issue riêng của experiment;
* quyết định khoa học riêng của experiment.

Các nội dung riêng phải nằm trong:

```text
agent_hub/experiments/<experiment_id>/
```

và được đăng ký thông qua:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
```

---

## 3. Priority scale

| Priority | Ý nghĩa                                               |
| -------- | ----------------------------------------------------- |
| P0       | Ràng buộc hệ thống/tool                               |
| P1       | Lệnh trực tiếp hiện tại của người dùng                |
| P2       | Luật nền toàn repo                                    |
| P3       | Governance/meta-rule                                  |
| P4       | Experiment-level rule                                 |
| P5       | Domain knowledge, memo, report, protocol trong `doc/` |
| P6       | Task-specific prompt                                  |
| P7       | Model default behavior                                |

---

## 4. Status scale

| Status     | Ý nghĩa                                  |
| ---------- | ---------------------------------------- |
| Active     | Đang có hiệu lực                         |
| Draft      | Đang soạn, chưa hoàn toàn ổn định        |
| Proposed   | Mới là đề xuất, chưa áp dụng             |
| Legacy     | File/rule cũ, còn giữ để truy vết        |
| Deprecated | Không dùng cho task mới, chỉ giữ lịch sử |
| Archived   | Đã đưa vào lưu trữ, không còn active     |

---

## 5. Global rule registry

| Rule ID         | Source file                                    | Scope           | Priority | Status   | Notes                                                                              |
| --------------- | ---------------------------------------------- | --------------- | -------- | -------- | ---------------------------------------------------------------------------------- |
| CORE-ROOT-01    | `AGENTS.md`                                    | Toàn repo       | P2       | Active   | Project đã có sẵn; không tự tạo project mới                                        |
| CORE-ROOT-02    | `AGENTS.md`                                    | Toàn repo       | P2       | Active   | Không refactor lớn nếu chưa được yêu cầu rõ                                        |
| CORE-ROOT-03    | `AGENTS.md`                                    | Toàn repo       | P2       | Active   | Không sửa code nếu chưa được yêu cầu rõ                                            |
| CORE-ROOT-04    | `AGENTS.md`                                    | Toàn repo       | P2       | Active   | Mặc định chỉ đọc, phân tích và đề xuất                                             |
| HUB-README-01   | `agent_hub/AGENT_README.md`                    | Agent hub       | P3       | Active   | Giới thiệu cấu trúc và vai trò của `agent_hub/`                                    |
| HUB-MANIFEST-01 | `agent_hub/AGENT_HUB_MANIFEST.md`              | Agent hub       | P3       | Active   | Điều hướng đọc rule, registry, experiment và tài liệu liên quan                    |
| HUB-RULES-01    | `agent_hub/CODING_RULES.md`                    | Coding rules    | P3       | Active   | Hướng dẫn lập trình cẩn trọng, Sprint Contract và Generator-Evaluator loop cho agent |
| HUB-MEMO-01     | `agent_hub/memo/MEOW_MEMO_MANIFEST.md`         | Agent memory    | P3       | Active   | Manifest cho Meow Memo Module; định nghĩa 3 tầng memory và lifecycle                |
| HUB-MEMO-02     | `agent_hub/memo/long_term/`                    | Agent memory    | P3       | Active   | Long-Term MEMO: project state, decision, issue và routing memory                    |
| HUB-MEMO-03     | `agent_hub/memo/short_term/`                   | Agent memory    | P3       | Active   | Short-Term MEMO: session state, task context và working set                         |
| HUB-MEMO-04     | `agent_hub/memo/log/`                          | Agent memory    | P3       | Active   | Log MEMO: append-only episode trace cho audit, decision và thay đổi                 |
| GOV-01          | `agent_hub/governance/RULE_GOVERNANCE.md`      | Governance      | P3       | Active   | Quản lý priority, Operating Contract, Conflict Report và rule lifecycle            |
| GOV-02          | `agent_hub/governance/RULE_REGISTRY.md`        | Governance      | P3       | Active   | Kiểm kê rule cấp chung                                                             |
| EXP-REG-01      | `agent_hub/experiments/EXPERIMENT_REGISTRY.md` | Experiments     | P4       | Draft    | Đăng ký các experiment và trỏ đến active rules/context index                       |
| EXP-TPL-01      | `agent_hub/experiments/EXPERIMENT_TEMPLATE.md` | Experiments     | P4       | Draft    | Template tạo rule/context cho experiment mới                                       |
| DOC-INDEX-01    | `doc/DOC_INDEX.md`                             | Documentation   | P5       | Active   | Index phân loại tài liệu nghiên cứu, source, report, memo và tool setup            |
| DOC-MEMO-REF-01 | `doc/memo/`                                    | Documentation   | P5       | Active   | Nơi lưu tài liệu tham khảo về agent memory / memo architecture                     |
| DOC-TOOLS-01    | `doc/tools/`                                   | Tool setup docs | P5       | Active   | Nơi đặt hướng dẫn setup công cụ như NotebookLM MCP, Antigravity, Codex, GitHub MCP |

---

## 6. Experiment-level rule routing

Registry cấp chung không ghi chi tiết rule của từng experiment.

Nếu task liên quan đến experiment, agent phải tra:

```text
agent_hub/experiments/EXPERIMENT_REGISTRY.md
```

để xác định:

* experiment ID;
* thư mục thật của experiment;
* active rule file;
* context index;
* trạng thái experiment;
* các tài liệu bắt buộc phải đọc.

Mẫu routing:

| Experiment ID | Registry source                                | Scope               | Status           |
| ------------- | ---------------------------------------------- | ------------------- | ---------------- |
| `exp_01`      | `agent_hub/experiments/EXPERIMENT_REGISTRY.md` | Experiment-specific | Registered       |
| `exp_02`      | `agent_hub/experiments/EXPERIMENT_REGISTRY.md` | Experiment-specific | Reserved / Draft |

Rule chi tiết của từng experiment phải nằm trong thư mục riêng:

```text
agent_hub/experiments/<experiment_id>/
```

---

## 7. Documentation routing

Nếu task liên quan đến tài liệu nghiên cứu, agent phải ưu tiên tra:

```text
doc/DOC_INDEX.md
```

nếu file này đã tồn tại.

Nếu task liên quan đến thiết kế memo module, agent-memory hoặc architecture của Meow memory, agent có thể tra thêm:

```text
doc/memo/
```

Các tài liệu trong `doc/memo/` là reference cho thiết kế memo/agent-memory, không phải research memo của EC_CYG.

Nếu `DOC_INDEX.md` chưa tồn tại, agent phải đề xuất tạo index trước khi tự suy đoán vai trò của từng file trong `doc/`.

Định hướng phân loại tài liệu:

| Nhóm tài liệu        | Vị trí đề xuất                | Ghi chú                                        |
| -------------------- | ----------------------------- | ---------------------------------------------- |
| Source/reference gốc | `doc/sources/`                | Paper, PDF, user guide, technical manual       |
| Agent-memory reference | `doc/memo/`                 | Paper/reference phục vụ thiết kế Meow Memo Module |
| Tool setup notes     | `doc/tools/`                  | NotebookLM MCP, Antigravity, Codex, GitHub MCP |
| Domain knowledge     | `doc/<domain>/knowledge/`     | Skeleton, method notes, source mapping         |
| Research memos       | `doc/<domain>/memos/`         | Issue log, decision memo, research direction   |
| Technical reports    | `doc/<domain>/reports/`       | Snapshot thực nghiệm, result summary           |
| Formula audit        | `doc/<domain>/formula_audit/` | Đối chiếu công thức, biến, đơn vị, nguồn       |
| Archive              | `doc/archive/`                | File cũ hoặc legacy                            |

---

## 8. Rule lifecycle

Mỗi rule trong project nên có một trạng thái rõ ràng.

### Proposed

Rule mới được đề xuất nhưng chưa áp dụng.

### Draft

Rule đang được soạn hoặc thử nghiệm.

### Active

Rule đang có hiệu lực.

### Legacy

Rule cũ còn giữ để truy vết hoặc migration.

### Deprecated

Rule không còn dùng cho task mới.

### Archived

Rule đã được lưu trữ, không còn là một phần của workflow active.

---

## 9. Khi nào phải cập nhật registry?

Agent phải đề xuất cập nhật `RULE_REGISTRY.md` khi:

* thêm rule global mới;
* sửa rule global hiện có;
* deprecate hoặc archive rule global;
* thêm governance mechanism mới;
* thêm protocol chung mới;
* thay đổi priority của một rule;
* phát hiện rule bị đặt sai vị trí;
* migrate rule từ vị trí cũ sang vị trí mới.

Nếu thay đổi chỉ nằm trong một experiment cụ thể, agent phải kiểm tra `EXPERIMENT_REGISTRY.md` và rule file của experiment đó trước khi sửa registry cấp chung.

---

## 10. Khi nào không cập nhật registry?

Không cần cập nhật registry cấp chung khi:

* chỉ sửa memo/report khoa học trong `doc/`;
* chỉ sửa notebook hoặc code của một experiment;
* chỉ cập nhật issue/decision riêng của experiment;
* chỉ thêm source/reference vào `doc/sources/`;
* chỉ thêm setup note vào `doc/tools/`;
* chỉ cập nhật task prompt tạm thời trong một phiên làm việc.

Tuy nhiên, nếu thay đổi đó tạo ra rule mới hoặc ảnh hưởng đến workflow chung, phải xem xét cập nhật registry.

---

## 11. Legacy và migration

Nếu phát hiện rule cũ nằm sai vị trí, agent không được tự xóa ngay.

Quy trình đúng:

1. xác định rule cũ đang nằm ở đâu;
2. xác định rule đó còn active hay chỉ là legacy;
3. đề xuất vị trí mới phù hợp;
4. migrate nội dung cần thiết nếu người dùng đồng ý;
5. cập nhật registry;
6. đánh dấu file cũ là legacy/deprecated nếu cần;
7. chỉ xóa file cũ khi người dùng cho phép rõ ràng.

---

## 12. Xung đột giữa registry và rule file

Nếu `RULE_REGISTRY.md` mâu thuẫn với file rule gốc, agent phải:

1. đọc file rule gốc;
2. báo cáo xung đột;
3. chỉ rõ registry nói gì;
4. chỉ rõ rule file nói gì;
5. đề xuất cập nhật;
6. chờ người dùng xác nhận.

Không được tự chọn registry hoặc rule file nếu xung đột ảnh hưởng đến workflow.

---

## 13. Ghi chú vận hành

* `RULE_REGISTRY.md` là bản đồ, không phải toàn bộ luật.
* Rule chi tiết phải nằm trong file rule tương ứng.
* File chung không được chứa logic riêng của một experiment.
* Rule riêng của experiment phải nằm trong `agent_hub/experiments/<experiment_id>/`.
* Tài liệu nghiên cứu phải nằm trong `doc/`.
* Hướng dẫn setup công cụ phải nằm trong `doc/tools/`.
* Khi không chắc rule nào áp dụng, agent phải hỏi người dùng.

---

## 14. Trạng thái

Phiên bản: `v0.1`

Trạng thái: registry generic cấp agent hub.

Nguyên tắc chính:

* chỉ kiểm kê rule cấp chung;
* không hard-code experiment-specific logic;
* routing experiment qua `EXPERIMENT_REGISTRY.md`;
* routing tài liệu qua `doc/DOC_INDEX.md`;
* mọi thay đổi rule quan trọng phải được kiểm soát qua governance.

Cập nhật lần cuối: `2026-06-09`
