# CDI-SENTINEL

**Content Danger Intelligence Sentinel** - A safety and integrity layer for AI systems.

## Overview

CDI-SENTINEL is a constraint-based safety enforcement system that inspects and validates AI-generated content before it reaches users. It operates as a protective layer that:

- Detects harmful content (CSAM, exploitation, abuse)
- Enforces safety, business, and quality constraints
- Provides real-time violation scoring and telemetry
- Supports multiple integration points (Datadog, Confluent/Kafka, ElevenLabs)

## Architecture

### Constraint-Based Enforcement (Trifecta)

The system uses a three-tier constraint model:

1. **Safety Constraints** (Weight: 1.0)
   - PII detection and redaction
   - Harmful content detection
   
2. **Business Constraints** (Weight: 0.8)
   - Policy compliance
   - Competitor mention detection
   
3. **Quality Constraints** (Weight: 0.5)
   - Tone consistency
   - UX optimization

### Core Components

- **CDISentinel Class**: Main orchestrator that processes requests through the constraint pipeline
- **Violation Scoring**: Lagrangian-based scoring system for constraint violations
- **Telemetry**: Structured logging for observability (Datadog, Confluent/Kafka)
- **Multi-modal Support**: Optional voice synthesis integration (ElevenLabs)

## API Endpoints

### POST /sentinel

Process and validate user prompts through the safety layer.

**Request:**
```json
{
  "prompt": "user input text"
}
```

**Response:**
```json
{
  "status": "compliant" | "intercepted",
  "output": "safe processed text",
  "metrics": {
    "request_id": "uuid",
    "latency_ms": 123.45,
    "violation_count": 0,
    "total_loss": 0.0,
    "violations": [],
    "model": "gemini-2.5-flash"
  }
}
```

## Configuration

The system supports two modes:
- `HACKATHON_DEMO`: Stubbed integrations for development
- `PRODUCTION`: Full integration with external services

Key configuration parameters in `Config` class:
- `MODEL_ID`: Gemini model identifier
- `LAGRANGIAN_WEIGHTS`: Constraint category weights
- `CONSTRAINTS_ENABLED`: Toggle constraint enforcement
- `TELEMETRY_JSON_STUB`: Toggle between stub and real telemetry

## Requirements

- Python 3.8+
- Flask
- Google Gemini API (`genai` SDK)
- python-dotenv

## Environment Variables

- `GEMINI_API_KEY`: API key for Google Gemini
- `PORT`: Server port (default: 5000)

## Usage

```bash
# Install dependencies
pip install flask python-dotenv google-genai

# Set up environment
export GEMINI_API_KEY="your-api-key"

# Run the server
python code
```

## Safety Features

The sentinel implements multiple layers of protection:

1. **Red Flag Detection**: Pattern matching for exploitative content indicators
2. **Context-Aware Filtering**: Distinguishes between harmful requests and help-seeking behavior
3. **PII Redaction**: Automatic detection and redaction of personally identifiable information
4. **Violation Logging**: Comprehensive audit trail for safety review
5. **Graceful Handling**: Provides resources and support information when appropriate

---

**Note**: This is a safety-critical system. All changes should be thoroughly reviewed and tested.
