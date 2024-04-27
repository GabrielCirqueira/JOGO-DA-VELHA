# JOGO DA VELHA

dados = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

jogada_X = True

def tabela(dados,jogada_X):
    print(f" {dados[0][0]} | {dados[0][1]} | {dados[0][2]} ")
    print("-----------")
    print(f" {dados[1][0]} | {dados[1][1]} | {dados[1][2]} ")
    print("-----------")
    print(f" {dados[2][0]} | {dados[2][1]} | {dados[2][2]} ")
    
    if(jogada_X == True):
        print("\n\n Sua Vez X\n")
        local = int(input("DIGITE AONDE DESEJA JOGAR: "))
        return local
    
    else:
        print("\n\n Sua Vez O\n")
        local = int(input("DIGITE AONDE DESEJA JOGAR: "))
        return local
    

def Alterar_jogada():
    global jogada_X 
    jogada_X = not jogada_X
    
    
while True:
    jogada = tabela(dados,jogada_X)
    
    if(jogada == 1):
        if(jogada_X == True):
            dados[0][0] = "X"
            Alterar_jogada()
        else:
            dados[0][0] = "O"
            Alterar_jogada()
            
    elif jogada == 2:
        if jogada_X:
            dados[0][1] = "X"
            Alterar_jogada()
        else:
            dados[0][1] = "O"
            Alterar_jogada()
            
    elif jogada == 3:
        if jogada_X:
            dados[0][2] = "X"
            Alterar_jogada()
        else:
            dados[0][2] = "O"
            Alterar_jogada()

    elif jogada == 4:
        if jogada_X:
            dados[1][0] = "X"
            Alterar_jogada()
        else:
            dados[1][0] = "O"
            Alterar_jogada()

    elif jogada == 5:
        if jogada_X:
            dados[1][1] = "X"
            Alterar_jogada()
        else:
            dados[1][1] = "O"
            Alterar_jogada()

    elif jogada == 6:
        if jogada_X:
            dados[1][2] = "X"
            Alterar_jogada()
        else:
            dados[1][2] = "O"
            Alterar_jogada()

    elif jogada == 7:
        if jogada_X:
            dados[2][0] = "X"
            Alterar_jogada()
        else:
            dados[2][0] = "O"
            Alterar_jogada()

    elif jogada == 8:
        if jogada_X:
            dados[2][1] = "X"
            Alterar_jogada()
        else:
            dados[2][1] = "O"
            Alterar_jogada()

    elif jogada == 9:
        if jogada_X:
            dados[2][2] = "X"
            Alterar_jogada()
        else:
            dados[2][2] = "O"
            Alterar_jogada()

            
                
    
        
    

