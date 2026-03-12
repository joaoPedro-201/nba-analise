import coleta
import analise

def gerar_relatorio():
    print("="*60)
    print("BEM-VINDO AO ANALISADOR DE TENDÊNCIAS DA NBA")
    print("="*60)
    
    time_alvo = input("\nDigite o nome do time (ex: Los Angeles Lakers, Boston Celtics): ").title()
    
    print(f"\n Coletando dados e calculando estatísticas para {time_alvo}...")
    
    try:
        df_jogos = coleta.buscar_jogos_time(time_alvo)
        df_fatores_temp = coleta.buscar_quatro_fatores(time_alvo)
        df_fatores_rec = coleta.buscar_quatro_fatores_recentes(time_alvo, ultimos_n="10")
        
        medias = analise.calcular_medias_gerais(df_jogos, qtd_jogos=10)
        cf = analise.calcular_desempenho_casa_fora_completo(df_jogos, qtd_jogos=10)
        
        fatores_temp = analise.analisar_quatro_fatores(df_fatores_temp)
        fatores_rec = analise.analisar_quatro_fatores(df_fatores_rec)
        
        print("\n" + "="*60)
        print(f"RELATÓRIO DE DESEMPENHO AVANÇADO: {time_alvo}")
        print("="*60)
        
        print(f"\n 1. ESTATÍSTICAS GERAIS (Temporada vs Últimos {medias['recorte_jogos']})")
        print(f"   • Pontos:  {medias['pts_temp']} pts  X {medias['pts_rec']} pts")
        print(f"   • Rebotes: {medias['reb_temp']} reb  X {medias['reb_rec']} reb")
        print(f"   • Assists: {medias['ast_temp']} ast  X {medias['ast_rec']} ast")
        print(f"   *Amostra da temporada: {medias['jogos_temporada']} jogos disputados.")
        
        print(f"\n 2. MANDO DE QUADRA (Temporada vs Últimos {cf['recorte_jogos']})")
        print(f"   • CASA:")
        print(f"     Temp ({cf['temp_casa']['qtd']}j): {cf['temp_casa']['pts']} pts | {cf['temp_casa']['reb']} reb | {cf['temp_casa']['ast']} ast")
        print(f"     Rec. ({cf['rec_casa']['qtd']}j): {cf['rec_casa']['pts']} pts | {cf['rec_casa']['reb']} reb | {cf['rec_casa']['ast']} ast")
        print(f"   • FORA:")
        print(f"     Temp ({cf['temp_fora']['qtd']}j): {cf['temp_fora']['pts']} pts | {cf['temp_fora']['reb']} reb | {cf['temp_fora']['ast']} ast")
        print(f"     Rec. ({cf['rec_fora']['qtd']}j): {cf['rec_fora']['pts']} pts | {cf['rec_fora']['reb']} reb | {cf['rec_fora']['ast']} ast")

        print(f"\n 3. OS 4 FATORES DE DEAN OLIVER (Temporada vs Últimos 10)")
        print(f"   1 Arremesso (eFG%):")
        print(f"      Ataque: {fatores_temp['ataque_efg']}% X {fatores_rec['ataque_efg']}%")
        print(f"      Defesa: {fatores_temp['defesa_efg']}% X {fatores_rec['defesa_efg']}%")
        print(f"   2 Desperdícios (TOV%):")
        print(f"      Comete: {fatores_temp['ataque_tov']}% X {fatores_rec['ataque_tov']}%")
        print(f"      Força:  {fatores_temp['defesa_tov']}% X {fatores_rec['defesa_tov']}%")
        print(f"   3 Rebotes Ofensivos (ORB%):")
        print(f"      Captura: {fatores_temp['ataque_orb']}% X {fatores_rec['ataque_orb']}%")
        print(f"   4 Faltas Cavadas (FT Rate):")
        print(f"      Ataque: {fatores_temp['ataque_ftr']}% X {fatores_rec['ataque_ftr']}%")
        
        print("\n" + "="*60 + "\n")
        
    except ValueError as e:
        print(f"\n{e}\n")
    except Exception as e:
        print(f"\n Ocorreu um erro inesperado: {e}\n")

if __name__ == "__main__":
    gerar_relatorio()