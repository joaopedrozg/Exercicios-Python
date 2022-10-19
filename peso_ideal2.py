"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

def peso_ideal_homem(altura):
    peso_h = (72.7 * altura) - 58

    return peso_h

def peso_ideal_mulher(altura):
    peso_m = (62.1 * altura) - 58

    return peso_m



if __name__ == '__main__':
    altura = float(input('Digite a altura a ser calculada: '))
    peso_M = peso_ideal_homem(altura)
    peso_H = peso_ideal_mulher(altura)
    print(f'O peso ideal para uma pessoa de altura {altura} se for Mulher {round(peso_M, 2)} Kg se for Homem {round(peso_H, 2)} Kg')
