import random

def gerando_numero():
    numero_aleatorio = random.randrange(1,7)
    print(numero_aleatorio)
    return numero_aleatorio


def usuario_responde():
    resposta = input('sim / nao: ')
    resposta = resposta.upper()
    if 'SIM' == resposta:
        resposta = True
        return resposta
    else:
        resposta = False
        return resposta


print('Você deseja jogar o Dado? ')
resposta = usuario_responde()


while resposta:
    if resposta == True:
        gerando_numero()
        print('deseja continuar jogando ?')
        resposta = usuario_responde()
    elif resposta == False:
        break
    else:
        print('* resposta inválida * Tente novamente *')
        usuario_responde()
