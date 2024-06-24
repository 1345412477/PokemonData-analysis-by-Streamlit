import streamlit as st

if st.session_state["authentication_status"]:
    st.title('安全页面。')
    st.write('这是一个仅适用于经过身份验证的用户的安全页面。')
else:
    st.error("您尚未登录。请登录以该页面。")
