"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total

"""

def calcula_galoes_a_pagar(quantidade_metros):
    valor_por_galao = 80
    galoes = quantidade_metros / 54
    if galoes == 1:
        galoes = 1
        return [galoes * valor_por_galao, galoes]

    if isinstance(galoes, float):
        galoes = round(galoes) + 1
        return [galoes * valor_por_galao, galoes]


if __name__ == '__main__':
    quantidade_metros = int(input(
                                  f'Digite a quantidade de metros quadrados a '
                                  f'serem pintados: '))
    result = calcula_galoes_a_pagar(quantidade_metros)
    print(
        f'A quantidade de {quantidade_metros} m² precirará de {result[1]} galoes'
        f'com um custo de R$ {result[0]}'
        )
