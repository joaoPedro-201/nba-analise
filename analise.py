import pandas as pd

def calcular_medias_recentes(df_jogos, qtd_jogos=5):
    ultimos_jogos = df_jogos.head(qtd_jogos)

    media_pontos = ultimos_jogos['PTS'].mean()
    media_rebotes = ultimos_jogos['REB'].mean()
    media_assistencias = ultimos_jogos['AST'].mean()

    resultados = {
        "recorte_jogos": qtd_jogos,
        "pontos": round(media_pontos, 1),
        "rebotes": round(media_rebotes, 1),
        "assistencias": round(media_assistencias, 1)
    }

    return resultados

def calcular_desempenho_casa_fora(df_jogos, qtd_jogos=10):
    ultimos_jogos = df_jogos.head(qtd_jogos)

    jogos_casa = ultimos_jogos[ultimos_jogos['MATCHUP'].str.contains('vs.')]
    jogos_fora = ultimos_jogos[ultimos_jogos['MATCHUP'].str.contains('@')]

    media_casa = jogos_casa['PTS'].mean() if not jogos_casa.empty else 0
    media_fora = jogos_fora['PTS'].mean() if not jogos_fora.empty else 0

    resultados = {
        "recorte_jogos": qtd_jogos,
        "jogos_casa_analisados": len(jogos_casa),
        "media_pontos_casa": round(media_casa, 1),
        "jogos_fora_analisados": len(jogos_fora),
        "media_pontos_fora": round(media_fora, 1)
    }

    return resultados

def analisar_quatro_fatores(df_fatores):
    dados = df_fatores.iloc[0]

    resultados = {
        "ataque_efg": round(dados['EFG_PCT'] * 100, 1),
        "defesa_efg": round(dados['OPP_EFG_PCT'] * 100, 1),

        "ataque_tov": round(dados['TM_TOV_PCT'] * 100, 1),
        "defesa_tov": round(dados['OPP_TOV_PCT'] * 100, 1),

        "ataque_orb": round(dados['OREB_PCT'] * 100, 1),

        "ataque_ftr": round(dados['FTA_RATE'] * 100, 1)
    }

    return resultados

if __name__ == "__main__":
    print("Testando a análise de dados...")
   