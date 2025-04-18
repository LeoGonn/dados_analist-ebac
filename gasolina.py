# Criando DataFrame do arquivo gasolina.csv
import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv', sep=',')
df = df.rename(columns={"dia": "Dia", "venda": "Venda"})

# Protando gráfico
with sns.axes_style('darkgrid'):
  grafico_gasolina= sns.lineplot(data=df, x="Dia", y="Venda", palette="pastel")
  grafico_gasolina.set(title='Preço da gasolina na cidade de SÃO PAULO', xlabel='Dia', ylabel='Preço (R$)')
  figura = grafico_gasolina.get_figure()
  figura.savefig(fname='gasolina.png', dpi=600)
