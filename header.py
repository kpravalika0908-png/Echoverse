import streamlit as st

def header():
    """
    Streamlit equivalent of the React Header component.
    Displays the EchoVerse title, logo placeholder, and subtitle.
    """
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="display: inline-flex; align-items: center; gap: 12px;">
                <!-- Logo placeholder -->
                <div style="width: 48px; height: 48px; background: #60A5FA; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-weight: bold; font-size: 20px;">EV</span>
                </div>
                
                <!-- Title with gradient -->
                <h1 style="
                    font-size: 2.5rem;
                    font-weight: bold;
                    background: linear-gradient(to right, #60A5FA, #A855F7);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    margin: 0;
                ">
                    EchoVerse
                </h1>
            </div>
            <p style="margin-top: 0.5rem; font-size: 1.125rem; color: #9CA3AF;">
                Transform text into expressive audiobooks with the power of AI.""")