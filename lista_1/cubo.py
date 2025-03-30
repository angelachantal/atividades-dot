# 8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. 
# Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.

def calc_cubo(n):
    cubo = n ** 3
    return cubo

while True:
    try:
        n = float(input('Digite um número: '))
        resposta = input('Deseja calcular o cubo desse número? (S-Sim, N-Não) ').strip().upper()
        if resposta == 'S':
            print (f'{resposta}\n{n}³ = {calc_cubo(n)}')
            break
        elif resposta == 'N':
            print(f'{resposta}\nPrograma encerrado.')
            break
        else:
            print ('Digite S para "Sim", e N para "Não".')
            continue
    except:
        print('Digite uma valor numérico.')
         
            