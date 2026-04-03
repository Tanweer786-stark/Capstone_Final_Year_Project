import os
from dotenv import load_dotenv

load_dotenv()

client = None
MODEL_NAME = "llama-3.1-8b-instant"
# MODEL_NAME = "llama-3.1-70b-versatile"

try:
    from groq import Groq

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except ModuleNotFoundError as e:
    # Deployment may not have groq installed yet. Keep app operational.
    print("WARNING: groq dependency is missing. AI features are disabled.", e)


def get_financial_advice(user_message, context=""):
    if client is None:
        return (
            "AI Financial Advisor is currently unavailable because the 'groq' package is not installed "
            "or GROQ_API_KEY is not set. Please ensure requirements.txt includes groq and the env var is configured."
        )

    prompt = f"""
You are an expert personal finance advisor.

User context:
{context}

User question:
{user_message}

Give clear, actionable and practical advice in bullet points.
Also suggest how to optimize spending and increase savings.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a smart AI financial advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content
    except Exception as e:
        print("ERROR: Groq API call failed:", e)
        return "AI service error: please try again later."
