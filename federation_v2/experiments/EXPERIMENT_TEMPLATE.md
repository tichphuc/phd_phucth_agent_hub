# EXPERIMENT_TEMPLATE.md

## 1. Purpose

Use this template to create a new experiment overlay inside:

```text
agent_hub/federation_v2/experiments/<experiment_id>/
```

The template keeps experiment-specific rules, context index, and registry
entries in v2 so the federation stays self-contained.

---

## 2. Minimum files

Each experiment should have at minimum:

```text
<EXPERIMENT_ID>_ACTIVE_RULES.md
<EXPERIMENT_ID>_CONTEXT_INDEX.md
```

If needed, add supporting notes in the experiment folder, but do not move
global governance into the experiment folder.

---

## 3. Registry fields

Add the experiment to `EXPERIMENT_REGISTRY.md` with:

* experiment ID;
* project path;
* agent-hub path;
* active rules path;
* context index path;
* status;
* notes.

Keep the registry descriptive, not prescriptive.

---

## 4. Active rules skeleton

```text
# <EXPERIMENT_ID>_ACTIVE_RULES.md

Purpose
Scope
Read order
Allowed actions
Forbidden actions
Scientific / operational rules
Escalation rules
Stop conditions
Status
```

---

## 5. Context index skeleton

```text
# <EXPERIMENT_ID>_CONTEXT_INDEX.md

Purpose
Mapping
Notebook inventory
Data inventory
Output inventory
Script/module inventory
Documentation and source mapping
Open issues
Active decisions
Suggested task routing
Stop conditions
Change log
```

---

## 6. Migration note

If an experiment has a legacy v1 overlay, keep the v1 copy in
`agent_hub/version/v1/` and point the active v2 registry to the v2 overlay.
