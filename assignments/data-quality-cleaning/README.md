# 📘 Atividade: Limpeza e Qualidade de Dados

## 🎯 Objetivo

Em uma ou duas aulas, use Python e pandas para identificar problemas em um conjunto de dados, aplicar regras de limpeza e comparar um resumo do arquivo original com o resultado limpo.

## 📝 Tarefas

### 🛠️ Auditar o conjunto de dados

#### Descrição
Carregue `data.csv` e investigue os dados antes de alterá-los. Mantenha uma cópia original para poder comparar os resultados.

#### Requisitos
O programa concluído deve:

- Carregar o CSV usando pandas e exibir as primeiras linhas.
- Informar o número inicial de registros e os valores ausentes por coluna.
- Identificar registros duplicados e valores fora do intervalo esperado: horas de estudo não negativas e notas entre 0 e 100.

### 🛠️ Limpar os dados

#### Descrição
Crie uma cópia limpa dos dados. Aplique as regras abaixo na ordem necessária para que registros duplicados com espaços extras nos nomes também sejam reconhecidos.

#### Requisitos
O programa concluído deve:

- Remover espaços extras no início e no fim dos nomes dos alunos.
- Converter horas de estudo e notas em valores numéricos.
- Tratar horas de estudo negativas e notas fora do intervalo de 0 a 100 como valores ausentes.
- Remover registros duplicados e preencher valores numéricos ausentes com a mediana dos valores válidos da respectiva coluna.
- Preservar os dados originais, sem sobrescrevê-los durante a limpeza.

### 🛠️ Comparar e salvar os resultados

#### Descrição
Resuma o efeito das regras de limpeza e salve o conjunto de dados pronto para análise.

#### Requisitos
O programa concluído deve:

- Exibir a quantidade de registros antes e depois da limpeza e quantos registros duplicados foram removidos.
- Exibir a quantidade de valores ausentes em cada coluna após a limpeza.
- Comparar a média das notas válidas no conjunto original com a média das notas no conjunto limpo.
- Salvar os dados limpos em `cleaned_students.csv`.