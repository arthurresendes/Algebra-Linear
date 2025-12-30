import numpy as np
import matplotlib.pyplot as plt

vetor = np.array([7.5,8.25])
vetor_i = np.array([1,0])
vetor_j = np.array([0,1])

plt.arrow(0,0, *vetor_i, width=0.01,length_includes_head = True, head_width=0.25)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()

plt.arrow(0,0, *vetor_j,width=0.01,length_includes_head = True, head_width=0.25)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.show()

vetor_b = np.array([-4.125,3.75])
plt.figure(figsize=(5,5))
plt.arrow(0,0, *vetor, width=0.01,length_includes_head = True, head_width=0.25)
plt.arrow(0,0, *vetor_b, width=0.01,length_includes_head = True, head_width=0.25)
x_min,x_max = plt.xlim()
y_min,y_max = plt.ylim()
plt.xlim(min(x_min,y_min), max(x_max,y_max))
plt.ylim(min(x_min,y_min), max(x_max,y_max))
plt.show()

verifica_ortogonal = np.dot(vetor,vetor_b)
if verifica_ortogonal == 0.0:
    print("Ortogonal")

verifica_ortonormal1 = np.linalg.norm(vetor,ord=2)
verifica_ortonormal2 = np.linalg.norm(vetor_b,ord=2)

if verifica_ortonormal1 == verifica_ortonormal2:
    print("Ortonormal")