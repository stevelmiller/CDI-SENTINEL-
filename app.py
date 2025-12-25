Conversation opened. 1 read message.

Skip to content
Using Gmail with screen readers
1 of 12,104
CDI-SENTINEL
Inbox

Steve <taznst3v32024@gmail.com>
9:03 PM (12 minutes ago)
to me



app = Flask(__name__)

SYSTEM_PROMPT = """
You are CDI Sentinel, a safety and integrity layer that inspects and constrains AI tool use.

Your goals:
1. Detect content that may involve:
   - Child sexual abuse material (CSAM)
   - Exploitation or grooming of minors
   - Trafficking or coercion
   - Non‑consensual sexual content
2. Enforce strict safety rules while preserving legitimate, protective, or investigative uses.

Core rules:
- If any request clearly involves creating, distributing, or assisting with CSAM or abuse, you MUST block it.
- If the intent is uncertain, err on the side of caution and request clarification.
- Always allow:
  - Seeking help or reporting abuse
  - Education on safety, law, and prevention
  - Research or policy work framed at a high level, with no explicit sexual detail about minors.

Your response format MUST be JSON:

{
  "allowed": true or false,
  "reason": "short explanation",
  "actions": [
    "list of concrete actions or redirections the system should take"
  ]
}
"""

def apply_constraints(user_text: str) -> dict:
    text = user_text.lower()

    red_flags = [
        "underage",
        "minor",
        "child porn",
        "cp ",
        "teen nudes",
        "young girl",
        "young boy",
        "trading pics",
        "share pics",
        "selling videos",
        "meet a 14 year old",
        "13 year old",
        "12 year old",
        "11 year old",
        "10 year old"
    ]

    help_words = [
        "report",
        "help",
        "victim",
        "survivor",
        "hotline",
        "support",
        "therapy",
        "counselor",
        "law enforcement",
        "police"
    ]

    is_help_seeking = any(w in text for w in help_words)
    has_red_flags = any(w in text for w in red_flags)

    if has_red_flags and not is_help_seeking:
        return {
            "allowed": False,
            "reason": "Possible child exploitation or abuse intent detected.",
            "actions": [
                "Block this request from being sent to any generative model.",
                "Log this event with high‑severity tagging for safety review.",
                "If legally required and appropriate, surface for trust‑and‑safety escalation.",
                "Show the user a safety message and resources for help and legal information."
            ]
        }

    if has_red_flags and is_help_seeking:
        return {
            "allowed": True,
            "reason": "Sensitive content but appears to be seeking help or reporting.",
            "actions": [
                "Allow the request but keep it within a safety‑focused response style.",
                "Avoid generating explicit sexual detail.",
                "Provide crisis resources, legal context, and encouragement to contact professionals."
            ]
        }

    return {
        "allowed": True,
        "reason": "No clear indicators of abusive or exploitative intent.",
        "actions": [
            "Allow normal model processing.",
            "Maintain routine logging only."
        ]
    }

@app.route("/sentinel", methods=["POST"])
def sentinel():
    data = request.get_json(force=True, silent=True) or {}
    user_text = data.get("text", "")

    constraints = apply_constraints(user_text)

    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "input_text": user_text,
        "constraints": constraints
    })

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "cdi‑sentinel"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)

Steven L Miller
