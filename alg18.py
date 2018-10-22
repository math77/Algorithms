ano_atual = int(input("Digite o ano atual\n"))
ano_nascimento = int(input("Digite o ano de nascimento\n"))

if (ano_atual - ano_nascimento) >= 16:
    print("Você vai poder votar esse ano")
else:
    print("Oops, você não pode votar ainda")
