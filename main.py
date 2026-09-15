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

# Gráfico dos valores nulos
plt.subplot(1,2,1)
plt.figure( figsize=(14,5))
plt.title ('Analise de campos nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False);



# Estasticias
Base_Dados.describe()
#info
Base_Dados.info()

# campos unicos
Base_Dados.nunique()

# analise por ano dos incendios
Analise = Base_Dados.groupby(by=['year']).sum().reset_index()
Analise.head()

# tamanho
plt.figure( figsize= (12,5))
#grafico de anos de incendio
plt.subplot(1,2,2)
plt.title(' Total indencios no brasil 1997 - 2017', loc='left', fontsize=14)
sns.lineplot( data=Analise, x='year', y='number', estimator='sum', lw=2, color='#ff5555', alpha=0.85 );


#labels
plt.xlabel('quantidade')
plt.ylabel('periodo'); 
plt.tight_layout()
plt.show()#