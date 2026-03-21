"""
Titanic Dataset - Exploratory Data Analysis (EDA)

Author: Marco Antonio Ponciano

Description
-----------
Este repositório foi criado com fins educacionais e de estudo em Python
aplicado à Análise Exploratória de Dados (EDA).

O objetivo é praticar conceitos fundamentais utilizados por analistas
de dados, incluindo:

- Manipulação de dados com Pandas
- Operações numéricas com NumPy
- Estatísticas descritivas
- Filtros e seleção de dados
- Visualização de dados com Matplotlib e Seaborn

Este código tem como objetivo ser um projeto que demonstra o processo de 
aprendizado e prática com datasets reais.

Dataset utilizado
-----------------
Titanic passenger dataset.

Bibliotecas utilizadas
----------------------
numpy
pandas
matplotlib
seaborn
"""

# ============================================================
# Importação de bibliotecas
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração padrão para gráficos
sns.set_theme(style="whitegrid")

# ============================================================
# Exemplo simples de uso do NumPy
# ============================================================

print("Exemplo de operação com NumPy:")
print(np.sqrt(144))
print(np.sqrt(188))

# ============================================================
# Importação do dataset
# ============================================================

# O dataset pode estar na pasta do projeto
# Ajuste o caminho se necessário

titanic = pd.read_excel("titanic.xlsx")

# ============================================================
# Exploração inicial do dataset
# ============================================================

print("\nInformações do dataset:")
print(titanic.info())

print("\nPrimeiras linhas do dataset:")
print(titanic.head())

# ============================================================
# Seleção de variáveis
# ============================================================

classe = titanic["classe"]

selecao_variaveis = titanic[["sobreviveu", "classe", "sexo"]]

# Removendo coluna que não será utilizada
selecao_variaveis = selecao_variaveis.drop(columns=["classe"])

# ============================================================
# Filtros e seleção de observações
# ============================================================

# Passageiros que sobreviveram
sobreviventes = titanic[titanic["sobreviveu"] == "sim"]

# Homens adultos
homens_adultos = titanic[
    (titanic["sexo"] == "masculino") & (titanic["idade"] >= 18)
]

# Mulheres ou crianças
mulheres_ou_criancas = titanic[
    (titanic["sexo"] == "feminino") | (titanic["idade"] < 18)
]

# Passageiros sem parentes
passageiros_sozinhos = titanic[
    (titanic["irmaos_conjuges"] == 0) &
    (titanic["pais_filhos"] == 0)
]

# Tarifas acima de 100 embarcando em Cherbourg
tarifas_altas = titanic[
    (titanic["valor_tarifa"] > 100) &
    (titanic["embarque"] == "Cherbourg")
]

# ============================================================
# Limpeza de dados
# ============================================================

# Remoção de coluna com muitos valores faltantes
titanic_limpo = titanic.drop(columns=["nivel_cabine"]).dropna()

print("\nDimensão do dataset após limpeza:")
print(titanic_limpo.shape)

# ============================================================
# Estatísticas descritivas
# ============================================================

print("\nFrequência de sobrevivência:")
print(titanic["sobreviveu"].value_counts())

print("\nPercentual de sobrevivência:")
print(titanic["sobreviveu"].value_counts(normalize=True))

print("\nEstatísticas da idade:")
print(titanic["idade"].describe())

print("\nEstatísticas de idade e tarifa:")
print(titanic[["idade", "valor_tarifa"]].describe())

# ============================================================
# Estatísticas agrupadas
# ============================================================

print("\nTarifa média por classe:")
print(
    titanic[["classe", "valor_tarifa"]]
    .groupby("classe")
    .mean()
)

print("\nPercentual de sobreviventes por sexo:")
print(
    titanic[["sobreviveu", "sexo"]]
    .groupby("sexo")["sobreviveu"]
    .value_counts(normalize=True)
)

# ============================================================
# Visualização de dados
# ============================================================

# Gráfico de contagem de sobreviventes
plt.figure()
sns.countplot(data=titanic, x="sobreviveu")
plt.title("Contagem de Sobreviventes")
plt.xlabel("Sobreviveu")
plt.ylabel("Contagem")
plt.show()

# Gráfico por sexo
plt.figure()
sns.countplot(data=titanic, x="sobreviveu", hue="sexo")
plt.title("Sobrevivência por Sexo")
plt.show()

# Histograma de idade
plt.figure()
sns.histplot(data=titanic, x="idade", bins=20, kde=True)
plt.title("Distribuição de Idade")
plt.show()

# Scatterplot idade vs tarifa
plt.figure()
sns.scatterplot(
    data=titanic[titanic["valor_tarifa"] < 100],
    x="idade",
    y="valor_tarifa",
    hue="classe"
)
plt.title("Idade vs Tarifa")
plt.show()

# ============================================================
# Boxplot da idade
# ============================================================

plt.figure()
sns.boxplot(y=titanic["idade"])

minimo = titanic["idade"].min()
q1 = titanic["idade"].quantile(0.25)
q2 = titanic["idade"].median()
q3 = titanic["idade"].quantile(0.75)
maximo = titanic["idade"].max()

plt.text(0, minimo, f"Min = {minimo}", ha="center")
plt.text(0, q1, f"Q1 = {q1:.1f}", ha="center")
plt.text(0, q2, f"Mediana = {q2:.1f}", ha="center")
plt.text(0, q3, f"Q3 = {q3:.1f}", ha="center")
plt.text(0, maximo, f"Max = {maximo}", ha="center")

plt.title("Boxplot da Idade")
plt.show()

print("\nAnálise exploratória finalizada.")