#perguntar ao usuário qual operação deseja fazer
#receber os valores e calcular

def operacao():
    operadores = ['+','-', '*','/']
    operador = input('digite o sinal da operação desejada: ')
    operador = operador.strip()
    while operador not in operadores:
        if operador not in operadores:
            print('< operação inválida! >')
            operador = input('digite o sinal da operação desejada: ')
            operador = operador.strip()
        else:
            return operador
    return operador

def adicao():
    print(3*'=',' SOMA ',3*'=')
    valor_um = int(input('digite primeiro valor: '))
    valor_dois = int(input('digite segundo valor: '))
    resultado_soma = valor_um + valor_dois
    return resultado_soma

def subtracao():
    print(3*'=',' SUBTRAÇÃO ',3*'=')
    valor_um = int(input('digite primeiro valor: '))
    valor_dois = int(input('digite segundo valor: '))
    resultado_subtracao = valor_um - valor_dois
    return resultado_subtracao

def multiplicacao():
    print(3*'=',' MULTIPLICAÇÃO ',3*'=')
    valor_um = int(input('digite primeiro valor: '))
    valor_dois = int(input('digite segundo valor: '))
    resultado_multiplica = valor_um * valor_dois
    return resultado_multiplica

def divisao():
    print(3*'=',' DIVISÃO ',3*'=')
    valor_um = int(input('digite primeiro valor: '))
    valor_dois = int(input('digite segundo valor: '))
    resultado_divisao = valor_um / valor_dois
    return resultado_divisao

def continuar_calculando():
    continuar = True
    while continuar:
        usuario_decide = int(input('(1) - continuar / (0) - sair : '))

        if usuario_decide == 1:
            continuar = True
            return continuar
        elif usuario_decide == 0:
            continuar = False
            return continuar
        else:
            print('<< OPÇÃO INVÁLIDA >>')


print(5*'*','calculadora',5*'*')

continuar = True

while continuar:
    sinal = operacao()

    if sinal == '+':
       soma = adicao()
       print('resultado é ',soma)
    elif sinal == '-':
        sub = subtracao()
        print('o resultado é ',sub)
    elif sinal == '*':
        mult = multiplicacao()
        print('o resultado é ', mult)
    else:
        divide = divisao()
        print('o resultado é ', divide)

    continuar = continuar_calculando()

