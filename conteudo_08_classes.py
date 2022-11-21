## IMPORTANDO UMA CLASSE

# import: Importa o modulo por completo
# from: Importa somente parte do modulo

## IMPORT
from conteudo_07_classes import usuario

## INSTANCIANDO A CLASSE
pessoa1 = usuario("Willian", "Fonseca", 25)

## IMPRIMINDO OS DADOS DA CLASSE
print(f"O meu nome é {pessoa1.nome} {pessoa1.sobre_nome} e eu tenho {pessoa1.idade} anos de idade!")
print(pessoa1.nome)
print(pessoa1.sobre_nome)
print(pessoa1.idade)


