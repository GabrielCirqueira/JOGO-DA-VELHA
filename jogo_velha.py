#---------------------JOGO DA VELHA - ELETIVA ---------------------

# Define a matriz que representa o tabuleiro do jogo da velha.
# Cada elemento da matriz representa uma posição no tabuleiro.
dados = [
        ['1', '2', '3'],  # Primeira linha do tabuleiro
        ['4', '5', '6'],  # Segunda linha do tabuleiro
        ['7', '8', '9']   # Terceira linha do tabuleiro
    ]

# Variável booleana que indica de quem é a vez de jogar.
# True indica que é a vez do jogador X, False indica que é a vez do jogador O.
jogada_X = True

# Função que imprime o tabuleiro do jogo e solicita a jogada do jogador.
def tabela(dados, jogada_X):
    
    # Verifica de quem é a vez de jogar e exibe a mensagem correspondente.
    if jogada_X == True: # Se for a vez do jogador X
        print("\nSua Vez Jogador X\n")
    else: # Se for a vez do jogador O
        print("\nSua Vez Jogador O\n")
        
    # Imprime o tabuleiro atualizado.
    print(f" {dados[0][0]} | {dados[0][1]} | {dados[0][2]} ") # Imprime a primeira linha do tabuleiro
    print("-----------")
    print(f" {dados[1][0]} | {dados[1][1]} | {dados[1][2]} ") # Imprime a segunda linha do tabuleiro
    print("-----------")
    print(f" {dados[2][0]} | {dados[2][1]} | {dados[2][2]} ") # Imprime a terceira linha do tabuleiro
    
    # Solicita ao jogador a posição onde deseja jogar e retorna a posição escolhida.
    local = int(input("DIGITE AONDE DESEJA JOGAR: "))
    return local
    
# Função que altera a vez do próximo jogador.
def Alterar_jogada():
    global jogada_X 
    jogada_X = not jogada_X    
    
# Loop principal do jogo.
while True:
    # Chama a função tabela para exibir o tabuleiro e obter a jogada do jogador.
    jogada = tabela(dados, jogada_X)
    
    # Verifica se a jogada é válida (entre 1 e 9).
    if jogada < 1 or jogada > 9:
        print("Número inválido. Escolha um número entre 1 e 9.")
        continue
    
    # Calcula a linha correspondente à posição escolhida pelo jogador.
    linha = (jogada - 1) // 3  # Divide (jogada - 1) por 3 para encontrar a linha do tabuleiro.
    
    # Calcula a coluna correspondente à posição escolhida pelo jogador.
    coluna = (jogada - 1) % 3  # Obtém o resto da divisão de (jogada - 1) por 3 para encontrar a coluna do tabuleiro.

 
    # Verifica se a posição escolhida pelo jogador já está ocupada.
    if dados[linha][coluna] == "X" or dados[linha][coluna] == "O":
        print("Posição já ocupada. Escolha outra.")
        continue

    # Marca a posição escolhida com "X" ou "O" dependendo de quem é a vez de jogar.
    if jogada_X:
        dados[linha][coluna] = "X"
        Alterar_jogada()
    else:
        dados[linha][coluna] = "O"
        Alterar_jogada()
    
    # Variável para verificar se alguém ganhou o jogo.
    ganhou = False
    
    # Verifica se alguma linha tem todos os elementos iguais.
    for linha in range(3):
        if dados[linha][0] == dados[linha][1] == dados[linha][2]: # Verifica se todos os elementos da linha são iguais.
            ganhou = True
            break

    # Verifica se alguma coluna tem todos os elementos iguais.
    for coluna in range(3):
        if dados[0][coluna] == dados[1][coluna] == dados[2][coluna]: # Verifica se todos os elementos da coluna são iguais.
            ganhou = True
            break

    # Verifica se alguma diagonal tem todos os elementos iguais.
    if dados[0][0] == dados[1][1] == dados[2][2] and dados[0][0] in ("X", "O"): # Verifica a diagonal principal.
        ganhou = True

    elif dados[0][2] == dados[1][1] == dados[2][0] and dados[0][2] in ("X", "O"): # Verifica a outra diagonal.
        ganhou = True
    
    # Se alguém ganhou, exibe o tabuleiro atualizado e anuncia o vencedor.
    if ganhou:
        print("\n\n\n")
        print(f" {dados[0][0]} | {dados[0][1]} | {dados[0][2]} ")
        print("-----------")
        print(f" {dados[1][0]} | {dados[1][1]} | {dados[1][2]} ")
        print("-----------")
        print(f" {dados[2][0]} | {dados[2][1]} | {dados[2][2]} ")
        
        # Verifica quem ganhou e exibe a mensagem adequada.
        if not jogada_X: # Se a última jogada foi do jogador O, significa que o jogador X ganhou.
            print("\n\nX GANHOU !!!\n")
        else: # Se a última jogada foi do jogador X, significa que o jogador O ganhou.
            print("\n\nO GANHOU !!!\n")
        
        # Encerra o loop do jogo.
        break