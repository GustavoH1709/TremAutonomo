
def coletaInputUsuario() -> list:
    numCommandos = int(input("Quantidade de comandos: "))
    commandos = []
    for x in range(numCommandos):
        commandos.append((input("Esquerda (E) ou Direita (D): ")).upper())
        
    return commandos

def calculaPosicaoFinal(commandos) -> int:
    valor_final = 0;
    for x in commandos:
        if x == "E":
            valor_final += -1
        
        if x == "D":
            valor_final += 1
    return valor_final

def validaExercicio2(num):
    if num < -2 or num > 10:
        return False

    return True

def validaExercicio3(num, limit_esq, limit_dir):
    if num < limit_esq or num > limit_dir:
        return False

    return True

def exercicio1():
    comandos = coletaInputUsuario()
    posicao_final = calculaPosicaoFinal(comandos)
    print(posicao_final)

def exercicio2():
    comandos = coletaInputUsuario()
    posicao_final = calculaPosicaoFinal(comandos)
    
    if validaExercicio2(posicao_final) == True:
        print(posicao_final)
    else:
        print("Valor está fora dos padrões")

def exercicio3():
    limite_esquerda = int(input('Qual limite da esquerda: '))
    limite_direita = int(input('Qual limite da direita: '))

    comandos = coletaInputUsuario()
    posicao_final = calculaPosicaoFinal(comandos)

    if validaExercicio3(posicao_final, limite_esquerda, limite_direita) == True:
        print(posicao_final)
    else:
        print("Valor está fora dos padrões")

qual_aplicacao = input("1, 2 ou 3: ")

if qual_aplicacao == '1':
    exercicio1()
elif qual_aplicacao == '2':
    exercicio2()
elif qual_aplicacao == '3':
    exercicio3()
else:
    print("invalido")



