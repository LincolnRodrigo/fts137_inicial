import csv

import pytest

from main import somar_dois_numeros, calcular_area_do_circulo, calcular_volume_do_paralelograma


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


# anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio,resultado_esperado', [
    # valores
    (1, 3.14),  # teste n° 1
    (2, 12.56),  # teste n° 2
    (3, 28.26),  # teste n° 3
    (4, 50.24),  # teste n° 4
    ('a', 'Falha no calculo - Raio não é um número'),  # teste n° 5
    (' ', 'Falha no calculo - Raio não é um número'),  # teste n° 6
])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentamos para que os parametros sejam lidos
    # raio = 2
    # resultado_esperado = 12.56

    # 2 _ Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3 - Valida
    assert resultado_atual == resultado_esperado


# Ler dados de um csv para usar no teste seguinte
def ler_dados_csv():
    dados_csv = []  # criação de uma lista vazia
    nome_arquivo = 'C:/users/linco/PycharmProjects/fts137_inicial/test/db/massa_caixa.csv'  # local e nome do arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  # repetir a leitura até o fim de arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())
def testar_calcular_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):
    # 1 - Configura
    '''
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    '''

    # 2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))

    # - Valida
    assert resultado_atual == int(resultado_esperado)
