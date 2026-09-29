# Código inicial: Limpeza e Qualidade de Dados

import pandas as pd

original = pd.read_csv("data.csv")

# Audite os dados originais antes de fazer alterações.
print("Dados originais:")
print(original.head())
print("Registros:", len(original))
print("Valores ausentes por coluna:")
print(original.isna().sum())
print("Registros duplicados:", original.duplicated().sum())
numeric_hours = pd.to_numeric(original["study_hours"], errors="coerce")
numeric_scores = pd.to_numeric(original["score"], errors="coerce")
print("Horas negativas:", numeric_hours.lt(0).sum())
print(
	"Notas fora de 0 a 100:",
	(~numeric_scores.between(0, 100) & numeric_scores.notna()).sum(),
)

# Use uma cópia para manter os dados originais disponíveis para comparação.
cleaned = original.copy()

# TODO: remova espaços extras dos nomes dos alunos.
# TODO: converta study_hours e score em valores numéricos.
# TODO: marque horas negativas e notas fora de 0 a 100 como ausentes.
# TODO: remova duplicatas e preencha valores numéricos ausentes com a mediana.

# TODO: compare os dados originais e limpos conforme os requisitos da atividade.
# TODO: salve o resultado como cleaned_students.csv.