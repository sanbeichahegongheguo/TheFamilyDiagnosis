import unittest
import numpy as np
from sklearn.cluster import KMeans
import sys
sys.path.append('"../utils"')
from utils.kmeansdata import apply_kmeans

class TestKMeans(unittest.TestCase):
    def setUp(self):
        # 可以在这里设置一些在每个测试之前运行的通用设置
        np.random.seed(0)
        self.data = np.random.rand(300, 2)  # 生成一些随机数据用于测试

    def test_kmeans_clustering(self):
        # 测试K-Means算法是否正确运行
        k = 3
        labels, centers = apply_kmeans(self.data, k)

        # 检查聚类中心是否在数据点的范围内
        self.assertTrue(np.all(centers >= self.data.min(axis=0)) and np.all(centers <= self.data.max(axis=0)))

        # 检查聚类标签的数量是否与预期的聚类数一致
        self.assertEqual(len(np.unique(labels)), k)

        # 检查聚类标签的合理性（例如，没有超出范围的标签）
        self.assertTrue(np.all(labels >= 0) and np.all(labels < k))

        # 可选：检查每个聚类中至少有一个点（这通常是自然的，除非数据或算法有问题）
        for i in range(k):
            self.assertTrue(np.sum(labels == i) > 0)

        # 可选：更复杂的验证，如聚类内距离小于聚类间距离（这通常不是K-Means的直接保证）
        # 这里只是给出一个概念性的示例，实际应用中可能需要更复杂的评估方法
        # 注意：以下代码只是为了说明目的，并不总是准确的评估方法
        from sklearn.metrics import pairwise_distances
        dist_matrix = pairwise_distances(self.data, metric='euclidean')
        cluster_members = [self.data[labels == i] for i in range(k)]
        intra_cluster_dists = [np.mean(pairwise_distances(cluster, metric='euclidean')) for cluster in cluster_members]
        # 这里需要额外的逻辑来计算聚类间距离，并与聚类内距离进行比较

        # 注意：上面的“聚类间距离”计算并不是直接由K-Means给出的，
        # 并且聚类间距离的定义可能因应用场景而异（例如，可以使用聚类中心之间的距离）。


        # 检查返回的标签和中心的数量是否正确
        self.assertEqual(len(labels), self.data.shape[0])
        self.assertEqual(centers.shape[0], k)

        # 你可以添加更多的断言来验证聚类结果的质量（如果需要的话）
        # 例如，检查聚类中心是否在数据点的范围内，或者检查聚类标签的合理性等

        # 这里我们简单验证聚类中心不是NaN或无穷大
        self.assertFalse(np.any(np.isnan(centers)) or np.any(np.isinf(centers)))

        # 你还可以考虑使用sklearn的评估函数来进一步验证聚类效果
        # 例如，轮廓系数（Silhouette Score）等

if __name__ == '__main__':
    unittest.main()
