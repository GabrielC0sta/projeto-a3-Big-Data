import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
data = pd.read_csv('consumo de energia .csv')



data['NumDispositivosEletronicos'] = data['NumDispositivosEletronicos'].str.extract(r'(\d+ até \d+)')


#Histograma para Distribuição do Número de Dispositivos Eletrônicos
plt.figure(figsize=(8, 6))
data['NumDispositivosEletronicos'].value_counts().plot(kind='bar')
plt.xlabel('Número de Dispositivos Eletrônicos')
plt.ylabel('Contagem')
plt.title('Distribuição do Número de Dispositivos Eletrônicos')
plt.tight_layout()
plt.show()



#Gráfico de Pizza para a Participação das Categorias de Tipo de Residência

plt.figure(figsize=(8, 6))
data['TipoResidencia'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Participação das Categorias de Tipo de Residência')
plt.tight_layout()
plt.show()

#Gráfico de Barras para Distribuição de Contas de Luz Caras por Região

plt.figure(figsize=(10, 6))
data[data['ContaLuzCara'] == 'Sim']['Região'].value_counts().plot(kind='bar')
plt.xlabel('Região')
plt.ylabel('Contagem de Contas de Luz Caras')
plt.title('Distribuição de Contas de Luz Caras por Região')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico de Barras para Número de Dispositivos Eletrônicos por Tipo de Residência

data['NumDispositivosEletronicos'].value_counts().plot(kind='bar', figsize=(8, 6))
plt.title('Distribuição de Dispositivos Eletrônicos')
plt.xlabel('Faixa de Dispositivos Eletrônicos')
plt.ylabel('Contagem')
plt.show()

#Gráfico de Pizza para Energia Alternativa nas Residências

plt.figure(figsize=(8, 8))
data['EnergiaAlternativa'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Uso de Energia Alternativa nas Residências')
plt.tight_layout()
plt.show()

#Gráfico de Barras para Automatização Residencial por Região
plt.figure(figsize=(10, 6))
data[data['AutomacaoResidencial'] == 'Sim']['Região'].value_counts().plot(kind='bar')
plt.xlabel('Região')
plt.ylabel('Contagem de Automação Residencial')
plt.title('Automação Residencial por Região')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico de Pizza para Esforço em Economizar Energia
plt.figure(figsize=(8, 8))
data['EsforcoEconomizar'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Esforço em Economizar Energia')
plt.tight_layout()
plt.show()

# Filtrar os dados para considerar apenas 'Enel' como Provedor de Energia
enel_data = data[data['ProvedorEnergia'] == 'Enel']
#Gráfico de Barras para Provedor de Energia por Tipo de Residência
plt.figure(figsize=(10, 6))
enel_data['TipoResidencia'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição do Provedor de Energia Enel por Tipo de Residência')
plt.ylabel('')
plt.tight_layout()
plt.show()

#Gráfico de Barras para Gasto Mensal de Luz por Tipo de Residência
plt.figure(figsize=(10, 6))
data.groupby('TipoResidencia')['GastoMensalLuz'].value_counts().unstack().plot(kind='bar')
plt.xlabel('Tipo de Residência')
plt.ylabel('Contagem de Gasto Mensal de Luz')
plt.title('Gasto Mensal de Luz por Tipo de Residência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Gasto Mensal de Luz')
plt.show()

#Gráfico de Barras para Distribuição de Número de Pessoas por Região
plt.figure(figsize=(8, 6))
data['NumPessoas'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Número de Pessoas por Residência')
plt.xlabel('Número de Pessoas')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Gráfico de barras para ContaLuzCara
plt.figure(figsize=(8, 6))
data['ContaLuzCara'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribuição de Conta de Luz Cara')
plt.xlabel('Faixa de Conta de Luz')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






