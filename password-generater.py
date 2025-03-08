import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Letters A-Z, a-z
    if use_digits:
        characters += string.digits  # Add numbers 0-9
    if use_special:
        characters += string.punctuation  # Add special characters

    return ''.join(random.choice(characters) for _ in range(length))

# 🎉 Streamlit App
st.title("🔐 Password Generator 🔑")

# User Inputs
length = st.slider("📏 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Numbers")
use_special = st.checkbox("💥 Include Special Characters")

# Generate Password
if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"🎯 Your Secure Password: `{password}`")
    st.write("✅ Keep it safe and secure! 🔒")

st.write("---")
st.write("👩‍💻 Made by Alwaz Ansari 💖")
