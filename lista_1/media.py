# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).

def calc_media (n1, n2):
    media = (n1+n2)/2

    if media >= 6:
        return f'Média: {media:.2f}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media:.2f}\nREPROVADO.'
    
while True:
    try:
        n1 = float(input(f'\nNota 1:'))
        n2 = float(input(f'\nNota 2:'))
        if n1 >= 0 and n2 >= 0:
            print (calc_media(n1, n2))
            break
        else:
            print ('Valor inválido. A nota deve ser maior ou igual a 0.')
    except:
        print ('Digite um valor válido!')
