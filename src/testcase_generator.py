import json
from src.gemini_client import call_gemini

def generate_test_cases(requirements_json_path: str, output_path: str = "outputs/testcases.json") -> dict:
    """
    Read requirements from a JSON file and generate test cases using Gemini.
    """
    with open(requirements_json_path, "r", encoding="utf-8") as f:
        requirements = json.load(f)

    prompt = f"""
    You are a QA automation assistant. Based on the following requirements,
    generate exhaustive test cases in **valid JSON**.

    Requirements:
    {json.dumps(requirements, indent=2)}

    Format strictly as:
    {{
      "test_cases": [
        {{
          "id": "TC-1",
          "requirement_id": "FR-1",
          "title": "Verify login with valid credentials",
          "steps": [
            "Open login page",
            "Enter valid username",
            "Enter valid password",
            "Click login"
          ],
          "expected_result": "User is logged in successfully"
        }}
      ]
    }}
    """

    response = call_gemini(prompt)

    try:
        test_cases = json.loads(response)
    except Exception:
        test_cases = {"error": "Model did not return valid JSON", "raw_output": response}

    # Save results
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(test_cases, f, indent=2, ensure_ascii=False)

    return test_cases
