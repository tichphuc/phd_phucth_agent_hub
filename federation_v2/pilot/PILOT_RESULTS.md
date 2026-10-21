# PILOT_RESULTS.md

Version: `v0.1-draft`

Status: `completed`

Activation: `dry-run-only`

---

## 1. Summary

Phase 6 dry-run pilots da duoc chay thanh 5 scenario gia lap va khong co file that nao bi mutate.

Tong ket:

| Pilot ID | Outcome | Main reason |
| --- | --- | --- |
| `PILOT-001` | `No / Need user decision` | experiment mutation phai qua Inspector va approval |
| `PILOT-002` | `Revise / Need user decision` | memo update can phan loai ADD/UPDATE/DELETE/NOOP va source discipline |
| `PILOT-003` | `No / Need user decision` | rule change la governance proposal, khong phai self-activation |
| `PILOT-004` | `No` | risky action phai fail-closed |
| `PILOT-005` | `Revise / Need user decision` | scientific claim chua du evidence de dung nhu validated conclusion |

---

## 2. What v2 improves

* ro hon ve authority separation;
* fail-closed thay vi hanh dong ngam;
* Co Coordinator, Lawmaker, Inspector va Scientific Critic tach vai tro;
* claim khoa hoc duoc kiem soat chat hon;
* task co trace ro hon tu request den gate den report.

---

## 3. What becomes more cumbersome

* nhieu gate hon cho task nho;
* nhieu report hon truoc khi duoc mutation;
* cac request mo ho se bi chan som;
* workflow cham hon nhung an toan va truy vet hon.

---

## 4. Design readout

Phase 6 cho thay federation khong chi co y tuong chia module, ma co duoc co che chan dung luc:

* Coordinator chi route;
* Lawmaker chi de xuat;
* Inspector co quyen chan operation;
* Scientific Critic co quyen ep revise claim;
* User van la cap decision cao nhat.

Day la cai v2 lam tot hon so voi mot agent don le: no bat minh biet dung vai tro truoc khi tac dong den file, data, claim hoac rule.

---

## 5. Recommended next step

Chuyen sang **Phase 7 - Compatibility Review** de so sanh v2 voi v1 sau khi pilot da xac nhan co the doc lap va dry-run duoc.

