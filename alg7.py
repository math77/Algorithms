anos = int(input("Digite seus anos de idade\n"))
meses = int(input("Digite seus meses de idade\n"))
dias = int(input("Digite seus dias de idade\n"))

anos_para_dias = anos * 365
meses_para_dias = meses * 30
idade_em_dias = anos_para_dias + meses_para_dias + dias

print("Sua idade em dias é: {}".format(idade_em_dias))
