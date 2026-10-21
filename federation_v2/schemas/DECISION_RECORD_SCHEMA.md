# DECISION_RECORD_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`DECISION_RECORD_SCHEMA.md` chuan hoa format cua **Decision Record** - tai lieu ghi lai decision da duoc xac nhan hoac da duoc ghi nhan trong Meow v2.

Decision Record giup phan biet ro:

* quyet dinh cua User (`USER_DECISION`);
* de xuat cua agent (`AGENCY_RECOMMENDATION`);
* quyet dinh bi tri hoan (`DEFERRED`);
* quyet dinh da bi supersede boi quyet dinh moi hon (`SUPERSEDED`).

Decision Record khong phai Operating Contract. Decision Record la ban ghi sau fact; Operating Contract la gate truoc action.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| Microsoft AGT | Audit / Decision Record de trace tung allow / deny | `ADAPT` - REF-DEC-002 |
| Meow v1 governance | Khong duoc bien proposal thanh decision | `ADOPT` - REF-DEC-024 |
| OpenAI Agents SDK | Tracing va guardrails giup trace decision | `ADAPT` - REF-DEC-012 |
| `CONSTITUTION.md` | User la cap quyet dinh cao nhat; Evidence Classification | phan anh truc tiep |
| `governance/DECISION_RECORDS.md` | Mo hinh co ban cua Decision Record trong governance | mo rong thanh schema day du |

---

## 3. Khi nao ghi Decision Record

Decision Record bat buoc khi:

* User xac nhan mot quyet dinh anh huong den scope, activation, rule, pipeline, baseline, claim hoac experiment;
* Coordinator ghi nhan mot quyet dinh quan trong tu User prompt;
* Lawmaker hoan chinh mot Rule Proposal da duoc approve;
* Conflict Court de xuat resolution da duoc User xac nhan.

Decision Record nen ghi khi:

* mot decision cu bi supersede boi decision moi;
* mot proposal bi User reject ro rang;
* mot task bi defer co ly do ro.

Decision Record khong dung de ghi:

* ket qua exploratory chua validated;
* noi dung thay the research memo / report;
* log tung phien lam viec (dung Memo Log thay the).

---

## 4. Template

```text
DECISION RECORD

Record ID:          DR-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Decision type:      [USER_DECISION / AGENCY_RECOMMENDATION / DEFERRED / SUPERSEDED]
Status:             [Open / Confirmed / Deferred / Superseded / Rejected]

Decision:
  [Noi dung quyet dinh ngan gon, du ro de tra cuu sau]

Context:
  [Hoan canh dan den quyet dinh nay: task, phase, van de can giai quyet]

Source or evidence:
  [Source canonical hoac User prompt dan den decision nay]
  [Ghi "User prompt - [date]" neu day la USER_DECISION khong tu file]

Related task or prompt:
  [Operating Contract ID, User prompt, file hoac task cu the]

Impact:
  [Tac dong den file nao, phase nao, rule nao, experiment nao]

Related files:
  [File bi anh huong boi quyet dinh nay]

Supersedes:
  [DR-ID cu neu decision nay thay the decision cu, hoac NONE]

Superseded by:
  [DR-ID moi hon neu decision nay da bi thay the, hoac NONE]

Notes:
  [Ghi chu them neu can]
```

---

## 5. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Record ID` | Khuyen nghi | Format: DR-[date]-[so], vi du DR-2026-06-18-001 |
| `Date` | Bat buoc | Ngay ghi nhan decision |
| `Decision type` | Bat buoc | Chon tu Section 6 |
| `Status` | Bat buoc | Chon tu Section 7 |
| `Decision` | Bat buoc | Ngan gon, ro rang, du de tra cuu |
| `Context` | Bat buoc | Hoan canh dan den decision |
| `Source or evidence` | Bat buoc | Source canonical hoac User prompt |
| `Related task or prompt` | Khuyen nghi | Link ve Operating Contract hoac task cu the |
| `Impact` | Bat buoc | Tac dong - khong duoc ghi "khong ro" |
| `Related files` | Khuyen nghi | File lien quan |
| `Supersedes` | Tung chon | DR-ID cu neu co |
| `Superseded by` | Tung chon | DR-ID moi hon neu decision da bi thay the |
| `Notes` | Tung chon | Thong tin them |

---

## 6. Decision type vocabulary

| Type | Y nghia |
| --- | --- |
| `USER_DECISION` | User da xac nhan ro rang quyet dinh nay |
| `AGENCY_RECOMMENDATION` | Agent de xuat va cho User xac nhan hoac reject |
| `DEFERRED` | Quyet dinh bi tri hoan co ly do ro |
| `SUPERSEDED` | Quyet dinh nay da bi thay the boi decision moi hon |

Nguyen tac bat bien:

```text
AGENCY_RECOMMENDATION != USER_DECISION
Proposal != Decision
Deferred != Rejected
Exploratory result != Validated result
```

Nguon: `CONSTITUTION.md`, `REF-DEC-024`.

---

## 7. Status vocabulary

| Status | Y nghia |
| --- | --- |
| `Open` | Decision dang cho xac nhan hoac dang co hieu luc |
| `Confirmed` | User da xac nhan ro rang |
| `Deferred` | Bi tri hoan, chua co decision |
| `Superseded` | Da bi thay the boi decision moi |
| `Rejected` | User da reject ro rang |

---

## 8. Evidence Classification reminder

Khi ghi Decision Record co lien quan den ket qua khoa hoc, phai phan loai dung theo `CONSTITUTION.md`:

| Classification | Y nghia |
| --- | --- |
| `Source-backed` | Co nguon tai lieu ro ho tro |
| `Implementation choice` | Lua chon ky thuat khong bat buoc tu source |
| `Inference / hypothesis` | Suy luan hoac gia thuyet, chua kiem chung |
| `Proposal` | De xuat chua duoc User approve |
| `User decision` | User da quyet dinh |
| `Exploratory result` | Ket qua kham pha, chua validated |
| `Validated result` | Da qua validation du co so |
| `Unknown / insufficient source` | Chua du nguon de phan loai |

Khong duoc ghi `USER_DECISION` cho noi dung chi la `Proposal` hoac `Inference`.

---

## 9. Fail-closed rule

Neu khong xac dinh duoc decision type hoac khong co source ro:

```text
Decision type: AGENCY_RECOMMENDATION
Status: Open
Source or evidence: pending - can User xac nhan
```

Khong duoc ghi `USER_DECISION` neu chua co xac nhan ro tu User.

Nguon: `REF-DEC-024` (khong bien proposal thanh decision - ADOPT).

---

## 10. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `OPERATING_CONTRACT_SCHEMA.md` | Operating Contract dan den Decision Record khi duoc approve |
| `RULE_PROPOSAL_SCHEMA.md` | Rule Proposal duoc approve -> Decision Record loai USER_DECISION |
| `INSPECTION_REPORT_SCHEMA.md` | Inspection findings co the dan den Decision Record |
| `governance/DECISION_RECORDS.md` | File governance mo ta vai tro Decision Record trong co cau v2 |
| `CONSTITUTION.md` | Evidence Classification bat buoc khi ghi decision khoa hoc |
