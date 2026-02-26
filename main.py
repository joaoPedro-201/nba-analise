import coleta
import analise

def gerar_relatorio():
    print("="*50)
    print("Bem-vindo ao analisador de tendências da NBA!")
    print("="*50)

    time_alvo = input("Digite o nome do time que deseja analisar (ex: Houston Rockets): ")

    print(f"\nColetando dados para o time: {time_alvo}...")

    try:
        df_jogos = coleta.buscar_jogos_time(time_alvo)

        medias_gerais = analise.calcular_medias_recentes(df_jogos, qtd_jogos=5)
        desempenho_cf = analise.calcular_desempenho_casa_fora(df_jogos, qtd_jogos=10)

        print("\n" + "="*50)
        print(f"Relatório de desempenho para {time_alvo}")
        print("="*50)

        print(f"Momento atual (ultimos {medias_gerais['recorte_jogos']} jogos):")
        print(f"   • Pontos Marcados: {medias_gerais['pontos']} pts/jogo")
        print(f"   • Rebotes: {medias_gerais['rebotes']} reb/jogo")
        print(f"   • Assistências: {medias_gerais['assistencias']} ast/jogo")

        print(f"\nFator mando de quadra (Últimos {desempenho_cf['recorte_jogos']} jogos):")
        print(f"   • Jogos em casa analisados: {desempenho_cf['jogos_casa_analisados']} jogos): {desempenho_cf['media_pontos_casa']} pts/jogo")
        print(f"   • Jogos fora de casa analisados {desempenho_cf['jogos_fora_analisados']} jogos): {desempenho_cf['media_pontos_fora']} pts/jogo")

        print("\n" + "="*50 + "\n")

    except ValueError as e:
        print(f"\n{e}\n")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}\n")

if __name__ == "__main__":
    gerar_relatorio()
