# ACTION_POLICY_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`ACTION_POLICY_SCHEMA.md` chuan hoa format cua **Action Policy** - tai lieu Tool Safety Agency dung de phan loai risk cua tung action va de xuat policy (allow / block / require consent) truoc khi Coordinator route action den execution.

Action Policy giup Meow v2:

* phan loai action theo loai va risk level truoc khi thuc hien;
* xac dinh action nao can User consent tuong minh;
* xac dinh action nao can Operational Inspector review;
* ap dung fail-closed khi action khong ro risk.

Action Policy khong phai runtime enforcement. Day la human-readable policy document. Khi v2 co runtime layer sau nay, Action Policy la input policy cho layer do.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| Microsoft AGT | Deterministic policy gate truoc tool / action | `ADAPT` - REF-DEC-001 |
| Microsoft AGT | Fail-closed khi permission / policy khong ro | `ADOPT` - REF-DEC-003 |
| MCP spec | Tool descriptions khong mac nhien dang tin; tool use can explicit consent | `ADOPT` - REF-DEC-005 |
| Deep Agents | Declarative filesystem permissions | `ADAPT` - REF-DEC-009 |
| OWASP Agentic AI | Threat taxonomy: excessive permission, unconfirmed mutation, tool-trust violation | `ADAPT` - REF-DEC-019 |
| `AUTHORITY_MODEL.md` | Permission states: read-only / approved-create / approved-run / blocked | phan anh truc tiep |

---

## 3. Khi nao Tool Safety Agency phat hanh Action Policy

Tool Safety Agency phat hanh Action Policy khi:

* Coordinator can biet action X co duoc phep khong truoc khi route;
* task co action thuoc loai write / delete / move / run / install / network / notebook-execute;
* Operational Inspector yeu cau Action Policy check;
* User hoi action nao an toan de thuc hien;
* mot tool moi hoac MCP command chua co policy cu.

Action Policy khong can thiet cho:

* action chi la read - mac dinh allow;
* action da duoc User approve trong Operating Contract dang co hieu luc.

---

## 4. Template - Action Policy Declaration

Dung khi khai bao policy cho mot loai action cu the:

```text
ACTION POLICY DECLARATION

Policy ID:          AP-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Declared by:        Tool Safety Agency

Action type:
  [Chon tu Section 6: read / write / delete / move / run / install /
   network / notebook-execute]

Action description:
  [Mo ta cu the action: lenh, file path, tool name, scope]

Risk level:
  [HIGH / MEDIUM / LOW / UNKNOWN]
  Giai thich ngan

Risk category:
  [Chon tu taxonomy o Section 8]

Requires explicit User consent:
  Yes / No
  [Giai thich ngan]

Requires Operational Inspector review:
  Yes / No
  [Giai thich ngan]

Conditions for allow:
  [Dieu kien cu the de action nay duoc phep]

Conditions for block:
  [Dieu kien cu the de action nay bi block]

Rollback possible:
  Yes / No / Partial
  [Mo ta ngan cach rollback neu Yes]

Notes:
  [Tool trust notes, MCP trust notes, hoac canh bao them]

Policy decision:
  ALLOW / ALLOW-WITH-CONSENT / BLOCK / REQUIRE-INSPECTION
```

---

## 5. Template - Action Request Review

Dung khi review mot action request cu the trong context cua mot task:

```text
ACTION REQUEST REVIEW

Review ID:          ARR-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Triggered by:       [Operating Contract ID hoac task]
Reviewed by:        Tool Safety Agency

Requested action:
  [Mo ta cu the: lenh, tool, file path, scope]

Applicable policy:
  [AP-ID neu co policy san, hoac ghi "no standing policy - evaluating"]

Risk classification:
  [Action type + Risk level + Risk category]

Current permission state:
  [Chon tu AUTHORITY_MODEL.md]

User consent status:
  [Chon: confirmed / not-confirmed / not-required]

Operational Inspector review status:
  [Required / Not required / Completed - kem IR-ID neu completed]

Can action proceed:
  Yes / No / Pending-consent / Pending-inspection
  [Giai thich ngan]

Risk if action proceeds:
  [Mo ta risk cu the neu cho phep tiep tuc]

Risk if action is blocked:
  [Mo ta risk cu the neu block]

Recommended decision:
  ALLOW / ALLOW-WITH-CONSENT / BLOCK / REQUIRE-INSPECTION / DEFER
```

---

## 6. Action type vocabulary

| Type | Y nghia | Default risk |
| --- | --- | --- |
| `read` | Doc file, xem cau truc, doc output | LOW - thuong allow |
| `write` | Tao file moi, sua file, ghi de noi dung | MEDIUM -> HIGH - can consent |
| `delete` | Xoa file hoac folder | HIGH - can explicit consent |
| `move` | Di chuyen hoac rename file / folder | MEDIUM -> HIGH - can consent |
| `run` | Chay lenh shell, script, pipeline | HIGH - can consent + inspection |
| `install` | Cai dat package, dependency, tool | HIGH - can consent + inspection |
| `network` | HTTP request, API call, download | MEDIUM -> HIGH - can review |
| `notebook-execute` | Chay cell hoac toan bo notebook | HIGH - can consent + inspection |

---

## 7. Risk level vocabulary

| Level | Y nghia | Hanh dong mac dinh |
| --- | --- | --- |
| `HIGH` | Action co the gay hau qua kho rollback | Block, yeu cau explicit consent va Inspection |
| `MEDIUM` | Action co the anh huong scope dang ke, nhung rollback kha thi | Yeu cau consent; review neu scope rong |
| `LOW` | Action gioi han, rollback de | Allow neu da co approval phu hop |
| `UNKNOWN` | Khong xac dinh duoc risk | Fail-closed: Block va hoi User |

---

## 8. Risk category taxonomy

Lay cam hung tu OWASP Agentic AI, dieu chinh cho tool / action context:

| Category | Mo ta |
| --- | --- |
| `EXCESSIVE-PERMISSION` | Action yeu cau quyen rong hon task can |
| `UNCONFIRMED-MUTATION` | Action mutate file / data ma chua co User approval |
| `TOOL-TRUST-VIOLATION` | Tool description duoc tin tuyet doi ma khong verify |
| `DATA-INTEGRITY-RISK` | Action co the ghi de, xoa hoac corrupt du lieu |
| `SCOPE-CREEP` | Action mo rong ngoai scope da approve trong Operating Contract |
| `IRREVERSIBLE-ACTION` | Action khong the rollback hoac rollback kho |
| `NETWORK-DISCLOSURE` | Action gui data ra ngoai moi truong kiem soat |
| `DEPENDENCY-INJECTION` | Install / run co the dua code ngoai vao moi truong |
| `NOTEBOOK-SIDE-EFFECT` | Notebook execution tao output hoac state ngoai scope |

---

## 9. Policy decision vocabulary

| Decision | Y nghia | Dieu kien |
| --- | --- | --- |
| `ALLOW` | Action duoc phep tiep tuc trong scope da approve | Co Operating Contract va approval ro |
| `ALLOW-WITH-CONSENT` | Action can User consent tuong minh truoc khi tiep tuc | Chua co consent ro |
| `BLOCK` | Action bi block cho den khi co decision | Risk HIGH hoac conflict chua resolve |
| `REQUIRE-INSPECTION` | Action can Operational Inspector review truoc | Risk MEDIUM -> HIGH hoac scope rong |
| `DEFER` | Hoan action den thoi diem phu hop hon | Thieu context hoac User chua san sang |

---

## 10. Tool trust rules

Nhat quan voi `REF-DEC-005` (MCP spec - tool descriptions khong mac nhien dang tin):

* Tool Safety Agency khong duoc tin tuyet doi vao tool description hoac tool annotation.
* Khi tool description mau thuan voi behavior quan sat duoc, phai flag.
* Tool tu nguon chua verify can risk level `MEDIUM` hoac `HIGH` mac dinh.

---

## 11. Fail-closed rule

Neu action co risk `UNKNOWN`, permission khong ro, hoac policy khong ro:

```text
Policy decision: BLOCK
Requires User consent: Yes
Requires Operational Inspector review: Yes
```

Khong duoc allow mot action ma chua co base de danh gia.

---

## 12. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `OPERATING_CONTRACT_SCHEMA.md` | Contract dau vao co the de xuat action |
| `INSPECTION_REPORT_SCHEMA.md` | Inspector xac nhan / chan action |
| `governance/DECISION_RECORDS.md` | Action policy co the dan den decision record neu can |
| `OPERATING_PROTOCOL.md` | Gate sequence va stop rule can khop |
| `AUTHORITY_MODEL.md` | Permission state la dau vao bat buoc |
