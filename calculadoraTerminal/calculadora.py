def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def elevaQuadrado(a):
    return pow(a, 2)


def main():
    opcao = 0
    while (opcao != 5):
        print("\n----CALCULADORA NO TERMINAL----\n")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = int(input("Digite a opção que deseja utilizar:"))

        if opcao < 1 or opcao > 5:
            print("Valor inválido")
            continue
        if opcao == 5:
            print("Saindo..")
            break
            a
        valorA = int(input("Digite o valor de a:"))
        valorB = int(input("Digite o valor de b:"))

        if opcao == 1:
            resultado = soma(valorA, valorB)
            print(f"{valorA} + {valorB} = {resultado}")
        if opcao == 2: 
            resultado = subtracao(valorA, valorB)
            print(f"{valorA} - {valorB} = {resultado}")
        if opcao == 3: 
            resultado = multiplicacao(valorA, valorB)
            print(f"{valorA} * {valorB} = {resultado}")
        if opcao == 4: 
            resultado = divisao(valorA, valorB)
            print(f"{valorA} / {valorB} = {resultado}")


if __name__ == "__main__":
    main()