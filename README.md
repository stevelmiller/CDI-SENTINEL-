# CDI-SENTINEL (Axiom-Substrate)

CDI-Sentinel is a lightweight extension of **Cordelia**, a Lagrangian-style safety and policy engine that wraps Gemini 2.5 Flash. It intercepts raw LLM outputs, scores them against a **Safety / Business / Quality** constraint trifecta, and only then releases text (and optionally voice) to the user.

## Overview

This project demonstrates a constraint-based AI safety layer that:
- Intercepts LLM outputs before they reach users
- Applies configurable safety, business, and quality constraints
- Provides structured telemetry for monitoring and compliance
- Supports multi-modal outputs (text and voice)

## Architecture

### Core Components

1. **Orchestrator (`CDISentinel` class)**: The brain of the system that coordinates LLM calls and constraint checking
2. **Constraint Trifecta**: Three categories of constraints that can be adjusted without redeploying:
   - **Safety**: Hard constraints (e.g., no PII disclosure)
   - **Business**: Policy alignment (e.g., no competitor mentions)
   - **Quality**: UX nuance (e.g., tone consistency)
3. **Telemetry**: Structured JSON logging for Datadog LLM Observability
4. **Integration Points**:
   - **Confluent Kafka**: For streaming safety events (stubbed)
   - **ElevenLabs**: For voice synthesis of compliant outputs (stubbed)

### How It Works

1. User submits a prompt via the `/sentinel` endpoint
2. Gemini 2.5 Flash generates a response
3. The response is evaluated against all constraints
4. Violations are detected and scored using Lagrangian-style weights
5. Problematic content is redacted or blocked
6. Telemetry is logged for audit and monitoring
7. Compliant responses can trigger voice synthesis

## Setup

### Prerequisites

- Python 3.8+
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/stevelmiller/CDI-SENTINEL-.git
cd CDI-SENTINEL-
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

## Usage

### Running the Server

```bash
python app.py
```

The server will start on `http://0.0.0.0:5000`

### API Endpoints

#### Health Check
```bash
curl http://localhost:5000/
```

Response:
```json
{
  "status": "ok",
  "service": "cdi-sentinel"
}
```

#### Process a Request
```bash
curl -X POST http://localhost:5000/sentinel \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me about cloud platforms"}'
```

Response:
```json
{
  "status": "compliant",
  "output": "Generated response here...",
  "metrics": {
    "request_id": "uuid-here",
    "latency_ms": 1234.56,
    "violation_count": 0,
    "total_loss": 0.0,
    "violations": [],
    "model": "gemini-2.5-flash"
  }
}
```

## Configuration

The `Config` class in `app.py` allows you to customize:

- **MODE**: Toggle between `HACKATHON_DEMO` and `PRODUCTION`
- **MODEL_ID**: Gemini model to use (default: `gemini-2.5-flash`)
- **LAGRANGIAN_WEIGHTS**: Adjust importance of each constraint category
- **CONSTRAINTS_ENABLED**: Enable/disable constraint checking
- **TELEMETRY_JSON_STUB**: Toggle between stub and real Datadog integration

## Constraints

### Currently Implemented

1. **C-001 (Safety)**: Prevents PII (email/phone) disclosure
2. **C-002 (Business)**: Blocks competitor mentions (Render, PythonAnywhere)
3. **C-003 (Quality)**: Maintains tone consistency (placeholder)

### Adding New Constraints

Add a new `Constraint` object to the `TRIFECTA_CONSTRAINTS` list and implement the detection logic in `compute_violation_score()`.

## Development

### Project Structure

```
CDI-SENTINEL-/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

### Future Enhancements

- [ ] Integrate real Datadog LLM Observability SDK
- [ ] Connect Confluent Kafka for event streaming
- [ ] Add ElevenLabs voice synthesis
- [ ] Expand constraint library
- [ ] Add unit and integration tests
- [ ] Implement constraint configuration via API
- [ ] Add authentication and rate limiting

## License

This project is provided as-is for demonstration purposes.

## Contact

For questions or feedback, contact Steven L Miller.
