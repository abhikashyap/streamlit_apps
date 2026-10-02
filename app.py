import streamlit as st


st.set_page_config(page_title="Streamlit App", page_icon="👋", layout="centered")

st.title("Your Streamlit app is ready")
st.write("Edit `app.py` to start building your app.")

with st.sidebar:
    st.header("Settings")
    name = st.text_input("Your name", "there")

st.success(f"Hello, {name}!")

value = st.slider("Try a widget", min_value=0, max_value=100, value=50)
st.write(f"You selected **{value}**.")
