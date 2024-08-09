import streamlit as st
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def apply_kmeans(data, k):
    # 应用K-Means算法
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    return kmeans.labels_, kmeans.cluster_centers_

def plot_clusters(data, labels, centers) -> None:
    plt.figure(figsize=(8, 6))
    colors = ['r', 'g', 'b', 'y', 'c', 'm']  # 假设最多6个聚类
    for i in range(len(centers)):
        # 绘制聚类中心
        plt.scatter(centers[i, 0], centers[i, 1], s=100, c='black', marker='X')
        # 绘制属于该聚类的数据点
        plt.scatter(data[labels == i, 0], data[labels == i, 1], s=50, c=colors[i])
    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()

def run_kmeans_and_plot(k) -> None:
    # 加载数据（这里简化为直接生成随机数据）
    np.random.seed(0)
    data = np.random.rand(300, 2)

    # 应用K-Means算法
    labels, centers = apply_kmeans(data, k)

    # 绘制聚类结果的图形
    # plot_clusters(data, labels, centers)


    # 显示聚类结果
    # st.write("Cluster labels:", labels)
    # st.write("Cluster centers:", centers)

    # 绘制聚类结果的图形
    st.pyplot(plot_clusters(data, labels, centers))
