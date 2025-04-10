def ordenar_chave(chave):
    partes = chave.split(" ")
    rodada = int(partes[1])
    jogo = int(partes[4])
    return (rodada, jogo)

def exibir_resultados(escanteios_por_jogo):
    chaves_ordenadas = sorted(escanteios_por_jogo.keys(), key=ordenar_chave)

    for chave in chaves_ordenadas:
        dados = escanteios_por_jogo[chave]
        print(f"{chave} - Mandante: {dados['mandante']}, Visitante: {dados['visitante']}, Total: {dados['total']}")