import pytest

    # Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
   return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2




if __name__ == '__main__':


    # Garçon - Requisições / chamadas
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}')  # <-- Prato

    subtracao = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    multiplicacao = multiplicar_dois_numeros(5,3)
    print(f'A multuplicação é {resultado}')

    divisao = dividir_dois_numeros(8,0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2,3)
    print(f'A exponenciação é {resultado}')


    #Degustador / Testar

def testar_somar_dois_numeros():
    # - 1' Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # - 2' Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3' Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

