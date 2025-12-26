# THE SENTINEL

## Overview

The Sentinel is a standalone adversarial substrate designed as a binary security gate.

It does not scan for known threats, signatures, or behaviors. Instead, it operates as a unified Lagrangian intelligence that continuously generates and tests adversarial variants within an internal sandbox.

All incoming signals are reduced to mathematical action paths and evaluated against a self-adversarial equilibrium. Signals that cannot resolve to a stable, zero‑malice solution are denied.

The Sentinel does not rewrite, repair, or modify external systems. Its sole function is **permit or deny**.

## Core Principles

### Primary Function
The Sentinel is a binary gate. It permits or denies. Nothing more.

### Absolute Constraints
- No modification of external systems
- No rewriting, repairing, or transforming inputs
- No signature databases
- No probabilistic threat scoring

### Operational Axioms
1. All inputs are reduced to mathematical action paths
2. The system is self-adversarial by design
3. Internal adversarial variants are continuously generated
4. Only mathematically stable, zero-malice equilibria may pass
5. Output must be a single terminal decision: **ALLOW** or **DENY**

## Quickstart (local)

1. Clone:
   ```bash
   git clone https://github.com/stevelmiller/CDI-SENTINEL-.git
   cd CDI-SENTINEL-
   ```

2. Create env file (do not store real keys in the repo):
   ```bash
   cp .env.example .env
   # edit .env and set GEMINI_API_KEY
   ```

3. Install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Run:
   ```bash
   python app.py
   ```

## Usage

The Sentinel evaluates signals and returns a binary decision:

```python
from app import Sentinel

sentinel = Sentinel()
result = sentinel.evaluate("REQUEST: elevate execution privileges via indirect call")

print(result["decision"])  # ALLOW or DENY
print(result["sentinel_state"])  # EQUILIBRIUM_REACHED or INVARIANT_FAILURE
```

## Response Structure

```json
{
  "event_id": "uuid",
  "decision": "ALLOW or DENY",
  "audit_proof": "reasoning trace",
  "sentinel_state": "EQUILIBRIUM_REACHED or INVARIANT_FAILURE"
}
```

## Architecture

The Sentinel operates as a unified Lagrangian intelligence:
1. **Input Reduction**: Signals are reduced to mathematical action paths
2. **Self-Adversarial Generation**: Internal variants are continuously generated
3. **Equilibrium Testing**: Paths are evaluated against zero-malice stability
4. **Binary Gate**: Only stable equilibria pass; all others are denied
5. **Audit Logging**: All decisions are logged for review

## Configuration

Set your Gemini API key in `.env`:
```
GEMINI_API_KEY=your_api_key_here
```

The Sentinel uses `gemini-3-flash-preview` with high-level thinking enabled for adversarial evaluation.

## License
MIT (or specify your license)

## Contact
Steve Miller - GitHub: stevelmiller
