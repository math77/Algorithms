custo_fabrica = float(input("Qual o valor de fábrica do carro?\n"))

porcentagem_distr = custo_fabrica*0.28
impostos = custo_fabrica*0.45
custo_final = custo_fabrica + porcentagem_distr + impostos
print("O custo final do carro é {} reais".format(custo_final))
