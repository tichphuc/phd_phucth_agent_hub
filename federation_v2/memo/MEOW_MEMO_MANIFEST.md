# MEOW_MEMO_MANIFEST.md

Version: `v0.1-draft`

Status: `advisory`

Activation: `scoped`

---

## 1. Muc dich

`agent_hub/federation_v2/memo/` la lop bo nho van hanh cho Meow v2.

Lop nay giup Meow v2 khoi dong nhanh hon, giu project state co truy vet, va tra loi nhanh
cau hoi ve tinh trang hien tai ma khong phai que toan bo repo.

Memo khong thay the:

* `AGENTS.md`
* `agent_hub/MEOW_AGENT.md`
* governance files
* reference track
* agency charters
* source canonical trong `federation_v2/`

Memo chi la lop dinh huong va tom tat co nguon tro ve.

Language reminder:

* noi dung chung cua Meow v2 uu tien tieng Viet;
* thuat ngu English giu lai khi can do chinh xac;
* neu session da chuyen sang English mot phan, phai quay ve policy nay khi cap nhat memo / governance / oversight.

---

## 2. Co so thiet ke

Memo v2 giu lai khung co ban tu v1, nhung state ben trong phai la state cua v2.

Ba y tuong chinh:

1. Long-term memory can on dinh, co nguon, co invalidation.
2. Short-term memory phuc vu session/task hien tai, co the thay doi nhanh.
3. Log memory append-only de giu trace cua episode, audit, decision va thay doi.

Rut gon:

```text
Long-term  -> project state / decision / issue / routing
Short-term -> session / task context / working set
Log        -> append-only trace
```

Short-term co the dua candidate vao promotion queue truoc khi nang len long-term.
Queue nay la trung gian, khong phai canonical memory.

---

## 3. Cau truc

```text
agent_hub/federation_v2/memo/
├── MEOW_MEMO_MANIFEST.md
├── long_term/
│   ├── PROJECT_STATE.md
│   ├── DECISION_MEMORY.md
│   ├── ISSUE_MEMORY.md
│   └── ROUTING_MEMORY.md
├── short_term/
│   ├── SESSION_STATE.md
│   ├── TASK_CONTEXT.md
│   └── WORKING_SET.md
└── log/
    └── MEMO_LOG_2026.md
```

### 3.1. Promotion queue adjunct

`PROMOTION_QUEUE.md` la queue trung gian cho short-term item can nang len long-term.
No khong thay the `TASK_CONTEXT.md` hay `WORKING_SET.md`.

---

## 4. Ba tang memo

### 4.1. Long-Term MEMO

Vai tro:

* luu trang thai ben cua federation v2
* luu decision da xac nhan
* luu issue/risk con mo
* luu routing on dinh

Khong dung de luu:

* log tung phien
* suy doan tam thoi
* ket luan khoa hoc chua validated

### 4.2. Short-Term MEMO

Vai tro:

* luu trang thai phien/task hien tai
* luu operating contract dang mo
* luu file da doc
* luu pending decision

Short-term memory co the stale nhanh va phai duoc kiem tra truoc khi dung lai.

### 4.3. Log MEMO

Vai tro:

* append-only episode trace
* ghi request, action, file doc/sua/tao
* ghi conflict/progress report
* ghi decision duoc xac nhan

Khong rewrite log cu neu khong co yeu cau ro.

---

## 5. Lifecycle

Moi cap nhat memo nen di qua lifecycle:

```text
INGEST     -> ghi nhan su kien hoac audit moi
EXTRACT    -> rut ra candidate issue/decision/routing/state
QUEUE      -> dua candidate on dinh vao promotion queue
UPDATE     -> ADD / UPDATE / DELETE / NOOP
VALIDATE   -> doi chieu source canonical truoc khi nang len long-term
PROMOTE    -> chuyen candidate da validate sang long-term
RETRIEVE   -> doc dung tang memory theo task
INVALIDATE -> danh dau stale khi source canonical doi
```

---

## 6. Startup routing de xuat

Khi Meow v2 can khoi dong nhanh cho task lien quan status/context:

```text
1. AGENTS.md
2. agent_hub/MEOW_AGENT.md
3. agent_hub/federation_v2/FEDERATION_MANIFEST.md
4. agent_hub/federation_v2/FEDERATION_MANIFEST.md
5. agent_hub/federation_v2/REGISTRY.md
6. agent_hub/federation_v2/memo/MEOW_MEMO_MANIFEST.md
7. agent_hub/federation_v2/memo/long_term/ROUTING_MEMORY.md
8. agent_hub/federation_v2/memo/long_term/PROJECT_STATE.md
9. agent_hub/federation_v2/memo/short_term/SESSION_STATE.md neu task noi tiep phien truoc
10. agent_hub/federation_v2/memo/short_term/PROMOTION_QUEUE.md neu task lien quan nang cap item
```

Neu task lien quan experiment, reference, governance hoac scientific claim, van phai doc file canonical tuong ung trong federation v2.

---

## 7. An toan

* Memo khong duoc bien proposal thanh decision.
* Memo khong duoc bien exploratory result thanh validated result.
* Memo khong duoc override governance, constitution, agency hoac reference track.
* Moi long-term item phai co source hoac ghi ro `source: pending`.
* Neu memo mau thuan voi source canonical, source canonical thang va memo phai stale.
* Short-term co the gom candidate vao promotion queue, nhung long-term promotion phai qua validate va gate.

---

## 8. Trang thai

Phien ban: `v0.1-draft`

Trang thai: memo support layer da duoc bootstrap cho federation v2.

Cap nhat lan dau: `2026-06-18`




