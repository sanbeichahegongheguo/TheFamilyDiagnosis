import streamlit as st
import datetime
# import sys
# sys.path.append("./utils")
from utils.kmeansdata import run_kmeans_and_plot
from utils.randomsdata import train_RandomForest, apply_RandomForest


def main() -> None:
    st.title("欢迎使用智能诊断系统!")
    st.write("请填入需要的指标以进行诊断推断。本系统结论仅供参考。")
    st.header("请输入患者基本信息")

    sex = st.radio(
        label = "请输入患性别",
        options = ("男", "女", "未知"),
        index = 0,
    )
    st.write('患者的性别是:', sex)

    birthday = st.date_input(label = '请输入您的出生年月',
                        value = None,
                        min_value = None,
                        max_value = datetime.date.today(),
                        help = '请输入您的出生年月')
                        value = None,
                        min_value = None,
                        max_value = datetime.date.today(),
                        help = '请输入您的出生年月')
    st.write(f'患者的出生年月是：{birthday}')

    if birthday:
        # 示例计算年龄，实际应使用更准确的日期计算库
        today = datetime.date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        st.write(f'患者的年龄是：{age} 岁.')
    else:
        age = None
        st.write('患者的年龄未知.')

    st.header("请输入检验指标")
    data1 = st.number_input(label = '请输入患者的转氨酶',
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的转氨酶',
                    key= 'transaminase'
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的转氨酶',
                    key= 'transaminase'
                    )
    data2 = st.number_input(label = '请输入患者的尿酸',
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的尿酸'
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的尿酸'
                    )
    data3 = st.number_input(label = '请输入患者的红细胞计数',
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的红细胞计数'
                    min_value = 0,
                    max_value = 100,
                    value = 0,
                    step = 1,
                    help = '请输入患者的红细胞计数'
                    )

    data = {"项目": ["转氨酶", "尿酸", "红细胞计数"],
            "数值": [data1, data2, data3],
            "单位": ["ug/ml", "ul/ml", "计数"]}
    st.table(data)

    st.header("请提供家族史信息")
    family = st.multiselect(
        label = '请选择患者家族史中有癌症史的家属',
        options = ('父亲', '母亲', '祖父', '祖母', '外祖父', '外祖母',
                   '儿子', '女儿', '其他母系亲属', '其他父系亲属', '无', '未知'),
                   '儿子', '女儿', '其他母系亲属', '其他父系亲属', '无', '未知'),
        default = [],
        help = '请选择患者家族史中有癌症史的家属'
        )

    st.header("使用K-Means算法进行聚类")
    kmean_result = st.slider('Number of clusters (k)', min_value=2, max_value=6, value=3)
    run_kmeans_and_plot(kmean_result)

    st.header("使用随机森林预测模型")
    new_patient_data = [[50, 0.3, 0.8, 0.4]]
    rf_model = train_RandomForest()
    s = apply_RandomForest(rf_model, new_patient_data)
    st.write(s)

if __name__ == '__main__':
    main()
