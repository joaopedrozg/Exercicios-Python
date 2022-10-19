""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de
peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
que você faça um programa que leia a variável peso (peso de peixes) e calcule o
excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar. Imprima os dados do
programa com as mensagens adequadas."""


def verifica_multa_peso(peso):
    taxa_por_peso = 4
    execedente = peso - 50

    if peso > 50:
        multa = execedente * taxa_por_peso
        return [execedente, multa]
    if execedente < 0:
        return ['Sem excesso', 'Sem Multa']


if __name__ == '__main__':
    peso = float(input('Quantos Kilos de peixe foram pescados: '))

    result = verifica_multa_peso(peso)

    print(f'Peso pescado: {peso} Peso Excedido: {result[0]} Multa: {result[1]} ')
