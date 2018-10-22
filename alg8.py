eleitores = int(input("Qual a quantidade total de eleitores?\n"))
votos_validos = int(input("Qual a quantidade de votos válidos?\n"))
votos_nulos = int(input("Qual a quantidade de votos nulos?\n"))
votos_brancos = int(input("Qual a quantidade de votos brancos?\n"))

print("Porcentagem de votos válidos: {}%".format((votos_validos/eleitores)*100))
print("Porcentagem de votos nulos: {}%".format((votos_nulos/eleitores)*100))
print("Porcentagem de votos brancos: {}%".format((votos_brancos/eleitores)*100))
