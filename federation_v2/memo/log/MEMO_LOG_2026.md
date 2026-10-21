# MEMO_LOG_2026.md

## 2026-06-18 - V2-MEMO-0001 - Bootstrap federation_v2 memo support layer

```text
Task: copy v1 memo structure into federation_v2 and sync v2 status text
Scope: federation_v2/memo support layer only
Outcome: support layer created with long_term / short_term / log split
Notes:
- v2 memo state uses federation_v2 project state, not EC_CYG state from root v1 memo.
- registry and read-order sync are required so the layer is discoverable.
```

## 2026-06-18 - V2-MEMO-0002 - Add short-term to long-term promotion queue

```text
Task: add a controlled bridge from short-term memory to long-term memory
Scope: federation_v2/memo support layer only
Outcome: promotion queue file added and memo docs updated to route candidates through validate -> promote
Notes:
- short-term can gather recurring/stable candidates into a queue;
- long-term promotion still requires validation and the proper gate;
- queue is a bridge, not a canonical source.
```
