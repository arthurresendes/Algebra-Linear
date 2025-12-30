import numpy as np
import matplotlib.pyplot as plt


vetor = np.array([7.5,8.25])
print(f"Valores do vetor: {vetor}")
print(f"Valor do tipo: {vetor.ndim}")
print(f"Quntas linhas e colunas: {vetor.shape}")
print(f"Quantos elementos: {vetor.size}")

# plt.scatter(x=vetor[0],y=vetor[1])
plt.scatter(*vetor)
plt.show()

plt.scatter(*vetor)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()

plt.scatter(*vetor)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.arrow(0,0,*vetor,length_includes_head = True, head_width=0.25)
plt.show()