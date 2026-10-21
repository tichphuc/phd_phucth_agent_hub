# TASK_CONTEXT.md

## 1. Muc dich

File nay luu context ngan han cua task dang mo.

---

## 2. Active task

```text
Task: complete memo support layer for federation_v2 with short-term to long-term promotion bridge
User requirement: keep v2 self-contained, keep references advisory only, and complete memo sync
Current implementation scope: memo support layer bootstrap + promotion queue + v2 registry/read order sync
```

---

## 3. Design basis

```text
Layer 1: Long-Term MEMO
Layer 2: Short-Term MEMO
Layer 3: Log MEMO
Bridge: Short-Term candidate queue before long-term promotion
Lifecycle: INGEST -> EXTRACT -> UPDATE -> VALIDATE -> RETRIEVE -> INVALIDATE
Update operations: ADD / UPDATE / DELETE / NOOP
```

---

## 4. Pending decisions

```text
PENDING-01: sync memo support layer with v2 registry and read order
PENDING-02: decide whether future phase should extend memo automation or keep it advisory
PENDING-03: keep v2 memo state independent from root v1 EC_CYG state
PENDING-04: define promotion thresholds for queue -> long-term commit
```
