# ESTRUTURA DO TRATAMENTO DE EXEÇÕES TRY/EXEPT
try:
    numero = 15/0 # Extrujtura de codigo
except ZeroDivisionError: # Tipo do erro
    print("Divisão por zero não existe") # tratamento da exeção

# ESTRUTURA DO TRATAMENTO DE EXEÇÕES TRY/FINALY
try:
    numero = 15/0
except ZeroDivisionError: # Tipo do erro
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada") # Finaliza a execução

# ESTRUTURA DO TRATAMENTO DE EXEÇÕES - GERANDO EXEÇÕES
try:
    raise ZeroDivisionError # Simula a passagem de uma exeção para testes
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

# ESTRUTURA DO TRATAMENTO DE EXEÇÕES - GERANDO EXEÇÕES A PARTIR DE UMA CONDIÇÃO
try:
    numero = 15
    divisor = 0
    assert divisor != 0
except:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")