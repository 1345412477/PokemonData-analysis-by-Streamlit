import streamlit as st

from Home import authenticator

def logout():
    if st.session_state["authentication_status"]:
        authenticator.logout()
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    logout()