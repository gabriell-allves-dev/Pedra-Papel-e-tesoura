import time
import random
import sys

def caixa():
    print('='*20)

n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'

green = '\033[1;32m'

print(f'{green}')

escolhas = (n1, n2, n3)

while True:
    while True:
        print('='*6 + ' JOKENPÔ ' + '='*6)

        print()
 
        print('[1] - J1 VS COM')
        print('[2] - J1 VS J2')

        print()

        try:
            opcao = int(input('Alternativa: '))
            caixa()

            print()

            break

        except ValueError:
            print('Apenas números')

            print()

    if opcao == 1:
        caixa()
        jogador_1 = input('Digite seu nome: ')
        caixa()

        print()

        while True:
            time.sleep(1.5)
            caixa()
            print('Espere um pouco...')
            time.sleep(2)
            print('Computador pensando...')
            caixa()
            time.sleep(2)
            print()

            n4 = random.choice(escolhas)

            caixa()
            n5 = input(f'{jogador_1} escolha: (Pedra - Papel - Tesoura): ').strip().capitalize()
            caixa()

            if n5 not in escolhas:
                print('\033[1;31m' + 'Escolha inválida!' + '\033[1;32m')
                print()
                continue

            time.sleep(1.5)

            print()

            caixa()
            print(f'{jogador_1} escolheu: {n5}')
            caixa()
            print()

            time.sleep(3)

            caixa()
            print(f'Computador escolheu: {n4}')
            caixa()

            print()

            if n5 == n4:
                caixa()
                print('Empate!')
                caixa()

            elif n5 == n1 and n4 == n2 or n5 == n2 and n4 == n3 or n5 == n3 and n4 == n1:
                caixa()
                print('CPU ganhou')
                caixa()

            else:
                caixa()
                print(f'{jogador_1} ganhou!')
                caixa()

            print()
            time.sleep(3)
            caixa()
            print('[1] - Jogar novamente')
            time.sleep(1.5)
            print('[2] - Voltar ao início')
            time.sleep(1.5)
            print('[3] - Sair')
            time.sleep(1.5)
            caixa()

            print()

            caixa()
            opcao = input('Escolher opção: ')
            caixa()

            print()

            if opcao == '1':
                pass
            elif opcao == '2':
                break
            elif opcao == '3':
                caixa()
                print('Finalizando programa...')
                time.sleep(1.5)
                print('3...')
                time.sleep(1.5)
                print(' 2..')
                time.sleep(1.5)
                print('  1.')
                time.sleep(1.5)
                print('\033[1;31m' + 'PROGRAMA FINALIZADO!' + '\033[1;32m')
                sys.exit()
            
            else:
                print('\033[1;31m' + 'Opção inválida!' + '\033[1;32m')

    elif opcao == 2:
        caixa()
        print('='*6 + 'JOGADORES' + '='*6)
        caixa()

        print()

        caixa()
        jogador_1 = input('Jogador 1: ')
        jogador_2 = input('Jogador 2: ')
        caixa()

        print()

        while True:
            time.sleep(1)
            caixa()
            print('Espere um pouco...')
            caixa()
            print()

            time.sleep(3)
            caixa()
            print('Jogador 1')
            caixa()
            print()
            time.sleep(1.5)
            caixa()
            print('Agora é a sua vez!')
            caixa()
            print()
            time.sleep(1.5)

            caixa()
            n4 = input('Escolha (Pedra - Papel - Tesoura): ').strip().capitalize()
            caixa()
            print()

            time.sleep(3)
            caixa()
            print('Jogador 2')
            caixa()
            print()
            time.sleep(1.5)
            caixa()
            print('Agora é a sua vez!')
            caixa()
            print()
            time.sleep(1.5)

            caixa()
            n5 = input('Escolha (Pedra - Papel - Tesoura): ').strip().capitalize()
            caixa()
            print()

            if n4 not in escolhas or n5 not in escolhas:
                print('\033[1;31m' + 'Escolha inválida!' + '\033[1;32m')
                print()
                time.sleep(2.5)
                continue

            time.sleep(1.5)

            print()

            caixa()
            print(f'{jogador_1} escolheu: {n4}')
            caixa()
            print()

            time.sleep(2)

            caixa()
            print(f'{jogador_2} escolheu: {n5}')
            caixa()

            print()
            time.sleep(3)

            if n5 == n4:
                caixa()
                print('Empate!')
                caixa()
                time.sleep(3)

            elif n5 == n1 and n4 == n2 or n5 == n2 and n4 == n3 or n5 == n3 and n4 == n1:
                caixa()
                print(f'{jogador_1} ganhou!')
                caixa()
                time.sleep(3)

            else:
                caixa()
                print(f'{jogador_2} ganhou!')
                caixa()
                time.sleep(3)

            print()

            caixa()
            print('[1] - Jogar novamente')
            time.sleep(1.5)
            print('[2] - Voltar ao início')
            time.sleep(1.5)
            print('[3] - Sair')
            caixa()
            time.sleep(1.5)

            print()

            caixa()
            opcao = input('Escolher opção: ')
            caixa()
            print()

            if opcao == '1':
                pass
            elif opcao == '2':
                break
            elif opcao == '3':
                caixa()
                print('Finalizando programa...')
                time.sleep(1.5)
                print('3...')
                time.sleep(1.5)
                print(' 2..')
                time.sleep(1.5)
                print('  1.')
                time.sleep(1.5)
                print('\033[1;31m' + 'PROGRAMA FINALIZADO!' + '\033[1;32m')
                sys.exit()
            
            else:
                print('\033[1;31m' + 'Opção inválida!' + '\033[1;32m')

    else:
        print('\033[1;31m' + 'Valor errado!' + '\033[1;32m')