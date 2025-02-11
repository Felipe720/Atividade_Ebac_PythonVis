import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')

print(df.dtypes)


corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Qtd_Vendidos_Cod']].corr()

#Heatmap para Correlação
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

#Gráficos para DF

#Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
plt.title('Densidade de Notas')
plt.xlabel('Nota')
plt.show()

#Histograma
plt.figure(figsize=(10,6))
plt.hist(df['Nota'], bins=100, color='blue', alpha=0.8)
plt.title('Histograma - Distribuição de Notas')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


#Dispersão
sns.jointplot(x='Nota', y='Preço', data=df, kind='scatter')
plt.show()


#Pizza
def pct_ajuste(pct):
    return ('%.1f%%' % pct) if pct > 4 else ''
plt.figure(figsize=(10,6))
plt.pie(df['Gênero'].value_counts().values, autopct=pct_ajuste, startangle=90)
plt.legend(df['Gênero'].value_counts().index)
plt.title('Distribuição dos Gêneros das Roupas')
plt.tight_layout()
plt.show()

#Barras
cores = ["#1f77b4", "#ff7f0e", "#2ca02c",'#278f65', '#863e9c','#34c289', '#e61bb5', '#0d26f7', '#4da051']
sns.barplot(x=df['Gênero'].value_counts().index,y=df['Gênero'].value_counts().values, hue=df['Gênero'].value_counts().index,legend=True, palette = cores).set_xticklabels([])
plt.title("Quantidade de Peças por Gênero")
plt.ylabel('Quantidade')
plt.show()

#Regressão
sns.regplot(x='N_Avaliações', y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color':'#34c289'})
plt.title('Regressão de Quantidade de vendidos por Numero de Avaliações')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade Vendidos')
plt.show()