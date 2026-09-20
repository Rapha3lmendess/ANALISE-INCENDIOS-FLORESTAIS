# ====================================
# IMPORTAÇÃO DAS BIBLIOTECAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.image as mpimg
import warnings

warnings.filterwarnings('ignore')

# ====================================
# LEITURA DOS DADOS
Base_Dados = pd.read_csv(
    "Dados/Dados_indendios.csv",
    encoding='latin-1'
)


# ====================================
# INFORMAÇÕES DOS DADOS
print(Base_Dados.isnull().sum())
print(Base_Dados.describe())
Base_Dados.info()
print(Base_Dados.nunique())


# ====================================
# ANÁLISE POR ANO
Analise = (
    Base_Dados
    .groupby('year')['number']
    .sum()
    .reset_index()
)


# ====================================
# ANÁLISE POR MÊS
Analise_02 = (
    Base_Dados
    .groupby(['year', 'month'])['number']
    .sum()
    .reset_index()
)


# ====================================
# ANÁLISE POR ESTADO
Analise_03 = (
    Base_Dados
    .groupby('state')['number']
    .sum()
    .reset_index()
    .sort_values('number', ascending=False)
)


# ====================================
# TOP 10 ESTADOS
Lista_Top10 = Analise_03['state'][0:10].values

print('Top 10 estados:')
print(Lista_Top10)


# ====================================
# ANÁLISE GEOGRÁFICA
Estados = (
    Analise_03
    .sort_values('state')['state']
    .values
)

Valores = (
    Analise_03
    .sort_values('state')['number']
    .values
)

Lat = [
    -8.77, -9.71, 1.41, -3.07, -12.96,
    -3.71, -15.83, -19.19, -16.64, -2.55,
    -12.64, -18.10, -7.06, -5.53, -8.28,
    -8.28, -22.84, -11.22, 1.89, -27.33,
    -23.55, -10.90, -10.25
]

Log = [
    -70.55, -35.73, -51.77, -61.66, -38.51,
    -38.54, -47.86, -40.34, -49.31, -44.30,
    -55.42, -44.38, -35.55, -52.29, -35.07,
    -43.68, -43.15, -62.80, -61.22, -49.44,
    -46.64, -37.07, -48.25
]

Dicionario = {
    'Estados': Estados,
    'Latitude': Lat,
    'Longitude': Log,
    'Incendios': Valores
}

Analise_Gografica = pd.DataFrame(Dicionario)

print(Analise_Gografica.head())


# ====================================
# CRIAÇÃO DO RELATÓRIO
fig_relatorio = plt.figure(
    figsize=(16, 16),
    constrained_layout=True
)

grade = fig_relatorio.add_gridspec(
    3,
    4,
    height_ratios=[1, 1, 1.25]
)


# ====================================
# GRÁFICO DE INCÊNDIOS POR ANO
grafico_ano = fig_relatorio.add_subplot(
    grade[0, 0:2]
)

grafico_ano.set_title(
    'Total de incêndios no Brasil: 1997 - 2017',
    loc='left',
    fontsize=13
)

sns.lineplot(
    data=Analise,
    x='year',
    y='number',
    color='#FF5555',
    lw=2,
    ax=grafico_ano
)

grafico_ano.set_xlabel('Período')
grafico_ano.set_ylabel('Quantidade de incêndios')


# ====================================
# GRÁFICO DE INCÊNDIOS POR MÊS
grafico_mes = fig_relatorio.add_subplot(
    grade[0, 2:4]
)

grafico_mes.set_title(
    'Incêndios por mês',
    loc='left',
    fontsize=13
)

sns.boxplot(
    data=Analise_02,
    x='month',
    y='number',
    palette='coolwarm',
    saturation=1,
    width=0.8,
    linewidth=1.5,
    ax=grafico_mes
)

grafico_mes.set_xlabel('Mês')
grafico_mes.set_ylabel('Número de incêndios')

grafico_mes.tick_params(
    axis='x',
    rotation=45
)


# ====================================
# GRÁFICO DE INCÊNDIOS POR ESTADO
grafico_estado = fig_relatorio.add_subplot(
    grade[1, 0:2]
)

grafico_estado.set_title(
    'Estados com maior número de incêndios',
    loc='left',
    fontsize=13
)

grafico_estado.bar(
    Analise_03['state'],
    Analise_03['number'],
    color='#f44e3f'
)

grafico_estado.set_xlabel('Estado')
grafico_estado.set_ylabel('Quantidade de incêndios')

grafico_estado.tick_params(
    axis='x',
    rotation=90,
    labelsize=8
)


# ====================================
# GRÁFICO DOS TOP 10 ESTADOS
grafico_top10 = fig_relatorio.add_subplot(
    grade[1, 2:4]
)

grafico_top10.set_title(
    'Top 10 estados com maior número de incêndios',
    loc='left',
    fontsize=13
)

Paleta_Cores = sns.color_palette(
    'inferno',
    10
)

for posicao, estado in enumerate(Lista_Top10):

    filtro_estado = Base_Dados.loc[
        Base_Dados['state'] == estado
    ]

    analise_estado = (
        filtro_estado
        .groupby('year')['number']
        .sum()
        .reset_index()
    )

    sns.lineplot(
        data=analise_estado,
        x='year',
        y='number',
        color=Paleta_Cores[posicao],
        lw=1.8,
        ax=grafico_top10
    )

grafico_top10.set_xlabel('Ano')
grafico_top10.set_ylabel('Quantidade de incêndios')

grafico_top10.legend(
    Lista_Top10,
    fontsize=7,
    ncol=2,
    loc='upper left'
)

# ====================================
# VISÃO GEOGRÁFICA DOS INCÊNDIOS
grafico_mapa = fig_relatorio.add_subplot(
    grade[2, :]
)

mapa = mpimg.imread('5.PNG')

grafico_mapa.imshow(
    mapa,
    aspect='equal'
)

grafico_mapa.set_title(
    'Visão Geográfica dos Incêndios',
    loc='left',
    fontsize=13
)

grafico_mapa.axis('off')

# ====================================
# TÍTULO DO RELATÓRIO
fig_relatorio.suptitle(
    ' Análise de Dados\n'
    'Projeto Análise de Incêndios Florestais no Brasil',
    fontsize=20,
    fontweight='bold'
)
# ====================================
# RODAPÉ DO RELATÓRIO

fig_relatorio.text(
    0.5,
    0.01,
    '\nEsse relatório foi elaborado para meu estudo de Python lendo dados',
    ha='center',
    va='bottom',
    fontsize=10
)
plt.show()