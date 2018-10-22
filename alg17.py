nota1 = int(input("Digite a nota da primeira avaliação\n"))
nota2 = int(input("Digite a nota da segunda avaliação\n"))
media = (nota1+nota2)/2
if media >= 6:
    print("Foi aprovado com média final de {}".format(media))
else:
    print("Foi reprovado com média final de {}".format(media))
