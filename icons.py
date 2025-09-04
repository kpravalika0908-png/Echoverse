import streamlit as st

def upload_icon(size: int = 24, color: str = "currentColor"):
    st.markdown(f"""
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" 
         viewBox="0 0 24 24" stroke-width="1.5" stroke="{color}" 
         width="{size}" height="{size}">
        <path stroke-linecap="round" stroke-linejoin="round" 
              d="M12 16.5V9.75m0 0l-3.75 3.75M12 9.75l3.75 3.75M3.75 18A5.25 
                 5.25 0 009 20.25h6a5.25 5.25 0 005.25-5.25c0-2.01-1.125-3.75-2.625-4.583
                 .155-.442.225-.902.225-1.367a5.25 5.25 0 00-10.5 0c0 .465.07.925.225 1.367
                 -1.5.833-2.625 2.573-2.625 4.583z" />
    </svg>
    """, unsafe_allow_html=True)


def sparkles_icon(size: int = 24, color: str = "currentColor"):
    st.markdown(f"""
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" 
         viewBox="0 0 24 24" stroke-width="1.5" stroke="{color}" 
         width="{size}" height="{size}">
        <path stroke-linecap="round" stroke-linejoin="round" 
              d="M9.813 15.904L9 18.75l-.813-2.846a4.5 
                 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 
                 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 
                 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 
                 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 
                 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 
                 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 
                 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 
                 3.375 0 00-2.456 2.456zM16.898 20.572L16.5 
                 21.75l-.398-1.178a3.375 3.375 0 00-2.455-2.456L12.75 
                 18l1.178-.398a3.375 3.375 0 002.455-2.456L16.5 
                 14.25l.398 1.178a3.375 3.375 0 002.456 
                 2.456l1.178.398-1.178.398a3.375 
                 3.375 0 00-2.456 2.456z" />
    </svg>
    """, unsafe_allow_html=True)


def spinner_icon(size: int = 24, color: str = "currentColor"):
    st.markdown(f"""
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" 
         viewBox="0 0 24 24" stroke-width="1.5" stroke="{color}" 
         width="{size}" height="{size}">
        <path stroke-linecap="round" stroke-linejoin="round" 
              d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 
                 0h4.992m-4.993 0l3.181 3.183a8.25 
                 8.25 0 0011.667 0l3.181-3.183m-11.667 
                 0a8.25 8.25 0 0111.667 0l3.181 
                 3.183M2.985 19.644l3.181-3.182m0 
                 0a8.25 8.25 0 0111.667 0l3.181 3.182" />
    </svg>
    """, unsafe_allow_html=True)


def download_icon(size: int = 24, color: str = "currentColor"):
    st.markdown(f"""
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" 
         viewBox="0 0 24 24" stroke-width="1.5" stroke="{color}" 
         width="{size}" height="{size}">
        <path stroke-linecap="round" stroke-linejoin="round" 
              d="M3 16.5v2.25A2.25 2.25 0 005.25 
                 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 
                 12L12 16.5m0 0L7.5 12m4.5 
                 4.5V3" />
    </svg>
    """, unsafe_allow_html=True)


def logo_icon(size: int = 24, color: str = "currentColor"):
    st.markdown(f"""
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" 
         viewBox="0 0 24 24" stroke-width="1.5" stroke="{color}" 
         width="{size}" height="{size}">
        <path stroke-linecap="round" stroke-linejoin="round" 
              d="M12 18.75a6 6 0 006-6v-1.5m-6 
                 7.5a6 6 0 01-6-6v-1.5m6 
                 7.5v3.75m-3.75 0h7.5M12 
                 15.75a3 3 0 01-3-3V4.5a3 
                 3 0 116 0v8.25a3 3 0 
                 01-3 3z" />
    </svg>
    """, unsafe_allow_html=True)