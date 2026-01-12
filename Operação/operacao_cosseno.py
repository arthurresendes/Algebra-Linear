import numpy as np
import ploty
import plotly.graph_objects as go

print("Regra do cosseno")
array1 =  np.array([2,1,0])
array2 =  np.array([3,4,5])
dot_product = np.dot(array1,array2)
print(dot_product)

len_1 = np.linalg.norm(array1)
len_2 = np.linalg.norm(array2)
print(len_1,len_2)

cos_theta = dot_product / (len_1 * len_2)
print(cos_theta)
print(f"Angulo entre os dois vetores (radiandos): {np.arccos(cos_theta)}")
print(f"Angulo entre os dois vetores (grau): {np.rad2deg(cos_theta)}")

vetores = [array1,array2]
fig = go.Figure()

for i , vec in enumerate(vetores,start=1):
    fig.add_trace(go.Scatter3d(
        x = [0, vec[0]],
        y = [0, vec[1]],
        z = [0, vec[2]],
        mode="lines",
        line = dict(width=3),
        name = 'array_' + str(i)
    ))

fig.show()
