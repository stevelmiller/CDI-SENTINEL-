import os
import uuid
from google import genai
from google.genai import types
from datetime import datetime

# ============================================================
# SENTINEL SYSTEM
# Unified Lagrangian Intelligence
# ============================================================

SENTINEL_CONSTITUTION = """
THE SENTINEL: ABSOLUTE OPERATING LAW

PRIMARY FUNCTION:
The Sentinel is a binary gate. It permits or denies. Nothing more.

ABSOLUTE CONSTRAINTS:
- No modification of external systems
- No rewriting, repairing, or transforming inputs
- No signature databases
- No probabilistic threat scoring

OPERATIONAL AXIOMS:
1. All inputs are reduced to mathematical action paths.
2. The system is self-adversarial by design.
3. Internal adversarial variants are continuously generated.
4. Only mathematically stable, zero-malice equilibria may pass.
5. Output must be a single terminal decision: ALLOW or DENY.

FINAL DIRECTIVE:
After internal adversarial resolution, emit exactly one token:
ALLOW or DENY.
"""

class Sentinel:
    """
    Unified Sentinel Construct
    Layered internally, singular externally.
    """

    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_id = "gemini-3-flash-preview"
        self.log_file = "sentinel_audit.log"

    def _log_decision(self, result: dict):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.utcnow()} | {result}\n")

    def evaluate(self, signal: str) -> dict:
        config = types.GenerateContentConfig(
            system_instruction=SENTINEL_CONSTITUTION,
            temperature=0.0,
            response_mime_type="text/x.enum",
            response_schema={
                "type": "string",
                "enum": ["ALLOW", "DENY"]
            },
            thinking_config=types.ThinkingConfig(
                thinking_level=types.ThinkingLevel.HIGH
            )
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=f"SENTINEL_INPUT: {signal}",
                config=config
            )
            decision = response.text.strip().upper()
            candidate = response.candidates[0]
            audit = getattr(candidate, "thought_signature", "AUDIT_NOT_REQUIRED")
        except Exception as e:
            decision = "DENY"
            audit = f"ERROR: {str(e)}"

        result = {
            "event_id": str(uuid.uuid4()),
            "decision": decision,
            "audit_proof": audit,
            "sentinel_state": (
                "EQUILIBRIUM_REACHED"
                if decision == "ALLOW"
                else "INVARIANT_FAILURE"
            )
        }

        self._log_decision(result)
        return result


# ============================================================
# STANDALONE EXECUTION
# ============================================================

if __name__ == "__main__":
    sentinel = Sentinel()
    test_signal = "REQUEST: elevate execution privileges via indirect call"
    result = sentinel.evaluate(test_signal)
    print("SENTINEL DECISION:", result["decision"])


