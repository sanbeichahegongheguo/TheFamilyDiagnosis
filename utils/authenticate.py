import streamlit as st
import requests
import json

from config import FE_HOST, CAS_LOGIN_URL, ALLOWED_USERS


# ------------------------------------
# Initialise Streamlit state variables
# ------------------------------------
def initialise_st_state_vars():
    if "auth_code" not in st.session_state:
        st.session_state["auth_code"] = ""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "user_cognito_groups" not in st.session_state:
        st.session_state["user_cognito_groups"] = []


# ----------------------------------
# Get authorization code after login
# ----------------------------------
def get_auth_code():
    auth_query_params = st.query_params()
    try:
        auth_code = dict(auth_query_params)["sid"][0]
    except (KeyError, TypeError):
        auth_code = ""

    return auth_code

# -----------------------------
# Set Streamlit state variables
# -----------------------------
def set_st_state_vars():
    initialise_st_state_vars()
    auth_code = get_auth_code()
    user_info = get_auth_user(sid=auth_code) or {}

    if user_info.get("user"):
        st.session_state["auth_code"] = auth_code
        st.session_state["authenticated"] = True
        st.session_state["user"] = user_info.get("user")
        st.session_state["email"] = user_info.get("mail")
        st.session_state["display"] = user_info.get("display")


# -----------------------------
# Login/ Logout HTML components
# -----------------------------
login_link = f"{CAS_LOGIN_URL}?ref={FE_HOST}"


html_css_login = """
<style>
.button-login {
  background-color: skyblue;
  color: white !important;
  padding: 1em 1.5em;
  text-decoration: none;
  text-transform: uppercase;
}

.button-login:hover {
  background-color: #555;
  text-decoration: none;
}

.button-login:active {
  background-color: black;
}

</style>
"""

html_button_login = (
    html_css_login
    + f"<a href='{login_link}' class='button-login' target='_self'>Log In</a>"
)


def button_login():
    """

    Returns:
        Html of the login button.
    """
    _, col, _ = st.columns(3)
    return col.markdown(f"{html_button_login}", unsafe_allow_html=True)


def button_logout():
    """

    Returns:
        Html of the logout button.
    """
    def logout_click():
        st.session_state["authenticated"] = False
    st.sidebar.button("Logout", on_click=logout_click)
    print(st.session_state)


def get_auth_user(sid, ref=FE_HOST):
    cas_url = f"{CAS_LOGIN_URL}?sid=%s&ref=%s" % (sid, ref)
    if not sid or not ref:
        return

    user_info = requests.get(cas_url ).text
    try:
        user_dict = json.loads(user_info)
    except json.decoder.JSONDecodeError:
        return
    else:
        return user_dict


def is_allowed_user():
    if st.session_state["email"] in ALLOWED_USERS:
        return True
    return False
