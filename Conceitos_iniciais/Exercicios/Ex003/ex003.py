import numpy as np
import matplotlib.pyplot as plt

x1_r1 = np.array([0,10,20,30,40,50,60])
x1_r2 = np.array([0,10,20,30,40,50,60])

'''
y= 200 + 3x -> Ok

2y=400 - 6x 
2y/2 = (400 -6x)/2
y = 200 - 3x -> Ok
'''

x2_r1 = 200 - 3 * x1_r1 
x2_r2 = 200 - 3 * x1_r2 

print(x2_r1)
print(x2_r2)

plt.plot(x1_r1,x2_r1,label="linha_1")
plt.plot(x1_r2,x2_r2, label="linha_2")
plt.legend()
plt.savefig("infinitas_solucoes.png")
plt.show()