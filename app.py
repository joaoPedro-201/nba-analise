import streamlit as st
import coleta
import analise
from datetime import date
from nba_api.stats.static import teams

st.set_page_config(
    page_title="NBA Advanced Trends",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stMetricValue"] {
    display: flex;
    justify-content: center;
}
[data-testid="stMetricLabel"] {
    display: flex;
    justify-content: center;
}
table {
    margin-left: auto !important;
    margin-right: auto !important;
}
</style>
""", unsafe_allow_html=True)

if 'time_selecionado' not in st.session_state:
    st.session_state.time_selecionado = None

st.title("Analisador de Tendências Avançadas da NBA")
st.markdown("Consuma dados oficiais e visualize o DNA estatístico das equipes.")
st.write(f"Dados atualizados até: {date.today().strftime('%d/%m/%Y')}")
st.markdown("---")

st.markdown("### Selecione uma equipe para analisar:")

nba_teams = sorted(teams.get_teams(), key=lambda x: x['full_name'])
colunas = st.columns(5)

for i, time_info in enumerate(nba_teams):
    nome = time_info['full_name']
    time_id = time_info['id']
    url_logo = f"https://cdn.nba.com/logos/nba/{time_id}/global/L/logo.svg"
    
    with colunas[i % 5]:
        with st.container(border=True):
            st.markdown(
                f'<img src="{url_logo}" style="display: block; margin: 0 auto; width: 90px;">', 
                unsafe_allow_html=True
            )
            st.write("")
            if st.button(nome, key=time_id, use_container_width=True):
                st.session_state.time_selecionado = nome

st.markdown("---")

time_alvo = st.session_state.time_selecionado

if time_alvo:
    with st.spinner(f"Coletando dados brutos da NBA API para {time_alvo}..."):
        try:
            df_jogos = coleta.buscar_jogos_time(time_alvo)
            df_fatores_temp = coleta.buscar_quatro_fatores(time_alvo)
            df_fatores_rec = coleta.buscar_quatro_fatores_recentes(time_alvo, ultimos_n="10")
            
            medias = analise.calcular_medias_gerais(df_jogos, qtd_jogos=10)
            cf = analise.calcular_desempenho_casa_fora_completo(df_jogos, qtd_jogos=10)
            fatores_temp = analise.analisar_quatro_fatores(df_fatores_temp)
            fatores_rec = analise.analisar_quatro_fatores(df_fatores_rec)

            st.header(f"Dashboard de Desempenho: {time_alvo}")
            
            st.subheader("1. Estatísticas Gerais")
            st.write(f"Amostra total da temporada: {medias['jogos_temporada']} jogos disputados.")
            
            col_pts, col_reb, col_ast = st.columns(3)
            
            with col_pts:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>PONTOS</h5>", unsafe_allow_html=True)
                    m1, m2 = st.columns(2)
                    m1.metric("Temporada", f"{medias['pts_temp']}")
                    m2.metric("Últimos 10", f"{medias['pts_rec']}")

            with col_reb:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>REBOTES</h5>", unsafe_allow_html=True)
                    m1, m2 = st.columns(2)
                    m1.metric("Temporada", f"{medias['reb_temp']}")
                    m2.metric("Últimos 10", f"{medias['reb_rec']}")

            with col_ast:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>ASSISTÊNCIAS</h5>", unsafe_allow_html=True)
                    m1, m2 = st.columns(2)
                    m1.metric("Temporada", f"{medias['ast_temp']}")
                    m2.metric("Últimos 10", f"{medias['ast_rec']}")

            st.markdown("<br>", unsafe_allow_html=True)

            st.subheader("2. Mando de Quadra")
            col_casa, col_fora = st.columns(2)
            
            with col_casa:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center;'>CASA</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Recorte | Pontos | Rebotes | Assists |
                    | :--- | :---: | :---: | :---: |
                    | Temporada ({cf['temp_casa']['qtd']}j) | {cf['temp_casa']['pts']} | {cf['temp_casa']['reb']} | {cf['temp_casa']['ast']} |
                    | Últimos 10 ({cf['rec_casa']['qtd']}j) | {cf['rec_casa']['pts']} | {cf['rec_casa']['reb']} | {cf['rec_casa']['ast']} |
                    """)

            with col_fora:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center;'>FORA</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Recorte | Pontos | Rebotes | Assists |
                    | :--- | :---: | :---: | :---: |
                    | Temporada ({cf['temp_fora']['qtd']}j) | {cf['temp_fora']['pts']} | {cf['temp_fora']['reb']} | {cf['temp_fora']['ast']} |
                    | Últimos 10 ({cf['rec_fora']['qtd']}j) | {cf['rec_fora']['pts']} | {cf['rec_fora']['reb']} | {cf['rec_fora']['ast']} |
                    """)
                    
            st.markdown("<br>", unsafe_allow_html=True)

            st.subheader("3. Os 4 Fatores de Dean Oliver")
            
            linha1_col1, linha1_col2 = st.columns(2)
            linha2_col1, linha2_col2 = st.columns(2)
            
            with linha1_col1:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>1. ARREMESSO EFETIVO (eFG%)</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Situação | Temporada | Últimos 10 |
                    | :--- | :---: | :---: |
                    | **Ataque** | {fatores_temp['ataque_efg']}% | {fatores_rec['ataque_efg']}% |
                    | **Defesa** | {fatores_temp['defesa_efg']}% | {fatores_rec['defesa_efg']}% |
                    """)

            with linha1_col2:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>2. DESPERDÍCIOS (TOV%)</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Situação | Temporada | Últimos 10 |
                    | :--- | :---: | :---: |
                    | **Comete** | {fatores_temp['ataque_tov']}% | {fatores_rec['ataque_tov']}% |
                    | **Força** | {fatores_temp['defesa_tov']}% | {fatores_rec['defesa_tov']}% |
                    """)
                    
            with linha2_col1:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>3. REBOTES OFENSIVOS (ORB%)</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Situação | Temporada | Últimos 10 |
                    | :--- | :---: | :---: |
                    | **Captura** | {fatores_temp['ataque_orb']}% | {fatores_rec['ataque_orb']}% |
                    """)

            with linha2_col2:
                with st.container(border=True):
                    st.markdown("<h5 style='text-align: center; color: gray;'>4. FALTAS CAVADAS (FT Rate)</h5>", unsafe_allow_html=True)
                    st.markdown(f"""
                    | Situação | Temporada | Últimos 10 |
                    | :--- | :---: | :---: |
                    | **Ataque** | {fatores_temp['ataque_ftr']}% | {fatores_rec['ataque_ftr']}% |
                    """)

        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")