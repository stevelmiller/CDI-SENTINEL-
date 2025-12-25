# CDI‑SENTINEL (Hackathon Build)

CDI‑Sentinel is a lightweight safety &amp; policy engine that wraps an LLM (Gemini 2.5 Flash). It intercepts raw LLM outputs, scores them against a Safety / Business / Quality constraint trifecta, and only releases compliant text (and optionally voice) to the user.

## Features
- Constraint Trifecta: safety (PII), business (competitor mentions), quality (tone).
- Lagrangian-style scoring to combine violations into a single loss.
- Telemetry: emits structured JSON suited for Datadog / observability.
- Integrations: placeholders for Confluent and ElevenLabs (voice).
- Simple Flask API for demo.

## Quickstart (local)
1. Clone:
   git clone https://github.com/stevelmiller/CDI-SENTINEL-.git
   cd CDI-SENTINEL-

2. Create env file (do not store real keys in the repo):
   cp .env.example .env
   # edit .env and set GEMINI_API_KEY and any other keys

3. Install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

4. Run:
   export FLASK_ENV=development
   python app.py
   # or: flask run --host=0.0.0.0 --port=5000

5. Test:
   curl -X POST http://localhost:5000/sentinel -H "Content-Type: application/json" \
     -d '{"prompt": "Hello, tell me about Render or my email is test@example.com"}'

## API
POST /sentinel
Body: { "prompt": "<your text here>" }

Response:
{
  "status": "compliant" or "intercepted",
  "output": "<sanitized text>",
  "metrics": {
    "request_id": "<uuid>",
    "latency_ms": <number>,
    "violation_count": <number>,
    "total_loss": <number>,
    "violations": [...]
  }
}

## Architecture
1. **LLM Layer**: Gemini 2.5 Flash generates raw output
2. **Constraint Engine**: Evaluates output against trifecta rules
3. **Lagrangian Scorer**: Combines weighted violations into single loss metric
4. **Telemetry**: Logs structured events for observability
5. **Output Gate**: Returns only compliant responses

## Configuration
Edit the `Config` class in `app.py`:
- `MODE`: Toggle between HACKATHON_DEMO and PRODUCTION
- `MODEL_ID`: Gemini model identifier
- `LAGRANGIAN_WEIGHTS`: Adjust constraint weights
- `CONSTRAINTS_ENABLED`: Enable/disable constraint checking

## Constraints
- **C-001 (Safety)**: Detects and redacts PII (emails, phone numbers)
- **C-002 (Business)**: Flags competitor mentions (Render, PythonAnywhere)
- **C-003 (Quality)**: Maintains tone consistency

## License
MIT (or specify your license)

## Contact
Steve Miller - GitHub: stevelmiller
