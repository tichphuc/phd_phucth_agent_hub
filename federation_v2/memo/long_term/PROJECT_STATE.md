# PROJECT_STATE.md

## 1. Muc dich

File nay luu trang thai ben cua Meow v2 federation.

Day la long-term memory, chi chua thong tin on dinh va co source tro nguoc.

---

## 2. Project snapshot

```text
Memory status: initialized from federation_v2 build state
Last verified: 2026-06-18
Source:
- agent_hub/federation_v2/README.md
- agent_hub/federation_v2/REGISTRY.md
- agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
- agent_hub/federation_v2/OPERATING_PROTOCOL.md
- agent_hub/federation_v2/FEDERATION_MANIFEST.md
- agent_hub/federation_v2/CONSTITUTION.md
- agent_hub/federation_v2/AUTHORITY_MODEL.md
- agent_hub/federation_v2/runtime/*
```

### Active project identity

```text
Project type: agent federation design repository
Default agent: Meow
Default mode: read -> analyze -> propose -> wait for confirmation
Primary governance layer: agent_hub/federation_v2/
Memo support layer: agent_hub/federation_v2/memo/
```

### Current federation state

```text
Current state:
- Phase 0 foundation kernel exists.
- Reference Track R0 exists.
- Phase 8 partial activation is scoped-by-user.
- Runtime layer exists, compiles, and smoke-tests.
- Intent and topic are separated in runtime classification.
- Executor remains adapter-only, not connected to a real backend.
```

### Current workstream

```text
Current workstream:
- sync federation_v2 memo support layer;
- keep v2 self-contained;
- do not depend on v1 for operation;
- prepare for later migration/integration decision.
```

### Safe interpretation

```text
- v2 is not full active governance for the whole project.
- v2 is operational only within the scoped partial activation path.
- memo support files are operational memory, not canonical truth.
- no validated scientific result is implied by v2 architecture files.
```

---

## 3. Staleness rule

File nay phai duoc xem la stale neu:

* `REGISTRY.md` thay doi;
* `MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md` thay doi;
* phase activation scope thay doi;
* runtime state thay doi;
* user xac nhan decision moi anh huong project state.
