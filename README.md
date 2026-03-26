# NBA Advanced Trends Analyzer

Um painel interativo (Dashboard) focado em dados esportivos avançados da NBA, desenvolvido em Python. O sistema consome dados brutos da API oficial da liga e processa estatísticas complexas para identificar tendências de desempenho, contrastando a linha base da temporada com o momento recente das equipes.

## Acesso à Aplicação

O projeto está hospedado e operando em nuvem. Você pode interagir com o dashboard diretamente pelo seu navegador, sem necessidade de instalações:

**Acessar o Dashboard Live:** [Site](https://nba-trends-dashboard.streamlit.app/)

## Arquitetura do Projeto

O projeto adota o padrão de separação de responsabilidades (Modularização), estruturado em três componentes principais:

* **coleta.py (Data Fetching):** Módulo encarregado de realizar requisições à biblioteca nba_api, capturando IDs oficiais e retornando DataFrames brutos (jogos gerais e métricas avançadas).
* **analise.py (Data Processing):** Módulo de processamento utilizando Pandas. Realiza a limpeza dos dados, aplica filtros de mando de quadra e calcula médias móveis e estatísticas avançadas.
* **app.py (Web Interface):** Front-end desenvolvido em Streamlit. Utiliza o conceito de Session State para navegação fluida e renderiza os indicadores em formato de KPI Cards e Tabelas, de forma responsiva.

## Funcionalidades e Métricas

A aplicação substitui a leitura básica de placares por uma análise do DNA estatístico das franquias através de:

1. **Seleção Visual:** Painel interativo com os 30 escudos oficiais das franquias da NBA, atualizados dinamicamente via CDN.
2. **Espelho de Desempenho (Baseline vs Trend):** Comparativo direto das médias da temporada completa contra o recorte dos últimos 10 jogos, permitindo a detecção de variações de performance (redução de variância).
3. **Fator Mando de Quadra (Home/Away Split):** Isolamento métrico do desempenho de pontos, rebotes e assistências em casa e fora.
4. **Os Quatro Fatores de Dean Oliver (Four Factors):**
    * **eFG% (Effective Field Goal):** Eficiência real de arremesso, ajustando o peso das bolas de 3 pontos.
    * **TOV% (Turnover Percentage):** Taxa de desperdício de posses de bola.
    * **ORB% (Offensive Rebound):** Taxa de rebotes ofensivos capturados.
    * **FT Rate (Free Throw Rate):** Frequência de idas à linha de lance livre.

## Como Executar Localmente (Para Desenvolvedores)

Caso queira clonar o repositório para estudos ou melhorias:

1. Certifique-se de ter o Python 3.12 ou superior instalado.
2. Clone o repositório e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação localmente:
    ```bash
    streamlit run app.py
    ```

## Fonte de Dados e Créditos
Os dados estatísticos brutos consumidos por este painel são extraídos em tempo real utilizando a biblioteca open-source nba_api, um cliente Python não-oficial para os endpoints web da NBA. Agradecimentos à comunidade open-source por manter os endpoints mapeados e acessíveis para análise de dados esportivos.
