from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_excel("planilha.xlsx")

x = df[['Diametro']]
y = df[['Preco']]

modelo = LinearRegression() # Como é um grafico onde é uma reta continua usamos a regressão
modelo.fit(x,y)

while True:
    try:
        diame = int(input("Digite o diametro da pizza(0 sair): "))
        if diame == 0:
            break
        if diame > 100 or diame < 10:
            print("Digite o diametro da pizza entre 10 até 100")
        else:
            print(f"Valor da pizza com o diametro {diame} eh de : {modelo.predict([[diame]])[0][0]:.2f}")
    except TypeError:
        print("Digite um valor numerico valido")