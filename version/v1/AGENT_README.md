# AGENT_README.md

## 1. Mục đích của `agent_hub/`

`agent_hub/` là kho quản trị agent của project.

Thư mục này dùng để tổ chức và quản lý:

* luật vận hành agent;
* cơ chế quản trị luật;
* registry các bộ luật;
* điều hướng theo từng experiment;
* template tạo experiment mới;
* protocol làm việc chung;
* vai trò agent nếu sau này cần mở rộng.

`agent_hub/` giúp agent làm việc có kiểm soát, tránh tình trạng nhiều prompt/rule rời rạc, trùng lặp hoặc xung đột nhau.

---

## 2. `agent_hub/` không phải là gì?

`agent_hub/` không phải là nơi chứa:

* notebook thực nghiệm;
* dữ liệu đầu vào;
* dữ liệu đầu ra;
* source code chính;
* tài liệu học thuật gốc;
* paper/PDF/reference;
* hướng dẫn setup công cụ.

Các nội dung đó phải được đặt ở nơi phù hợp hơn:

| Loại nội dung                                       | Nơi đặt          |
| --------------------------------------------------- | ---------------- |
| Notebook, data, output của experiment               | `Experiment_xx/` |
| Source code/module dùng chung                       | `src/`, `utils/` |
| Tài liệu nghiên cứu, memo, report, source/reference | `doc/`           |
| Hướng dẫn setup công cụ                             | `doc/tools/`     |
| Rule, governance, agent protocol                    | `agent_hub/`     |

---

## 3. Nguyên tắc thiết kế

`agent_hub/` được thiết kế theo nguyên tắc tách tầng:

```text
Global rules
→ Governance
→ Experiment registry
→ Experiment-specific rules
→ Task-specific instructions
```

Trong đó:

* file chung chỉ chứa luật chung;
* file chung không chứa chi tiết riêng của một experiment cụ thể;
* rule riêng của experiment phải nằm trong thư mục riêng của experiment đó trong `agent_hub/experiments/`;
* tài liệu nghiên cứu và source/reference phải nằm trong `doc/`;
* setup/tool notes phải nằm trong `doc/tools/`.

---

## 4. Cấu trúc hiện tại

```text
agent_hub/
├── AGENT_README.md
├── AGENT_HUB_MANIFEST.md
│
├── governance/
│   ├── RULE_GOVERNANCE.md
│   └── RULE_REGISTRY.md
│
└── experiments/
    ├── EXPERIMENT_REGISTRY.md
    ├── EXPERIMENT_TEMPLATE.md
    │
    ├── exp_01/
    │   └── EXP01_ACTIVE_RULES.md
    │
    └── exp_02/
```

---

## 5. Vai trò các file cấp chung

### `AGENT_README.md`

File giới thiệu tổng quan về `agent_hub/`.

File này dành cho người đọc hoặc agent mới vào project để hiểu:

* `agent_hub/` là gì;
* thư mục này quản lý gì;
* nội dung nào không được đặt trong `agent_hub/`;
* cấu trúc tổng thể của kho agent.

### `AGENT_HUB_MANIFEST.md`

File điều hướng chính của `agent_hub/`.

Agent phải đọc file này để biết:

* thứ tự đọc rule;
* khi nào cần đọc governance;
* khi nào cần tra experiment registry;
* khi nào cần đọc rule riêng của experiment;
* khi nào phải tạo `Operating Contract`;
* khi nào phải tạo `Conflict Report`.

### `governance/RULE_GOVERNANCE.md`

File quy định cơ chế quản lý luật.

Nó trả lời các câu hỏi:

* rule nào ưu tiên hơn rule nào;
* nếu hai rule xung đột thì xử lý thế nào;
* khi nào agent phải dừng;
* khi nào agent phải hỏi người dùng;
* khi nào được tiếp tục;
* khi nào cần cập nhật registry.

### `governance/RULE_REGISTRY.md`

File kiểm kê các bộ luật.

Nó không phải nơi viết rule chi tiết, mà là nơi ghi:

* rule ID;
* rule nằm ở file nào;
* phạm vi áp dụng;
* mức ưu tiên;
* trạng thái;
* ghi chú migration hoặc conflict nếu có.

### `experiments/EXPERIMENT_REGISTRY.md`

File đăng ký các experiment trong project.

Nó giúp agent biết:

* project hiện có những experiment nào;
* thư mục thật của từng experiment nằm ở đâu;
* rule active của experiment nằm ở đâu;
* context index của experiment nằm ở đâu;
* experiment nào đang active, archived hoặc reserved.

### `experiments/EXPERIMENT_TEMPLATE.md`

Template để tạo rule/context cho experiment mới.

Khi có `exp_02`, `exp_03`, agent không tự nghĩ cấu trúc mới, mà phải dựa trên template này.

---

## 6. Nguyên tắc vận hành mặc định

Trừ khi người dùng yêu cầu rõ ràng, agent phải mặc định làm việc ở chế độ:

```text
chỉ đọc → phân tích → đề xuất → chờ xác nhận
```

Agent được phép:

* đọc file;
* kiểm tra cấu trúc project;
* phân tích logic;
* tra registry;
* xác định rule áp dụng;
* đề xuất hướng xử lý;
* đề xuất nội dung file;
* báo cáo rủi ro;
* báo cáo xung đột.

Agent không được tự ý:

* sửa code;
* sửa notebook;
* refactor project;
* tạo experiment mới;
* đổi pipeline;
* đổi công thức;
* đổi giả định;
* di chuyển hoặc đổi tên file;
* ghi đè dữ liệu;
* biến đề xuất thành quyết định.

---

## 7. Luồng đọc chung cho agent

Với tác vụ không đơn giản, agent nên bắt đầu theo luồng:

```text
AGENTS.md
→ agent_hub/AGENT_HUB_MANIFEST.md
→ agent_hub/governance/RULE_GOVERNANCE.md
→ agent_hub/governance/RULE_REGISTRY.md
→ agent_hub/experiments/EXPERIMENT_REGISTRY.md nếu task liên quan experiment
→ rule/context riêng của experiment nếu cần
```

File chung không được hard-code logic riêng của một experiment cụ thể.

Nếu task liên quan một experiment, agent phải tra `EXPERIMENT_REGISTRY.md` để tìm file rule/context tương ứng.

---

## 8. Quan hệ với `doc/`

`doc/` là kho tài liệu nghiên cứu và nguồn tham khảo.

`agent_hub/` có thể trỏ tới tài liệu trong `doc/`, nhưng không nên sao chép toàn bộ nội dung tài liệu nghiên cứu vào rule file.

Định hướng:

```text
doc/
├── README.md
├── DOC_INDEX.md
├── sources/
├── tools/
├── ec_cyg/
└── archive/
```

Trong đó:

* `doc/sources/`: paper, PDF, user guide, tài liệu gốc;
* `doc/tools/`: hướng dẫn setup công cụ;
* `doc/<domain>/`: memo, report, knowledge, formula audit theo từng domain;
* `doc/archive/`: tài liệu cũ hoặc legacy.

---

## 9. Nguyên tắc mở rộng

Khi thêm experiment mới, không sửa lung tung các file chung.

Quy trình đúng:

1. thêm experiment vào `experiments/EXPERIMENT_REGISTRY.md`;
2. tạo thư mục mới trong `agent_hub/experiments/`;
3. dùng `EXPERIMENT_TEMPLATE.md` để tạo rule/context riêng;
4. chỉ cập nhật file chung nếu có rule thật sự áp dụng cho mọi experiment.

Khi thêm rule mới, không tự ý thêm vào nhiều nơi.

Quy trình đúng:

1. xác định rule là global hay experiment-specific;
2. đặt rule vào đúng file;
3. cập nhật `RULE_REGISTRY.md`;
4. nếu có xung đột, tạo `Conflict Report`;
5. chờ người dùng xác nhận nếu rule ảnh hưởng đến workflow hiện tại.

---

## 10. Trạng thái

Phiên bản: `v0.1`

Trạng thái: thiết lập khung quản trị agent tối thiểu.

Mục tiêu hiện tại:

* gom rule và governance vào `agent_hub/`;
* tách rule khỏi thư mục experiment;
* tách setup/tool notes sang `doc/tools/`;
* tạo cơ chế điều hướng cho nhiều experiment;
* tránh file chung bị nhiễm nội dung riêng của một experiment.

Cập nhật lần cuối: `2026-06-09`
