quantidade = int(input("Digite a quantidade de maçãs compradas\n"))
if quantidade > 0 and quantidade < 12:
    print("O preço final da compra é {} reais".format(quantidade*1.30))
else:
    print("O preço final da compra é {} reais".format(quantidade*1.00))
