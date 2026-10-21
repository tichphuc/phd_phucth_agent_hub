# STATUS_MATRIX.md

Version: `v0.1-draft`

Status: `advisory`

Activation: `scoped-by-user`

---

## 1. Muc dich

File nay la mot ban snapshot ngan gon ve trang thai hien tai cua Meow v2.

Muc tieu:

* nhin nhanh phase nao da xong, phase nao con draft;
* biet khoi nao dang active han che, khoi nao chi advisory;
* tranh nham lan giua completed, draft va partial-active;
* khong thay the REGISTRY.md.

---

## 2. Phase matrix

| Phase | Trang thai | Activation | Ghi chu |
| --- | --- | --- | --- |
| Phase 0 - Foundation Kernel | `active` | `scoped-by-user` | co core kernel doc, dung lam default entry |
| Phase 1 - Governance / Oversight | `draft` | `inactive` | da harden, cho review |
| Phase 2 - Core Coordinator | `draft` | `inactive` | da co coordinator, routing va gate protocol |
| Phase 3 - Schema Layer | `draft` | `inactive` | da co bo schema output/report |
| Phase 4 - Functional Agencies | `draft` | `inactive` | 7 agency da harden, cho review |
| Phase 5 - Reference Consolidation | `draft` | `inactive` | co audit/review artifacts, chua khoa tria trang thai thanh completed |
| Phase 6 - Dry-run Pilots | `completed` | `dry-run-only` | 5 scenario da chay xong, khong mutate file that |
| Phase 7 - Compatibility Review | `completed` | `advisory` | chi so sanh/advisory, khong phai migration plan |
| Phase 8 - Partial Activation | `partial-active` | `scoped-by-user` | chi QUERY/ANALYSIS muc FAST/GUIDED |

---

## 3. Support matrix

| Khoi | Trang thai | Activation | Ghi chu |
| --- | --- | --- | --- |
| `memo/` | `advisory` | `scoped` | operational memory, khong phai canonical source |
| `agencies/librarian/` | `draft` | `inactive` | source access broker cho Zotero, NotebookLM, va filesystem paths |
| `references/` | `reference-only` | `inactive` | support track, khong phai active rule |
| `compatibility/` | `completed` | `advisory` | chi la doi chieu giua v1 va v2 |
| `runtime/` | `partial-active` | `scoped` | enforcement layer toi thieu, adapter-only |
| `experiments/` | `active` | `scoped` | overlay experiment hosted inside v2 |
| `activation/PARTIAL_ACTIVATION.md` | `partial-active` | `scoped-by-user` | scope kich hoat han che cho Phase 8 |

---

## 4. Readiness notes

### 4.1. Da san sang

* foundation kernel da co va da active;
* pilot da xong;
* compatibility da xong o muc advisory;
* runtime da co enforcement toi thieu;
* memo support layer da bootstrap.
* Librarian da co charter toi thieu de quan ly source access.

### 4.2. Con draft

* Phase 1 governance / oversight;
* Phase 2 coordinator;
* Phase 3 schema layer;
* Phase 4 functional agencies;
* Phase 5 reference consolidation.

### 4.3. Broader activation status

Meow v2 co the phuc vu task hep trong scope da duoc duyet.

Noi khong the hieu nhu active governance toan phan cho den khi:

* Phase 5 duoc khoa tron hon;
* User chot scope activation ro rang;
* khong con mismatch lon giua status file va registry.

---

## 5. Reading rule

File nay chi dung de nhin nhanh trang thai.

Neu can noi ro file nao canonical, file nao active, hay file nao gate task, phai doc:

```text
README.md
VERSIONING_POLICY.md
OPERATING_PROTOCOL.md
REGISTRY.md
```
