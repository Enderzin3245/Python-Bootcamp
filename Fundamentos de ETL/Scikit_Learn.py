#Biblioteca Scikit Learn / / / /

#dispõe de ferramentas simples e eficientes

#Construida sobre os pacotes NumPy, ScriPy e matplotlib

#ele e usado para a pratica de machine learning
#criação de modelos para anasile 

#Ex:

#massa de dados com 200 observações, com apenas uma variável preditora, 
# que será a variável x e a variável target, que será a y. Para isso 
# indicamos os parâmetros n_samples = 200 e n_features = 1.

from sklearn.datasets import make_regression
# gerando uma massa de dados:
x, y = make_regression(n_samples=200, n_features=1, noise=30)
#o codigo gerará um banco com 200 informações completamente diferentes