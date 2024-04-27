dados = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

jogada_X = True

def tabela(dados,jogada_X):
    
    if(jogada_X == True):
        print("\nSua Vez Jogador X\n")
    else:
        print("\n Sua Vez Jogador O\n")
        
    print(f" {dados[0][0]} | {dados[0][1]} | {dados[0][2]} ")
    print("-----------")
    print(f" {dados[1][0]} | {dados[1][1]} | {dados[1][2]} ")
    print("-----------")
    print(f" {dados[2][0]} | {dados[2][1]} | {dados[2][2]} ")
    
    local = int(input("DIGITE AONDE DESEJA JOGAR: "))
    return local
    
def Alterar_jogada():
    global jogada_X 
    jogada_X = not jogada_X    
    
while True:
    jogada = tabela(dados,jogada_X)
    
    if jogada < 1 or jogada > 9:
        print("Número inválido. Escolha um número entre 1 e 9.")
        continue
    
    linha = (jogada - 1) // 3
    coluna = (jogada - 1) % 3
 
    if dados[linha][coluna] == "X" or dados[linha][coluna] == "O":
        print("Posição já ocupada. Escolha outra.")
        continue

    if jogada_X:
        dados[linha][coluna] = "X"
        Alterar_jogada()
    else:
        dados[linha][coluna] = "O"
        Alterar_jogada()
    
    ganhou = False
    
    for linha in range(3):
        if dados[linha][0] == dados[linha][1] == dados[linha][2]:
            ganhou = True
            break

    for coluna in range(3):
        if dados[0][coluna] == dados[1][coluna] == dados[2][coluna]:
            ganhou = True
            break

    if dados[0][0] == dados[1][1] == dados[2][2] and dados[0][0] in ("X", "O"):
        ganhou = True

    elif dados[0][2] == dados[1][1] == dados[2][0] and dados[0][2] in ("X", "O"):
        ganhou = True
    
    if ganhou:
        print("\n\n\n")
        print(f" {dados[0][0]} | {dados[0][1]} | {dados[0][2]} ")
        print("-----------")
        print(f" {dados[1][0]} | {dados[1][1]} | {dados[1][2]} ")
        print("-----------")
        print(f" {dados[2][0]} | {dados[2][1]} | {dados[2][2]} ")
        if not jogada_X:
            print("\n\nX GANHOU !!!\n")
        else:
            print("\n\nO GANHOU !!!\n")
        break

    

