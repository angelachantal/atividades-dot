# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas: - para homens : (72.7 * h) – 58  - para mulheres : (62.1 * h) – 44.7 Observação: Altura = h (na fórmula acima).

def peso_ideal(altura, sexo):
    if sexo == 2 and altura > 0:
        return (72.7 * altura) - 58
    elif sexo == 1 and altura > 0:
        return (62.1 * altura) - 44.7
    else:
        raise ValueError('Valor inválido.')


def main():
    try:
        altura = float(input('Altura (em metros): '))
        sexo = int(input('Sexo (1-Feminino, 2-Masculino): '))

        # Verifica se os valores são válidos
        if altura <= 0 or sexo not in [1, 2]:
            print('Erro: Altura deve ser maior que 0 e sexo deve ser 1 ou 2.')
            return  # Sai da função para evitar erro posterior

        print(f'Peso Ideal: {peso_ideal(altura, sexo):.2f} kg')

    except ValueError:
        print('Erro: Entrada inválida. Digite valores numéricos corretamente.')


if __name__ == '__main__':
    main()
