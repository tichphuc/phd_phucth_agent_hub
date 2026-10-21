# MEOW_V1_COMPARISON.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive`

---

## 1. Muc dich

File nay so sanh Meow v1 va Meow v2 o muc kien truc va van hanh.

Muc tieu:

* thay ro cai gi v2 giu lai;
* thay ro cai gi v2 bo bot;
* khong nham lan v2 voi v1;
* khong ket luan migration khi chua co User decision.

---

## 2. Toc do so sanh

| Truc so sanh | Meow v1 | Meow v2 | Nhan xet |
| --- | --- | --- | --- |
| Kien truc | agent don / workflow coordinator | agent federation | v2 tach vai ro hon |
| Dieu phoi | mot agent trung tam + memo routing | Coordinator + governance + oversight + agencies | v2 ro phan quyen hon |
| Gate | co contract va conflict co ban | full gates, inspector, scientific critique | v2 tach kiem tra ro hon va chat hon |
| Task nho | thuan tien, nhieu luc lam nhanh | co FAST/GUIDED/FULL | v2 giam phan thu tuc cho task nho |
| Mutation | de xuong task flow cu | bat buoc qua contract/gate | v2 an toan hon |
| Scientific claim | co can trong, nhung chua tach oversight doc lap ro | Scientific Critic rieng | v2 manh hon ve scientific boundary |
| Memory | memo module la routing/cache | memo tach voi reference va governance | v2 co trace ro hon |
| Reference handling | tham chieu thiet ke | reference track + audit + decision review | v2 co kieu soat nguon ro hon |
| Risk handling | co conflict detection | fail-closed, inspector, tool safety | v2 chat hon |

## 2.1. Reuse / Rewrite / Avoid

| Nhom | Noi dung | Hanh dong |
| --- | --- | --- |
| `reuse` | Operating Contract, Conflict Report, memo lifecycle y tuong, task routing co y thuc scope | Gi? lai y tuong, viet lai theo v2 self-contained |
| `rewrite` | scientific critique, inspector boundary, handoff protocol, registry/status, source handling | Viet lai theo federation v2 va advisory posture |
| `avoid` | mot luong full-gate cho task nho, memo thay source canonical, Coordinator thay User, khoa hoc va van hanh gom chung | Khong mang nguyen sang v2 |

---

## 3. Diem v2 giu lai tu v1

* Operating Contract cho task khong don gian.
* Conflict report khi co xung dot rule.
* Priority routing co y thuc ro rang.
* Memo dung cho routing va recall, khong thay canonical source.
* Cach biet proposal va decision.

---

## 4. Diem v2 nen giu cach khac v1

* Tach Operational Inspector ra khoi Coordinator.
* Tach Scientific Critic ra khoi Research Agency.
* Khong bat task nho phai di qua full governance.
* Khong de Coordinator ngan ngam thay cho User decision.
* Khong tron memo voi source canonical.

---

## 5. Diem v2 khong nen mang nguyen

* Routing qua nhieu thu tuc cho task hoi-dap nho.
* Memo duoc dung nhu bo nho thay cho source canonical.
* Mot agent om qua nhieu vai tro.
* Task khoa hoc khong co lop phan bien rieng.
* Tham chieu phien ban cu de giai thich phien ban moi.

---

## 6. Ket luan

Meow v2 khong phai ban sao cua v1.

v1 cho v2 mot so mau dung:

* tinh can trong;
* phan tich rule;
* conflict awareness;
* memo awareness.

Nhung v2 da di xa hon:

* federation thay cho coordinator don;
* oversight doc lap;
* task classification nhe/nang;
* reference audit;
* scientific critique rieng.

---

## 7. Reuse guidance

Co the reuse:

* cach route task va gate;
* memo lifecycle y tuong;
* contract style;
* conflict style.

Khong nen reuse nguyen:

* mot luong duy nhat cho tat ca task;
* nghi thang task nho cung phai qua full gate;
* khoa hoc va van hanh gom chung mot lop dieu phoi.

## 8. Migration note

Migration has moved from advisory comparison to default-entry migration.

Current posture:

```text
Meow defaults to v2; v1 is archived in agent_hub/version/v1/.
```

This file remains useful for comparing design choices and legacy behavior, but it should not be read as the active runtime entry.
