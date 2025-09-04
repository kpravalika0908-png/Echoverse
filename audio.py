import streamlit as st

def audio_player(audio_bytes: bytes, audio_mime_type: str = "audio/mp3"):
    """
    Streamlit equivalent of the React AudioPlayer component.

    Parameters:
    - audio_bytes: bytes → audio file content
    - audio_mime_type: str → MIME type of the audio (e.g., "audio/mp3", "audio/wav")
    """
    # Derive file extension from MIME type
    file_extension = audio_mime_type.split("/")[-1].split(";")[0] if "/" in audio_mime_type else "audio"
    file_name = f"echoverse_audio.{file_extension}"

    st.markdown("### 🎧 Audio Player")

    # Audio playback
    st.audio(audio_bytes, format=audio_mime_type)

    # Download button
    st.download_button(
        label="⬇️ Download Audiobook",
        data=audio_bytes,
        file_name=file_name,
        mime=audio_mime_type,
    )