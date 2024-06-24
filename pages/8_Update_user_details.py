import streamlit as st

from Home import save ,authenticator
from streamlit_authenticator.utilities.exceptions import (UpdateError) 


#更新用户信息
def update_user_details():
    if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state["username"]):
                st.success('Entries updated successfully')
                save()
        except UpdateError as e:
            st.error(e)
    else:
        st.error("您尚未登录。请登录以该页面。")

if __name__ == '__main__':
    update_user_details()