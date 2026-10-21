# EVIDENCE_REPORT_SCHEMA.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

Phase: `3 - Schema Layer`

---

## 1. Muc dich

`EVIDENCE_REPORT_SCHEMA.md` chuan hoa format cua **Evidence Report** - output cua Knowledge / Evidence Agency khi kiem tra xem mot claim, cong thuc, citation hoac ket qua khoa hoc co du source backing hay khong.

Evidence Report giup Meow v2 phan biet ro:

* cai gi co nguon tai lieu ro rang;
* cai gi la lua chon ky thuat;
* cai gi la suy luan hoac gia thuyet;
* cai gi la ket qua exploratory chua validated;
* cai gi chua du nguon.

Evidence Report khong phai Scientific Critique Report. Evidence Report tra loi cau hoi "claim nay co source gi?". Scientific Critique Report tra loi cau hoi "claim nay co du co so khoa hoc de trinh bay khong?".

File nay khong kich hoat v2. File nay la template va instruction huong dan.

---

## 2. Nguon goc thiet ke

| Source | Idea | Decision |
| --- | --- | --- |
| `CONSTITUTION.md` | Scientific Integrity va Evidence Classification | phan anh truc tiep |
| `CONSTITUTION.md` | Scientific Research Standards | phan anh truc tiep |
| Nguyen Van Tuan - Di vao nghien cuu khoa hoc | research question, scientific basis, data integrity, plagiarism, credit integrity | `ADOPT` - REF-DEC-026 / 028 / 029 |
| OpenAI Agents SDK | Agent can instructions, input/output boundary ro | `ADAPT` - REF-DEC-010 |

---

## 3. Khi nao Knowledge Agency phat hanh Evidence Report

Knowledge / Evidence Agency phai phat hanh Evidence Report khi:

* task lien quan cong thuc, tham so, don vi hoac hang so vat ly;
* task lien quan citation, tai lieu tham khao hoac nguon du lieu;
* task lien quan claim khoa hoc quan trong;
* task lien quan validation claim;
* Coordinator hoac Scientific Critic yeu cau kiem tra evidence;
* task can phan biet source-backed vs exploratory vs hypothesis.

Evidence Report khong can thiet cho:

* task chi doc va tom tat rule governance;
* task chi lien quan coding style khong anh huong ket qua khoa hoc;
* task don gian khong lien quan claim hoac formula.

---

## 4. Template

```text
EVIDENCE REPORT

Report ID:          ER-[YYYY-MM-DD]-[NNN]
Date:               [YYYY-MM-DD]
Triggered by:       [Operating Contract ID, task description hoac Scientific Critique request]
Checked by:         Knowledge / Evidence Agency

Research question context:
  [Cau hoi nghien cuu ma claim nay lien quan, hoac ghi N/A neu khong ap dung]

Claims or items checked:
  [liet ke cu the claim, cong thuc, citation hoac ket qua can kiem tra]

Source list:
  [Danh sach source da kiem tra]
  Format:
  - [Ten nguon / file path / DOI / citation]
    Type: [primary / secondary / memo / dataset / tool-output / unknown]
    Verified: Yes / No / Partially
    Notes: [Ghi chu ngan ve coverage hoac limitation]

Evidence classification (per claim or item):
  [Phan loai tung claim/item theo taxonomy o Section 7]
  Format:
  - Claim/item: [...]
    Classification: [Source-backed / Implementation choice / Inference-hypothesis /
                    Proposal / User decision / Exploratory result /
                    Validated result / Unknown-insufficient source]
    Basis: [Source hoac ly do classification]

Source gaps identified:
  [liet ke claim/item co source gap quan trong, hoac ghi NONE]

Credit and integrity check:
  [Kiem tra attribution, plagiarism risk, conflict of interest - xem Section 8]
  [Ghi NONE neu khong co van de]

Recommended action:
  [De xuat cu the: giu claim, ha cap classification, bo sung source, hoi User]

Can task proceed on current evidence:
  Yes / No / Partial (voi dieu kien)
  [Giai thich ngan]

Need Scientific Critique:
  Yes / No
  [Ghi ly do neu Yes - route sang GATE-SCIENTIFIC-CRITIQUE]
```

---

## 5. Field definitions

| Field | Bat buoc | Giai thich |
| --- | --- | --- |
| `Report ID` | Khuyen nghi | Format: ER-[date]-[so], vi du ER-2026-06-18-001 |
| `Date` | Bat buoc | Ngay phat hanh |
| `Triggered by` | Bat buoc | Nguon goc trigger |
| `Research question context` | Khuyen nghi | Cau hoi nghien cuu theo REF-DEC-026; ghi N/A neu khong ap dung |
| `Claims or items checked` | Bat buoc | Liet ke cu the - khong ghi chung chung |
| `Source list` | Bat buoc | Kem Type va Verified cho tung source |
| `Evidence classification` | Bat buoc | Theo taxonomy; tung claim phai duoc phan loai |
| `Source gaps identified` | Bat buoc | Ghi NONE neu khong co |
| `Credit and integrity check` | Bat buoc | Ghi NONE neu khong co van de |
| `Recommended action` | Bat buoc | De xuat cu the, khong duoc ghi "tuy Coordinator" |
| `Can task proceed` | Bat buoc | Yes / No / Partial |
| `Need Scientific Critique` | Bat buoc | Yes hoac No kem ly do |

---

## 6. Source type vocabulary

| Type | Y nghia |
| --- | --- |
| `primary` | Tai lieu goc: paper peer-reviewed, dataset goc, user guide chinh thuc |
| `secondary` | Review, textbook, summary co trich dan ro tu primary |
| `memo` | Memo hoac report noi bo cua project - khong phai primary source |
| `dataset` | File du lieu thuc nghiem hoac du lieu dau vao |
| `tool-output` | Output tu tool hoac notebook - khong phai source canonical cua claim khoa hoc |
| `unknown` | Khong xac dinh duoc loai hoac nguon goc |

Ghi chu: `memo` va `tool-output` **khong phai primary source** cho claim khoa hoc. Neu claim chi co source loai nay, classification phai la `Exploratory result` hoac `Unknown / insufficient source`, khong duoc ghi `Source-backed`.

---

## 7. Evidence Classification taxonomy

| Classification | Y nghia | Dieu kien |
| --- | --- | --- |
| `Source-backed` | Co primary / secondary source ro ho tro truc tiep | Source da duoc doc va verify |
| `Implementation choice` | Lua chon ky thuat hop ly nhung khong bat buoc tu source | Khong co primary source, nhung khong co van de khoa hoc nghiem trong |
| `Inference-hypothesis` | Suy luan tu evidence co san, chua kiem chung doc lap | Co co so nhung chua co confirmation |
| `Proposal` | De xuat chua duoc User approve | User chua xac nhan |
| `User decision` | User da quyet dinh | User da xac nhan ro rang |
| `Exploratory result` | Ket qua tu thu nghiem, chua co validation nghiem ngat | Output ton tai nhung chua qua validation process |
| `Validated result` | Da qua validation du co so | Co validation source va ket qua khong mau thuan |
| `Unknown / insufficient source` | Khong tim duoc source phu hop hoac source khong du coverage | Mac dinh khi khong ro |

Chuyen classification phai co ly do ro.

---

## 8. Credit and integrity check

Knowledge Agency phai kiem tra:

| Muc | Cau hoi can tra loi |
| --- | --- |
| **Attribution** | Cong thuc, phuong phap, y tuong co duoc ghi credit dung nguon goc khong? |
| **Plagiarism risk** | Co cau, doan, hinh, phuong phap, cau truc lap luan lay tu nguon khac ma khong ghi ro khong? |
| **Data integrity** | Du lieu co bi chon loc, loai bo hoac xu ly theo cach co the gay bias ma khong khai bao khong? |
| **Conflict of interest** | Co loi ich xung dot nao anh huong cach trinh bay ket qua khong? |

Neu co van de ve credit hoac integrity, phai flag trong report va route sang `GATE-SCIENTIFIC-CRITIQUE`.

---

## 9. Research question anchor

Theo `REF-DEC-026`, moi claim khoa hoc quan trong nen neo vao cau hoi nghien cuu ro.

Khi kiem tra Evidence Report, Knowledge Agency nen hoi:

1. Claim nay lien quan den cau hoi nghien cuu nao?
2. Evidence co tra loi truc tiep cau hoi do khong?
3. Evidence co du de dua ra ket luan o muc claim hien tai khong?
4. Neu cau hoi nghien cuu chua ro, claim phai ha xuong `Inference-hypothesis` hoac `Proposal`.

Theo `REF-DEC-028`, co so khoa hoc cua mot claim phai gom:

* evidence;
* method;
* data / provenance;
* theory / mechanism hoac rationale;
* checkability;
* proportionate conclusion.

---

## 10. Fail-closed rule

Neu khong xac dinh duoc source phu hop cho mot claim quan trong:

```text
Can task proceed on current evidence: No
Need Scientific Critique: Yes
```

Khong duoc nang claim len `Source-backed` neu chua co primary hoac secondary source du manh.

Nguon: `CONSTITUTION.md`, `REF-DEC-026`, `REF-DEC-028`.

---

## 11. Quan he voi cac schema va file khac

| File | Quan he |
| --- | --- |
| `SCIENTIFIC_CRITIC.md` | Scientific Critic dung Evidence Report de danh gia claim |
| `DECISION_RECORD_SCHEMA.md` | Decision co the tham chieu Evidence Report |
| `OPERATING_CONTRACT_SCHEMA.md` | Contract co the yeu cau Evidence check truoc action |
| `governance/DECISION_RECORDS.md` | Decision trace co the tham chieu Evidence Report |
| `CONSTITUTION.md` | Evidence Classification bat buoc khi ghi claim khoa hoc |
