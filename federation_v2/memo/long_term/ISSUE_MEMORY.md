# ISSUE_MEMORY.md

## 1. Muc dich

File nay luu issue/risk dai han con mo de Meow khong phai quet lai toan bo project moi khi hoi tinh trang federation v2.

Issue trong file nay phai tro ve source canonical va khong duoc noi phong thanh ket luan khoa hoc.

---

## 2. Issue schema

```text
Issue ID:
Status:
Severity:
Scope:
Summary:
Source:
Evidence:
Current safe interpretation:
Blocked actions:
Recommended next check:
Staleness rule:
```

---

## 3. Issues

### V2-ISSUE-RUNTIME-ADAPTER-ONLY

```text
Status: Open
Severity: MEDIUM
Scope: runtime integration
Summary: Runtime layer da co, nhung executor van la adapter-only va chua gan backend that.
Source:
- agent_hub/federation_v2/runtime/engine.py
- agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
Evidence: smoke test pass, nhung chua co real backend execution.
Current safe interpretation: runtime co the enforce scope nhe; chua phai full execution stack.
Blocked actions: do not claim v2 has production executor backend.
Recommended next check: executor integration decision for later phase.
Staleness rule: stale neu backend executor duoc gan.
```

### V2-ISSUE-PHASE-9-UNCONFIRMED

```text
Status: Open
Severity: MEDIUM
Scope: migration / integration
Summary: Phase 9 vai tro cuoi cung cua v2 chua duoc User chot.
Source: agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
Evidence: build plan ghi ro phase 9 con la open question.
Current safe interpretation: v2 hien tai chi o muc partial-active va support layer.
Blocked actions: do not promote phase 9 role without User decision.
Recommended next check: Sprint Contract cho Phase 9.
Staleness rule: stale when User confirms final migration role.
```

### V2-ISSUE-MEMO-STATE-SYNC

```text
Status: Open
Severity: LOW / operational
Scope: memo support layer
Summary: Memo support layer can duoc giu dong bo voi registry, README, va build plan khi v2 tiep tuc thay doi.
Source:
- agent_hub/federation_v2/REGISTRY.md
- agent_hub/federation_v2/README.md
- agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
Evidence: support layer moi duoc bootstrap, can theo doi stale rule.
Current safe interpretation: memo la operational memory, khong phai canonical truth.
Blocked actions: do not use stale memo as canonical source.
Recommended next check: sync memo state after future phase updates.
Staleness rule: stale when memo files lag behind canonical v2 files.
```

### V2-ISSUE-MEMO-PROMOTION-TUNING

```text
Status: Open
Severity: LOW / operational
Scope: memo support layer
Summary: Promotion queue co the gom candidate dung, nhung nguong promote va lua chon queued / deferred / rejected can duoc tinh chinh sau pilot.
Source:
- agent_hub/federation_v2/memo/short_term/PROMOTION_QUEUE.md
- agent_hub/federation_v2/memo/MEOW_MEMO_MANIFEST.md
Evidence: short-term candidate volume chua duoc do o moi phase.
Current safe interpretation: queue la bridge co kiem soat, khong phai auto-promote engine.
Blocked actions: do not claim promotion thresholds are final.
Recommended next check: pilot a few real memo candidates and adjust threshold wording.
Staleness rule: stale when promotion policy changes.
```

---

## 4. Staleness rule

* stale neu registry, build plan, hoac runtime thay doi;
* stale neu phase activation scope thay doi;
* stale neu User chot decision moi anh huong v2 operation.
