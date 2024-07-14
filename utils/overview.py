import datetime
import streamlit as st

# from utils import dict_to_dataframe, authenticate
# from utils.plotly_utils import plotly_pie, plotly_bar

st.set_page_config(
    page_title="Overview",
    page_icon="👋",
    layout="wide"
)

st.subheader("数据量概览")
overview_data = {
    "updateTime": "2023-01-01 00:00:00",
    "total": "12345614",
    "todaySeen": "12345",
    "recent7daysSeen": "1234561",
    "black": "2435"
}
overview_group_data = {
    'all': {
        'source': {
            'source1': 13467,
            'source2': 56900,
            'source3': 89580409,
            'source4': 25405
        },
        'tag1st': {
            'tag1': 1414953,
            'tag2': 3112059,
            'tag3': 48486,
            'tag4': 23226,
            'tag5': 4907815,
            'tag6': 9690544
        },
        'category': {
            'red': 1382345,
            'green': 258362
        },
        'updateTime': '2023-03-01T08:31:00.345000Z'
    },
    'recent7Days': {
        'source': {
            'source1': 245,
            'source2': 2457,
        },
        'tag1st': {
            'tag1': 12345,
            'tag3': 12345,
            'tag4': 1235,
        },
        'category': {
            'red': 1341,
            'green': 3456
        },
        'updateTime': '2023-03-01T08:31:00.345000Z'
    },
    'calculateDate': '20230301'
}

st.markdown(f"`概览统计时间：{overview_data['updateTime']}`")

recent_7_group_data = overview_group_data["recent7Days"]
all_group_data = overview_group_data["all"]
overview_group_date = overview_group_data["calculateDate"]

col1, col2, col3, col4 = st.columns(4)
col1.metric("数据总量", overview_data["total"])
col2.metric("今日生效", overview_data["todaySeen"])
col3.metric("最近7日生效", overview_data["recent7daysSeen"])
col4.metric("无效数据", overview_data["black"])

st.markdown("### 数据分类统计")
st.markdown(f"`分类数据生效时间：{datetime.datetime.strptime(overview_group_date, '%Y%m%d')}`")
date_range = st.sidebar.radio(
    "您关注哪一时间段数据？",
    ('最近七日', '全量'),
    index=1
)

display_type = st.sidebar.multiselect(
    "您想使用哪些方式展示数据？",
    ('图形', '表格'),
    default=('图形', '表格')
)

if date_range == "最近七日":
    group_data = recent_7_group_data
else:
    group_data = all_group_data

source_data = group_data["source"]
tag1st_data = group_data["tag1st"]
category_data = group_data["category"]


def write_overview_data_charts(data):
    tab1, tab2 = st.tabs(["Pie(default)", "Bar"])
    with tab1:
        fig_pie = plotly_pie(data)
        st.plotly_chart(fig_pie, use_container_width=True)
    with tab2:
        fig_bar = plotly_bar(data)
        st.plotly_chart(fig_bar, use_container_width=True)


def write_overview_data_table(data, key_name):
    tab1, tab2 = st.tabs(["table(default)", "json"])
    with tab1:
        st.dataframe(dict_to_dataframe(data, key_name), use_container_width=True)
    with tab2:
        st.json(data)


def write_overview_to_column(data, title, table_key):
    st.markdown(f"#####  {title}")
    if "图形" in display_type:
        write_overview_data_charts(data, )
    if "表格" in display_type:
        write_overview_data_table(data, key_name=table_key)


if not display_type:
    st.sidebar.error("请至少选择一种展示方式")
    st.error("请在左侧复选框选择至少一种展示方式")

if display_type:
    col5, col6, col7 = st.columns(3)
    with col5:
        write_overview_to_column(source_data, title="情报源分布", table_key="数据源")
    with col6:
        write_overview_to_column(tag1st_data, title="标签分布", table_key="标签")
    with col7:
        write_overview_to_column(category_data, title="数据类别分布", table_key="数据类别")
