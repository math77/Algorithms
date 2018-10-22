salario = float(input("Digite o valor atual do seu salário\n"))
reajuste = float(input("Digite o percentual de reajuste do salário\n"))

novo_salario = salario + (salario*(reajuste/100))
print("O seu salário reajustado é {} reais".format(novo_salario))
