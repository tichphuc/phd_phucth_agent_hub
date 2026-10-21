# MEMO_UPDATE_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`MEMO_UPDATE_SCHEMA.md` chuan hoa format cua **Memo Update** - tai lieu Memo Agency dung de phan loai va apply update vao he thong memory cua Meow v2.

Memo Update phan biet ro:

* update nao thuoc long-term memory (can source canonical hoac User confirmation);
* update nao thuoc short-term memory (session / task context);
* update nao chi la log entry (append-only, khong viet lai);
* operation la gi: ADD / UPDATE / DELETE / NOOP.

Memo khong phai source canonical. Neu memo mau thuan voi source canonical, source canonical thang va memo phai duoc danh dau stale.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| MiMoCode local note | Auto-update chi nen cho short-term; long-term can source / User confirm | `ADOPT` - REF-DEC-014 |
| Zep / Mem0 / GraphRAG | Memory lifecycle: retrieve / update / invalidate va local-to-global summaries | `ADAPT` - REF-DEC-015 |
| Meow v1 memo module | Long-term / short-term / log split; ADD / UPDATE / DELETE / NOOP lifecycle | `ADOPT` - REF-DEC-024 |
| `MEOW_MEMO_MANIFEST.md` | Ba tang memory: Long-Term, Short-Term, Log | dieu chinh cho v2 |
| `CONSTITUTION.md` | Memo khong phai source canonical neu co source goc | phan anh truc tiep |

---

## 3. Ba tang memory trong Meow v2

| Tang | Vai tro | Source required | Viet lai duoc khong |
| --- | --- | --- | --- |
| **Long-Term** | State, decision, issue, routing on dinh | Can source canonical hoac User confirmation | Khong - phai qua UPDATE / DELETE ro rang |
| **Short-Term** | Task / session context, working set, pending decision | Session source du | Co - co the overwrite nhanh |
| **Log** | Episode trace: action, conflict, decision, change | Action trace du | Khong - append-only, khong rewrite cu |

---

## 4. Template

```text
MEMO UPDATE

Update ID:          MU-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Triggered by:       [Operating Contract ID, task description hoac event]
Updated by:         Memo Agency

Target layer:
  [long-term / short-term / log]

Operation:
  [ADD / UPDATE / DELETE / NOOP]
  Giai thich ngan neu DELETE hoac NOOP

Item:
  [Noi dung item can update - dung ngon ngu ro rang, ngan gon]

Source or evidence:
  [Source canonical hoac User confirmation - bat buoc cho long-term]
  [Session prompt hoac task context - du cho short-term]
  [Action trace - du cho log]

Previous value (neu UPDATE hoac DELETE):
  [Noi dung cu se bi thay the hoac xoa]

New value (neu ADD hoac UPDATE):
  [Noi dung moi]

Staleness check:
  [Source canonical co thay doi khong? Memo co stale khong?]
  [Ghi NONE neu khong co van de stale]

Requires User confirmation:
  Yes / No
  [Long-term ADD / UPDATE cho decision / state quan trong: Yes]
  [Short-term: No neu chi la session context]
  [Log: No - append-only]

Log entry:
  [Ghi ngan vao Log tang neu operation nay can trace]
  Format: [date] [operation] [item summary] [source]
```

---

## 5. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Update ID` | Khuyen nghi | Format: MU-[date]-[so], vi du MU-2026-06-18-001 |
| `Date` | Bat buoc | Ngay apply update |
| `Triggered by` | Bat buoc | Nguon goc trigger |
| `Target layer` | Bat buoc | long-term / short-term / log |
| `Operation` | Bat buoc | Chon tu Section 6 |
| `Item` | Bat buoc | Noi dung item - khong duoc ghi chung chung |
| `Source or evidence` | Bat buoc cho long-term | Source canonical hoac User confirmation |
| `Previous value` | Bat buoc khi UPDATE / DELETE | Noi dung cu - de truy vet |
| `New value` | Bat buoc khi ADD / UPDATE | Noi dung moi |
| `Staleness check` | Bat buoc | Ghi NONE neu khong co van de |
| `Requires User confirmation` | Bat buoc | Yes cho long-term decision / state quan trong |
| `Log entry` | Khuyen nghi khi long-term | Append vao Log tang |

---

## 6. Operation vocabulary

| Operation | Y nghia |
| --- | --- |
| `ADD` | Them item moi vao memory layer |
| `UPDATE` | Cap nhat item da co - ghi ro previous value |
| `DELETE` | Xoa item khoi memory layer - ghi ro ly do |
| `NOOP` | Khong thay doi - ghi ro vi sao NOOP |

---

## 7. Permission model

| Layer | Source required | User confirmation | Co the auto-update |
| --- | --- | --- | --- |
| `long-term` | Can source canonical hoac User confirmation | Yes cho state / decision / issue quan trong | Khong - phai qua operation ro |
| `short-term` | Session source du | No neu chi la task / session context | Co - voi can than |
| `log` | Action trace du | No - append-only | Co - nhung khong rewrite cu |

Nguon: `REF-DEC-014` (auto-update chi cho short-term; long-term can source / User confirm - ADOPT).

---

## 8. Staleness rules

Memo phai duoc danh dau stale neu:

* source canonical thay doi ma memo chua duoc update;
* Decision Record moi supersede decision da co trong memo;
* experiment registry hoac active rules thay doi;
* User xac nhan mot direction moi mau thuan voi long-term memo;
* notebook hoac output canonical thay doi.

Khi phat hien stale:

1. Danh dau item la `stale`;
2. ghi log entry;
3. de xuat UPDATE hoac DELETE voi source moi;
4. cho User confirmation neu la long-term item quan trong.

Khong duoc tiep tuc dung stale memo lam source canonical cho claim khoa hoc.

---

## 9. Fail-closed rule

Neu khong xac dinh duoc source canonical cho mot long-term memo item quan trong:

```text
Operation: NOOP (hoac ADD voi source: pending)
Requires User confirmation: Yes
```

Khong duoc nang item len long-term memo neu chua co source canonical hoac User confirmation.

Nguon: `CONSTITUTION.md`, `REF-DEC-014`.

---

## 10. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `DECISION_RECORD_SCHEMA.md` | Long-term memo update cho decision can kem Decision Record |
| `INSPECTION_REPORT_SCHEMA.md` | Inspection findings co the trigger memo update |
| `EVIDENCE_REPORT_SCHEMA.md` | Evidence Report co the invalidate stale memo ve source |
| `MEOW_MEMO_MANIFEST.md` | Thiet ke memo module cua Meow v2 |
| `CONSTITUTION.md` | Memo khong phai source canonical |
