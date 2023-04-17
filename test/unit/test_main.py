import pytest

from main import somar_dois_numeros, calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1' Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / input
    num1 = 4
    num2 = 5
    # Saída / Output
    resultado_esperado = 9

    # - 2' Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3' Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    # 1 - Configura
    raio = 1
    resultado_esperado = 3.14

    # 2 _ Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado
