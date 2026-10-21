# MIGRATION_NOTES.md

Version: `v0.1-draft`

Status: `draft`

Activation: `inactive`

---

## 1. Muc dich

File nay ghi chu migration advisory giua v1 va v2.

Day khong phai migration plan that.

---

## 2. Co the giu

* Memo la operational cache, khong phai canonical source.
* Operating Contract cho task lon.
* Conflict report cho xung dot.
* Scientific caution trong response.
* Task routing theo nguon va scope.

---

## 3. Nen tranh

* Mang nguyen full governance flow sang task hoi-dap nho.
* Dung v1 lam precedent cho moi boundary cua v2.
* Cho memo override source canonical.
* De Coordinator thay User quyet dinh cuoi.
* Tron scientific critique voi operational inspection.

---

## 4. Co the mang sang nhung can canh bao

| Chu de | Co the mang sang | Can canh bao |
| --- | --- | --- |
| Routing | co | phai co FAST/GUIDED/FULL |
| Contract | co | phai gon cho task nho |
| Conflict handling | co | khong duoc lam cham task nho qua muc |
| Memo | co | khong duoc thanh source |
| Risk handling | co | phai fail-closed khi mo ho |

---

## 5. Migration posture

Hien tai posture phu hop nhat la:

```text
parallel reference, independent operation
```

Nghia la:

* v1 van la reference lich su;
* v2 van self-contained;
* khong co soi day bat buoc v2 phai phu thuoc v1 de chay;
* neu sau nay can migration that, phai co sprint rieng.

---

## 6. Note for later phases

Neu sau nay User muon chon cach dong bo mot phan v1 sang v2, nen chia thanh:

1. luat co the reuse;
2. luat nen viet lai;
3. luat chi nen tham khao.

Khong nen migrate theo kieu copy-paste.

## 7. Migration note

The migration posture is now:

```text
v2-default entry, v1 legacy archive
```

Use this file only as advisory compatibility guidance. The active runtime entry is `agent_hub/federation_v2/`.

## 8. Compatibility boundary

Compatibility review chi ghi nhan:

* cai gi co the reuse;
* cai gi phai rewrite;
* cai gi nen tranh.

Noi dung nay khong phai migration plan, khong phai instruction de doi tung file v1 sang v2, va khong tao dependency moi giua hai dong.
