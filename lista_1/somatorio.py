# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def calc_somatorio(n):
    somatorio = 0
    for i in range (1, n+1):
        somatorio += i
    return somatorio
         
def main():
    while True:
        try:
            n = int(input('Número: '))
            
            if n<=0:
                print ('Digite um número inteiro maior que zero.')
                continue
    
            print(f'Divisores do número: {calc_somatorio(n)}')
            break
        except:
            print('Digite um número válido.')
            continue

if __name__ == '__main__':
    main()