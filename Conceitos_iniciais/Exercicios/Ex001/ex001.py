import numpy as np
import matplotlib.pyplot as plt

x1_r1 = np.array([0,10,20,30,40,50,60])
x1_r2 = np.array([0,10,20,30,40,50,60])

x2_r1 = 100 - x1_r1
x2_r2 = 80 - x1_r2

plt.plot(x1_r1,x2_r1,label="linha_1")
plt.plot(x1_r2,x2_r2, label="linha_2")
plt.legend()
plt.savefig("sem_solucao1.png")
plt.show()