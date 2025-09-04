import os
import streamlit as st
from dotenv import load_dotenv
import requests

load_dotenv()

GRANITE_API_KEY = os.getenv("GRANITE_API_KEY")
GRANITE_API_BASE = os.getenv("GRANITE_API_BASE", "https://api.granite.example.com")
LLM_ENDPOINT = f"{GRANITE_API_BASE}/v1/llm/generate"
TTS_ENDPOINT = f"{GRANITE_API_BASE}/v1/tts/speak"

AVAILABLE_VOICES = {
    "Lisa": "lisa",
    "Michael": "michael",
    "Allison": "allison",
}

HEADERS = {
    "Authorization": f"Bearer {GRANITE_API_KEY}",
    "Content-Type": "application/json",
}

def call_granite_llm(prompt: str, model: str = "granite-medium", max_tokens: int = 1024):
    if not GRANITE_API_KEY:
        raise ValueError("GRANITE_API_KEY environment variable not set")

    payload = {
        "model": model,
        "input": prompt,
        "max_tokens": max_tokens,
    }

    resp = requests.post(LLM_ENDPOINT, headers=HEADERS, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    if "output" in data and isinstance(data["output"], list) and len(data["output"]) > 0:
        return data["output"][0]
    if "text" in data:
        return data["text"]
    raise ValueError("Unexpected response format from Granite LLM")

def call_granite_tts(text: str, voice: str = "lisa", format: str = "mp3") -> bytes:
    if not GRANITE_API_KEY:
        raise ValueError("GRANITE_API_KEY environment variable not set")

    payload = {
        "voice": voice,
        "text": text,
        "format": format,
    }

    resp = requests.post(TTS_ENDPOINT, headers=HEADERS, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.content

def build_rewrite_prompt(original_text: str, tone: str) -> str:
    tone_instructions = {
        "Neutral": "Rewrite the following text with a clear, objective, and neutral tone.",
        "Suspenseful": "Transform the following text into a suspenseful and thrilling narrative.",
        "Inspiring": "Adapt the following text to have an inspiring and motivational tone.",
        "Professional": "Rewrite the following text in a professional tone.",
        "Casual": "Rewrite the following text in a casual tone.",
        "Narrative": "Rewrite the following text in a narrative tone.",
    }
    instruction = tone_instructions.get(tone, "Rewrite the following text.")
    return f"{instruction}\n\nOriginal Text:\n{original_text}"

def main():
    st.set_page_config(
        page_title="EchoVerse: AI Audiobook Generator",
        page_icon="🎧",
        layout="centered",
    )

    st.title("🎧 EchoVerse: AI Audiobook Generator")

    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    text_input = ""
    if uploaded_file:
        text_input = uploaded_file.read().decode("utf-8")
    else:
        text_input = st.text_area("Paste your text here...", height=200)

    tone = st.radio("Choose a Tone", ["Neutral", "Suspenseful", "Inspiring", "Professional", "Casual", "Narrative"], horizontal=True)
    voice = st.selectbox("Select a Voice", list(AVAILABLE_VOICES.keys()))
    model = st.text_input("LLM model", value="granite-medium")

    if st.button("✨ Generate Audiobook", disabled=not text_input.strip()):
        with st.spinner("Generating..."):
            try:
                prompt = build_rewrite_prompt(text_input, tone)
                rewritten_text = call_granite_llm(prompt, model=model)
                audio_bytes = call_granite_tts(rewritten_text, voice=AVAILABLE_VOICES[voice])
                st.subheader("Rewritten Text")
                st.write(rewritten_text)
                st.subheader("Listen & Download")
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button(
                    "Download narration",
                    data=audio_bytes,
                    file_name="narration.mp3",
                    mime="audio/mp3",
                )
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
