import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Carregar dados
df = pd.read_csv('/home/ubuntu/sourcing_data.csv')

# Preparar dados para o modelo de IA (Predição de Hired)
# Vamos usar colunas que o recrutador tem no início ou meio do processo
features = ['source_channel', 'seniority', 'years_experience', 'department', 'work_mode']
X = df[features].copy()
y = df['hired'].astype(int)

# Encoding de variáveis categóricas
le_dict = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    le_dict[col] = le

# Treinar um modelo simples para ver importância de features
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Importância das features
importance = pd.DataFrame({
    'Feature': features,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

importance.to_csv('/home/ubuntu/feature_importance.csv', index=False)

# Análise de "Quando vale a pena persistir?"
# Comparar tempo de resposta com sucesso na contratação
df['response_time_days'] = pd.to_numeric(df['response_time_days'], errors='coerce')
persistence_analysis = df.groupby('hired').agg(
    avg_response_time=('response_time_days', 'mean'),
    median_response_time=('response_time_days', 'median')
).reset_index()
persistence_analysis.to_csv('/home/ubuntu/persistence_analysis.csv', index=False)

# Análise de Scores vs Contratação
score_cols = ['technical_test_score', 'behavior_score', 'manager_score']
scores_hired = df.groupby('hired')[score_cols].mean().reset_index()
scores_hired.to_csv('/home/ubuntu/scores_analysis.csv', index=False)

print("Análise avançada concluída.")
