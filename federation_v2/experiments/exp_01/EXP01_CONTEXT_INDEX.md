# EXP01_CONTEXT_INDEX.md

## 1. Mục đích

`EXP01_CONTEXT_INDEX.md` là bản đồ ngữ cảnh cho experiment `exp_01`.

File này dùng để giúp agent xác định:

* experiment này tương ứng với thư mục project nào;
* notebook nào đang có;
* data đầu vào nằm ở đâu;
* output/kết quả nằm ở đâu;
* script/module nào liên quan;
* tài liệu/memo/report nào cần đọc;
* file nào là active, legacy, archived hoặc cần kiểm tra thêm;
* trạng thái hiện tại của experiment là gì;
* task nên bắt đầu từ đâu.

File này **không phải rule file**.
Rule active của experiment nằm ở:

```text
agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md
```

---

## 2. Trạng thái file

Phiên bản: `v0.2`

Trạng thái: `audited — initial fill`

Ghi chú:

```text
File đã được điền dựa trên audit cấu trúc project thật ngày 2026-06-09.
Một số mục có thể cần kiểm tra sâu hơn khi đọc nội dung notebook chi tiết.
Notebook là file .ipynb nên agent chưa đọc nội dung cell, chỉ xác định vai trò qua tên file,
output data hiện có, và thông tin từ EXP01_ACTIVE_RULES.md + Experiment_01/AGENTS.md.
```

---

## 3. Experiment mapping

| Mục              | Giá trị                                               |
| ---------------- | ----------------------------------------------------- |
| Experiment ID    | `exp_01`                                              |
| Project folder   | `Experiment_01/`                                      |
| Agent-hub folder | `agent_hub/federation_v2/experiments/exp_01/`                       |
| Active rules     | `agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md`  |
| Context index    | `agent_hub/federation_v2/experiments/exp_01/EXP01_CONTEXT_INDEX.md` |
| Status           | `Active`                                              |
| Domain           | EC_CYG — GNSS-R salinity estimation via CYGNSS        |
| AOI              | Vietnam (Vinh Long bbox primary; Mekong Delta region) |

---

## 4. Audit status

| Nhóm             | Trạng thái | Ghi chú                                                          |
| ---------------- | ---------- | ---------------------------------------------------------------- |
| Notebook         | ✅ Done    | 5 notebook xác định, vai trò và status ghi ở §5                  |
| Data input       | ✅ Done    | CYGNSS raw, SMAP L2/L3, boundary, soil, truth — ghi ở §6        |
| Output           | ✅ Done    | 126+ output CSV + shp trong `data/cygnss/` — ghi ở §7           |
| Script/source    | ✅ Done    | `src/cygnss/data_process.py`, `utils/` — ghi ở §8               |
| Shared modules   | ✅ Done    | `utils/gis_tool.py`, `utils/paths.py`, `utils/raster_query.py`  |
| Documentation    | ✅ Done    | 8+ files trong `doc/` liên quan exp_01 — ghi ở §9                |
| Memo/report      | ✅ Done    | Memo, report, debug ideas, studying notes — ghi ở §9             |
| Legacy files     | ✅ Done    | `Experiment_01/AGENTS.md` = legacy rule file                     |
| Open issues      | ⚠️ Partial | Trích từ active rules; cần đọc memo để bổ sung chi tiết          |
| Active decisions | ⚠️ Partial | Trích từ active rules; cần xác nhận user                         |

---

## 5. Notebook inventory

| Notebook | Path | Role | Status | Notes |
| -------- | ---- | ---- | ------ | ----- |
| 01_CYGNSS_extraction | `Experiment_01/01_CYGNSS_extraction.ipynb` | CYGNSS netCDF extraction & point tabulation | Completed (cơ bản hoàn thiện) | Tạo raw point table từ CYGNSS L1 netCDF |
| 02_Data_Querying | `Experiment_01/02_Data_Querying.ipynb` | Collocation & ancillary data querying | Completed (cơ bản hoàn thiện) | Truy vấn/collocation SMAP, boundaries, ancillary |
| 03.0_EC_CYG_SMAPL2 | `Experiment_01/03.0_EC_CYG_SMAPL2.ipynb` | EC_CYG pipeline — SMAP L2 branch (2.3MB) | Active / Sensitivity branch | Pipeline EC_CYG dùng SMAP L2_SM_SP 3km/1km. Theo EXP01-EC-06: nhánh thực nghiệm/sensitivity |
| 03.0_EC_CYG_SMAPL3 | `Experiment_01/03.0_EC_CYG_SMAPL3.ipynb` | EC_CYG pipeline — SMAP L3 baseline (3.5MB) | Active / Needs update | Pipeline chính EC_CYG dùng SMAP L3 9km. Theo active rules: cần cập nhật trong phase tiếp theo |
| 03.1_SMAP_L3SMPE_Process | `Experiment_01/03.1_SMAP_L3SMPE_Process.ipynb` | SMAP L3 SM P Enhanced processing | Active / Support | Xử lý/subset SMAP L3 Enhanced data |

Ghi chú:

* Active rules (§5) ghi notebook chính là `03_EC_CYG.ipynb`. Thực tế thư mục có 2 biến thể: `03.0_EC_CYG_SMAPL2` và `03.0_EC_CYG_SMAPL3`. Agent phải xem `SMAPL3` là nhánh baseline gần nhất và `SMAPL2` là sensitivity branch, theo EXP01-EC-06.
* Không có file `03_EC_CYG.ipynb` đơn thuần — có thể đã được tách thành 2 biến thể trên.

---

### 5.1. Legacy notebook folder
* **Thư mục:** `notebook/` (ở cấp root project).
* **Trạng thái:** Legacy / Reference (được quy định bởi `DECISION-NOTEBOOK-LEGACY-01`).
* **Vai trò:** Giữ lại để tham khảo các code/notebook cũ được viết trước khi project phân rã theo experiment. Không dùng làm active pipeline.

---

## 6. Data inventory

### 6.1. CYGNSS raw input

| Data group | Path | Type | Role | Status | Notes |
| ---------- | ---- | ---- | ---- | ------ | ----- |
| CYGNSS raw VN | `Z:\01. save_satellite_data\cygnss\raw_vn` (external) | Raw | Input | Active | Trỏ qua `configs/data_config.yaml`; external drive |
| CYGNSS extracted VN 2020 | `data/cygnss/cyg_exr_vnbuffer10km_2020.csv` | Processed | Input (extracted) | Active | ~17.6 GB; output của notebook 01 |
| CYGNSS extracted VN 2021 | `data/cygnss/cyg_exr_vnbuffer10km_2021.csv` | Processed | Input (extracted) | Active | ~17.8 GB; output của notebook 01 |
| CYGNSS grid | `data/cygnss/cygnss_grid.csv` | Processed | Ancillary | Active | 45 MB |
| CYGNSS grid AOI | `data/cygnss/cygnss_grid_aoi.csv` | Processed | Ancillary | Active | 14.7 MB |

### 6.2. SMAP data

| Data group | Path | Type | Role | Status | Notes |
| ---------- | ---- | ---- | ---- | ------ | ----- |
| SMAP L2 SM SP | `data/SMAP_L2_SM_SP/` | Raw | Input | Active | Hàng trăm file .h5, ~4-6 MB/file; 2018-2020 |
| SMAP L3 SM P E subsetted | `data/SMAP_L3_SM_P_E_subsetted/` | Processed | Input | Active | Subsetted cho AOI |
| SMAP misc | `data/SMAP/` | Raw/Processed | Input | Needs audit | Chưa rõ nội dung |
| CYGNSS L3 Soil Moisture | `data/CYGNSS_Salinity/` | Raw | Diagnostic | Active | V3.2; chỉ dùng như diagnostic (EXP01-SENS-03) |

### 6.3. Ground truth & ancillary

| Data group | Path | Type | Role | Status | Notes |
| ---------- | ---- | ---- | ---- | ------ | ----- |
| VN Admin boundaries L0 | `data/bounds/vnm_admin_boundaries/vnm_admin0.shp` | External | Ancillary | Active | Trỏ qua data_config.yaml |
| VN Mainland | `data/bounds/vnm_admin_boundaries/vnm_adm0_mainland.shp` | External | Ancillary | Active | |
| VN Admin L1 | `data/bounds/vnm_admin_boundaries/vnm_admin1.shp` | External | Ancillary | Active | |
| Mekong stations (cuonghm) | `data/cuonghm/` | External | Validation/Truth | Active | EC ground truth; Mekong stations; salinity 2021-2022 |
| Soil sand fraction | `data/sol_sand...tif` | External | Ancillary | Active | SoilGrids 250m; 2.3 GB GeoTIFF |

### 6.4. Experiment-local data

| Data group | Path | Type | Role | Status | Notes |
| ---------- | ---- | ---- | ---- | ------ | ----- |
| Phase 9 SMAP L2 shapefiles | `Experiment_01/data/cygnss/phase9_smapl2_shp/` | Output | Exploratory | Active | Shapefile output từ SMAP L2 branch |

---

## 7. Output inventory

Output chính nằm trong `data/cygnss/`. Pipeline tạo output theo phase, class (A/AB), và variant (baseline 9km / SMAP L2 3km/1km / SoilGrids).

### 7.1. Baseline pipeline (SMAP L3 9km)

| Phase | Output pattern | Class | Role | Status |
| ----- | -------------- | ----- | ---- | ------ |
| Phase 2 | `df_cyg_vinhlong_phase2_filtered.csv` | — | Intermediate | Active |
| Phase 3 | `df_cyg_vinhlong_phase3_ddq8_pctl_land_*.csv` | A, AB, labeled | Intermediate | Active |
| Phase 4 | `df_cyg_vinhlong_phase4_gamma_class*.csv` | A, AB | Intermediate | Active |
| Phase 5 | `df_cyg_vinhlong_phase5_gamma_smap_class*.csv` + reports | A, AB | Intermediate | Active |
| Phase 6 | `df_cyg_vinhlong_phase6_rrl_class*.csv` + reports | A, AB | Intermediate | Active |
| Phase 7 | `df_cyg_vinhlong_phase7_epsilon_class*.csv` + for_dobson + reports | A, AB | Intermediate | Active |
| Phase 8 | `df_cyg_vinhlong_phase8_dobson_class*.csv` + for_ec + reports | A, AB | Intermediate | Active |
| Phase 9 | `df_cyg_vinhlong_phase9_ec_cyg_class*.csv` + for_truth | A, AB | Exploratory | Active |
| Phase 10 | `df_cyg_vinhlong_phase10_smapl3_truth_*.csv` + figures | A, AB | Exploratory | Active |

### 7.2. SMAP L2 branch

| Phase | Output pattern | Variants | Class | Status |
| ----- | -------------- | -------- | ----- | ------ |
| Phase 5 | `phase5_smapl2_*` | points/grid, 1km/3km | A, AB | Sensitivity |
| Phase 6 | `phase6_smapl2_rrl_*` | 1km/3km | A, AB | Sensitivity |
| Phase 7 | `phase7_smapl2_epsilon_*` + for_dobson | 1km/3km | A, AB | Sensitivity |
| Phase 8 | `phase8_smapl2_soilgrids_dobson_*` + for_ec | 1km/3km | A, AB | Sensitivity |
| Phase 9 | `phase9_smapl2_soilgrids_ec_cyg_*` + for_truth | 1km/3km | A, AB | Sensitivity |

### 7.3. SoilGrids variant (baseline nhưng dùng SoilGrids)

| Phase | Output pattern | Class | Status |
| ----- | -------------- | ----- | ------ |
| Phase 8 | `phase8_soilgrids_dobson_class*.csv` + for_ec + report | A, AB | Sensitivity |
| Phase 9 | `phase9s_soilgrids_ec_cyg_class*.csv` + for_truth | A, AB | Sensitivity |

### 7.4. Shapefile/figure output

| Output | Path | Status |
| ------ | ---- | ------ |
| Phase 9 9km shapefile | `data/cygnss/phase9_9km_shp/` | Exploratory |
| Phase 9 SMAP L2 shapefile | `data/cygnss/phase9_smapl2_shp/` + `Experiment_01/data/cygnss/phase9_smapl2_shp/` | Exploratory |
| Phase 10 figures | `data/cygnss/phase10_smapl3_truth_figures/` | Exploratory |

**Tổng cộng: ~126 file CSV + nhiều thư mục shp/figure.**

Không có output nào được đánh dấu `Validated`. Tất cả phase 9/10 là `Exploratory` theo EXP01-EC-09.

---

## 8. Script and module inventory

| File/module | Path | Scope | Role | Status | Notes |
| ----------- | ---- | ----- | ---- | ------ | ----- |
| data_process.py | `src/cygnss/data_process.py` | Shared (exp_01 primary) | CYGNSS netCDF extraction, time derivation, spatial clip, point tabulation | Active | 252 lines; dùng netCDF4, numpy, pandas, geopandas |
| gis_tool.py | `utils/gis_tool.py` | Shared | GIS utility | Active | 1.3 KB |
| paths.py | `utils/paths.py` | Shared | Path resolution | Active | 510 B |
| raster_query.py | `utils/raster_query.py` | Shared | Raster data query/extraction | Active | 20.8 KB |

---

## 9. Documentation and source mapping

| Document | Path | Type | Role | Status | Notes |
| -------- | ---- | ---- | ---- | ------ | ----- |
| Research Coding Agent Protocol | `doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md` | Protocol | Bắt buộc đọc trước khi làm với EC_CYG | Active | 39 KB; protocol gốc cho agent |
| EC_CYG Baseline Knowledge Skeleton | `doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md` | Knowledge | Bắt buộc đọc; baseline STEP 0–7 | Active | 13 KB |
| EC_CYG Research Memo | `doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md` | Memo | Đọc khi liên quan trạng thái thực nghiệm | Active | 17 KB |
| EC_CYG Technical Report | `doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md` | Report | Đọc khi liên quan kết quả đã chạy | Active | 15 KB |
| EC_CYG Debug Ideas | `doc/ec_cyg/memos/EC_CYG_DEBUG_IDEAS_20260531.md` | Memo | Debug/troubleshoot ideas | Active | 2.7 KB |
| Studying CYGNSS Note v01 | `doc/ec_cyg/knowledge/studying_CYGNSS_note_v01.docx` | Source | Đối chiếu công thức/logic gốc | Active | 7.6 MB (Word) |
| Studying CYGNSS Note v02 (phase7) | `doc/ec_cyg/knowledge/studying_CYGNSS_note_v02_phase7.md` | Knowledge | Phase 7 chi tiết | Active | 16 KB |
| Studying CYGNSS Note v03 (SMAP L2) | `doc/ec_cyg/knowledge/studying_CYGNSS_note_v03_SMAPL2_SM_SP.md` | Knowledge | SMAP L2 SM SP analysis | Active | 17 KB |
| Studying CYGNSS Note v04 | `doc/ec_cyg/knowledge/studying_CYGNSS_note_v04_20260602.docx` | Knowledge | Cập nhật mới nhất | Active | 18 KB (Word) |
| SMAP Enhanced L3 User Guide | `doc/sources/SMAP - Enhanced Level 3 Passive Soil Moisture.pdf` | Source | Dataset reference | Active | 1.4 MB PDF |
| FY-3E GNOS-II Format | `doc/sources/FY-3E GNOS-II GNSS-R L1 Data Format V0.9.5_20220419.pdf` | Source | Tham khảo; không dùng trực tiếp cho exp_01; dành cho EC_FY (exp_02) | Active | 658 KB PDF |
| NotebookLM MCP Setup | `doc/tools/NotebookLM_MCP_Setup_To_AskQuestion_20260529.md` | Tool note | Hướng dẫn setup | Active | 8.3 KB |

---

## 10. Active knowledge files

| Knowledge file | Path | Role | Required before task type |
| -------------- | ---- | ---- | ------------------------- |
| Baseline Knowledge Skeleton | `doc/ec_cyg/knowledge/EC_CYG_BASELINE_KNOWLEDGE_SKEL_20260528.md` | Baseline skeleton (STEP 0–7) | Mọi task EC_CYG |
| Research Coding Agent Protocol | `doc/protocols/RESEARCH_CODING_AGENT_PROTOCOL_20260529.md` | Agent protocol | Mọi task EC_CYG |
| Research Memo | `doc/ec_cyg/memos/EC_CYG_RESEARCH_MEMO_20260602.md` | Trạng thái thực nghiệm | Task liên quan kết quả/trạng thái |
| Technical Report | `doc/ec_cyg/reports/EC_CYG_TECHNICAL_REPORT_20260602.md` | Snapshot kết quả | Task liên quan kết quả đã chạy |
| EXP01 Active Rules | `agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md` | Rule overlay | Mọi task exp_01 |

---

## 11. Open issues

| Issue ID | Source file | Summary | Severity | Status | Notes |
| -------- | ----------- | ------- | -------- | ------ | ----- |
| EXP01-ISSUE-01 | EXP01_ACTIVE_RULES §EXP01-EC-08 | Phase 8 red gate: `epsilon_real_dobson > epsilon_magnitude` gây mất mẫu lớn | MAJOR | Open | Không được nới gate; cần giải pháp khác |
| EXP01-ISSUE-02 | EXP01_ACTIVE_RULES §EXP01-EC-09 | Phase 9 output là exploratory, chưa validated | MAJOR | Open | Cần Phase 10 validation |
| EXP01-ISSUE-03 | EXP01_ACTIVE_RULES §5 | Notebook `03_EC_CYG` cần update; thực tế đã tách thành SMAPL2/SMAPL3 | MINOR | Open | Cần xác nhận notebook nào là canonical |
| EXP01-ISSUE-04 | Context audit | `Experiment_01/AGENTS.md` là legacy rule file, nội dung đã migrate sang `EXP01_ACTIVE_RULES.md` | MINOR | Open | Cần đánh dấu Legacy hoặc archive |
| EXP01-ISSUE-05 | Context audit | `doc/NotebookLM_MCP_Setup...md` đã di chuyển vào `doc/tools/` | TRIVIAL | Resolved | Đã sửa khi quy hoạch doc/ (2026-06-09) |

---

## 12. Active decisions

| Decision ID | Source | Summary | Scope | Status | Notes |
| ----------- | ------ | ------- | ----- | ------ | ----- |
| EXP01-DEC-01 | EXP01_ACTIVE_RULES §EXP01-EC-02 | Baseline theo thứ tự STEP 0–7 | Baseline | Active | Đã xác nhận qua active rules |
| EXP01-DEC-02 | EXP01_ACTIVE_RULES §EXP01-EC-04 | LES/TES chỉ dùng cho DDM quality, không phải predictor | Baseline | Active | |
| EXP01-DEC-03 | EXP01_ACTIVE_RULES §EXP01-EC-05 | SMAP roughness/vegetation trong baseline không được thay | Baseline | Active | |
| EXP01-DEC-04 | EXP01_ACTIVE_RULES §EXP01-EC-06 | SMAP L2 SM SP = sensitivity branch, không phải baseline | Sensitivity | Active | |
| EXP01-DEC-05 | DECISION-NOTEBOOK-LEGACY-01 | Thư mục `notebook/` root chỉ dùng để tham khảo, active pipeline nằm ở `Experiment_01/` | Project | Active | |

---

## 13. Suggested task routing

| Task type           | Required files to read | Recommended first action | Notes |
| ------------------- | ---------------------- | ------------------------ | ----- |
| Notebook audit      | Active rules, Context index, notebook file | Đọc notebook, xác nhận output tương ứng | Chú ý: agent không thể đọc .ipynb trực tiếp |
| Formula audit       | Knowledge skeleton, studying notes v01-v04 | So sánh công thức trong notebook vs skeleton | Cần source-back tracking |
| Data QA             | Context index §6-§7 | Kiểm tra file tồn tại, size, consistency | Chú ý file rất lớn (17+ GB CSV) |
| Output review       | Context index §7, Technical report | So sánh output hiện có vs expected | Tất cả phase 9/10 = Exploratory |
| Validation          | Research memo, Technical report | Đánh giá Phase 10 output vs EC_truth | Chưa có validated result |
| Memo/report writing | Research memo, Technical report, Debug ideas | Cập nhật memo/report sau khi có kết quả mới | |
| Code proposal       | Active rules, Knowledge skeleton, `src/cygnss/data_process.py` | Đề xuất plan trước khi sửa | GATE-PLAN + GATE-USER-CONFIRMATION |

---

## 14. Audit procedure for filling this file

Khi được yêu cầu cập nhật `EXP01_CONTEXT_INDEX.md`, agent phải thực hiện theo trình tự:

1. đọc root `AGENTS.md`;
2. đọc `agent_hub/MEOW_AGENT.md`;
3. đọc `agent_hub/federation_v2/FEDERATION_MANIFEST.md`;
4. đọc `agent_hub/federation_v2/REGISTRY.md`;
5. đọc `agent_hub/federation_v2/experiments/EXPERIMENT_REGISTRY.md`;
6. đọc `agent_hub/federation_v2/experiments/exp_01/EXP01_ACTIVE_RULES.md`;
7. duyệt cấu trúc thư mục `Experiment_01/`;
8. duyệt các file liên quan trong `doc/`;
9. đề xuất bản điền context index;
10. chờ người dùng xác nhận trước khi ghi file.

Không được tự ý di chuyển, đổi tên, xóa hoặc sửa file trong quá trình audit.

---

## 15. Stop conditions

Agent phải dừng và hỏi người dùng nếu:

* không xác định được file nào là canonical;
* có nhiều notebook cùng vai trò nhưng chưa rõ notebook chính;
* output có vẻ quan trọng nhưng nguồn tạo output chưa rõ;
* tài liệu có vẻ mâu thuẫn nhau;
* rule cũ trong experiment folder mâu thuẫn với rule mới trong `agent_hub`;
* task yêu cầu điền thông tin nhưng chưa audit project thật;
* task yêu cầu xóa/di chuyển file trong quá trình context audit.

---

## 16. Change log

| Date       | Change                          | Author/Agent     | Notes                                |
| ---------- | ------------------------------- | ---------------- | ------------------------------------ |
| 2026-06-09 | Created template only           | User + assistant | Chưa audit project thật              |
| 2026-06-09 | Initial audit fill (v0.2)       | Meow             | Quét Experiment_01/, data/, src/, doc/; điền §3–§13 |

