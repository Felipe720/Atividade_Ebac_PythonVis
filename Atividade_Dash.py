import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc


df = pd.read_csv('ecommerce_estatistica.csv')

corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Qtd_Vendidos_Cod']].corr()

#Heatmap para Correlação
grafHP = px.imshow(corr,
                text_auto=".2f",
                color_continuous_scale="viridis",
                title="Mapa de Calor da Correlação entre Variáveis",
                labels=dict(color="Correlação")
               )

#Gráficos para DF

#Densidade
graf0 = px.histogram(df, x='Nota', histnorm='density', marginal='rug', nbins=20, title='Densidade de Notas')


#Histograma
graf1 = px.histogram(df, x='Nota', nbins=20, title='Histograma - Distribuição de Notas')


#Dispersão
graf2 = px.scatter(df,x='Nota', y='Preço')
graf2.update_layout(title='Dispersão entre Preço e Nota')


#Pizza
graf3 = px.pie(df, names='Gênero', color='Gênero', hole=0.1, color_discrete_sequence=px.colors.sequential.RdBu)


#Gráfico de Barra
df_genero = df['Gênero'].value_counts().reset_index()
df_genero.columns = ['Gênero', 'Quantidade']

graf4 = px.bar(df_genero, x='Gênero',y='Quantidade', color='Gênero', color_discrete_sequence=px.colors.qualitative.Bold)
graf4.update_layout(
    title='Quantidade de Peças por Gênero',
    xaxis_title=None,
    yaxis_title='Quantidade',
    legend_title='Roupas por Gênero',
    plot_bgcolor='rgba(222,255,253,1)', #Fundo Interno
    paper_bgcolor='rgba(186,245,241,1)' #Fundo Externo
)


#Criar App
app=Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=grafHP),
    dcc.Graph(figure=graf0),
    dcc.Graph(figure=graf1),
    dcc.Graph(figure=graf2),
    dcc.Graph(figure=graf3),
    dcc.Graph(figure=graf4)
])

#Executa App
app.run_server(debug=True, port=8050) #Default 8050