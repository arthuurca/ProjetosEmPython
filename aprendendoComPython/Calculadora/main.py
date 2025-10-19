def subtracao(a, b):
    return a - b

def multiplicacao(a,b):
    return a * b

def soma(a, b):
    return a + b

def divisao(a, b):
    return a/b

a = int(input("Digite um valor: "))

b = int(input("Digite outro valor: "))

x = 0

while( x != 5):
    x = int(input(f"Selecione a opção para calculadora: \n1. {a} + {b}\n2. {a} - {b}\n3. {a} * {b}\n4. {a}/{b}\n5. Sair\n"))

    if x == 1:
        resultado = soma(a, b)
        print(f"{a} + {b} = {resultado}\n")
    if x == 2:
        resultado = subtracao(a, b)
        print(f"{a} - {b} = {resultado}\n")
    if x == 3:
        resultado = multiplicacao(a, b)
        print(f"{a} * {b} = {resultado}\n")
    if x == 4:
        resultado = divisao(a, b)
        print(f"{a} / {b} = {resultado}\n")
    if x > 5 or x < 1:
        print(f"{x} não é uma opção valida (idiota) digite novamente.\n")