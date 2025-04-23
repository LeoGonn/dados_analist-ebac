# código de geração do gráfico
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(12, 7))
sns.lineplot(x='dia', y='preco', data=df, marker='o', color='blue')
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Preço (R$)', fontsize=14)
plt.title('Preço da Gasolina por Dia', fontsize=16)
plt.grid(True, linestyle='--')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('gasolina.png')
plt.show()
