
# 📘 Atividade: Jogo da Forca

## 🎯 Objective

Construa um jogo da Forca em Python para praticar manipulação de strings, seleção aleatória, loops, condicionais e entrada de dados do usuário.

## 📝 Tasks

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição
Escolha aleatoriamente uma palavra de uma lista predefinida e prepare as variáveis necessárias para acompanhar o progresso da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista de palavras disponível.
- Manter o controle das letras adivinhadas e das tentativas incorretas restantes.
- Exibir a palavra oculta com espaços para as letras ainda não adivinhadas, por exemplo, `_ _ _ _`.

### 🛠️ Implementar o Ciclo de Palpites

#### Descrição
Peça ao jogador palpites de letras e atualize o estado do jogo até que a palavra seja adivinhada ou as tentativas incorretas acabem.

#### Requisitos
O programa concluído deve:

- Solicitar palpites de letras ao jogador.
- Revelar no progresso todas as ocorrências de uma letra correta.
- Reduzir as tentativas restantes quando o palpite não estiver na palavra.
- Encerrar a partida quando o jogador adivinhar a palavra ou ficar sem tentativas.
- Exibir uma mensagem indicando vitória ou derrota.