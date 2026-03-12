# NBA Stats Analyzer: Advanced Model

Um analisador de dados esportivos focado na NBA, construído em Python. Este projeto consome dados brutos da API oficial da NBA (`nba_api`) e processa estatísticas avançadas para identificar tendências de desempenho, contrastando a linha base da temporada com o momento recente das equipes.

## Arquitetura do Projeto

O projeto foi construído utilizando o conceito de separação de responsabilidades (Modularização), dividido em três componentes principais:

* **`coleta.py` (O Operário):** Responsável por fazer as requisições à API da NBA, buscar o ID das franquias e retornar os DataFrames brutos (jogos gerais e recortes de *Four Factors*).
* **`analise.py` (O Cérebro):** Módulo de processamento de dados usando Pandas. Limpa os dados, aplica filtros de texto (Casa/Fora) e calcula médias móveis e estatísticas avançadas.
* **`main.py` (O Maestro):** O ponto de entrada da aplicação. Orquestra a coleta e a análise, exibindo um *Dashboard* formatado e interativo no terminal.

## Estatísticas Implementadas

Em vez de focar apenas no placar, este modelo analisa o "DNA" das equipes através de:

1.  **Espelho de Desempenho (Baseline vs Trend):** Compara as médias da temporada inteira com o recorte dos últimos 10 jogos (redução de variância).
2.  **Fator Mando de Quadra (Home/Away Split):** Isola o desempenho de pontos, rebotes e assistências em casa (`vs.`) e fora (`@`).
3.  **Os Quatro Fatores de Dean Oliver (Four Factors):**
    * **eFG% (Effective Field Goal):** Eficiência real de arremesso.
    * **TOV% (Turnover Percentage):** Taxa de desperdício de posses.
    * **ORB% (Offensive Rebound):** Taxa de rebotes ofensivos capturados.
    * **FT Rate (Free Throw Rate):** Frequência de lances livres cavados.

## Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3 instalado e instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Executando o Dashboard
No seu terminal, rode o arquivo principal e digite o nome da franquia desejada:

```bash
python main.py
```

Desenvolvido para estudos em Engenharia de Dados e Análise Estatística Esportiva.