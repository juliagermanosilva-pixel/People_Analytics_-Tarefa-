# People_Analytics_-Tarefa-
Responder perguntas de acordo com os dados fornecidos em uma planilha. 
Desafio Técnico de People Analytics: Análise de Sourcing com IA

Este repositório contém a solução para o desafio técnico de People Analytics, focado na análise do processo de sourcing e recrutamento. A solução inclui análise de dados, visualizações e a aplicação de Inteligência Artificial para identificar padrões e otimizar as estratégias de contratação.

Conteúdo do Repositório

•
sourcing_data.csv: O dataset utilizado para a análise.

•
analysis.py: Script Python contendo a análise exploratória de dados, funil de recrutamento e taxas de conversão por canal.

•
advanced_analysis.py: Script Python com a implementação de um modelo de Machine Learning (Random Forest) para identificar a importância das features na decisão de contratação.

•
relatorio_final.md: Relatório detalhado em Markdown com os insights, análises e recomendações.

•
relatorio_final.pdf: Versão em PDF do relatório final.

•
recruitment_funnel.png: Visualização do funil de recrutamento.

•
source_conversion.png: Visualização da taxa de conversão por canal de sourcing.

•
people_analytics_notebook.ipynb: Jupyter Notebook consolidando toda a análise, código e visualizações.

Como Executar a Análise

Para replicar a análise e gerar os resultados, siga os passos abaixo:

1.
Clone o Repositório:

Bash


git clone <URL_DO_SEU_REPOSITORIO>
cd <SEU_REPOSITORIO>





2.
Crie um Ambiente Virtual (Opcional, mas Recomendado):

Bash


python3 -m venv venv
source venv/bin/activate





3.
Instale as Dependências:

Bash


pip install pandas matplotlib seaborn scikit-learn jupyter





4.
Execute os Scripts de Análise:

Bash


python3 analysis.py
python3 advanced_analysis.py



Estes scripts irão gerar os arquivos CSV de resultados e as imagens dos gráficos.



5.
Visualize o Jupyter Notebook:
Para uma experiência interativa e para ver a análise passo a passo, abra o Jupyter Notebook:

Bash


jupyter notebook people_analytics_notebook.ipynb





Abordagem e Metodologia

A abordagem seguiu as seguintes etapas:

1.
Entendimento do Problema: Análise do PDF do desafio para compreender os objetivos e entregáveis.

2.
Coleta e Preparação de Dados: Download e carregamento do dataset de sourcing.

3.
Análise Exploratória: Investigação das etapas do funil de recrutamento, identificação de gargalos e análise de canais de sourcing.

4.
Modelagem com IA: Aplicação de um modelo de Random Forest para determinar a importância das features na decisão de contratação.

5.
Geração de Insights e Recomendações: Formulação de conclusões acionáveis para otimizar o processo de recrutamento.

Insights Chave

•
Funil de Conversão: Identificação de uma queda significativa entre o teste técnico e a oferta.

•
Canais de Sourcing: Diferenças na taxa de conversão entre os canais.

•
Fatores de Sucesso (IA): Anos de experiência, canal de origem e departamento são os principais preditores de contratação.

•
Scores: Candidatos contratados apresentam scores consistentemente mais altos.

Recomendações

•
Focar em candidatos com experiência alinhada ao perfil ideal.

•
Melhorar o follow-up para reduzir a perda de candidatos por "no response".

•
Alinhar expectativas salariais precocemente.

•
Não descartar candidatos com tempo de resposta ligeiramente maior.

