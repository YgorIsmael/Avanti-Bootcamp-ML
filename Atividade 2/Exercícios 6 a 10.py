
# Exercício 6 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Observe os espaços sublinhados e complete o código
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')
fig.suptitle('plt.subplots()')

# Exercício 7 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Observe os espaços sublinhados e complete o código
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

# Exercício 8 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
# Passo 1: importar o pandas:
import pandas as pd
# Ler o arquivo CSV: utilizando a função pd.read_csv() para ler o arquivo CSV.
df = pd.read_csv('caminho/do/arquivo.csv')
# Exibir as primeiras linhas: usando o método .head() do DataFrame.
print(df.head())

# Exercício 9 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um DataFrame com base em uma condição?
# Passo 1: selecionar a coluna 'Nome' (exemplo):
coluna_nome = df['Nome']
# Passo 2: filtrar linhas com base em uma condição:
df_filtrado = df[df['Idade'] > 50]
# Passo 3: mostrar os dados filtrados:
print("Coluna 'Nome':")
print(coluna_nome)
print("\nDataFrame filtrado:")
print(df_filtrado)

# Exercício 10 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
# Há diversos método para lidar com valores ausentes, mas podemos removê-los por exemplo:
# Passo 1: definir DataFrame:
df = pd.DataFrame(dados)
# Passo 2: identificar valores ausentes:
print(df.isna())
# Passo 3: remover linhas que têm valores ausentes:
df_sem_nas = df.dropna()
print(df_sem_nas)
# Passo 4: remover colunas que têm valores ausentes:
df_sem_nas_colunas = df.dropna(axis=1)
print(df_sem_nas_colunas)