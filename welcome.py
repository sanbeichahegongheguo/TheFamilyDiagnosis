import streamlit as st

from utils import authenticate
from utils.authenticate import is_allowed_user


st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

# 初始化鉴权变量
authenticate.set_st_state_vars()

# Add login/logout buttons，点击可跳转
if not st.session_state.get("authenticated"):
    st.warning("Please login!")
    authenticate.button_login()
else:
    authenticate.button_logout()

    if not is_allowed_user():
        st.error("You do not have access. Please contact the administrator.")
    else:
        # else,页面展示代码位于通过鉴权后
        st.title("欢迎使用XX仪表盘 👋")

        st.markdown(
            """

            该项目为streamlit跳转登陆测试项目\n
            **👈 请从侧边栏进入功能页**
            ### 官方参考文档
            - Streamlit: [Streamlit](https://docs.streamlit.io/)
            - 表单登陆: [streamlit-authenticator](https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/)

            ### 实现跳转登陆参考文档
            - [参考文档](https://levelup.gitconnected.com/building-a-multi-page-app-with-streamlit-and-restricting-user-access-to-pages-using-aws-cognito-89a1fb5364a3)

        """
        )
