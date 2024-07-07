import streamlit as st


def navigation_bar():
    st.sidebar.write('文档管理导航栏')


    add_selectbox = st.sidebar.radio(
        "文档管理",
        ("上传文档", "下载文档", "文档查询")
    )

    if add_selectbox == '上传文档':
        fileupload()
    elif add_selectbox == '下载文档':
        filedownload()
    elif add_selectbox == '文档查询':
        querybooks()

    return add_selectbox

def main():
    navigation_bar()

if __name__ == '__main__':
    main()
