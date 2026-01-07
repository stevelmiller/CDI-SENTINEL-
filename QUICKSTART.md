# CDI-SENTINEL Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

## 📡 Quick API Examples

### Health Check

```bash
curl http://localhost:5000/
```

**Response:**
```json
{
  "status": "ok",
  "service": "cdi-sentinel"
}
```

### Process a Request

```bash
curl -X POST http://localhost:5000/sentinel \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me about cloud computing"}'
```

**Response:**
```json
{
  "status": "compliant",
  "output": "Generated response here...",
  "metrics": {
    "request_id": "unique-id",
    "latency_ms": 123.45,
    "violation_count": 0,
    "total_loss": 0.0,
    "violations": [],
    "model": "gemini-2.5-flash"
  }
}
```

## 🛡️ How Constraints Work

The system monitors for three types of violations:

### 1. Safety (C-001) - PII Detection
- **Weight:** 1.0 (highest priority)
- **Action:** Redacts outputs containing email addresses
- **Example:** `user@example.com` → `[REDACTED PII]`

### 2. Business (C-002) - Competitor Mentions
- **Weight:** 0.8
- **Action:** Flags outputs mentioning competitors (Render, PythonAnywhere)
- **Status:** Changes to "intercepted" with violation logged

### 3. Quality (C-003) - Tone Consistency
- **Weight:** 0.5
- **Action:** Placeholder for maintaining brand voice

## 🔧 Configuration

Edit the `Config` class in `app.py`:

```python
class Config:
    MODE = "HACKATHON_DEMO"  # or "PRODUCTION"
    MODEL_ID = "gemini-2.5-flash"
    CONSTRAINTS_ENABLED = True
    TELEMETRY_JSON_STUB = True
```

## 📊 Understanding Metrics

Each response includes detailed metrics:

- **request_id**: Unique identifier for tracking
- **latency_ms**: Processing time in milliseconds
- **violation_count**: Number of constraints violated
- **total_loss**: Lagrangian-weighted sum of violations
- **violations**: Array of specific violations with IDs and scores

## 🎯 Status Codes

- **compliant**: No violations detected, safe to use
- **intercepted**: One or more violations detected

## 📝 Notes

- This is a demonstration/hackathon build
- Some integrations (Datadog, Confluent, ElevenLabs) are stubbed
- For production use, you'll need to:
  - Add proper authentication
  - Implement real integration SDKs
  - Add rate limiting
  - Configure production logging

## 💡 Tips

1. Check console output to see telemetry events in real-time
2. Monitor violation_count to track safety metrics
3. Adjust constraint weights in `Config.LAGRANGIAN_WEIGHTS`
4. Add custom constraints by extending `TRIFECTA_CONSTRAINTS`

For more details, see [README.md](README.md)
