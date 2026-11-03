import time
import random
import sys

n1 = 'pedra'
n2 = 'papel'
n3 = 'tesoura'

escolhas = (n1, n2, n3)

while True:
    while True:
        print('='*6 + ' JOKENPÔ ' + '='*6)

        print()
 
        print('[1] - Jogador 1 vs CPU')
        print('[2] - Jogador 1 vs Jogador 2')

        print()

        try:
            opcao = int(input('Alternativa: '))

            print()

            break

        except ValueError:
            print('Apenas números')

            print()

    if opcao == 1:

        jogador_1 = input('Digite seu nome: ')

        print()

        while True:
            time.sleep(1)
            print('Espere um pouco...')
            time.sleep(1.5)
            print('Computador pensando...')
            time.sleep(2.5)
            n4 = random.choice(escolhas)

            print()

            n5 = input('Escolha (Pedra - Papel - Tesoura): ').strip().lower()

            if n5 not in escolhas:
                print('Escolha inválida!')
                print()
                continue

            time.sleep(1.5)

            print()

            print('='*20)
            print(f'{jogador_1} escolheu: {n5}')
            print('='*20)

            time.sleep(1.5)
            print()

            print('='*20)
            print(f'Computador escolheu: {n4}')
            print('='*20)

            print()

            if n5 == n4:
                print('Empate!')
                time.sleep(3)

                print()

            elif n5 == n1 and n4 == n2 or n5 == n2 and n4 == n3 or n5 == n3 and n4 == n1:
                print('CPU ganhou')

            else:
                print(f'{jogador_1} ganhou!')

            print('='*20)
            print('[1] - Jogar novamente')
            print('[2] - Voltar ao início')
            print('[3] - Sair')
            print('='*20)

            print()

            opcao = input('Escolher opção: ')

            print()

            if opcao == '1':
                pass
            elif opcao == '2':
                break
            elif opcao == '3':
                sys.exit()
            else:
                print('Opção inválida!')

    elif opcao == 2:
        print('Em produção...')
        print

    else:
        print('Valor errado!')

        print()