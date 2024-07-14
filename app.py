import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

# Pass the list of passwords directly to the
# Hasher constructor and generate the hashes
# passwords_to_hash = ['fashion@123', 'increff@fashion']
# hashed_passwords = Hasher(passwords_to_hash).generate()

# print(hashed_passwords)
import datetime
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


# 如下代码数据，可以来自数据库
names = ['肖永威', '管理员']
usernames = ['xiaoyw', 'admin']
passwords = ['S0451', 'ad4516']

authenticator = stauth.Authenticate(
    {'usernames': {'李森茂': {'email': None, 'name': '李森茂', 'password': '123'}}},
    'st_debug_cookie',
    'kjsdnfkjdsnjfknskd',
    30.0,
    {'emails': None}
)


# name, authentication_status, username = authenticator.login('Login', 'main')
name, authentication_status, username = authenticator.login()

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

        st.write("DB username:", st.secrets["db_username"])
        st.write("DB password:", st.secrets["db_password"])
        st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

        mydata.main()

    with cols2.container():
        authenticator.logout()
        st.stop()

elif authentication_status is False:
    st.error('Username/Password 错误。')

elif authentication_status is None:
    st.warning('请输入你的 username 和 password')
