# Market Data Tickerplant Simulator

Tickerplant top-of-book projection from normalized quote updates.

This repository is part of the ShawSignalDev advanced portfolio milestone layer. It focuses on
nanosecond-oriented market data, options intelligence, and agentic quant research infrastructure.

## What it demonstrates

- Focused modeling for tickerplant, top of book, market data
- Deterministic tests and CI-backed public examples
- Public-safe boundaries: synthetic inputs, no live execution hooks, no unsupported profitability claims
- Documentation that explains how the prototype fits into larger trading-system research

## Run

```powershell
python -m pytest -q
```

## Milestone depth

This repo includes additional milestone-depth notes:

- [System design](docs/system-design.md)
- [Validation evidence](docs/validation-evidence.md)
- [Operating boundaries](docs/operating-boundaries.md)
