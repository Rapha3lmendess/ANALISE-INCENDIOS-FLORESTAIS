# Libs para Modelagem e Matrizes
import numpy as np
import pandas as pd

# Libs para análise gráfica
import matplotlib.pyplot as plt
import seaborn as sns

# Lib para ignorar avisos
import warnings

# Desabilitando avisos
warnings.filterwarnings('ignore')

# Lendo os dados
Base_Dados = pd.read_csv(
    "Dados/Dados_Indendio.csv",
    encoding='latin-1'
)

# Nulos
Base_Dados.isnull().sum()

# Estatísticas
Base_Dados.describe()

# Info
Base_Dados.info()

# Campos únicos
Base_Dados.nunique()


# --------------------------------------------------
# ANÁLISE POR ANO DOS INCÊNDIOS
# --------------------------------------------------

Analise = Base_Dados.groupby(by=['year']).sum().reset_index()

Analise.head()


# --------------------------------------------------
# GRÁFICOS
# --------------------------------------------------

# Criando uma única figura
plt.figure(figsize=(18, 6))


# GRÁFICO 1 - CAMPOS NULOS
plt.subplot(1, 2, 1)

plt.title('Análise de campos nulos')

sns.heatmap(
    Base_Dados.isnull(),
    cbar=False
)


# GRÁFICO 2 - INCÊNDIOS POR ANO
plt.subplot(1, 2, 2)

plt.title(
    'Total de incêndios no Brasil: 1998 - 2017',
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


# Organizar os gráficos
plt.tight_layout()

# Mostrar os gráficos
plt.show()