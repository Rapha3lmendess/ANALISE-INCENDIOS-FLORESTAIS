# ==============================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# =====================
# 2. LEITURA DOS DADOS

Base_Dados = pd.read_csv(
    "Dados/Dados_indendios.csv",
    encoding='latin-1'
)
# =====================
# 3. ANÁLISE DOS DADOS

# Campos nulos
print(Base_Dados.isnull().sum())

# Estatísticas
print(Base_Dados.describe())

# Informações
Base_Dados.info()

# Quantidade de valores únicos
print(Base_Dados.nunique())

# ===========================
# 4. GRÁFICO DE CAMPOS NULOS

plt.figure(figsize=(14, 5))

plt.title('Análise de campos nulos')

sns.heatmap( Base_Dados.isnull(), cbar=False)

# ================================
# 5. ANÁLISE DE INCÊNDIOS POR ANO

Analise = (
    Base_Dados
    .groupby('year')['number']
    .sum()
    .reset_index()
)
print(Analise.head())

plt.figure(figsize=(12, 5))

plt.style.use('ggplot')

plt.title(
    'Total de incêndios no Brasil 1997-2017',
    loc='left',
    fontsize=14
)

sns.lineplot(
    data=Analise,
    x='year',
    y='number',
    lw=2,
    color='#ff5555',
    alpha=0.85
)

plt.xlabel('Ano')
plt.ylabel('Quantidade de incêndios')

plt.tight_layout()
plt.show()

# ================================
# 6. ANÁLISE DE INCÊNDIOS POR MÊS
# analise por ano dos incendios
Analise_02 = Base_Dados.groupby( by=['year', 'month'] ).sum().reset_index()
Analise_02.head()

# Tamanho
plt.figure( figsize=(12, 5) )

# Grafico
plt.title( 'Indêncidios por mês', loc='left', fontsize=14 )
sns.boxplot( data=Analise_02, x='month', y='number', palette='coolwarm', saturation=1, width=0.9, linewidth=2,
            order=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] )

# Labels
plt.xlabel('Mês')
plt.ylabel('Número de incêndios');

# ===================================
# 7. ANÁLISE DE INCÊNDIOS POR ESTADO

Analise_03 = (
    Base_Dados
    .groupby('state')['number']
    .sum()
    .reset_index()
    .sort_values('number', ascending=False)
)
print(Analise_03.head())

plt.figure(figsize=(12, 5))

plt.title(
    'Estados com maior número de incêndios',
    loc='left',
    fontsize=14
)

plt.bar(
    Analise_03['state'],
    Analise_03['number'],
    color='#900e03'
)

plt.ylabel('Quantidade')
plt.xlabel('Estado')

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# ======================================
# 8. TOP 10 ESTADOS COM MAIS INCÊNDIOS

Lista_Top10 = Analise_03['state'][0:10].values

print('Top 10 estados:')
print(Lista_Top10)


plt.figure(figsize=(12, 5))

plt.title(
    'TOP 10 ESTADOS COM INCÊNDIOS',
    loc='left',
    fontsize=14
)


# Loop pelos 10 estados
for Coluna in Lista_Top10:

    # Filtrar estado
    Filtro = Base_Dados.loc[ Base_Dados['state'] == Coluna]

    # Agrupar por ano
    Analise_Local = (
        Filtro
        .groupby('year')['number']
        .sum()
        .reset_index()
    )

    # Gráfico
    sns.lineplot(
        data=Analise_Local,
        x='year',
        y='number',
        lw=2,
        alpha=0.85
    )

plt.xlabel('Período')
plt.ylabel('Número de incêndios')

plt.legend(
    Lista_Top10,
    bbox_to_anchor=(1, 0.7)
)

plt.tight_layout()
plt.show()


# =======================
# 9. ANÁLISE GEOGRÁFICA


# Estados em ordem alfabética
Estados = (
    Analise_03 .sort_values('state')['state'] .values)

# Quantidade de incêndios
Valores = (
    Analise_03
    .sort_values('state')['number']
    .values
)

# Latitudes
Lat = [ -8.77, -9.71, 1.41, -3.07, -12.96, -3.71, -15.83, -19.19, -16.64, -2.55, -12.64, -18.10, -7.06, -5.53, -8.28,
       -8.28, -22.84, -11.22, 1.89, -27.33,-23.55, -10.90, -10.25]


# Longitudes
Log = [-70.55, -35.73, -51.77, -61.66, -38.51, -38.54, -47.86, -40.34, -49.31, -44.30, -55.42, -44.38, -35.55, -52.29, -35.07,
    -43.68, -43.15, -62.80, -61.22, -49.44, -46.64, -37.07, -48.25]


# Criando dicionário
Dicionario = {
    'Estados': Estados,
    'Latitude': Lat,
    'Longitude': Log,
    'Incendios': Valores
}
# Criando DataFrame geográfico
Analise_Gografica = pd.DataFrame(Dicionario)
print(Analise_Gografica.head())

# =============================
# 10. MAPA DE CALOR GEOGRÁFICO

import plotly.express as px
fig = px.density_map(
    Analise_Gografica,
    lat='Latitude',
    lon='Longitude',
    z='Incendios',
    radius=30,
    center=dict(
        lat=-12.700,
        lon=-46.5555
    ),
    zoom=3,
    map_style='open-street-map'
)
fig.show()