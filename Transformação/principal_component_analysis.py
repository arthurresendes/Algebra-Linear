import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import scipy

A = np.array([[-2.1 , -0.26],
              [-1.3 ,  0.22],
              [ 0.25,  1.7 ],
              [ 0.43,  2.1 ],
              [ 0.61,  2.32]])

x_1 = A[:, 0]
x_2 = A[:, 1]
print(x_1, x_2)

var_x_1 = np.var(x_1).round(2)
var_x_2 = np.var(x_2).round(2)
print(var_x_1, var_x_2)
print(np.mean(x_1), np.mean(x_2))

plt.scatter(x = x_1, y = x_2)
plt.axhline(y = 0, linestyle = '--')
plt.axvline(x = 0, linestyle = '--')
plt.xlabel(f'x_1, var={var_x_1}')
plt.ylabel(f'x_2, var={var_x_2}')
plt.show()

pca = PCA()
pca.fit(A)

A_transformed = pca.transform(A)
pc_1 = A_transformed[:, 0]
pc_2 = A_transformed[:, 1]
print(pc_1,pc_2)

var_pc_1 = np.var(pc_1).round(2)
var_pc_2 = np.var(pc_2).round(2)
print(var_pc_1,var_pc_2)

print(np.mean(pc_1), np.mean(pc_2))

plt.scatter(x=pc_1, y=pc_2)
plt.axhline(y=0, linestyle='--')
plt.axvline(x=0, linestyle='--')
plt.xlabel(f'pc_1, var={var_pc_1}')
plt.ylabel(f'pc_2, var={var_pc_2}')
plt.show()

lr = LinearRegression()
lr.fit(X = pc_1.reshape(-1, 1), y = pc_2)
print(lr.coef_, lr.intercept_)

print(pca.mean_)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_, pca.explained_variance_ratio_.sum())