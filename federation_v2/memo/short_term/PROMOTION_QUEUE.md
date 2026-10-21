# PROMOTION_QUEUE.md

## 1. Muc dich

File nay giu danh sach candidate short-term co the duoc nang len long-term memory.

Day khong phai la canonical memory, khong phai decision record, va khong phai log trace.
No chi la hang doi trung gian de gom, loc, va trinh xin promote.

---

## 2. Khi nao dua vao queue

Mot item co the vao queue neu:

* xuat hien lap lai nhieu lan trong short-term;
* da on dinh qua nhieu session/task;
* co source/evidence ro rang;
* duoc User xac nhan;
* la routing/state/issue/decision candidate can nang len long-term.

Khong dua vao queue neu:

* chi la suy doan tam thoi;
* con exploratory;
* chua co source hoac evidence;
* mau thuan voi source canonical;
* chua ro co can ton tai o long-term hay khong.

---

## 3. Candidate schema

```text
Candidate ID:
Origin:
Trigger:
Status:
Layer origin:
Short-term item:
Evidence:
Proposed long-term target:
Required gate:
Staleness check:
Next action:
```

Status values:

* `queued`
* `validated`
* `promoted`
* `deferred`
* `rejected`

---

## 4. Promotion flow

```text
short-term item
  -> promotion queue candidate
  -> validate source / evidence
  -> check User confirmation if needed
  -> Memo Update for long-term ADD / UPDATE
  -> append log entry
  -> mark old short-term item stale or archived if needed
```

Nguyen tac:

* queue co the gom candidate tu dong;
* promote long-term khong duoc silent;
* long-term item van phai qua source canonical hoac User confirmation;
* queue khong duoc dung thay source canonical.

---

## 5. Minimal rules

* Queue chi la bo dem trung gian.
* Queue co the bi ghi de, rut lai, hoac xoa candidate neu stale.
* Moi candidate phai co ly do tai sao no dang duoc giu lai.
* Neu candidate khong con can thiet, danh `deferred` hoac `rejected`.
* Neu candidate du dieu kien, tao Memo Update va route sang long-term target.

