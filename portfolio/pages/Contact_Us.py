import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_form"):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")


    fmessage = f"""\
Subject: Greetings from {email}
From: {email}

{message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(fmessage)

st.write("Feel free to contact me if you want to collaborate or chat")
