"""
Handles all communication with the Groq API (LLaMA-3.3-70B).
Loads the API key from a .env file via python-dotenv.
"""

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def query_llm(prompt: str) -> str:
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY is not set.\n"
        )

    client = Groq(api_key=api_key)

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert chef and nutritionist who generates safe, "
                    "delicious, and detailed dinner recipes tailored to individual "
                    "dietary needs. Always show your chain-of-thought reasoning "
                    "before producing the final recipe."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=1500,
    )

    return chat_completion.choices[0].message.content