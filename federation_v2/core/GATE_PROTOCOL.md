# GATE_PROTOCOL.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive-by-default`

---

## 1. Muc dich

File nay mo ta gate protocol cho Coordinator.

Gate protocol quyet dinh khi nao dung, khi nao route tiep, khi nao hoi User, va khi nao escalate.

---

## 2. Gate sequence

Mac dinh:

```text
read -> classify -> route -> inspect/critique -> synthesize -> stop or ask User
```

Coordinator khong duoc nhay thang sang action neu gate chua qua.

---

## 3. Gate hierarchy

Uu tien xu ly:

1. `GATE-SCOPE`
2. `GATE-READ`
3. `GATE-REFERENCE`
4. `GATE-EVIDENCE`
5. `GATE-SCIENTIFIC-CRITIQUE`
6. `GATE-INSPECTION`
7. `GATE-PLAN`
8. `GATE-USER-CONFIRMATION`
9. `GATE-REVIEW`

Neu nhieu gate cung xuat hien, phai xu ly gate chat hon truoc.

---

## 4. When to stop

Coordinator phai dung neu:

* scope khong ro;
* permission khong ro;
* source canonical khong ro;
* task yeu cau mutation nhung chua co approval;
* claim khoa hoc chua du evidence;
* route tao conflict authority hoac rule;
* body lien quan tra ve `No` hoac `Revise`.

---

## 5. When to ask User

Coordinator phai hoi User khi:

* co quyet dinh anh huong scope hoac activation;
* co conflict khong the resolve bang file hien co;
* can mutation moi;
* can doi scientific assumption, baseline, hoac claim;
* can mo rong phase / module ngoai plan hien tai.

---

## 6. When to escalate

Coordinator phai escalate khi:

* `Operational Inspector` tra ve `Can proceed: No`;
* `Scientific Critic` tra ve `Can claim proceed: No` hoac `Revise`;
* `Conflict Court` bao conflict phai hoi User;
* task co dual-route nhung hai body cho ket luan khong tuong thich.

---

## 7. Required output

Moi gate decision nen duoc ghi lai duoi dang:

```text
GATE DECISION

Task:
Gate checked:
Route:
Result:
Reason:
Next action:
Need User decision:
```
