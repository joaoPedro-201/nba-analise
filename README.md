# Analisador de tendências de jogos da NBA 

Um painel interativo (Dashboard) focado em dados esportivos avançados da NBA, desenvolvido em Python. O sistema consome dados brutos da API oficial da liga e processa estatísticas complexas para identificar tendências de desempenho, contrastando a linha base da temporada com o momento recente das equipes.

## Arquitetura do Projeto

O projeto adota o padrão de separação de responsabilidades (Modularização), estruturado em três componentes principais:

* **coleta.py (Data Fetching):** Módulo encarregado de realizar requisições à biblioteca `nba_api`, capturando IDs oficiais e retornando DataFrames brutos (jogos gerais e métricas avançadas).
* **analise.py (Data Processing):** Módulo de processamento utilizando Pandas. Realiza a limpeza dos dados, aplica filtros de mando de quadra e calcula médias móveis e estatísticas avançadas.
* **app.py (Web Interface):** Front-end desenvolvido em Streamlit. Utiliza o conceito de Session State para navegação fluida e renderiza os indicadores em formato de KPI Cards e Tabelas limpas, de forma totalmente responsiva.

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

## Como Executar Localmente

### Pré-requisitos
Certifique-se de ter o Python 3 instalado. É recomendado o uso de um ambiente virtual (venv). Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

(Nota: Certifique-se de que as bibliotecas pandas, nba_api e streamlit estão declaradas no seu arquivo requirements.txt).

### Executando a Aplicação Web
No terminal, dentro do diretório do projeto, execute o comando do Streamlit:
```bash
streamlit run app.py
```

O aplicativo abrirá automaticamente no seu navegador padrão (geralmente na porta 8501).

## Fonte de Dados e Creditos

Os dados estatisticos brutos consumidos por este painel sao extraidos em tempo real utilizando a biblioteca open-source [nba_api](https://github.com/swar/nba_api), um cliente Python nao-oficial para os endpoints web da NBA (stats.nba.com). 

Agradecimentos a comunidade open-source por manter os endpoints mapeados e acessiveis para fins de estudo e analise de dados esportivos.