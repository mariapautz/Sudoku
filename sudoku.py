import random #importa aleatoriedade
tab = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]] #tabuleiro
tabDefault = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(0, 9): #gerador de numeros no tabuleiro
    for j in range(0, 9):
        if random.random() > 0.5 :
            tab[i][j] = int((i*3 + i/3 + j) % (3*3) + 1)
            tabDefault[i][j] = 1
        else:
            tab[i][j] = 0

posX = 0 #variavel da fileira
posY = 0 #variavel da coluna
num = 0  #variavel do numero que sera inputado
option = 0 #variavel de que opcao o usuario deseja executar
win = False #vitoria que começa falsa para rodar o jogo

def jogo():
    global win
    print('\n ############################\n # BEM VINDO AO JOGO SUDOKU #\n ############################') #introducao
    while not win:
        printTab()
        option = int(input(' 1- Adicionar numero\n 2- Remover numero\n '))
        posX = int(input(' Selecione a fileira: '))
        posY = int(input(' Selecione a coluna: '))
        if option == 1:
            num = int(input(' Qual numero quer colocar? '))
            if verify(posX, posY, num) == True:
                insert(posX, posY, num)
            else:
                print(' Não é possivel inserir esse numero aqui!\n')
        elif option == 2:
            remove(posX, posY)
        else:
            print(' Opção inválida!')
        
        if verifyWin(): #verifica se há vitoria
            printTab()  #printa o tabuleiro
            print('\n   ########################\n   # PARABENS, VOCE CONCLUIU O SUDOKU #\n   ########################\n')
            win = True

def printTab(): #funcao para printar o tabuleiro
    print('\n      0 1 2 3 4 5 6 7 8')
    print('     |-----------------|')
    for x in range(0, 9):
        print('  ', x,'|', end='')
        for y in range(0, 9):
            if y == 8 and (x == 2 or x == 5 or x == 8):
                if tab[x][y] == 0:
                    print(' ', end='')
                else:
                    print(tab[x][y], end='')
                print('|', x)
            elif y == 8:
                if tab[x][y] == 0:
                    print(' ', end='')
                else:
                    print(tab[x][y], end='')
                print('|', x, end='')
            elif y == 2 or y == 5:
                if tab[x][y] == 0:
                    print(' ', end='')
                else:
                    print(tab[x][y], end='')
                print('|', end='')
            else:
                if tab[x][y] == 0:
                    print(' ', end='')
                else:
                    print(tab[x][y], end='')
                print(' ', end='')
        if x == 2 or x == 5 or x == 8:
            print('     |-----------------|', end='')
        print()
    print('      0 1 2 3 4 5 6 7 8\n')
def insert(posX, posY, num): #funcao para inserir um numero
    tab[posX][posY] = num
    print('\n # Numero inserido!\n')
def remove(posX, posY): #funcao para remover um numero
    if tabDefault[posX][posY] == 1:
        print('\n # Esse numero é padrão, você não pode removelo!')
    else:
        tab[posX][posY] = 0
        print('\n # Numero removido!')
def verifyWin(): #funcao para verificar se há vitoria
    zeros = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if tab[x][y] == 0:
                zeros = 1
    if zeros == 0:
        return True
    else:
        return False
def verify(posX, posY, num):
    can = 27
    # verificar na coluna
    for x in range(0, 9):
        if tab[x][posY] == num:
            can -= 1
    # verificar na linha
    for y in range(0, 9):
        if tab[posX][y] == num:
            can -= 1
    # procurar qual quadrande esta
    if posX < 3:
        # quadrante 1
        if posY < 3:
            for x in range(0, 3):
                for y in range(0, 3):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 2
        elif posY < 6:
            for x in range(0, 3):
                for y in range(3, 6):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 3
        else:
            for x in range(0, 3):
                for y in range(6, 9):
                    if tab[x][y] == num:
                        can -= 1
    elif posX < 6:
        # quadrante 4
        if posY < 3:
            for x in range(3, 6):
                for y in range(0, 3):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 5
        elif posY < 6:
            for x in range(3, 6):
                for y in range(3, 6):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 6
        else:
            for x in range(3, 6):
                for y in range(6, 9):
                    if tab[x][y] == num:
                        can -= 1
    else:
        # quadrante 7
        if posY < 3:
            for x in range(6, 9):
                for y in range(0, 3):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 8
        elif posY < 6:
            for x in range(6, 9):
                for y in range(3, 6):
                    if tab[x][y] == num:
                        can -= 1
        # quadrante 9
        else:
            for x in range(6, 9):
                for y in range(6, 9):
                    if tab[x][y] == num:
                        can -= 1
    # pode colocar
    if can == 27:
        return True
    else:
        return False
jogo()
