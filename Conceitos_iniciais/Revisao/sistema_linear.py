import numpy as np
import matplotlib.pyplot as plt

x1_r1 = np.array([0,10,20,30,40,50,60])
x1_r2 = np.array([0,10,20,30,40,50,60])

x2_r1 = 127.35 - x1_r1
x2_r2 = 229.24 - 2 * x1_r2

print(x2_r1)
print(x2_r2)

plt.plot(x1_r1,x2_r1 , label="casal_1")
plt.plot(x1_r2,x2_r2,label = "casal_2")
plt.legend()
plt.savefig('sem solucao.png')
plt.show()

x1_r3 = np.array([0,10,20,30,40,50])
x2_r3 = 134.85 - 2 * x1_r3
print(x2_r3)

plt.plot(x1_r1,x2_r1 , label="casal_1")
plt.plot(x1_r3,x2_r3,label = "casal_3")
plt.legend()
plt.savefig('se cruzam.png')
plt.show()