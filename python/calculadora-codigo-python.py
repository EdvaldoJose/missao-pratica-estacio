# Calculadora usando uma funcao python.

def calculadora():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    resultado_adicao = valor1 + valor2
    print("Resultado da adicao: ", resultado_adicao)

    resultado_subtracao = valor1 - valor2
    print("Resultado da subtracao: ", resultado_subtracao)

    resultado_multiplicacao = valor1 * valor2
    print("Resultado da multiplicacao: ", resultado_multiplicacao)

    resultado_divisao = valor1 / valor2
    print("Resultado da divisao: ", resultado_divisao)

    if valor2 == 0:
        print("Erro: Divisa por zero")
    else:
        resultado_divisao = valor1 / valor2
        print("Resultado da divisao: ", resultado_divisao)


calculadora()
