# ROUTING_MEMORY.md

## 1. Muc dich

File nay la routing memory on dinh cho Meow v2.

No giup Meow chon file nao can doc truoc theo tung loai task, nhung khong thay the canonical read rule trong governance hoac reference track.

---

## 2. Routing table

| Task type | First memory file | Canonical files still required | Notes |
| --------- | ----------------- | ------------------------------ | ----- |
| Project status | `PROJECT_STATE.md` | `REGISTRY.md`, `MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md`, relevant canonical files | Memo chi dung de dinh huong nhanh |
| Current session | `short_term/SESSION_STATE.md` | User prompt hien tai | Short-term co the stale |
| Current working set | `short_term/WORKING_SET.md` | file canonical lien quan | Dung de giu file scope nho |
| Decision-sensitive task | `DECISION_MEMORY.md` | `CONSTITUTION.md`, `AUTHORITY_MODEL.md`, `REGISTRY.md` | Khong tu quyet decision |
| Open issue / risk | `ISSUE_MEMORY.md` | canonical source, report, runtime or registry | Khong goi issue la validated result |
| Memo update | `MEOW_MEMO_MANIFEST.md` | `MEMO_UPDATE_SCHEMA.md` neu can format chi tiet | Phai phan biet long/short/log |
| Governance change | `MEOW_MEMO_MANIFEST.md` | `RULE_GOVERNANCE.md`, `RULE_REGISTRY.md`, `OPERATING_PROTOCOL.md` | Can conflict check |

---

## 3. Fast startup route for Meow v2

```text
Always read first for non-simple federation_v2 tasks:
1. AGENTS.md
2. agent_hub/MEOW_AGENT.md
3. agent_hub/federation_v2/FEDERATION_MANIFEST.md
4. agent_hub/federation_v2/FEDERATION_MANIFEST.md
5. agent_hub/federation_v2/REGISTRY.md

Then read federation_v2 memo quick layer if task touches status/context/memory:
6. agent_hub/federation_v2/memo/MEOW_MEMO_MANIFEST.md
7. agent_hub/federation_v2/memo/long_term/ROUTING_MEMORY.md
8. agent_hub/federation_v2/memo/long_term/PROJECT_STATE.md
9. agent_hub/federation_v2/memo/short_term/SESSION_STATE.md neu task noi tiep phien truoc
10. agent_hub/federation_v2/memo/short_term/WORKING_SET.md neu can xem scope doc hien tai
```

Memo quick layer co the giam repo-wide scanning, nhung khong the thay the canonical reads khi task cham governance, reference, runtime, phase activation, khoa hoc, hay mutation.

---

## 4. Promotion queue bridge

Khi task lien quan toi viec nang cap memory tu short-term len long-term:

```text
1. Doc short_term/PROMOTION_QUEUE.md truoc.
2. Xac dinh candidate can promote hay chi can giu o short-term.
3. Neu can promote, validate source canonical va user confirmation gate.
4. Tao Memo Update cho long-term target.
5. Append log entry va danh stale short-term item neu can.
```

Khong dung promotion queue nhu canonical source. No chi la bo dem trung gian.

---

## 5. Memo-update route

Khi cap nhat memo:

```text
1. Xac dinh target layer:
   - long_term cho state/decision/issue/routing ben
   - short_term cho current task/session
   - log cho append-only event trace

2. Phan loai operation:
   ADD / UPDATE / DELETE / NOOP

3. Validate source:
   - source canonical required cho long_term
   - user prompt/session source du cho short_term
   - action trace du cho log

4. Apply update.

5. Append log entry.

6. Bao conflict/progress neu source mismatch.
```

---

## 6. Staleness rule

Routing memory phai duoc kiem tra lai neu:

* startup flow trong `FEDERATION_MANIFEST.md` doi;
* `REGISTRY.md` doi;
* runtime scope doi;
* memo support layer duoc nang cap;
* project phase boundary thay doi.




