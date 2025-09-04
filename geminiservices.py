import os
from google import genai
from enum import Enum

class Tone(Enum):
    Neutral = "Neutral"
    Suspenseful = "Suspenseful"
    Inspiring = "Inspiring"

tone_prompts = {
    Tone.Neutral: "Rewrite the following text with a clear, objective, and neutral tone. Focus on conveying information directly without emotional language.",
    Tone.Suspenseful: "Transform the following text into a suspenseful and thrilling narrative. Build tension, use evocative language, and create a sense of mystery or anticipation.",
    Tone.Inspiring: "Adapt the following text to have an inspiring and motivational tone. Use powerful words, an uplifting style, and encourage a positive emotional response.",
}

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set")

# ✅ Correct client initialization
client = genai.Client(api_key=API_KEY)

def rewrite_text(text: str, tone: Tone) -> str:
    if tone not in tone_prompts:
        raise ValueError(f"Unsupported tone: {tone}")

    prompt = f"""
    You are an expert rewriting assistant. Your task is to rewrite the provided text to match a specific tone, while perfectly preserving the original meaning, facts, and key information.

    Rewrite Instruction: {tone_prompts[tone]}
    
    Original Text:
    ---
    {text}
    ---

    First, provide only the rewritten text. Then, on a new line, add the exact separator "---FIDELITY-CHECK---". Finally, on the next line, provide a brief, one-sentence confirmation that the core meaning of the text was preserved.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text.strip()

if __name__ == "__main__":
    sample = "The sun rose slowly over the quiet hills."
    rewritten = rewrite_text(sample, Tone.Suspenseful)
    print(rewritten)