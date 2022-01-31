def lernotas():
    n=float(input("Digite a Nota para o aluno(a): "))
    return n

def resultado(n1, n2, n3):
    media=(n1+n2+n3)/3
    print("nota 1: ",n1)
    print("nota 2: ", n2)
    print("nota 3: ", n3)
    print("Média: ", media, "resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")




a = lernotas()
b = lernotas()
c = lernotas()
resultado(a,b, c)





