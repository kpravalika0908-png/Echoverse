import streamlit as st

st.set_page_config(
    page_title="EchoVerse: AI Audiobook Generator",
    page_icon="🎧",
    layout="centered",
)

# Apply dark background (like Tailwind bg-gray-900 #111827)
page_bg = """
<style>
body {
    background-color: #111827;
    color: #f9fafb; /* gray-50 */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App root (equivalent to <div id="root"></div>)
st.title("🎧 EchoVerse: AI Audiobook Generator")

# --- Input Area ---
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
text = ""
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
else:
    text = st.text_area("Paste your text here...", height=200)

# --- Tone Selection ---
tone = st.radio("Choose a Tone", ["Professional", "Casual", "Narrative"], horizontal=True)

# --- Voice Selection ---
voice = st.selectbox("Select a Voice", ["Allison (en-US)", "Michael (en-US)", "Lisa (en-UK)"])
st.caption("Voices may vary depending on browser/OS. Recommended: Allison, Michael, Lisa.")

# --- Generate Button ---
if st.button("✨ Generate Audiobook", disabled=not text.strip()):
    with st.spinner("Generating audiobook..."):
        # Here’s where you’d integrate with Google GenAI or a TTS library (gTTS/pyttsx3/etc.)
        # Example:
        # from gtts import gTTS
        # tts = gTTS(text=text, lang="en")
        # tts.save("audiobook.mp3")
        st.success(f"Audiobook generated with tone: {tone}, voice: {voice}")
        # st.audio("audiobook.mp3")
import streamlit as st

def app():
    st.title("🎧 EchoVerse: AI Audiobook Generator")

    # --- Input Area ---
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    text = ""
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = st.text_area("Paste your text here...", height=200)

    # --- Tone Selection ---
    tone = st.radio("Choose a Tone", ["Professional", "Casual", "Narrative"], horizontal=True)

    # --- Voice Selection ---
    voice = st.selectbox("Select a Voice", ["Allison (en-US)", "Michael (en-US)", "Lisa (en-UK)"])
    st.caption("Voices may vary depending on browser/OS. Recommended: Allison, Michael, Lisa.")

    # --- Generate Button ---
    if st.button("✨ Generate Audiobook", disabled=not text.strip()):
        with st.spinner("Generating audiobook..."):
            # Example integration with TTS
            # from gtts import gTTS
            # tts = gTTS(text=text, lang="en")
            # tts.save("audiobook.mp3")
            st.success(f"Audiobook generated with tone: {tone}, voice: {voice}")
            # st.audio("audiobook.mp3")

# ---- Entry point (like ReactDOM.createRoot().render(<App />)) ----
if __name__ == "__main__":
    app()