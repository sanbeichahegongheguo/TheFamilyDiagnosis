import streamlit as st
import streamlit_authenticator as stauth

import utils.mydata as mydata

# 初始化一个Streamlit应用
st.set_page_config(
    page_title="智能诊断学习平台",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

if st.button('点我'):
    st.write('今天是个好日子！')


authenticator = stauth.Authenticate(
    {'usernames': {"李森茂":
                   {'email': None, 'name': "李森茂", 'password': "123"}}},
    'st_debug_cookie',
    'kjsdnfkjdsnjfknskd',
    30.0,
    {'emails': None}
)


# name, authentication_status, username = authenticator.login('Login', 'main')
name, authentication_status, username = authenticator.login(location="sidebar", fields={'Form name': '登陆页面', 'Username': '用户名', 'Password': '密码',
                      'Login':'登录'}, clear_on_submit=True)

# def initialize_session_state():
#     if 'name' not in st.session_state:
#         st.session_state['name'] = None
#     if 'authentication_status' not in st.session_state:
#         st.session_state['authentication_status'] = None
#     if 'username' not in st.session_state:
#         st.session_state['username'] = None

# initialize_session_state()


if authentication_status:
    with st.container():
        cols1, cols2 = st.columns(2)
        cols1.write('欢迎用户 *%s*' % (name))

        mydata.main()

    with cols2.container():
        authenticator.logout(button_name="退出")
        st.stop()

elif authentication_status is False:
    st.error('Username/Password 错误。')

elif authentication_status is None:
    st.warning('请输入你的 username 和 password')
