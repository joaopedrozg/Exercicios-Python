""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""

def peso_ideal(altura):
    peso = (72.7 * altura) - 58
    return peso



if __name__ == '__main__':
    altura = input('Digite a altura a ser calculada: ')
    peso = peso_ideal(1.73)
    print(f'O peso ideal para uma pessoa de altura {altura} é de {peso} Kg')
