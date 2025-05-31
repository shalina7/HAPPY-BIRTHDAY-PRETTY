
import streamlit as st
import base64

# Set page config
st.set_page_config(
    page_title="HAPPY BIRTHDAY",
    layout="centered",
)

# Background dengan emoji
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://em-content.zobj.net/source/apple/354/birthday-cake_1f382.png"),
                          url("https://em-content.zobj.net/source/apple/354/cherries_1f352.png"),
                          url("https://em-content.zobj.net/source/apple/354/elephant_1f418.png"),
                          url("https://em-content.zobj.net/source/apple/354/hippopotamus_1f99b.png");
        background-size: 100px 100px;
        background-position: top left, top right, bottom left, bottom right;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>HAPPY BIRTHDAY 🎉</h1>", unsafe_allow_html=True)

# Ucapan
st.write("Selamat ulang tahun! 🎂 Semoga harimu menyenangkan, penuh kebahagiaan, dan diberkati selalu.")

# Audio
def add_bg_audio(mp3_file):
    audio_bytes = open(mp3_file, "rb").read()
    base64_audio = base64.b64encode(audio_bytes).decode()
    audio_html = f'''
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{base64_audio}" type="audio/mp3">
        </audio>
        '''
    st.markdown(audio_html, unsafe_allow_html=True)

add_bg_audio("happy_birthday_piano.mp3")
