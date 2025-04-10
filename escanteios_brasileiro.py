from abreSofaScore import abrir_sofascore
from obtemRodada import obter_rodada
from loopJogos import loop_jogos
from exibirResultados import exibir_resultados
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

#abre o site
driver = abrir_sofascore()

#dicionário para armazenar os escanteios
escanteios_por_jogo = {}

#obtém o valor da rodada
rodada = obter_rodada(driver)

#loop para clicar em cada jogo
rodada = loop_jogos(driver, escanteios_por_jogo, rodada)

driver.quit()

#resultados ordenados
exibir_resultados(escanteios_por_jogo)

#análise: tabela e gráfico
totais = [dados["total"] for dados in escanteios_por_jogo.values()]
contagem = Counter(totais)

#converte para DataFrame
df = pd.DataFrame(sorted(contagem.items()), columns=["Total de Escanteios", "Número de Ocorrências"])
print("\nTabela de Frequência de Escanteios:\n")
print(df)

# gráfico
plt.figure(figsize=(10, 6))
plt.bar(df["Total de Escanteios"], df["Número de Ocorrências"], color="skyblue", edgecolor="black")
plt.xlabel("Total de Escanteios por Jogo")
plt.ylabel("Número de Ocorrências")
plt.title("Distribuição de Escanteios por Jogo")
plt.xticks(df["Total de Escanteios"])
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()