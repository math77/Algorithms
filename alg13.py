aluno = input("Digite o nome do aluno\n")
nota1 = int(input("Digite a primeira nota do aluno\n"))
nota2 = int(input("Digite a segunda nota do aluno\n"))
nota3 = int(input("Digite a terceira nota do aluno\n"))

media_final = (nota1*2+nota2*3+nota3*5)/10
print("A media final de {} foi: {}".format(aluno, media_final))
