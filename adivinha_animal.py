from sklearn.svm import LinearSVC
import numpy as np


gato1 = np.array([1,0,2])
gato2 = np.array([1,0,0])

dog1 = np.array([1,1,1])
dog2 = np.array([1,2,2])

galo1 = np.array([0,1,0])
galo2 = np.array([0,0,0])

treino_x = [gato1,gato2,dog1,dog2,galo1,galo2]
treino_y = [0,0,1,1,2,2]

modelo = LinearSVC() # Usamos esse pois separa por 'etiquetas'
modelo.fit(treino_x,treino_y)

res = modelo.predict([np.array([1,0,2])])

if res == 0:
    print("Gato")
elif res ==1:
    print("Cachorro")
elif res == 2:
    print("Galo")
else:
    print("Nao identificado")