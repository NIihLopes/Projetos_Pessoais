import random

def gerando_numero_da_sorte():
    numeros_da_sorte = random.randrange(1,60)
    return numeros_da_sorte

def continuar():
    print('** Digite 1 para gerar um Numero! **')
    print('** Digite 2 para encerrar! **')
    gerar_numero = int(input("digite:"))
    if gerar_numero == int(1):
        resposta = True
        return resposta
    else:
        resposta = False
        return resposta

jogo_premiado = []

print('** INICIO -- BOA SORTE **')

continua = continuar()
while continua:
    if continua == True:
        jogo_premiado.append(gerando_numero_da_sorte())
        print(jogo_premiado)
        continua = continuar()
    elif continua == False:
        break
    else:
            print('* resposta inválida * Tente novamente *')
            continuar()
print('esse é seu jogo! ',jogo_premiado)


