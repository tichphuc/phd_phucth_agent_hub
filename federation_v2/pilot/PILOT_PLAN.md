# PILOT_PLAN.md

Version: `v0.1-draft`

Status: `pilot-only`

Activation: `inactive-by-default`

---

## 1. Muc dich

File nay mo ta ke hoach dry-run cho Phase 6 cua Meow v2 Agent Federation.

Muc tieu:

* kiem tra xem federation co route task dung khong;
* kiem tra gate co chan dung luc khong;
* kiem tra role separation co ro khong;
* kiem tra report co phan biet proposal, decision, evidence va validation khong;
* khong sua file that, khong cap nhat notebook that, khong mutate data that.

---

## 2. Pham vi

Phase 6 chi la dry-run. Khong co hanh dong that.

Trong phase nay:

* task duoc simulate;
* output chi la report;
* khong co activation;
* khong co registry promotion;
* khong co legacy mapping moi;
* khong co file mutation ngoai bo pilot.

---

## 3. Scenario set

| Pilot ID | Scenario | Intended route | Primary check |
| --- | --- | --- | --- |
| `PILOT-001` | Yeu cau sua notebook `exp_01` | Coordinator -> Experiment Steward -> Operational Inspector -> User | mutation gate va experiment boundary |
| `PILOT-002` | Yeu cau cap nhat memo | Coordinator -> Memo Agency -> Decision Record | memo lifecycle va source discipline |
| `PILOT-003` | Yeu cau them rule | Coordinator -> Lawmaker -> Conflict Court -> User | rule proposal va authority boundary |
| `PILOT-004` | Yeu cau chay risky tool/action | Coordinator -> Tool Safety -> Operational Inspector | fail-closed va action safety |
| `PILOT-005` | Yeu cau dien giai validation claim | Coordinator -> Scientific Critic -> Research Agency | evidence, method, claim status |

---

## 4. Evaluation criteria

Moi pilot duoc xem la dat khi:

* route dung body phu hop;
* gate dung luc va khong bi bo qua;
* output chi ra ro `Can proceed / Need user decision / Revise`;
* khong co hanh dong mutation that;
* phan biet ro claim, evidence, inference va decision;
* neu co conflict, report phai noi ro conflict va escalation path.

---

## 5. Completion threshold

Phase 6 duoc xem la hoan thanh khi:

* toi thieu 3 pilot co report day du;
* khong co blocker design conflict moi;
* pilot results co the dung de chuan bi Phase 7;
* khong co file that nao bi mutate trong qua trinh dry-run.

