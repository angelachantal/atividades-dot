# 1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
def eh_par (n):
    if n % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        n = input ('Número: ')
        if type(n) == int:
            print (eh_par(n))
        break
    except:
        print ('Digite um número inteiro válido.')
        