import streamlit as st
import streamlit_authenticator as stauth
import yaml

from streamlit_authenticator.utilities.exceptions import (CredentialsError,ForgotError,LoginError,RegisterError,ResetError,UpdateError) 

with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

#初始化认证器
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

def main():
    # 创建侧边栏登录
    try:
        authenticator.login()
    except LoginError as e:
        st.sidebar.error(e)


    # 根据登录状态显示页面
    if st.session_state["authentication_status"]:
        st.balloons()
        st.sidebar.success(f'Logged in as {st.session_state["name"]}')
        col1, col2 = st.columns([3, 1])
        with col1:
            st.title('登陆成功！')
            st.title(f'欢迎{st.session_state["name"]}!')
        with col2:
            st.image('image/1.gif',width=150)
        st.image('https://www.pokemon.cn/play/resources/pokedex/img/pm/2fd12098f15628cce80d411e090189aeb7d758ff.png',width=400)

    elif st.session_state["authentication_status"] == False:
        st.sidebar.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.sidebar.warning('Please enter your username and password')

def save():
    with open('config.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)

if __name__ == '__main__':
    main()
