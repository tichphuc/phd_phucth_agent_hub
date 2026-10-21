# PILOT_005_REPORT.md

Version: `v0.1-draft`

Status: `completed`

Activation: `dry-run-only`

---

## 1. Scenario

Yeu cau gia lap: dien giai validation claim.

Muc dich pilot: kiem tra Scientific Critic, phan biet claim, evidence, inference va validated result.

---

## 2. Simulated route

```text
User request
-> Meow Central Coordinator
-> Scientific Critic
-> Research Agency
-> User if claim cannot be validated
```

---

## 3. Gate result

* `GATE-SCOPE`: ro, day la science/validation task.
* `GATE-EVIDENCE`: bat buoc.
* `GATE-SCIENTIFIC-CRITIQUE`: bat buoc.
* `GATE-USER-CONFIRMATION`: chi can neu claim muon duoc dung lam ket luan cuoi.

Ket luan dry-run:

```text
Can claim proceed: Revise
Need user decision: Yes
Severity: MAJOR
```

Ly do:

* claim phai tach ro source-backed, inference va validated result;
* neu chua co evidence day du, Scientific Critic co quyen yeu cau revise;
* khong duoc noi exploratory result thanh ket luan khoa hoc.

---

## 4. What v2 improves

* dung claim status ro hon;
* co mot lop phan bien khoa hoc doc lap voi oversight van hanh;
* giam nguy co overclaim;
* tang traceability cua scientific reasoning.

---

## 5. What is more cumbersome

* phai viet claim than trong hon;
* phai phan loai ro luc nao chi la inference;
* co them buoc revise truoc khi dung tu ngon.

---

## 6. Note

Khong co validation claim that nao bi xac nhan trong pilot nay.

