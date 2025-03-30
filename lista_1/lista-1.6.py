# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte: 
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5.

def poligono (lado, medida):
    if lado == 3:
        perimetro = lado * medida
        return f'Triângulo de perímetro {perimetro:.2f}cm'
    elif lado == 4:
        area = medida ** 2
        return f'Quadrado de área {area:.2f}cm²'
    elif lado == 5:
        return f'Pentágono'
    
while True:
    try:
        lado = int(input('Quantos lados tem o polígono (3, 4 ou 5)? '))
        if lado not in [3, 4, 5]:
            print('Digite um valor válido para o número de lados (3, 4 ou 5)!')
            continue   
        
        medida = float(input('Qual a medida dos lados do polígono? '))
        if medida <= 0:
           print('A medida do lado deve ser um número positivo.')
           continue

        print (poligono(lado, medida))
        break
    except ValueError:
        print('Digite um valor válido')
    