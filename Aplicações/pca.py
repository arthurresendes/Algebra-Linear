import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sklearn.datasets.load_iris(return_X_y=True, as_frame=True)
X, y = iris

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns = X.columns)
iris_scaled = X_scaled.copy()
iris_scaled['target'] = y
print(iris_scaled)

sns.pairplot(iris_scaled, hue = "target")
pca = PCA()
pca.fit(X_scaled)
X_scaled_pca = pca.transform(X_scaled)
X_scaled_pca = pd.DataFrame(X_scaled_pca, columns=[f'PC{i}' for i in range(1, 5)])

iris_scaled_pca = X_scaled_pca.copy()
iris_scaled_pca['target'] = y
sns.pairplot(iris_scaled_pca, hue='target')

print(pca.explained_variance_ratio_)
plt.scatter(X_scaled_pca['PC1'], X_scaled_pca['PC2'], c=y)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()