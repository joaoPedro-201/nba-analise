from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
import pandas as pd

def buscar_jogos_time(nome_time):
    nba_teams = teams.get_teams()
    time_encontrado = [team for team in nba_teams if team['full_name'].lower() == nome_time.lower()]
    
    if not time_encontrado:
        raise ValueError(f"Time '{nome_time}' não encontrado.")
    
    time_id = time_encontrado[0]['id']
    gamelog = teamgamelog.TeamGameLog(team_id=time_id)
    df_jogos = gamelog.get_data_frames()[0]

    return df_jogos

if __name__ == "__main__":
    print("Testando a coleta de dados...")
