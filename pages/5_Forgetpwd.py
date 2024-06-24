import streamlit as st
from Home import save ,authenticator

from streamlit_authenticator.utilities.exceptions import (ForgotError) 

def forgot_pwd():
    try:
        (username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password) = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.success('New password sent securely')
            st.write(new_random_password)
            save()
        elif not username_of_forgotten_password:
            st.error('Username not found')
    except ForgotError as e:
        st.error(e)
         
if __name__ == '__main__':
    forgot_pwd()