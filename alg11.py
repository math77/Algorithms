carros_vendidos = int(input("Digite a quantidade de carros vendidos\n"))
total_vendas = float(input("Digite o valor total de suas vendas\n"))
salario_fixo = float(input("Digite o valor do seu salário fixo\n"))
valor_por_carro = float(input("Digite o valor que você recebe por carro vendido\n"))

salario_final = salario_fixo + (total_vendas*0.05) + (carros_vendidos*valor_por_carro)
print("O seu salário final é de {} reais".format(salario_final))
