# 导入NumPy库
import numpy as np

# 定义矩阵A和矩阵B
A = np.array([[1, 0], [0, 1]])
B = np.array([[4, 1], [2, 2]])

# 计算矩阵A和矩阵B的乘积，得到矩阵C
C = np.dot(A, B)

# 计算矩阵C的逆矩阵，得到矩阵D
D = np.linalg.inv(C)

# 输出矩阵C和矩阵D
print(C)
print(D)