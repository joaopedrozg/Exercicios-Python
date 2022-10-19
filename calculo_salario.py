"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

def calcula_salario(valor_por_hora, quantidade_horas):
    salario_bruto = valor_por_hora * quantidade_horas
    imposto_renda = (11 * salario_bruto) / 100
    inss = (8 * salario_bruto) / 100
    sindicato = (5 * salario_bruto) / 100
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato
    return [salario_bruto, imposto_renda, inss, sindicato, salario_liquido]


if __name__ == '__main__':
    valor_por_hora = float(input('Qual o valor da hora: '))
    quantidade_horas = float(input('Qual a quantidade de horas trabalhadas: '))
    result = calcula_salario(valor_por_hora, quantidade_horas)
    print(f'+ Salário Bruto: R$ {result[0]}')
    print(f'- IR : R$ {result[1]}')
    print(f'- INSS : R$ {result[2]}')
    print(f'- Sindicato : R$ {result[3]}')
    print(f'Salário Liquido: R$ {result[4]}')
