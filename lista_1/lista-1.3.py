# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius. Fórmula: C = ((F-32)/9)*5

def celsius (f):
    c = ((f - 32)/9*5)
    return c


while True:
    try:
        temp_f = float(input('Digite a temperatura em Fahrenheit: '))
        print (f'\nA temperatura em Celsius é {celsius(temp_f):.1f}°C.')
        break
    except TypeError:
        print ('Digite um valor válido.')
