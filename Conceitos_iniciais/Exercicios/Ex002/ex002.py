import numpy as np
import matplotlib.pyplot as plt

x1_r1 = np.array([0,10,20,30,40,50])
x1_r2 = np.array([0,10,20,30,40,50])

x2_r1 = 150 - 2 * x1_r1
x2_r2 = 30 + x1_r2

print(x2_r1)
print(x2_r2)

plt.plot(x1_r1,x2_r1,label="linha_1")
plt.plot(x1_r2,x2_r2, label="linha_2")
plt.legend()
plt.savefig("uma_solucao.png")
plt.show()