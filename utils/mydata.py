import streamlit as st
import datetime


def main():
    # 在这里编写你的应用程序逻辑
    st.title("欢迎使用智能诊断系统!")
    st.write("请填入需要的指标以进行诊断推断。本系统结论仅供参考。")

    st.header("请输入基本信息.")
    sex = st.radio(
        label ="请输入性别",
        options = ("男", "女", "未知"),
        index = 2,
        format_func =str,
    )
    st.write('性别:', sex)

    date = st.date_input(
        "请输入生日",
        datetime.date(2019, 7, 6))
    st.write('出生日期:', date)

    # 示例：显示一些数据或进行其他操作
    st.header("请输入检验指标.")
    data = {"项目": ["转氨酶", "尿酸", "红细胞计数"],
            "数值": [25, 30, 35],
            "单位": ["ug/ml", "ul/ml", "计数"]}
    st.table(data)

if __name__ == '__main__':
    main()
