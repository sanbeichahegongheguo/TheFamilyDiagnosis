import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 后端数据接口地址,用于请求实际的数据
API_HOST = "http://127.0.0.1:8080/api"


# streamlit运行后访问地址
FE_HOST = "http://127.0.0.1:8501"

# CAS跳转登陆地址
CAS_LOGIN_URL = "https://127.0.0.1:4436/sec/login"


# 允许访问的用户名
ALLOWED_USERS = [
    "user1",
    "user2",
    "user3"
]
