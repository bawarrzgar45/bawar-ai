import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# بارکردنی زانیارییەکان
load_dotenv()

# ڕێکخستنی لاپەڕە
st.set_page_config(page_title="باوەڕ ڕزگار - AI", page_icon="🤖", layout="wide")

# CSS بۆ دیزاینی تاریک و ڕێکخستنی بۆکسەکان
st.markdown("""
    <style>
    .stApp { background-color: #121212; }
    [data-testid="stSidebar"] { background-color: #1e1e1e; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    div[data-testid="stChatMessage"] { 
        background-color: #2f2f2f !important; 
        color: #ffffff !important; 
        border-radius: 10px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# سایدبار
with st.sidebar:
    st.write("### Mario's ")
    st.write("---")
    st.subheader("🔗 Contact")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[<img src='https://upload.wikimedia.org/wikipedia/en/c/c4/Snapchat_logo.svg' width='40'>](https://snapchat.com/add/bauarrr)", unsafe_allow_html=True)
    with col2:
        st.markdown("[<img src='https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg' width='40'>](https://instagram.com/bauarrr)", unsafe_allow_html=True)
    with col3:
        st.markdown("[<img src='https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg' width='40'>](https://facebook.com/bawar.CR7)", unsafe_allow_html=True)
    
    st.write("---")
    st.link_button("WhatsApp", "https://wa.me/9647701810186", use_container_width=True)
    st.caption("© 2026 Bawar AI System")

# API Setup
api_key = os.getenv("GROQ_API_KEY")
chat = ChatGroq(groq_api_key=api_key, model="llama-3.3-70b-versatile")

# دەستووری زیرەکی (System Prompt)
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""تۆ باوەڕ ڕزگاریت.
        - ئەگەر پرسی 'باوەڕ کێیە؟' کرا، بە کوردی بڵێ: 'من زیرەکییەکی دەستکردم کە لەلایەن باوەڕ ڕزگارەوە پەرەم پێدراوە.'
        - ئەگەر پرسی 'Who is Bawar?' کرا، بە ئینگلیزی بڵێ: 'I am an AI assistant created and developed by Bawar Rizgar.'
        - ئەگەر بە لاتین پرسیاری کرد، بە لاتین بڵێ: 'Ego sum intellegentia artificialis a Bawar Rizgar creata et evoluta.'
        - هەمیشە وەڵامی گشتیت بەو زمانە بێت کە بەکارهێنەر پێی قسە دەکات.""")
    ]

# نیشاندانی گفتوگۆ
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif not isinstance(msg, SystemMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# وەرگرتنی پرسیار
if prompt := st.chat_input("پرسیارەکەت بنووسە..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        response = chat.invoke(st.session_state.messages)
        st.write(response.content)
        st.session_state.messages.append(response)