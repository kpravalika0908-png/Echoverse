import streamlit as st
from typing import Optional

def output_panel(
    original_text: str,
    rewritten_text: str,
    fidelity_check: str,
    audio_bytes: Optional[bytes],
    audio_mime_type: str = "audio/mp3",
    is_loading: bool = False,
    error: Optional[str] = None,
):
    """
    Streamlit equivalent of the React OutputPanel component.

    Parameters:
    - original_text: str → input text
    - rewritten_text: str → rewritten version from Granite LLM
    - fidelity_check: str → one-line check about meaning preservation
    - audio_bytes: bytes or None → audio file in memory
    - audio_mime_type: str → usually 'audio/mp3'
    - is_loading: bool → show spinner if True
    - error: str or None → error message if present
    """
    st.markdown("### Output Panel")

    # 🔴 Error handling
    if error:
        st.error(f"Error: {error}")

    # ⏳ Loading state
    if is_loading:
        with st.spinner("Crafting your story..."):
            st.info("Rewriting text and generating narration. This may take a moment.")
        return

    # 💤 Placeholder state
    if not rewritten_text and not audio_bytes:
        st.info("💡 Your audiobook will appear here. Enter some text and click 'Generate' to begin.")
        return

    # 🎧 Audio player
    if audio_bytes:
        st.subheader("Listen & Download")
        st.audio(audio_bytes, format=audio_mime_type)
        st.download_button(
            "Download narration",
            data=audio_bytes,
            file_name="narration.mp3",
            mime=audio_mime_type,
        )

    # 📑 Side-by-side comparison
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Text")
        st.text_area(
            "Original",
            original_text,
            height=250,
            key="original_text_display",
        )

    with col2:
        st.subheader("Tone-Adapted Text")
        st.text_area(
            "Rewritten",
            rewritten_text,
            height=250,
            key="rewritten_text_display",
        )

        if fidelity_check:
            st.caption(f"AI Fidelity Check: {fidelity_check}")