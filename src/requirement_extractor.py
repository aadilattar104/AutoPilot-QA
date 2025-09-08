import json
from src.gemini_client import call_gemini

def extract_requirements(srs_text: str) -> dict:
    """Send SRS text to Gemini and return requirements in JSON"""
    prompt = f"""
    Extract requirements from the following SRS text and return ONLY valid JSON:
    {{
      "functional_requirements": [
        {{"id": "FR-1", "text": "..." }}
      ],
      "non_functional_requirements": [
        {{"id": "NFR-1", "text": "..." }}
      ]
    }}

    SRS TEXT:
    {srs_text}
    """

    response = call_gemini(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {"error": "Invalid JSON returned", "raw_output": response}
