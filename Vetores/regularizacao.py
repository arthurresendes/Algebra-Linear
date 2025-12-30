import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge

coef_x1 = 2.5
coef_x2 = -1.8
coef_x3 = 0.05
intercept = 3.0

# Gerar sempre os mesmo numeros aleatorios
np.random.seed(10)

x1 = np.random.uniform(0,10, size = 10)
x2 = np.random.uniform(0,10, size = 10)
x3 = np.random.uniform(0,10, size = 10)
print(x1)
print(x2)
print(x3)

y = coef_x1 * x1 + coef_x2 * x2 +coef_x3 * x3 + intercept
unindo_variaveis = np.column_stack((x1,x2,x3))

print(unindo_variaveis)
print(unindo_variaveis.shape)
print(y)

# OLS
modelo = LinearRegression()
modelo.fit(unindo_variaveis,y)
print(modelo.coef_)
print(modelo.intercept_)

# L1
model_lasso =  Lasso()
model_lasso.fit(unindo_variaveis,y)
print(model_lasso.coef_)
print(model_lasso.intercept_)

# L2
model_ridge =  Ridge()
model_ridge.fit(unindo_variaveis,y)
print(model_ridge.coef_)
print(model_ridge.intercept_)