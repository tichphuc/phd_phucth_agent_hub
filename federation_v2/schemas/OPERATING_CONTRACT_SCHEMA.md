# OPERATING_CONTRACT_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`OPERATING_CONTRACT_SCHEMA.md` chuan hoa format cua **Operating Contract** - tai lieu bat buoc phai tao truoc moi task khong don gian trong Meow v2.

Operating Contract la gate truoc khi Coordinator route task den agency hoac truoc khi bat ky mutation nao xay ra.

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| Meow v1 governance | Operating Contract lam gate truoc task khong don gian | `ADOPT` - REF-DEC-024 |
| OpenAI Agents SDK | Agent can instructions, input/output boundary va guardrails ro | `ADAPT` - REF-DEC-010 |
| Deep Agents subagents | Agency tra report, khong tu mutate | `ADAPT` - REF-DEC-008 |
| `OPERATING_PROTOCOL.md` | Template toi thieu cho Operating Contract | dieu chinh va mo rong field definitions |

---

## 3. Khi nao can Operating Contract

Operating Contract bat buoc khi task lien quan den:

* rule hoac governance;
* code hoac notebook;
* data hoac output;
* experiment hoac pipeline;
* scientific claim, formula hoac validation;
* tool execution;
* file mutation (tao, sua, xoa, di chuyen, rename);
* baseline hoac assumption;
* memo update;
* module hoac agency architecture;
* bat ky scope nao khong ro.

Task nho, chi doc hoac chi hoi giai nghia thuat ngu co the khong can Operating Contract neu Coordinator xac dinh task that su don gian.

---

## 4. Ai tao Operating Contract

* **Meow Central Coordinator** tao hoac yeu cau tao Operating Contract.
* Coordinator co the tong hop dau vao tu agency report hoac tu Operational Inspector truoc khi hoan chinh contract.
* User khong viet contract, nhung phai duoc trinh bay contract truoc khi mutation xay ra.
* Operational Inspector co the yeu cau dieu chinh contract neu phat hien conflict hoac thieu gate.

---

## 5. Template

```text
OPERATING CONTRACT

Contract ID:        OC-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Phase / context:    [phase hoac context ngan]
Version:            [v0.x]

Task:
  [Mo ta ro task can lam]

Task type:
  [Chon: read-only / analysis / proposal / governance / coding / notebook /
   data / experiment / memo-update / tool-execution / file-mutation / multi-type]

Scope:
  [Pham vi ro: file nao, folder nao, experiment nao, phase nao]

Permission state:
  [Chon: read-only / proposal-only / approved-create / approved-edit /
   approved-run / blocked]
  Mac dinh neu khong ro: read-only

Applicable rules:
  [liet ke file rule ap dung, vi du: CONSTITUTION.md, AUTHORITY_MODEL.md,
   OPERATING_PROTOCOL.md, active rules cua experiment neu co]

Required sources:
  [File, tai lieu, reference hoac source canonical can doc truoc khi lam]

Required agencies:
  [Agency, oversight body hoac governance body can duoc goi]

Allowed actions:
  [liet ke cu the action duoc phep]

Forbidden actions:
  [liet ke cu the action khong duoc phep trong task nay]

Required gates:
  [liet ke gate bat buoc phai di qua, vi du:
   GATE-SCOPE, GATE-READ, GATE-REFERENCE, GATE-EVIDENCE,
   GATE-SCIENTIFIC-CRITIQUE, GATE-PLAN, GATE-INSPECTION,
   GATE-USER-CONFIRMATION, GATE-REVIEW]

Potential conflicts:
  [liet ke conflict da phat hien hoac ghi NONE neu khong co]

Risk:
  [mo ta risk chinh, severity so bo neu co]

Need User confirmation before mutation:
  Yes / No
  [giai thich ngan neu Yes]
```

---

## 6. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Contract ID` | Khuyen nghi | Format: OC-[date]-[so thu tu], vi du OC-2026-06-18-001 |
| `Date` | Khuyen nghi | Ngay tao contract |
| `Phase / context` | Tung chon | Giai doan build hoac context ngan |
| `Version` | Tung chon | Version cua contract neu co revise |
| `Task` | Bat buoc | Mo ta task, du ro de Operational Inspector kiem tra |
| `Task type` | Bat buoc | Chon tu danh sach chuan o Section 7 |
| `Scope` | Bat buoc | Pham vi cu the, khong duoc ghi chung chung |
| `Permission state` | Bat buoc | Chon tu danh sach chuan o Section 8 |
| `Applicable rules` | Bat buoc | It nhat CONSTITUTION.md va OPERATING_PROTOCOL.md |
| `Required sources` | Bat buoc neu task lien quan claim/formula/data | File canonical phai doc truoc |
| `Required agencies` | Khuyen nghi | Ghi NONE neu task tu xu ly |
| `Allowed actions` | Bat buoc | Cu the, khong duoc ghi "bat cu gi can thiet" |
| `Forbidden actions` | Bat buoc | Cu the, khong duoc ghi "khong co gi" |
| `Required gates` | Bat buoc | Khong duoc bo gate |
| `Potential conflicts` | Bat buoc | Ghi NONE neu that su khong co |
| `Risk` | Khuyen nghi | Mo ta risk chinh |
| `Need User confirmation` | Bat buoc | Yes hoac No, kem giai thich neu Yes |

---

## 7. Task type vocabulary

| Task type | Dung khi |
| --- | --- |
| `read-only` | Chi doc va phan tich, khong co mutation |
| `analysis` | Phan tich va de xuat, khong co mutation |
| `proposal` | De xuat file, code, rule, plan - cho approve |
| `governance` | Task lien quan rule, registry, policy, protocol |
| `coding` | Task lien quan code, script, module |
| `notebook` | Task lien quan Jupyter notebook |
| `data` | Task lien quan data file, output, provenance |
| `experiment` | Task lien quan experiment scope, phase, step |
| `memo-update` | Task lien quan Memo Agency memory update |
| `tool-execution` | Task lien quan chay tool, command, pipeline |
| `file-mutation` | Task tao, sua, xoa, di chuyen hoac rename file |
| `multi-type` | Task thuoc nhieu loai cung luc |

---

## 8. Permission state vocabulary

Nhat quan voi `AUTHORITY_MODEL.md`:

| State | Y nghia |
| --- | --- |
| `read-only` | Chi doc va phan tich |
| `proposal-only` | Duoc de xuat noi dung hoac plan |
| `approved-create` | Duoc tao file da duoc User approve |
| `approved-edit` | Duoc sua file da duoc User approve |
| `approved-run` | Duoc chay lenh / test da duoc User approve |
| `blocked` | Khong duoc tiep tuc neu chua co decision |

Mac dinh cho task chua ro: `read-only`.

---

## 9. Gate vocabulary

Nhat quan voi `OPERATING_PROTOCOL.md` va `core/GATE_PROTOCOL.md`:

| Gate | Khi dung |
| --- | --- |
| `GATE-SCOPE` | Moi task khong don gian |
| `GATE-READ` | Can doc rule/source truoc phan tich |
| `GATE-REFERENCE` | Truoc khi thiet ke hoac implement module governance / agency / schema moi |
| `GATE-EVIDENCE` | Task lien quan source, formula, claim, validation |
| `GATE-SCIENTIFIC-CRITIQUE` | Truoc claim khoa hoc quan trong, ket luan, validation claim hoac thay doi gia thuyet |
| `GATE-PLAN` | Task co the dan den mutation |
| `GATE-INSPECTION` | Task co risk/conflict hoac truoc execution quan trong |
| `GATE-USER-CONFIRMATION` | Truoc moi mutation |
| `GATE-REVIEW` | Sau khi co proposal hoac action |

---

## 10. Fail-closed rule

Neu Operating Contract khong the hoan chinh vi thieu thong tin ve scope, permission hoac source:

```text
Permission state: blocked
Need User confirmation: Yes
```

Agent khong duoc tiep tuc task cho den khi co du thong tin.

Nguon: `REF-DEC-003` (fail-closed khi policy / permission khong ro - ADOPT).

---

## 11. Quan he voi cac schema khac

| Schema | Quan he |
| --- | --- |
| `INSPECTION_REPORT_SCHEMA.md` | Operational Inspector review contract truoc execution |
| `DECISION_RECORD_SCHEMA.md` | Contract da qua approval co the dan den Decision Record |
| `RULE_PROPOSAL_SCHEMA.md` | Governance contract co the dan den Rule Proposal |
| `ACTION_POLICY_SCHEMA.md` | Contract lien quan tool/action can xet policy |
