# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada quatro números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
# b) O programa principal lê 4 séries de 4 números a, b, c, d. Para cada série lida imprime o maior dos quatro números usando a função Max.

import random

def max(a, b, c, d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    elif d>a and d>b and d>c:
        return d
    elif a == b == c == d:
        return random.choice([a,b,c,d])
        
def main():
    while True:
        try:
            a = int(input('Primeiro Número: '))
            b = int(input('Segundo Número: '))
            c = int(input('Terceiro Número: '))
            d = int(input('Quarto Número: '))
            
            print(f'Maior número: {max(a,b,c,d)}')
            break
        except:
            print('Digite um número válido.')
            continue

if __name__ == '__main__':
    main()