import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar os dados
df = pd.read_csv('/home/ubuntu/sourcing_data.csv')

# Configurações de estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Análise de Funil de Conversão
funnel_stages = {
    'Sourced': len(df),
    'First Contact': df['response_received'].sum(),
    'Screening Pass': df['screening_pass'].sum(),
    'Interview 1 Pass': df['interview1_pass'].sum(),
    'Test Taken': df['test_taken'].sum(),
    'Offer Sent': df['offer_sent'].sum(),
    'Hired': df['hired'].sum()
}

funnel_df = pd.DataFrame(list(funnel_stages.items()), columns=['Stage', 'Count'])
funnel_df['Conversion_Rate'] = funnel_df['Count'] / funnel_df['Count'].shift(1)
funnel_df['Total_Conversion'] = funnel_df['Count'] / len(df)

# Salvar Funil
funnel_df.to_csv('/home/ubuntu/funnel_analysis.csv', index=False)

# 2. Quais estratégias de sourcing convertem melhor? (Contratação por Canal)
source_conversion = df.groupby('source_channel').agg(
    total=('candidate_id', 'count'),
    hired=('hired', 'sum')
).reset_index()
source_conversion['conversion_rate'] = (source_conversion['hired'] / source_conversion['total']) * 100
source_conversion = source_conversion.sort_values('conversion_rate', ascending=False)

# 3. Sinais de maior chance de avançar (Correlação de scores com contratação)
# Converter colunas booleanas para int
df['hired_int'] = df['hired'].astype(int)
df['screening_pass_int'] = df['screening_pass'].astype(int)

# 4. Padrões entre Canais, Recrutadores ou Perfis
recruiter_perf = df.groupby('recruiter').agg(
    total=('candidate_id', 'count'),
    hired=('hired', 'sum')
).reset_index()
recruiter_perf['conversion_rate'] = (recruiter_perf['hired'] / recruiter_perf['total']) * 100

# 5. Visualizações
# Gráfico de Canais de Sourcing
plt.figure(figsize=(10, 6))
sns.barplot(data=source_conversion, x='source_channel', y='conversion_rate', palette='viridis')
plt.title('Taxa de Conversão por Canal de Sourcing (%)')
plt.ylabel('Taxa de Conversão (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/ubuntu/source_conversion.png')

# Gráfico de Funil
plt.figure(figsize=(10, 6))
sns.barplot(data=funnel_df, x='Stage', y='Count', color='skyblue')
plt.title('Funil de Recrutamento (Volume por Etapa)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/home/ubuntu/recruitment_funnel.png')

# 6. Insights para IA (Preparação de dados para recomendações)
# Vamos analisar os motivos de rejeição mais comuns
rejection_reasons = df['rejection_reason'].value_counts().reset_index()
rejection_reasons.columns = ['Reason', 'Count']
rejection_reasons.to_csv('/home/ubuntu/rejection_analysis.csv', index=False)

print("Análise concluída. Arquivos gerados.")
