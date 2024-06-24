import streamlit as st

from Home import save,authenticator
from streamlit_authenticator.utilities.exceptions import (RegisterError) 

def registration():
    try:
        (email_of_registered_user,
            username_of_registered_user,
            name_of_registered_user) = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            save()
    except RegisterError as e:
        st.error(e)
        
if __name__ == '__main__':
    registration()