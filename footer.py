import streamlit as st

def footer():
    """
    Streamlit equivalent of the React Footer component.
    Displays credits and API usage information.
    """
    st.markdown("---")  # horizontal line
    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem; padding: 1rem 0;">
            <p style="font-size: 0.9rem; color: #6B7280;">
                Created by a world-class senior frontend React engineer.
            </p>
            <p style="font-size: 0.75rem; color: #9CA3AF; margin-top: 0.25rem;">
                This application uses the Gemini API for text generation and the browser's Web Speech API for narration.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )