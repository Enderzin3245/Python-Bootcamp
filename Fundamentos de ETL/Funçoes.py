#visualização

#todos os metodos e funções são iguais ou semelhantes ao do Colab
#valores ausentes(nao possuem valores) = NaN

df.head(n=4)
#visualizar 4 linhas
df.shape()
#informa linhas e colunas
df.info()
#informa os formatos dos dados de cada coluna
df.isnull().sum()
#contar a quantidade de valores nulos
df['culuna'].unique()
#informa valores unicos da coluna

#podemos gerar informações graficas usando a biblioteca
#matplotlib.axes
#utilizando codigos e funções

df.describe()
#retorna a soma de todos os valores das colunas