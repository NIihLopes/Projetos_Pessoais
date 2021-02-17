#criar uma lista com todas as frases
#criar uma função para selecionar aleatóreamente um item da lista
#imprimir na tela a resposta com a pergunta do usuário
import random


frases = [
'sim, vai lá\n',
'Melhor não\n',
'Eu acho que sim\n',
'Eu acho que não\n',
'Sim, com certeza\n',
'Com certeza não\n',
'Você esta certo(a)\n',
'Você esta errado(a)\n',
'Eu não faria isso\n',
'Isso é o que eu faria\n',
'Eu não tenho resposta pra tudo\n'
]
def pergunta_usuario():
    pergunta = input('>> pergunte: ')
    return pergunta

def seleciona_resposta():
    posicao = random.randrange(0, 12)
    return posicao

def continuar_pergntando():
    print('** deseja fazer outra pergunta? **')
    continuar = input('sim / nao: ')
    continuar = continuar.upper()
    return continuar


print('**FAÇA UMA PERGUNTA E TERÁ SUA RESPOSTA **')
pergunta = pergunta_usuario()

posicao = seleciona_resposta()
print(frases[posicao])

continuar = continuar_pergntando()

while continuar == 'SIM' or continuar != 'nao':
    if continuar == 'SIM':
        pergunta = pergunta_usuario()
        posicao = seleciona_resposta()
        print(frases[posicao])
        continuar = continuar_pergntando()
    elif continuar == 'NAO':
        break
    else:
        print('** Resposta Inválida **')
        continuar = continuar_pergntando()
