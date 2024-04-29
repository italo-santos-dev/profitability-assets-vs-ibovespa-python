import yfinance as yf
import matplotlib.pyplot as plt

ativos = ['ITUB3.SA', 'PETR3.SA', 'VALE3.SA', '^BVSP']

dados = yf.download(ativos, start='2018-06-12', end='2023-06-12')['Adj Close']

rentabilidades = dados.pct_change()

rantabilidades = rentabilidades.iloc[1:]

rentabilidades_acumulada = (1 + rantabilidades).cumprod()

plt.figure(figsize=(10, 6))

plt.style.use('seaborn-v0_8')

cores = ['blue', 'red', 'green', 'yellow', 'black']

for i, ativo in enumerate(rentabilidades_acumulada.columns):
    plt.plot(rentabilidades_acumulada.index,
             rentabilidades_acumulada[ativo] * 100,
             label=ativo, color=cores[i])

plt.title(
    'Rentabilidade Acumulada dos Ativos nos últimos 5 anos',
          fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Rentabilidade Acumulada (%)', fontsize=12)
plt.legend(fontsize=10)

plt.xticks(fontsize=10, rotation=45)

plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
