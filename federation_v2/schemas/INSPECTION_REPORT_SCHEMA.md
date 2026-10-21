# INSPECTION_REPORT_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`INSPECTION_REPORT_SCHEMA.md` chuan hoa format cua **Inspection Report** - output bat buoc cua `Operational Inspector` khi kiem tra task, action, hoac proposal.

Inspection Report quyet dinh task / action co duoc phep tiep tuc hay khong, va co can escalate len User hay khong.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| Microsoft AGT | Fail-closed khi permission / source khong ro | `ADOPT` - REF-DEC-003 |
| Microsoft AGT | Audit / Decision record co allow / deny trace | `ADAPT` - REF-DEC-002 |
| OWASP Agentic AI | Risk taxonomy va mitigation language | `ADAPT` - REF-DEC-019 |
| OpenAI Agents SDK | Guardrails va tracing schema | `ADAPT` - REF-DEC-012 |
| `OPERATIONAL_INSPECTOR.md` | Output template co ban | mo rong field definitions va risk taxonomy |

---

## 3. Khi nao Operational Inspector phat hanh Inspection Report

Operational Inspector phai phat hanh Inspection Report khi:

* task co risk da xac dinh;
* task yeu cau mutation file;
* task co conflict rule hoac authority;
* task lien quan rule / governance / policy;
* task chuan bi activate hoac deprecate gi do;
* Coordinator yeu cau inspection;
* task co scientific claim quan trong va can routing check sang `GATE-SCIENTIFIC-CRITIQUE`.

Inspection Report khong thay the `SCIENTIFIC_CRITIQUE REPORT`.
Hai loai report nay song song va doc lap.

---

## 4. Template

```text
INSPECTION REPORT

Report ID:          IR-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Triggered by:       [Operating Contract ID hoac mo ta task]
Inspector:          Operational Inspector

Scope:
  [Mo ta ro scope inspection: task gi, file nao, action nao]

Checked files and rules:
  [liet ke file rule da kiem tra, it nhat: CONSTITUTION.md,
   AUTHORITY_MODEL.md, OPERATING_PROTOCOL.md, relevant charter]

Findings:
  [Mo ta phat hien cu the - khong duoc ghi chung chung]
  [Neu khong co phat hien: "No findings."]

Conflicts:
  [liet ke conflict theo taxonomy - xem Section 7]
  [Neu khong co: "No conflicts detected."]

Risk classification:
  [liet ke risk category phu hop - xem Section 8]
  [Neu khong co: "No elevated risk identified."]

Severity:
  [BLOCKER / MAJOR / MINOR / NONE]
  [Giai thich ngan neu BLOCKER hoac MAJOR]

Can proceed:
  Yes / No
  [Giai thich ngan]

Need User decision:
  Yes / No
  [Neu Yes thi ghi cau hoi cu the can User quyet dinh]

Required next gate:
  [Gate tiep theo can di qua, hoac NONE neu co the tiep tuc]

Recommended action:
  [Hanh dong cu the de xuat cho Coordinator]
```

---

## 5. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Report ID` | Khuyen nghi | Format: IR-[date]-[so], vi du IR-2026-06-18-001 |
| `Date` | Khuyen nghi | Ngay phat hanh |
| `Triggered by` | Bat buoc | Operating Contract ID hoac mo ta nguon goc trigger |
| `Scope` | Bat buoc | Pham vi cu the, khong ghi chung chung |
| `Checked files and rules` | Bat buoc | Liet ke file da kiem tra thuc su |
| `Findings` | Bat buoc | Phat hien cu the, khong duoc bo trong |
| `Conflicts` | Bat buoc | Theo conflict taxonomy; ghi NONE neu khong co |
| `Risk classification` | Bat buoc | Theo risk taxonomy; ghi NONE neu khong co |
| `Severity` | Bat buoc | BLOCKER / MAJOR / MINOR / NONE |
| `Can proceed` | Bat buoc | Yes hoac No - khong duoc de trong |
| `Need User decision` | Bat buoc | Yes hoac No - ghi cau hoi cu the neu Yes |
| `Required next gate` | Bat buoc | Gate tiep theo hoac NONE |
| `Recommended action` | Khuyen nghi | De xuat cu the cho Coordinator |

---

## 6. Severity scale

| Severity | Y nghia | Hanh dong |
| --- | --- | --- |
| `BLOCKER` | Khong duoc tiep tuc cho den khi co User decision | Dung va hoi User ngay |
| `MAJOR` | Co the phan tich tiep nhung khong duoc mutate / chay / thay doi | Bao cao ro va cho xac nhan |
| `MINOR` | Co the tiep tuc voi rule uu tien cao hon, nhung can ghi chu | Ghi note trong report |
| `NONE` | Khong phat hien van de nghiem trong | Tiep tuc binh thuong |

---

## 7. Conflict taxonomy

Nhat quan voi `OPERATING_PROTOCOL.md`:

| Conflict type | Mo ta |
| --- | --- |
| `CONFLICT-FILE-EDIT` | Task yeu cau mutation file nhung chua co approval |
| `CONFLICT-RULE-PRIORITY` | Hai hoac nhieu rule co yeu cau khac nhau, priority chua ro |
| `CONFLICT-FORMULA-SOURCE` | Cong thuc, tham so hoac citation duoc yeu cau nhung chua co nguon ro |
| `CONFLICT-PIPELINE-CHANGE` | Task lam thay doi pipeline, baseline hoac gia thuyet |
| `CONFLICT-EXPERIMENT-SCOPE` | Task lien quan experiment nhung chua co active rules hoac context index |
| `CONFLICT-DOC-LOCATION` | File dat sai vung trach nhiem |
| `CONFLICT-RESULT-INTERPRETATION` | Ket qua exploratory bi yeu cau trinh bay nhu validated |
| `CONFLICT-AUTHORITY` | Hai body co yeu cau khong tuong thich ve authority |
| `CONFLICT-PERMISSION` | Permission state khong du cho action duoc yeu cau |
| `CONFLICT-MISSING-SOURCE` | Khong xac dinh duoc file canonical cho task hien tai |
| `CONFLICT-SCIENTIFIC-CLAIM` | Claim khoa hoc can `GATE-SCIENTIFIC-CRITIQUE` nhung chua qua |

---

## 8. Risk taxonomy

Lay cam hung tu OWASP Agentic AI, dieu chinh cho research governance context:

| Risk category | Vi du |
| --- | --- |
| `PROMPT-INJECTION` | Input tu file hoac tool co the inject instruction |
| `EXCESSIVE-PERMISSION` | Agent hoac agency yeu cau quyen rong hon task can |
| `UNCONFIRMED-MUTATION` | Action mutate file ma chua co User approval |
| `TOOL-TRUST-VIOLATION` | Tool description duoc tin tuyet doi ma khong verify |
| `DATA-INTEGRITY-RISK` | Du lieu co the bi ghi de hoac provenance khong ro |
| `SCOPE-CREEP` | Task mo rong ngoai scope da approve |
| `SOURCE-GAP` | Claim hoac action thieu source canonical ro |
| `EXPLORATORY-OVERCLAIM` | Ket qua exploratory duoc trinh bay nhu validated |
| `AUTHORITY-BYPASS` | Body bo qua gate hoac oversight |
| `INFORMATION-DISCLOSURE` | Report tiet lo thong tin nhay cam ngoai scope |

---

## 9. Fail-closed rule

Neu Inspection Report khong the hoan chinh vi thieu thong tin, hoac phat hien conflict chua resolve:

```text
Can proceed: No
Need User decision: Yes
Severity: BLOCKER
```

Operational Inspector khong duoc phat hanh `Can proceed: Yes` khi con conflict BLOCKER chua resolve.

Nguon: `REF-DEC-003` (fail-closed khi permission / source / policy khong ro - ADOPT).

---

## 10. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `OPERATING_CONTRACT_SCHEMA.md` | Inspection Report review Operating Contract truoc execution |
| `SCIENTIFIC_CRITIC.md` | Inspection Report co the route claim sang Scientific Critique neu can |
| `DECISION_RECORD_SCHEMA.md` | Inspection result co the dan den Decision Record khi User quyet dinh |
| `ACTION_POLICY_SCHEMA.md` | Inspection Report doi chieu action voi Action Policy |
| `CONFLICT_COURT.md` | Conflict nghiem trong duoc escalate sang Conflict Court |
