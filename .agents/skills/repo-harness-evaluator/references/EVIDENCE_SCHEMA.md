# Evidence Schema

The generated `audit.json` is the source of truth.

## Purpose

```json
{
  "profile": "mvp",
  "horizon_days": 28,
  "expected_lifetime": "3-6 months",
  "primary_optimization": ["pilot validation", "fast iteration"],
  "team_size": 5,
  "autonomy": "supervised",
  "failure_cost": "medium",
  "data_sensitivity": "internal",
  "reuse": "evolving product",
  "overlays": ["team_concurrency"],
  "targets": {},
  "assumptions": []
}
```

## Requirement status

- `verified`
- `partial`
- `unverified`
- `not_applicable`

## Evidence level

- `E4`
- `E3`
- `E2`
- `E1`
- `E0`

## Friction item

```json
{
  "id": "feedback_latency",
  "name": "Feedback latency",
  "weight": 4,
  "level": 2,
  "highest_evidence": "E4",
  "evidence": ["EV-014"],
  "justification": "Every tiny change blocks on a 24-minute suite."
}
```

## Purpose gate

```json
{
  "id": "critical_path",
  "name": "Critical user path works",
  "applicable": true,
  "passed": true,
  "max_fit_if_failed": 49,
  "evidence": ["EV-021"]
}
```
