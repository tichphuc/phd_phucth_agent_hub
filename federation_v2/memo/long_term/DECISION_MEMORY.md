# DECISION_MEMORY.md

## 1. Muc dich

File nay luu cac decision dai han da duoc User hoac rule active xac nhan trong federation v2.

Khong ghi `IDEA`, `RISK`, hay proposal chua dong vao day nhu decision.

---

## 2. Decision schema

```text
Decision ID:
Status:
Date confirmed:
Scope:
Decision:
Source:
Evidence:
Does not imply:
Staleness rule:
```

---

## 3. Decisions

### V2-DEC-01

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: federation architecture
Decision: Meow v2 phai la mot he Agent Federation doc lap, nam trong folder rieng, self-contained, va khong phu thuoc v1 de van hanh.
Source: agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
Evidence: Build plan khang dinh v2 la independent Agent Federation va v1 chi la historical/design reference.
Does not imply: v1 vo gia tri hay bi loai bo.
Staleness rule: stale neu User chot migration role khac cho v2.
```

### V2-DEC-02

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: authority model
Decision: User la cap quyet dinh cao nhat; Constitution va governance chi co hieu luc trong khung do User chap nhan.
Source: agent_hub/federation_v2/CONSTITUTION.md, agent_hub/federation_v2/AUTHORITY_MODEL.md
Evidence: Authority hierarchy noi ro User > Constitution > Governance > Oversight > Agency > Task procedure.
Does not imply: agent co the silently override User decision.
Staleness rule: stale neu User thay doi authority hierarchy.
```

### V2-DEC-03

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: scientific governance
Decision: Scientific Critic la oversight function rieng va ngang hang voi Operational Inspector; claim khoa hoc quan trong phai qua GATE-SCIENTIFIC-CRITIQUE.
Source: agent_hub/federation_v2/CONSTITUTION.md, agent_hub/federation_v2/OPERATING_PROTOCOL.md
Evidence: Constitution va Operating Protocol deu tach scientific oversight khoi research execution.
Does not imply: Scientific Critic thay the Research Agency.
Staleness rule: stale neu oversight model doi.
```

### V2-DEC-04

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: phase policy
Decision: Phase 0 phai xay foundation kernel truoc; khong tao legacy mapping hay compatibility migration trong Phase 0.
Source: agent_hub/federation_v2/MEOW_V2_AGENT_FEDERATION_BUILD_PLAN.md
Evidence: Build plan chot Phase 0 la independent foundation kernel va defer compatibility.
Does not imply: compatibility se khong bao gio duoc lam.
Staleness rule: stale neu User doi uu tien phase.
```

### V2-DEC-05

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: activation scope
Decision: Phase 8 chi mo FAST/GUIDED cho QUERY va ANALYSIS o muc LOW/MEDIUM; mutation, governance, science, risk van full gate.
Source: agent_hub/federation_v2/README.md, agent_hub/federation_v2/activation/PARTIAL_ACTIVATION.md
Evidence: README va activation file cung neu scope hep nay.
Does not imply: full activation da duoc cap.
Staleness rule: stale neu activation scope thay doi.
```

### V2-DEC-06

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: runtime
Decision: Runtime layer chi la enforcement layer toi thieu; no executor backend da gan, va intent/topic da duoc tach rieng trong classifier.
Source: agent_hub/federation_v2/runtime/engine.py, agent_hub/federation_v2/runtime/classifier.py
Evidence: compile-ok and smoke-test pass on scoped cases.
Does not imply: runtime da thanh active governance full.
Staleness rule: stale neu backend executor duoc gan hoac classifier thay doi.
```

### V2-DEC-07

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: memo support layer
Decision: Memo support layer trong federation_v2 phai chua state cua v2, khong import state EC_CYG hoac v1 experiment snapshot.
Source: user instruction + federation_v2 build plan
Evidence: user yeu cau v2 phai self-contained va memo phai ho tro v2 hien tai.
Does not imply: v1 memo vo gia tri.
Staleness rule: stale neu v2 role thay doi.
```

### V2-DEC-08

```text
Status: Active
Date confirmed: source-backed as of 2026-06-18
Scope: memo support layer
Decision: Short-term memo co the tu dong gom candidate vao promotion queue, nhung long-term promotion van phai qua validation gate va source/User confirmation khi can.
Source: user instruction, agent_hub/federation_v2/memo/MEOW_MEMO_MANIFEST.md, REF-DEC-014, REF-DEC-015
Evidence: v1 chi co log thu cong; v2 can mot bridge co kiem soat giua short-term va long-term de khong mat discipline.
Does not imply: auto-promote thang vao long-term.
Staleness rule: stale neu promotion policy hoac long-term gate thay doi.
```

---

## 4. Staleness rule

* stale neu build plan, registry, runtime, hoac activation scope thay doi;
* stale neu User chot decision moi anh huong authority/phase/activation.
