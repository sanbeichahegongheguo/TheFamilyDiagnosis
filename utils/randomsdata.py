import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data():
    # 假设你已经有了一个DataFrame df，其中包含列'age', 'a', 'b', 'c', 'label'
    # 这里我们使用一些随机数据来模拟
    data = {
        'age': [25, 35, 45, 55, 65] * 10,
        'a': [0.1, 0.2, 0.3, 0.4, 0.5] * 10,
        'b': [0.6, 0.7, 0.8, 0.9, 1.0] * 10,
        'c': [0.2, 0.3, 0.4, 0.5, 0.6] * 10,
        'label': [0, 1] * 25
    }

    df = pd.DataFrame(data)

    # 划分数据集
    X = df[['age', 'a', 'b', 'c']].values  # 特征
    y = df['label'].values  # 标签
    return train_test_split(X, y, test_size=0.2, random_state=42)


@st.cache_resource
def train_RandomForest():
    # 训练随机森林模型
    X_train, X_test, y_train, y_test = load_data()
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # 模型评估
    y_pred = rf_model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classi   fication Report:\n", classification_report(y_test, y_pred))
    return rf_model

# def apply_RandomForest():

def apply_RandomForest(rf_model, new_patient_data) -> None:
    # 使用模型进行预测
    # rf = apply_RandomForest()
    prediction = rf_model.predict_proba(new_patient_data)
    print(prediction[0][0])
    return "结果预测: 患有癌症的概率: {:.2f}%.没有癌症的概率: {:.2f}%.".format(prediction[0][0]*100, prediction[0][1]*100)


if __name__ == "__main__":
    new_patient_data = [[50, 0.3, 0.8, 0.4]]
    rf_model = train_RandomForest()
    s = apply_RandomForest(rf_model, new_patient_data)
    print(s)
