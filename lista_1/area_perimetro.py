# 2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo. Área = PI * r2; Perímetro = PI * 2 * r;

def calc_area (raio):
    area = 3.14 * (raio**2)
    return area

def calc_perimetro (raio):
    perimetro = 3.14 * 2 * raio
    return perimetro

while True:
    try:
        raio = float(input('Digite o raio do círculo:'))
        print(f'\nÁrea do círculo: {calc_area(raio):.2f}')
        print(f'\nPerímetro do círculo: {calc_perimetro(raio):.2f}')
        break
    except:
        print('Digite um número válido.')
