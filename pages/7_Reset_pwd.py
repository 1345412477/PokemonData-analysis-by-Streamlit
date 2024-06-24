import streamlit as st

from Home import save ,authenticator
from streamlit_authenticator.utilities.exceptions import (CredentialsError,ResetError)

#密码重置
def reset_pwd():
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"]):
                st.success('Password modified successfully')
                save()
        except ResetError as e:
            st.error(e)
        except CredentialsError as e:
            st.error(e)
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    reset_pwd()