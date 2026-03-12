import pandas as pd

def calcular_medias_gerais(df_jogos, qtd_jogos=10):
    pts_temp = df_jogos['PTS'].mean()
    reb_temp = df_jogos['REB'].mean()
    ast_temp = df_jogos['AST'].mean()
    
    ultimos_jogos = df_jogos.head(qtd_jogos)
    pts_rec = ultimos_jogos['PTS'].mean()
    reb_rec = ultimos_jogos['REB'].mean()
    ast_rec = ultimos_jogos['AST'].mean()
    
    return {
        "jogos_temporada": len(df_jogos),
        "recorte_jogos": qtd_jogos,
        "pts_temp": round(pts_temp, 1),
        "reb_temp": round(reb_temp, 1),
        "ast_temp": round(ast_temp, 1),
        "pts_rec": round(pts_rec, 1),
        "reb_rec": round(reb_rec, 1),
        "ast_rec": round(ast_rec, 1)
    }


def calcular_desempenho_casa_fora_completo(df_jogos, qtd_jogos=10):
    casa_temp = df_jogos[df_jogos['MATCHUP'].str.contains('vs.')]
    fora_temp = df_jogos[df_jogos['MATCHUP'].str.contains('@')]
    
    ultimos_jogos = df_jogos.head(qtd_jogos)
    casa_rec = ultimos_jogos[ultimos_jogos['MATCHUP'].str.contains('vs.')]
    fora_rec = ultimos_jogos[ultimos_jogos['MATCHUP'].str.contains('@')]
    
    def extrair_medias(df):
        if df.empty: return 0, 0, 0, 0
        return len(df), round(df['PTS'].mean(), 1), round(df['REB'].mean(), 1), round(df['AST'].mean(), 1)
        
    qtd_c_t, pts_c_t, reb_c_t, ast_c_t = extrair_medias(casa_temp)
    qtd_f_t, pts_f_t, reb_f_t, ast_f_t = extrair_medias(fora_temp)
    qtd_c_r, pts_c_r, reb_c_r, ast_c_r = extrair_medias(casa_rec)
    qtd_f_r, pts_f_r, reb_f_r, ast_f_r = extrair_medias(fora_rec)
    
    return {
        "recorte_jogos": qtd_jogos,
        "temp_casa": {"qtd": qtd_c_t, "pts": pts_c_t, "reb": reb_c_t, "ast": ast_c_t},
        "temp_fora": {"qtd": qtd_f_t, "pts": pts_f_t, "reb": reb_f_t, "ast": ast_f_t},
        "rec_casa": {"qtd": qtd_c_r, "pts": pts_c_r, "reb": reb_c_r, "ast": ast_c_r},
        "rec_fora": {"qtd": qtd_f_r, "pts": pts_f_r, "reb": reb_f_r, "ast": ast_f_r}
    }


def analisar_quatro_fatores(df_fatores):
    dados = df_fatores.iloc[0]
    
    return {
        "ataque_efg": round(dados['EFG_PCT'] * 100, 1),
        "defesa_efg": round(dados['OPP_EFG_PCT'] * 100, 1),
        "ataque_tov": round(dados['TM_TOV_PCT'] * 100, 1),
        "defesa_tov": round(dados['OPP_TOV_PCT'] * 100, 1), 
        "ataque_orb": round(dados['OREB_PCT'] * 100, 1),
        "ataque_ftr": round(dados['FTA_RATE'] * 100, 1)
    }