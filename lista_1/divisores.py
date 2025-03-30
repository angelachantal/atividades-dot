# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def contar_divisores(n):
    divisores = 0
    for i in range (1, n+1):
        if n%i == 0:
            divisores += 1
    return divisores
        
def main():
    while True:
        try:
            n = int(input('Número: '))
            
            if n<=0:
                print ('Digite um número inteiro maior que zero.')
                continue
    
            print(f'Divisores do número: {contar_divisores(n)}')
            break
        except:
            print('Digite um número válido.')
            continue

if __name__ == '__main__':
    main()