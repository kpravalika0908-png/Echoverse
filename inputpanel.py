import streamlit as st

# Enum-like tones
TONE_OPTIONS = ["Professional", "Casual", "Narrative"]

def input_panel():
    st.markdown(
        """
        <div style="padding: 20px; border-radius: 12px; background: rgba(31,41,55,0.5); 
                    border: 1px solid #374151;">
        """,
        unsafe_allow_html=True,
    )

    # --- Text Area ---
    st.markdown("*Your Text*")
    original_text = st.text_area(
        "Paste your text here or upload a .txt file...",
        height=200,
        label_visibility="collapsed",
    )

    # --- File Upload ---
    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])
    if uploaded_file is not None:
        original_text = uploaded_file.read().decode("utf-8")

    # --- Tone Selection ---
    st.markdown("### Choose a Tone")
    selected_tone = st.radio(
        "Tone",
        TONE_OPTIONS,
        horizontal=True,
        label_visibility="collapsed",
    )

    # --- Voice Selection ---
    st.markdown("*Select a Voice*")
    # Example voices (Streamlit can’t access browser voices directly)
    voices = ["Allison (en-US)", "Michael (en-US)", "Lisa (en-UK)"]
    selected_voice = st.selectbox(
        "Voice Options",
        options=voices,
        index=0,
        label_visibility="collapsed",
    )
    st.caption("Voices may vary depending on browser/OS. Recommended: Allison, Michael, Lisa.")

    # --- Generate Button ---
    generate_button = st.button(
        "✨ Generate Audiobook",
        use_container_width=True,
        type="primary",
        disabled=not original_text.strip(),
    )

    st.markdown("</div>", unsafe_allow_html=True)

    return original_text, selected_tone, selected_voice, generate_button