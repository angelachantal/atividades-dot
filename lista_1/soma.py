# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
def somar(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1): 
        soma += i
    return soma

def main():
    try:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Último número: '))
    except ValueError:  
        print('Erro: Digite um número inteiro válido.')
        return  

    soma = somar(n1, n2)
    print(f'Soma: {soma}')

if __name__ == '__main__':
    main()


