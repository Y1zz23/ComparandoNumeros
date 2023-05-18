n1 = int(input("Digite o 1 número: "))
n2 = int(input("Digite o 2 número: "))
if n1 > n2:
    print("O primeiro número ({}) é maior que o segundo número ({})".format(n1,n2))
elif n2 > n1:
    print("O segundo número ({}) é maior que o primeiro número ({})".format(n2,n1))
else:
    print("Os dois números sao iguais")