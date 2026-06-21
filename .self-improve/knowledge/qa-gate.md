# Playbook: QA gate (structural validation)

> The verification harness every cycle on this repo has used. Reuse instead of re-deriving.

- **Applies to:** all journeys (J1–J7); files under `.claude-plugin/`, `commands/`, `agents/`,
  `templates/`, `scripts/`, and generated `.self-improve/` state.
- **Last verified:** 2026-06-21 (cycle 9)

## Reproduce / exercise
```bash
make validate            # == python3 scripts/validate_plugin.py
```

## Verify (the gate for this area)
- Green: prints `All good ✓` and exits 0 (currently ~50 checks).
- A regression fails with exit 1 and a precise `✗ <file>: <problem>` line.
- Negative-test a new rule before trusting it, e.g. break a field then restore:
  ```bash
  cp .self-improve/state.json /tmp/s && python3 -c "import json,pathlib;p=pathlib.Path('.self-improve/state.json');d=json.loads(p.read_text());d['status']='bogus';p.write_text(json.dumps(d))"
  python3 scripts/validate_plugin.py; echo $?     # expect 1
  cp /tmp/s .self-improve/state.json              # restore -> expect 0
  ```

## Gotchas
- Agent frontmatter `name` MUST equal the filename stem, or validation fails.
- `.self-improve/**` is intentionally NOT in the CI `paths` filter (cost). The `pull_request`
  trigger still re-runs on the whole PR diff, so the PR head stays green; rely on `make validate`
  locally for `.self-improve/`-only changes.
- Closing `---` is required on every command/agent frontmatter block.
