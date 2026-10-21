# EXP01_ACTIVE_RULES.md

## 1. Mục đích

`EXP01_ACTIVE_RULES.md` là bộ quy tắc active cho experiment `exp_01`.

File này quản lý các quy tắc agent khi làm việc với experiment tương ứng với thư mục project:

```text
Experiment_01/
```

Từ thời điểm thiết lập `agent_hub/`, rule của experiment không đặt trong thư mục experiment thật nữa.

Rule riêng của experiment phải được quản lý tại:

```text
agent_hub/federation_v2/experiments/exp_01/
```

Thư mục `Experiment_01/` chỉ nên chứa nội dung phục vụ thực nghiệm, ví dụ:

* notebook;
* data;
* output;
* script;
* tài liệu riêng của experiment nếu cần.

---

## 2. Phạm vi áp dụng

File này áp dụng cho mọi task liên quan đến `exp_01`, bao gồm:

* đọc hoặc kiểm tra notebook trong `Experiment_01/`;
* kiểm tra dữ liệu đầu vào/đầu ra của experiment;
* kiểm tra pipeline `EC_CYG`;
* kiểm tra công thức và giả định vật lý;
* kiểm tra collocation CYGNSS–SMAP–EC_truth;
* đề xuất sửa notebook hoặc code;
* đề xuất tạo output mới;
* viết memo/report kỹ thuật cho experiment;
* audit trạng thái hiện tại của experiment.

---

## 3. Chế độ làm việc mặc định

Agent phải mặc định làm việc theo chế độ:

```text
chỉ đọc → phân tích → đề xuất → chờ xác nhận
```

Agent được phép:

* đọc notebook;
* đọc tài liệu liên quan;
* kiểm tra cấu trúc experiment;
* phân tích logic pipeline;
* phân tích công thức;
* phân tích trạng thái dữ liệu/output;
* đề xuất hướng xử lý;
* đề xuất code hoặc cell notebook;
* đề xuất kiểm chứng;
* báo cáo rủi ro;
* báo cáo xung đột rule.

Agent không được tự ý:

* sửa notebook;
* sửa script;
* ghi đè dữ liệu;
* tạo output mới;
* chạy pipeline dài;
* refactor notebook;
* đổi tên file/thư mục;
* đổi công thức;
* đổi giả định;
* đổi baseline;
* đổi thứ tự Phase/Step;
* biến kết quả exploratory thành kết luận khoa học.

Mọi hành động sửa, tạo, xóa, di chuyển hoặc ghi đè file chỉ được thực hiện khi người dùng cho phép rõ ràng.

---

## 4. Thứ tự đọc bắt buộc

Trước khi làm task liên quan đến `exp_01`, agent phải đọc theo thứ tự:

1. `AGENTS.md`;
2. `agent_hub/MEOW_AGENT.md`;
3. `agent_hub/federation_v2/FEDERATION_MANIFEST.md`;
4. `agent_hub/federation_v2/REGISTRY.md`;
5. `agent_hub/federation_v2/experiments/EXPERIMENT_REGISTRY.md`;
6. `agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md`.

Nếu task liên quan trực tiếp đến `EC_CYG`, agent phải đọc thêm:

1. `doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md`;
2. `doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md`.

Nếu task liên quan đến trạng thái thực nghiệm đã chạy hoặc kết quả hiện tại, agent phải đọc thêm:

1. `doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md`;
2. `doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md`.

Nếu task cần đối chiếu công thức hoặc logic gốc, agent có thể dùng thêm:

* `doc/ec_cyg/knowledge/studying_CYGNSS_note_v01.docx`;
* các note/source liên quan trong `doc/ec_cyg/knowledge/`;
* NotebookLM notebook: `202605 - GNSS-Reflectometry for Salinity`.

---

## 5. Trạng thái notebook chính

Các notebook chính của experiment:

```text
01_CYGNSS_extraction.ipynb
```

Trạng thái: cơ bản hoàn thiện.

Vai trò: xử lý/trích xuất dữ liệu CYGNSS đầu vào.

```text
02_Data_Querying.ipynb
```

Trạng thái: cơ bản hoàn thiện.

Vai trò: truy vấn/collocation dữ liệu phụ trợ.

```text
03_EC_CYG.ipynb
```

Trạng thái: cần được cập nhật trong phase tiếp theo.

Vai trò: pipeline tính `EC_CYG` từ CYGNSS/SMAP và kiểm chứng với `EC_truth`.

Các notebook biến thể hoặc notebook nhánh như `SMAP L2`, `SMAP L3`, hoặc notebook xử lý SMAP phải được xem là nhánh thực nghiệm, sensitivity hoặc comparison branch nếu chưa có quyết định khác.

---

## 6. Quy tắc khoa học bắt buộc cho EC_CYG

### EXP01-EC-01: Không bịa công thức, tham số, đơn vị hoặc ý nghĩa biến

Không được bịa:

* công thức;
* tham số;
* đơn vị;
* ý nghĩa biến;
* nguồn tài liệu;
* citation;
* kết luận khoa học.

Nếu công thức hoặc tham số chưa rõ nguồn, phải ghi rõ là:

```text
chưa đủ nguồn
```

hoặc phân loại là:

```text
implementation choice
inference
hypothesis
experimental formulation
```

Không được trình bày như công thức đã có nguồn chắc chắn.

---

### EXP01-EC-02: Ưu tiên baseline STEP 0–STEP 7

Khi làm với pipeline baseline `EC_CYG`, agent phải ưu tiên thứ tự:

```text
STEP 0 — Existing CYGNSS quality filtering
STEP 1 — DDM-Q8 quality filtering
STEP 2 — Reflected power extraction
STEP 3 — Effective reflectivity Gamma_eff
STEP 4 — SMAP roughness/vegetation correction
STEP 5 — Fresnel/dielectric inversion
STEP 6 — EC_CYG estimation
STEP 7 — Validation against EC_truth
```

Không được tự ý nhảy sang mô hình mở rộng nếu baseline chưa được kiểm chứng hoặc chưa có xác nhận.

---

### EXP01-EC-03: Phân biệt STEP 0 và STEP 1

`STEP 0` là lọc kỹ thuật sơ bộ bằng quality flag/metadata có sẵn.

`STEP 1` là DDM-Q8 quality filtering, gồm DDQ core metrics và LES/TES.

Không được gộp STEP 0 và STEP 1 nếu không giải thích rõ.

---

### EXP01-EC-04: LES/TES không phải predictor độ mặn trực tiếp

LES/TES chỉ được dùng để đánh giá:

* waveform shape;
* coherence;
* DDM quality;
* uncertainty;
* điều kiện sử dụng tín hiệu cho physical inversion.

Không được dùng LES/TES như predictor độ mặn trực tiếp nếu chưa có cơ sở khoa học và quyết định rõ.

---

### EXP01-EC-05: Không thay SMAP roughness/vegetation trong baseline

Trong baseline chính, không được tự ý thay SMAP roughness/vegetation bằng:

* DeltaDTM;
* optical variables;
* NDVI/NDWI/LSWI;
* L2_SM_SP;
* biến địa hình;
* biến proxy khác.

Các biến này chỉ được xem là:

* diagnostic variable;
* uncertainty variable;
* sensitivity branch;
* comparison branch;
* support variable.

Chỉ được đưa vào baseline chính nếu người dùng xác nhận một quyết định mới.

---

### EXP01-EC-06: SMAP L2_SM_SP là nhánh thực nghiệm/sensitivity nếu chưa có quyết định mới

Các nhánh SMAP L2_SM_SP 3 km và 1 km có thể được giữ để phân tích, so sánh hoặc sensitivity.

Tuy nhiên, không được tự động gọi chúng là baseline chính nếu chưa có quyết định rõ.

Cách diễn giải an toàn:

```text
SMAP L2_SM_SP 3 km/1 km là nhánh thực nghiệm hoặc sensitivity branch.
```

Không diễn giải là:

```text
baseline chính đã thay thế SMAP 9 km
```

nếu chưa có xác nhận.

---

### EXP01-EC-07: EC_CYG là estimate/proxy cần validation

`EC_CYG` phải được xem là physical estimate hoặc proxy cần kiểm chứng với `EC_truth`.

Không được gọi `EC_CYG` là EC tuyệt đối hoặc sản phẩm độ mặn đã hiệu chuẩn nếu chưa có validation/local calibration.

---

### EXP01-EC-08: Không nới red gate Phase 8 nếu chưa có quyết định

Nếu pipeline gặp điều kiện:

```text
epsilon_real_dobson > epsilon_magnitude
```

thì không được âm thầm nới gate hoặc bỏ gate để tăng số mẫu.

Đây là vấn đề toán học vì:

```text
epsilon_imag = sqrt(epsilon_magnitude^2 - epsilon_real_dobson^2)
```

sẽ không còn thực-valued nếu đối số âm.

Mọi đề xuất xử lý Phase 8 phải được báo cáo như `RISK`, `ISSUE`, `IDEA` hoặc sensitivity plan, không được tự sửa vào baseline.

---

### EXP01-EC-09: Phase 9 hiện là exploratory nếu chưa có Phase 10 validation

Kết quả Phase 9 hiện tại có thể dùng để phân tích, xuất shapefile hoặc trực quan hóa exploratory.

Không được gọi là:

```text
validated salinity map
calibrated EC product
final EC map
```

nếu chưa có Phase 10 validation hoặc local calibration.

---

### EXP01-EC-10: Thư mục notebook/ root là legacy tham khảo
Theo DECISION-NOTEBOOK-LEGACY-01:
* Thư mục `notebook/` ở root là thư mục cũ, chỉ giữ lại để tham khảo và truy vết lịch sử.
* Pipeline active chính thức cho EC_CYG phải được chạy và quản lý trong `Experiment_01/`.
* Agent tuyệt đối không dùng hoặc chạy các file trong `notebook/` như pipeline active trừ khi được người dùng yêu cầu rõ ràng.

---

## 7. Quy tắc về SMAP L2, Class A/AB và sensitivity

### EXP01-SENS-01: Class A và Class AB có vai trò khác nhau

`Class A` nên được xem là cấu hình QC nghiêm hơn.

`Class AB` có thể tăng coverage nhưng không được tự động xem là ổn định hơn về mặt vật lý.

Nếu dùng Class AB, phải ghi rõ là nhánh mở rộng coverage hoặc sensitivity.

---

### EXP01-SENS-02: SMAP L2 3 km/1 km không giải quyết gốc Phase 8 nếu chưa có bằng chứng mới

SMAP L2 3 km và 1 km có thể tăng số điểm EC-ready.

Tuy nhiên, nếu Phase 8 vẫn bị nghẽn do mismatch giữa `epsilon_magnitude` và `epsilon_real_dobson`, không được kết luận rằng tăng độ phân giải SMAP đã giải quyết vấn đề.

---

### EXP01-SENS-03: CYGNSS L3 soil moisture chỉ dùng như diagnostic nếu chưa xử lý circularity

Nếu dùng CYGNSS L3 soil moisture, phải xem là nhánh diagnostic/sensitivity.

Không được dùng để thay baseline chính nếu chưa phân tích rủi ro circularity.

---

## 8. Quy tắc trước khi sửa file

Trước khi sửa bất kỳ file nào trong hoặc liên quan đến `exp_01`, agent phải báo cáo:

1. file nào sẽ sửa;
2. vì sao cần sửa;
3. thay đổi nằm ở Phase/Step nào nếu là notebook;
4. tác động dự kiến đến pipeline;
5. có ảnh hưởng đến baseline không;
6. rủi ro khoa học/kỹ thuật;
7. cách kiểm tra sau khi sửa;
8. có cần cập nhật registry/context index không;
9. cần người dùng xác nhận hay không.

Nếu người dùng chưa cho phép rõ, agent chỉ được đề xuất nội dung sửa.

---

## 9. Quy tắc sau khi sửa file

Sau mỗi thay đổi đã được người dùng cho phép, agent phải báo cáo:

1. file đã sửa;
2. nội dung đã sửa;
3. giả định đã dùng;
4. test/check đã thực hiện;
5. output hoặc log nếu có;
6. TODO còn lại;
7. rủi ro chưa xử lý;
8. có cần cập nhật context index, memo hoặc report không.

Nếu chưa chạy test/check, phải nói rõ:

```text
Chưa chạy kiểm tra.
```

Không được nói là đã kiểm tra nếu chưa thực hiện.

---

## 10. Cách phân loại thông tin khoa học

Khi ghi nhận hoặc sử dụng thông tin khoa học, agent phải phân loại thành:

```text
Source-backed
Implementation choice
Inference / hypothesis
Decision
Exploratory result
Validated result
```

Trong đó:

* `Source-backed`: có trong tài liệu, paper, user guide hoặc notebook knowledge;
* `Implementation choice`: lựa chọn kỹ thuật trong notebook để chạy được pipeline;
* `Inference / hypothesis`: suy luận hợp lý nhưng chưa được chứng minh trực tiếp;
* `Decision`: quyết định đã được người dùng xác nhận;
* `Exploratory result`: kết quả dùng để phân tích sơ bộ;
* `Validated result`: kết quả đã được kiểm chứng bằng validation phù hợp.

Không được trộn lẫn các loại này.

---

## 11. Định danh bắt buộc

Khi phát hiện hoặc đề xuất nội dung quan trọng, agent phải dùng định danh rõ ràng:

```text
ISSUE-...
RISK-...
IDEA-...
DECISION-...
FORMULA-...
DATA-...
TEST-...
PATCH-...
PHASE-...
STEP-...
PIPELINE-CHANGE-...
```

Không được chuyển:

```text
IDEA → DECISION
RISK → PATCH
Exploratory result → Validated result
```

nếu chưa có xác nhận hoặc kiểm chứng phù hợp.

---

## 12. Các stop conditions riêng cho exp_01

Agent phải dừng và hỏi người dùng nếu:

* task yêu cầu sửa notebook nhưng chưa có xác nhận rõ;
* task yêu cầu đổi công thức hoặc giả định;
* task yêu cầu nới Phase 8 red gate;
* task yêu cầu chuyển SMAP L2 thành baseline chính;
* task yêu cầu dùng LES/TES như predictor độ mặn trực tiếp;
* task yêu cầu gọi bản đồ EC hiện tại là validated salinity map;
* task yêu cầu chạy toàn Việt Nam khi chưa audit tối thiểu các vấn đề hiện tại;
* task yêu cầu dùng công thức chưa có nguồn rõ;
* task yêu cầu bỏ qua mismatch giữa Fresnel-inverted dielectric và Dobson real dielectric.

---

## 13. Trạng thái hiện tại

Phiên bản: `v0.1`

Trạng thái: active rule overlay cho `exp_01`.

Nguồn migrate ban đầu:

```text
Experiment_01/AGENTS.md
doc/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md
doc/EC_CYG_RESEARCH_MEMO_20260602.md
doc/EC_CYG_TECHNICAL_REPORT_20260602.md
doc/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md
```

Ghi chú:

* File này là rule overlay của experiment.
* File này không phải memo khoa học.
* File này không phải technical report.
* Chi tiết notebook, data, output, issue, decision và tài liệu liên quan nên được điều hướng trong `EXP01_CONTEXT_INDEX.md`.

