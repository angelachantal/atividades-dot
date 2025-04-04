# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.

def fatorial(n):
    n_fatorial = n
    for i in range(1, n):
        n_fatorial *= i
    return f'{n}! = {n_fatorial}'

while True:
    try:
        n = int(input('Digite um número inteiro positivo: '))
        if n <= 0:
            print ('O número deve ser maior que zero.')
            continue
        print (fatorial(n))
    except ValueError:
        print ('Digite um número válido!')