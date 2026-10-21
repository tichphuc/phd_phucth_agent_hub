# REGISTRY.md

Version: `v0.1-draft`

Status: `active`

Activation: `scoped-by-user`

---

## 1. Mục đích

`REGISTRY.md` là registry nội bộ của Meow v2 Agent Federation.

File này ghi:

* file nào đang tồn tại trong v2;
* vai trò của từng file;
* file thuộc phase nào;
* trạng thái của file;
* file có phải canonical hay support artifact;
* file có active hay chưa.

Registry này chỉ quản lý nội bộ v2.

Registry này không thay thế registry của Meow v1.

---

## 2. Status scale

| Status | Ý nghĩa |
| --- | --- |
| `planned` | Có trong kế hoạch, chưa tạo |
| `draft` | Đã tạo, còn đang thiết kế |
| `planning-only` | Chỉ dùng trong giai đoạn planning |
| `pilot-only` | Chỉ dùng cho dry-run/pilot |
| `advisory` | Có thể tham khảo trong task thật, chưa active governance |
| `partial-active` | Chỉ kích hoạt trong scope hẹp đã được User duyệt |
| `active` | Được User xác nhận là active |
| `deprecated` | Không dùng cho task mới |
| `archived` | Lưu trữ |

---

## 3. Artifact type

| Type | Ý nghĩa |
| --- | --- |
| `canonical` | File nền phải đọc để hiểu/vận hành v2 |
| `support` | File hỗ trợ, không phải nền bắt buộc |
| `agency` | Charter của agency |
| `oversight` | Charter của cơ chế giám sát/kiểm tra |
| `schema` | Chuẩn output/report |
| `reference` | Nguồn tham khảo |
| `pilot` | Dry-run hoặc pilot report |
| `compatibility` | So sánh/migration với hệ khác |

---

## 4. Phase 0 registry

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md` | Roadmap xây dựng v2, legacy pointer | Planning | support | `archived` | inactive |
| `README.md` | Giới thiệu v2, status, cách đọc nhanh | Phase 0 | canonical | `active` | scoped |
| `USAGE_GUIDE.md` | Hướng dẫn sử dụng nhanh Meow v2 | Phase 0 | support | `active` | scoped |
| `VERSIONING_POLICY.md` | Version states, activation policy, phase policy | Phase 0 | canonical | `active` | scoped |
| `CONSTITUTION.md` | Hiến pháp nền và nguyên tắc bất biến | Phase 0 | canonical | `active` | scoped |
| `AUTHORITY_MODEL.md` | Decision authority và execution authority | Phase 0 | canonical | `active` | scoped |
| `OPERATING_PROTOCOL.md` | Task intake, gates, conflict, mutation protocol | Phase 0 | canonical | `active` | scoped |
| `FEDERATION_MANIFEST.md` | Điều hướng đọc file và route task | Phase 0 | canonical | `active` | scoped |
| `REGISTRY.md` | Registry nội bộ v2 | Phase 0 | canonical | `active` | scoped |

---

## 5. Reference Track R0 registry

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `references/REFERENCES.md` | Danh mục nguồn tham khảo | R0 | reference | `reference-only` | inactive |
| `references/SOURCE_MAPPING.md` | Map source vào module/phase | R0 | reference | `reference-only` | inactive |
| `references/READ_ORDER.md` | Thứ tự đọc nguồn theo phase/module | R0 | reference | `reference-only` | inactive |
| `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | Quyết định thiết kế rút ra từ reference | R0 | reference | `reference-only` | inactive |

Reference Track là support layer chạy song song với các phase build v2.

Reference files không tự trở thành active rule.

---

### 5.1. Memo support layer registry

Memo support layer bootstrap cho federation v2.

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `memo/MEOW_MEMO_MANIFEST.md` | Memo quick layer and lifecycle | Support | support | `advisory` | scoped |
| `memo/long_term/PROJECT_STATE.md` | Federation v2 project state snapshot | Support | support | `advisory` | scoped |
| `memo/long_term/DECISION_MEMORY.md` | Long-term confirmed decisions | Support | support | `advisory` | scoped |
| `memo/long_term/ISSUE_MEMORY.md` | Long-term open issues and risks | Support | support | `advisory` | scoped |
| `memo/long_term/ROUTING_MEMORY.md` | Memo routing quick layer | Support | support | `advisory` | scoped |
| `memo/short_term/SESSION_STATE.md` | Short-term session state | Support | support | `advisory` | scoped |
| `memo/short_term/TASK_CONTEXT.md` | Short-term task context | Support | support | `advisory` | scoped |
| `memo/short_term/WORKING_SET.md` | Current memo task working set | Support | support | `advisory` | scoped |
| `memo/short_term/PROMOTION_QUEUE.md` | Short-term to long-term promotion queue | Support | support | `advisory` | scoped |
| `memo/log/MEMO_LOG_2026.md` | Append-only memo trace | Support | support | `advisory` | scoped |

Status: `advisory` - memo support layer initialized from v1 structure and adapted to v2-only state.

### 5.2. Status matrix support layer

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `STATUS_MATRIX.md` | Compact snapshot of current v2 phase/support status, legacy pointer | Support | support | `archived` | inactive |

Status: `archived` - compact snapshot moved to `agent_hub/version/v2/legacy/`; root file kept as a legacy pointer.

### 5.3. Librarian support layer

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `agencies/librarian/LIBRARIAN_AGENT.md` | Document librarian / source access broker for Zotero, NotebookLM, and filesystem paths | Support | agency | `draft` | inactive |

Status: `draft` - minimal retrieval broker created as a support agency for multi-project document access.

---

## 6. Sprint C0 update registry

Sprint C0 cập nhật các file hiện có, không tạo file mới.

Updated artifacts:

```text
README.md
CONSTITUTION.md
AUTHORITY_MODEL.md
OPERATING_PROTOCOL.md
FEDERATION_MANIFEST.md
MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
REGISTRY.md
references/REFERENCES.md
references/SOURCE_MAPPING.md
references/READ_ORDER.md
references/DESIGN_DECISIONS_FROM_REFERENCES.md
```

Status: `completed`

Activation: inactive

Purpose:

* bổ sung scientific research standards;
* đăng ký nguồn Nguyễn Văn Tuấn - Đi vào nghiên cứu khoa học;
* thêm `GATE-SCIENTIFIC-CRITIQUE`;
* định hướng Phase 1 thành Governance and Oversight Core.

---

## 7. Planned later phases

### Phase 1 - Governance and Oversight Core

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `governance/LAWMAKER_AGENT.md` | Rule proposal charter | Phase 1 | agency | `draft` | inactive |
| `governance/CONFLICT_COURT.md` | Conflict triage and resolution charter | Phase 1 | agency | `draft` | inactive |
| `governance/DECISION_RECORDS.md` | Decision record model | Phase 1 | support | `draft` | inactive |
| `oversight/OPERATIONAL_INSPECTOR.md` | Operational compliance inspection | Phase 1 | oversight | `draft` | inactive |
| `oversight/SCIENTIFIC_CRITIC.md` | Scientific critique and claim quality control | Phase 1 | oversight | `draft` | inactive |

Status: `draft` - draft stage completed on `2026-06-19`; ready for review

### Phase 2 - Core Coordinator

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `core/MEOW_COORDINATOR.md` | Central coordination charter | Phase 2 | canonical | `draft` | inactive |
| `core/TASK_ROUTING.md` | Task routing matrix | Phase 2 | support | `partial-active` | scoped |
| `core/GATE_PROTOCOL.md` | Gate sequencing and stop rules | Phase 2 | support | `draft` | inactive |

Status: `draft` - draft stage completed on `2026-06-19`; ready for review

### Phase 3 - Schema Layer

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `schemas/OPERATING_CONTRACT_SCHEMA.md` | Template và instruction cho Operating Contract | Phase 3 | schema | `draft` | inactive |
| `schemas/INSPECTION_REPORT_SCHEMA.md` | Template và instruction cho Inspection Report của Operational Inspector | Phase 3 | schema | `draft` | inactive |
| `schemas/DECISION_RECORD_SCHEMA.md` | Template và instruction cho Decision Record | Phase 3 | schema | `draft` | inactive |
| `schemas/RULE_PROPOSAL_SCHEMA.md` | Template và instruction cho Rule Proposal của Lawmaker | Phase 3 | schema | `draft` | inactive |
| `schemas/EVIDENCE_REPORT_SCHEMA.md` | Template và instruction cho Evidence Report của Knowledge Agency | Phase 3 | schema | `draft` | inactive |
| `schemas/MEMO_UPDATE_SCHEMA.md` | Template và instruction cho Memo Update của Memo Agency | Phase 3 | schema | `draft` | inactive |
| `schemas/ACTION_POLICY_SCHEMA.md` | Template và instruction cho Action Policy của Tool Safety Agency | Phase 3 | schema | `draft` | inactive |

Status: `draft` - draft stage completed on `2026-06-19`; ready for review

### Phase 4 - Functional Agencies

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `agencies/research/RESEARCH_AGENT.md` | Scientific evidence integrity, claim mapping, evidence classification | Phase 4 | agency | `draft` | inactive |
| `agencies/coding/CODING_AGENT.md` | Sprint Contract, Generator-Evaluator, code implementation | Phase 4 | agency | `draft` | inactive |
| `agencies/memo/MEMO_AGENT.md` | Long-term/short-term/log memory lifecycle | Phase 4 | agency | `draft` | inactive |
| `agencies/knowledge/KNOWLEDGE_AGENT.md` | Source canonical lookup, source verification, source gap detection | Phase 4 | agency | `draft` | inactive |
| `agencies/tool_safety/TOOL_SAFETY_AGENT.md` | Action classification, risk assessment, action policy | Phase 4 | agency | `draft` | inactive |
| `agencies/experiment/EXPERIMENT_STEWARD_AGENT.md` | Experiment scope routing, baseline protection, branch classification | Phase 4 | agency | `draft` | inactive |
| `agencies/data_output/DATA_OUTPUT_AGENT.md` | Data/output status, provenance, data integrity, overwrite protection | Phase 4 | agency | `draft` | inactive |

Status: `draft` — tất cả 7 files đã harden và đồng bộ ngày 2026-06-19, chờ review.

### Phase 5 - Reference Consolidation

Planned files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `references/REFERENCE_AUDIT.md` | Audit nguồn tham khảo và coverage | Phase 5 | reference | `draft` | inactive |
| `references/STALE_SOURCE_REPORT.md` | Báo cáo nguồn stale/weak/outdated | Phase 5 | reference | `draft` | inactive |
| `references/DESIGN_DECISION_REVIEW.md` | Rà soát lại design decisions từ reference | Phase 5 | reference | `draft` | inactive |

Status: `draft`

### Phase 6 - Dry-run Pilots

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `pilot/PILOT_PLAN.md` | Dry-run plan and evaluation criteria | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_001_REPORT.md` | Simulated notebook edit pilot | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_002_REPORT.md` | Simulated memo update pilot | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_003_REPORT.md` | Simulated rule-add pilot | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_004_REPORT.md` | Simulated risky action pilot | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_005_REPORT.md` | Simulated validation-claim pilot | Phase 6 | pilot | `pilot-only` | inactive |
| `pilot/PILOT_RESULTS.md` | Phase 6 summary and design readout | Phase 6 | pilot | `pilot-only` | inactive |

Status: `completed` - 5 scenario dry-run đã hoàn tất và tổng kết trong `pilot/PILOT_RESULTS.md`; vẫn là `dry-run-only`, không activation.

### Phase 7 - Compatibility Review

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `compatibility/MEOW_V1_COMPARISON.md` | Side-by-side comparison between v1 and v2 | Phase 7 | compatibility | `draft` | inactive |
| `compatibility/MIGRATION_NOTES.md` | Advisory migration notes and reuse guidance | Phase 7 | compatibility | `draft` | inactive |

Status: `completed` - compatibility review hoàn tất ở mức advisory vào `2026-06-19`; giữ vai trò tham khảo, không phải migration plan.

---

## 8. Phase 8 registry

Phase 8 chỉ mở scope hẹp cho partial activation.

Draft files:

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `activation/PARTIAL_ACTIVATION.md` | Scoped activation scope, allowed actions, rollback path | Phase 8 | support | `partial-active` | scoped |

Status: `active` - scoped activation enabled on `2026-06-18` for query/analysis task classes only.

---

## 9. Runtime registry

Runtime package added and smoke-tested for Phase 8 enforcement.

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `runtime/README.md` | Runtime layer overview and source-of-truth mapping | Phase 8 | support | `partial-active` | scoped |
| `runtime/__init__.py` | Runtime public API exports | Phase 8 | support | `partial-active` | scoped |
| `runtime/config.py` | Runtime paths and config | Phase 8 | support | `partial-active` | scoped |
| `runtime/models.py` | Runtime dataclasses and enums | Phase 8 | support | `partial-active` | scoped |
| `runtime/loader.py` | Markdown spec loader | Phase 8 | support | `partial-active` | scoped |
| `runtime/classifier.py` | Task class, risk classifier, and topic classifier | Phase 8 | support | `partial-active` | scoped |
| `runtime/router.py` | Scope router for FAST/GUIDED/FULL | Phase 8 | support | `partial-active` | scoped |
| `runtime/gates.py` | Gate evaluator | Phase 8 | support | `partial-active` | scoped |
| `runtime/policy.py` | Action policy evaluator | Phase 8 | support | `partial-active` | scoped |
| `runtime/executor.py` | Executor adapter | Phase 8 | support | `partial-active` | scoped |
| `runtime/audit.py` | Audit logger | Phase 8 | support | `partial-active` | scoped |
| `runtime/errors.py` | Runtime error types | Phase 8 | support | `partial-active` | scoped |
| `runtime/engine.py` | Runtime orchestration entry point | Phase 8 | support | `partial-active` | scoped |

Status: `active` - runtime package created on `2026-06-18`, compile-ok, smoke-tested, and currently limited to the scoped Phase 8 query/analysis path. Topic handling is now separated from intent handling; executor remains adapter-only.

---

## 10. Update rule

Khi tạo file mới trong v2:

1. xác định phase;
2. xác định file type;
3. xác định status;
4. cập nhật registry nếu file có vai trò trong workflow;
5. không update registry v1 nếu chưa có User request.

Không được xóa entry cũ nếu chưa có lý do và approval rõ.

## 10. Experiment registry

| File | Role | Phase | Type | Status | Activation |
| --- | --- | --- | --- | --- | --- |
| `experiments/EXPERIMENT_REGISTRY.md` | Experiment registry for v2 overlays | Support | support | `active` | scoped |
| `experiments/EXPERIMENT_TEMPLATE.md` | Template for new experiment overlays | Support | support | `advisory` | scoped |
| `experiments/exp_01/EXP01_ACTIVE_RULES.md` | Active rules for exp_01 in v2 | Support | support | `active` | scoped |
| `experiments/exp_01/EXP01_CONTEXT_INDEX.md` | Context index for exp_01 in v2 | Support | support | `active` | scoped |

Status: `active` - experiment overlay is hosted inside v2 and no longer depends on the root registry path.
