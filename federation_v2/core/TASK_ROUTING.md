# TASK_ROUTING.md

Version: `v0.1-draft`

Status: `draft`

Activation: `scoped-by-user`

---

## 1. Muc dich

File nay mo ta cach Coordinator route task trong Meow v2.

Muc tieu la giu routing nhat quan, khong lam sai body, va khong bo qua gate.

---

## 2. Routing model

Moi task duoc chia thanh mot trong cac nhom:

* `INFO` - hoi thong tin, chi can doc / phan tich;
* `GOVERNANCE` - luat, authority, conflict, registry;
* `OVERSIGHT` - inspection hoac scientific critique;
* `AGENCY` - nhiem vu chuyen mon cua agency;
* `MUTATION` - tao / sua / xoa / di chuyen file hoac chay output;
* `SCIENCE` - claim, validation, method, evidence;
* `UNKNOWN` - chua du ro, phai hoi User.

---

## 3. Routing table

| Task class | Primary route | Secondary route | Notes |
| --- | --- | --- | --- |
| `QUERY + LOW` | `SELF-HANDLE` | `READ` | tra loi truc tiep sau khi doc dung nguon |
| `QUERY + MEDIUM` | `ROUTE` | `GUIDED` | doc them source / registry lien quan |
| `ANALYSIS + LOW` | `SELF-HANDLE` | `READ` | phan tich ngan, khong mutation |
| `ANALYSIS + MEDIUM` | `ROUTE` | `GUIDED` | can them boi canh hoac kiem tra nguon |
| `MUTATION / SCIENCE / GOVERNANCE / RISK` | `DUAL-ROUTE` hoac `ROUTE` | `FULL` | giu full governance path |
| `UNKNOWN` | `STOP` | `User` | hoi lai thay vi doan |

| Task type | Primary route | Secondary route | Notes |
| --- | --- | --- | --- |
| hoi Meow v2 la gi | `README.md`, `FEDERATION_MANIFEST.md` | `REGISTRY.md` | tra loi theo trang thai hien tai |
| hoi quyen han / authority | `AUTHORITY_MODEL.md` | `CONSTITUTION.md` | khong route sang agency |
| hoi luat nen | `CONSTITUTION.md` | `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | chi dung chuan cot loi |
| hoi workflow / gates | `OPERATING_PROTOCOL.md` | `FEDERATION_MANIFEST.md` | xac dinh gate bat buoc |
| hoi lawmaking | `governance/LAWMAKER_AGENT.md` | `references/DESIGN_DECISIONS_FROM_REFERENCES.md` | proposal only |
| hoi conflict resolution | `governance/CONFLICT_COURT.md` | `governance/DECISION_RECORDS.md` | can triage va trace |
| hoi operational inspection | `oversight/OPERATIONAL_INSPECTOR.md` | `OPERATING_PROTOCOL.md` | fail-closed, mutation safety |
| hoi scientific critique | `oversight/SCIENTIFIC_CRITIC.md` | `CONSTITUTION.md` | claim quality, evidence, method |
| hoi task routing chi tiet | `core/TASK_ROUTING.md` | `core/GATE_PROTOCOL.md` | routing decision path |
| hoi gate protocol | `core/GATE_PROTOCOL.md` | `OPERATING_PROTOCOL.md` | dung, di tiep, escalate |
| code / notebook / data / output | dung agency tuong ung | `OPERATING_PROTOCOL.md` | neu mutation thi them Inspector |
| scientific claim / validation | `oversight/SCIENTIFIC_CRITIC.md` | `OPERATING_PROTOCOL.md` | neu can mutation thi them Inspector |
| file mutation | `oversight/OPERATIONAL_INSPECTOR.md` | `OPERATING_PROTOCOL.md` | phai co User approval |
| unknown / ambiguous | `COORDINATION REPORT` | `User` | khong doan mo |

---

## 4.1. Soft scoring

Routing ben tren la rule-based va giu vai tro chinh.

Meow v2 co them hai soft score nhe:

* `task_risk_score` trong khoang `0..100`
* `scope_confidence` trong khoang `0.0..1.0`

Nguyen tac:

* score chi la `soft signal`, khong phai decision thay the rule;
* `task_risk_score` giup giai thich muc do rui ro;
* `scope_confidence` giup biet do chac cua routing;
* neu `scope_confidence` thap hoac task con phan van, Meow phai hoi User thay vi doan;
* hard rules van thang score: mutation, scientific claim, governance conflict, permission issue va unknown scope deu phai di gate cham hon.

## 4. Dual-route rules

Coordinator phai dung `DUAL-ROUTE` khi:

* task vua co mutation vua co scientific claim;
* task vua dut quyen van hanh vua dut claim khoa hoc;
* task can vua route chuyen mon vua kiem tra an toan.

Trong truong hop do:

* `Operational Inspector` xu ly phan permission / gate / action;
* `Scientific Critic` xu ly phan claim / evidence / method;
* Coordinator chi tong hop ket qua va hoi User neu con conflict.

---

## 5. Stop rules

Coordinator phai dung va hoi User khi:

* task type khong ro;
* canonical source khong ro;
* route doi quyen chua co;
* body duoc route tra ve conflict chua resolve;
* claim khoa hoc khong du co so de giu nguyen muc hien tai.

---

## 6. Route decision output

Moi routing decision nen ghi duoi dang:

```text
ROUTE DECISION

Task:
Task class:
Route:
Bodies involved:
Need Operating Contract:
Need User decision:
Reason:
Next action:
```
