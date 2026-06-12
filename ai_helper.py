import requests

def ask_ai(question):

    prompt = f"""
You are a study planner assistant.

Your job is to help students prepare for exams.

When answering:
- Give study advice
- Mention important topics
- Suggest a study plan
- Give revision tips
- Keep answers practical

Student Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"llama3.2",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()["response"]
