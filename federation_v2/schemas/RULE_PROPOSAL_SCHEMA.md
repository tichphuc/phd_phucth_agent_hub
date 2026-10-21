# RULE_PROPOSAL_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`RULE_PROPOSAL_SCHEMA.md` chuan hoa format cua **Rule Proposal** - tai lieu Lawmaker dung de de xuat them, sua, deprecate hoac archive rule trong Meow v2.

Rule Proposal la gate truoc khi bat ky rule moi nao co hieu luc. Lawmaker khong the activate rule. Rule chi co the tro thanh active sau khi User xac nhan ro rang.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| Meow v1 governance | Rule lifecycle: Proposed -> Active -> Deprecated | `ADOPT` - REF-DEC-024 |
| Microsoft AGT | Audit / Decision record cho moi policy change | `ADAPT` - REF-DEC-002 |
| `governance/LAWMAKER_AGENT.md` | Output template co ban cua Lawmaker | mo rong thanh schema day du |
| `CONSTITUTION.md` | Proposal before Mutation - khong activate truc tiep | phan anh truc tiep |
| `AUTHORITY_MODEL.md` | Lawmaker khong tu activate luat | phan anh truc tiep |

---

## 3. Khi nao Lawmaker phat hanh Rule Proposal

Lawmaker phat hanh Rule Proposal khi:

* phat hien can them rule moi vao governance kernel v2;
* phat hien rule hien co can sua, clarify hoac mo rong;
* phat hien rule khong con phu hop va can deprecate hoac archive;
* Coordinator hoac Operational Inspector yeu cau Lawmaker de xuat rule;
* User yeu cau thay doi rule.

Lawmaker khong phat hanh Rule Proposal cho:

* thay doi nho khong anh huong governance logic;
* quyet dinh khoa hoc ve cong thuc, phuong phap hoac ket qua;
* memo update cua Memo Agency.

---

## 4. Template

```text
RULE PROPOSAL

Proposal ID:        RP-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Proposal type:      [NEW / MODIFY / DEPRECATE / ARCHIVE]
Status:             [Proposed / Under review / Approved / Rejected / Deferred]
Proposed by:        [Lawmaker / Coordinator / User request]

Rule name:
  [Ten rule ngan gon, dung duoc nhu label]

Rule scope:
  [global-v2 / phase-specific / experiment-specific / agency-specific]

Problem:
  [Van de ma rule nay giai quyet, hoac ly do sua / deprecate rule cu]

Current state (neu MODIFY / DEPRECATE / ARCHIVE):
  [Noi dung rule hien tai, file dang chua, status hien tai]

Proposed content (neu NEW / MODIFY):
  [Noi dung de xuat - du ro de User va Conflict Court danh gia]

Rationale:
  [Ly do cu the, co the kem reference]

Reference basis:
  [Source hoac Design Decision ho tro proposal: REF-DEC-*, file noi bo, v.v.]

Conflict check:
  [liet ke conflict tiem nang voi rule hien co, hoac ghi NONE]

Impact:
  [Anh huong den file nao, phase nao, agency nao, workflow nao]

Registry update required:
  Yes / No
  [Giai thich ngan neu Yes - REGISTRY.md nao can update]

Required gates:
  [Gate bat buoc phai di qua: GATE-REFERENCE, GATE-INSPECTION, GATE-SCIENTIFIC-CRITIQUE, GATE-USER-CONFIRMATION]

Need User decision:
  Yes / No
  [Ghi ro cau hoi can User quyet dinh neu Yes]

Risk:
  [Mo ta risk neu proposal duoc approve hoac neu khong duoc approve]
```

---

## 5. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Proposal ID` | Khuyen nghi | Format: RP-[date]-[so], vi du RP-2026-06-18-001 |
| `Date` | Bat buoc | Ngay phat hanh |
| `Proposal type` | Bat buoc | Chon tu Section 6 |
| `Status` | Bat buoc | Chon tu Section 7 |
| `Proposed by` | Bat buoc | Ai khoi tao proposal |
| `Rule name` | Bat buoc | Ten ngan gon, dung duoc nhu label |
| `Rule scope` | Bat buoc | Chon tu Section 8 |
| `Problem` | Bat buoc | Van de can giai quyet |
| `Current state` | Bat buoc khi MODIFY / DEPRECATE / ARCHIVE | Noi dung hien tai cua rule |
| `Proposed content` | Bat buoc khi NEW / MODIFY | Noi dung de xuat ro rang |
| `Rationale` | Bat buoc | Ly do - khong duoc ghi "de tot hon" chung chung |
| `Reference basis` | Bat buoc khi co reference | Source hoac REF-DEC ho tro |
| `Conflict check` | Bat buoc | Ghi NONE neu khong co conflict |
| `Impact` | Bat buoc | Tac dong cu the |
| `Registry update required` | Bat buoc | Yes hoac No |
| `Required gates` | Bat buoc | Liet ke gate phai di qua |
| `Need User decision` | Bat buoc | Yes hoac No kem cau hoi cu the |
| `Risk` | Khuyen nghi | Risk neu approve hoac khong approve |

---

## 6. Proposal type vocabulary

| Type | Y nghia |
| --- | --- |
| `NEW` | De xuat them rule moi vao he v2 |
| `MODIFY` | De xuat sua noi dung rule dang active |
| `DEPRECATE` | De xuat khong con dung rule cho task moi |
| `ARCHIVE` | De xuat dua rule vao luu tru, khong active |

---

## 7. Status vocabulary

| Status | Y nghia |
| --- | --- |
| `Proposed` | Moi phat hanh, chua review |
| `Under review` | Dang review boi Operational Inspector hoac Conflict Court |
| `Approved` | User da approve - can kem Decision Record |
| `Rejected` | User da reject - ghi ly do |
| `Deferred` | Bi tri hoan co ly do ro |

---

## 8. Rule scope vocabulary

| Scope | Y nghia |
| --- | --- |
| `global-v2` | Ap dung cho toan bo Meow v2 federation |
| `phase-specific` | Chi ap dung cho mot phase build cu the |
| `experiment-specific` | Chi ap dung cho mot experiment cu the |
| `agency-specific` | Chi ap dung trong mandate cua mot agency |

---

## 9. Rule lifecycle

```text
Proposed
  -> Under review (Operational Inspector, Conflict Court)
  -> Approved (User decision) -> Decision Record DR-*
     -> Active (sau khi duoc activate trong phase phu hop)
        -> Deprecated (khong dung cho task moi)
           -> Archived (luu tru)
  -> Rejected (User reject - ghi ly do)
  -> Deferred (hoan lai - ghi ly do)
```

Mot Rule Proposal **khong tro thanh Active rule** neu khong co:

1. `Status: Approved` tu User;
2. Decision Record kem theo (`USER_DECISION`).

Nguon: `AUTHORITY_MODEL.md`, `CONSTITUTION.md`, `REF-DEC-024`.

---

## 10. Fail-closed rule

Neu Proposal co conflict chua resolve voi rule hien co hoac Constitution:

```text
Status: Under review
Need User decision: Yes
```

Lawmaker khong duoc ghi `Status: Approved` neu User chua xac nhan ro rang.

Neu proposal cham claim khoa hoc hoac method:

```text
Required gates: them GATE-SCIENTIFIC-CRITIQUE
```

Nguon: `governance/LAWMAKER_AGENT.md`.

---

## 11. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `DECISION_RECORD_SCHEMA.md` | Rule Proposal duoc approve -> Decision Record USER_DECISION |
| `INSPECTION_REPORT_SCHEMA.md` | Operational Inspector review proposal truoc khi submit User |
| `governance/LAWMAKER_AGENT.md` | Charter cua Lawmaker - mandate, inputs, outputs |
| `governance/CONFLICT_COURT.md` | Conflict Court review neu proposal tao conflict |
| `REGISTRY.md` | Registry can update khi rule moi duoc approve |
