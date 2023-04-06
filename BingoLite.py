''' Integrantes: Diogo Lourenzon Hatz - TIA: 32247389
                 Leila Akina Ino - TIA: 32261128

    Layout das cartelas no terminal testado em Python 3.10. Em versões anteriores é possível que o layout esteja levemente distorcido
'''

from datetime import date
import time
import random


def gerarCartela():                 # Função para gerar as quatro cartelas aleatórias do arquivo ''cartelas.txt''
    cartela = [0]*4
    arquivo = open('cartelas.txt', 'r', encoding='utf-8')
    tam = len(arquivo.readlines())
    arquivo.seek(0, 0)
    a = random.sample(range(0, tam), 4)

    for i in range(len(a)):
        line = arquivo.readlines()[a[i]]
        cartela[i] = line.rstrip()
        arquivo.seek(0, 0)

    arquivo.close()
    return cartela


def novaRodada(x, y, z, k, atual, respostas):                      # Função para printar as cartelas a cada rodada
    print('            ', *respostas[0], sep=' ')
    print('Cartela 1: ', x, end='')
    if atual == 1:
        print('  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', end='')
    print('\n            ', *respostas[4], sep=' ')

    print('            ', *respostas[1], sep=' ')
    print('Cartela 2: ', y, end='')
    if atual == 2:
        print('  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', end='')
    print('\n            ', *respostas[5], sep=' ')

    print('            ', *respostas[2], sep=' ')
    print('Cartela 3: ', z, end='')
    if atual == 3:
        print('  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', end='')
    print('\n            ', *respostas[6], sep=' ')

    print('            ', *respostas[3], sep=' ')
    print('Cartela 4: ', k, end='')
    if atual == 4:
        print('  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', end='')
    print('\n            ', *respostas[7], sep=' ')


def sortearNumero(tabela):                 # Função para sortear os números do bingo de forma que não sejam sorteados os mesmos números
    numero = random.randint(1, 50)

    if tabela[numero-1] == 0:
        tabela[numero-1] = 1

    else:
        while tabela[numero-1] == 1:
            numero = random.randint(1, 50)
        tabela[numero-1] = 1

    print('\n###############################################################')
    print('#                      NÚMERO SORTEADO:', numero, '                   #')
    print('###############################################################')
    return numero


def trocarCartela(atual):             # Função para mostrar ao usuário qual cartela ele trocou para
    print('\n###############################################################')
    print('#             VOCÊ AGORA É DONO(A) DA CARTELA:', atual, '             #')
    print('###############################################################')


def checagem(x, y, z, k, numero, respostas, acertos):         # Função para checar se o número sorteado já foi riscado nas cartelas
    for i in range(0, len(x)):
        if x[i] == numero and respostas[0][i] == '    ':
            respostas[0][i] = '____'
            respostas[4][i] = '‾‾‾‾'
            acertos[0] += 1

        if y[i] == numero and respostas[1][i] == '    ':
            respostas[1][i] = '____'
            respostas[5][i] = '‾‾‾‾'
            acertos[1] += 1

        if z[i] == numero and respostas[2][i] == '    ':
            respostas[2][i] = '____'
            respostas[6][i] = '‾‾‾‾'
            acertos[2] += 1

        if k[i] == numero and respostas[3][i] == '    ':
            respostas[3][i] = '____'
            respostas[7][i] = '‾‾‾‾'
            acertos[3] += 1

    return respostas, acertos


def rol():                  # Função para salvar o nome do ganhador no arquivo ''vencedores.txt''
    nome = input('Digite o seu nome para constar no rol de vencedores: ')
    data = str(date.today()).split('-')
    data = data[2] + '/' + data[1] + '/' + data[0]
    hora = time.strftime('%H:%M:%S')
    file = open('vencedores.txt', 'a', encoding='utf-8')
    file.write(nome + ' - ' + data + ' - ' + hora)
    file.write('\n')
    file.close()


def main():           # Função principal do quiz
    cartela_atual = 1
    acertos = [0]*4
    tabela = [0]*50      # Vetor que será responsável por verificar quais números já foram sorteados para que não sejam repitidos
    vencedor = -1
    cartela_1, cartela_2, cartela_3, cartela_4 = '| ', '| ', '| ', '| '
    respostas = [['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ['    ', '    ', '    ', '    ', '    '],
                 ]

    cartela = gerarCartela()
    cartela_inicial = [0]*len(cartela)

    for i in range(len(cartela)):           # Laço para transformar as cartelas de strings para inteiros
        cartela_inicial[i] = cartela[i].split(',')
        cartela_inicial[i] = list(map(int, cartela_inicial[i]))

    x, y, z, k = cartela_inicial[0], cartela_inicial[1], cartela_inicial[2], cartela_inicial[3]   # Cada cartela possui uma variável atribuída

    input('Olá! Seja bem-vindo(a) ao Bingo Lite!\nPressione qualquer tecla para iniciar o jogo.')

    for i in range(len(x)):                             # Laço para aplicar o layout das cartelas no terminal
        if not x[i] < 10:
            cartela_1 += str(x[i]) + ' | '
        else:
            cartela_1 += '0' + str(x[i]) + ' | '

        if not y[i] < 10:
            cartela_2 += str(y[i]) + ' | '
        else:
            cartela_2 += '0' + str(y[i]) + ' | '

        if not z[i] < 10:
            cartela_3 += str(z[i]) + ' | '
        else:
            cartela_3 += '0' + str(z[i]) + ' | '

        if not k[i] < 10:
            cartela_4 += str(k[i]) + ' | '
        else:
            cartela_4 += '0' + str(k[i]) + ' | '

    while True:                    # Laço ininterrupto do jogo
        aux = 'f'
        novaRodada(cartela_1, cartela_2, cartela_3, cartela_4, cartela_atual, respostas)

        if acertos[0] == 5 or acertos[1] == 5 or acertos[2] == 5 or acertos[3] == 5:    # Checagem da quantidade de acertos por cartela
            for j in range(len(acertos)):
                if acertos[j] == 5:
                    vencedor = j
            break

        alternativas = ''

        for i in range(1, 5):                 # Laço que mostra ao usuário para quais cartelas ele pode trocar na rodada
            if i != cartela_atual:
                alternativas += str(i) + ','
        alternativas = alternativas.split(',')
        alternativas = str(alternativas[0]) + ', ' + str(alternativas[1]) + ' ou ' + str(alternativas[2])

        while aux != str(1) and aux != str(2) and aux != str(3) and aux != str(4) and aux != '':      # Somente aceitar 5 inputs diferentes
            aux = input('# SELECIONE OUTRA CARTELA (' + alternativas + ') ou PRESSIONE ENTER PARA SORTEAR: ')

        if aux == '':                                                                         # Sortear número
            numero = sortearNumero(tabela)
            respostas, acertos = checagem(x, y, z, k, numero, respostas, acertos)
        else:                                                                                 # Trocar de cartela
            trocarCartela(aux)
            cartela_atual = int(aux)

    if cartela_atual == vencedor + 1:                                                         # No caso de vitória
        print('# PARABÉNS! VOCÊ VENCEU!!!')
        rol()

    else:                                                                                     # No caso de derrota
        print('# OUTRA CARTELA FOI COMPLETADA!')
        print('# Melhor sorte da próxima vez!')


if __name__ == '__main__':
    main()