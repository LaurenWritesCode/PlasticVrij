import streamlit as st
from utils import verify_user, create_user_account

def auth_page(is_logged_in):
    tabs = st.sidebar.radio("Selecteer Tab", ["Login", "Register"])

    if tabs == "Login":
        login_page(is_logged_in)
    elif tabs == "Register":
        register_page()

def login_page(is_logged_in):
    st.header("Inloggen")

    st.markdown(
        """
        <style>
        .login-input label {
            color: #00ff00;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    email = st.text_input("E-mail", key="login-email")
    password = st.text_input("Wachtwoord", type="password", key="login-password")
    login_button = st.button("Inloggen")

    if is_logged_in:
        # Log uit
        st.session_state['is_logged_in'] = False
        st.session_state['current_user'] = ''
        st.success("Succesvol uitgelogd!")
    elif login_button:
        if verify_user(email, password):
            # Inloggen
            st.session_state['is_logged_in'] = True
            st.session_state['current_user_email'] = email
            st.experimental_rerun()  # Trigger a rerun of the app to redirect to form_page
        else:
            st.error("Ongeldige e-mail of wachtwoord.")

def register_page():
    st.header("Create an Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        create_user_account(username, email, password)
        st.success("Account created successfully! You can now log in.")
