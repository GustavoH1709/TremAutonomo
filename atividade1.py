
def calculaPosicaoFinal(lista) -> int:
    valor_final = 0;
    for x in commandos:
        if x == "E":
            valor_final += -1
        
        if x == "D":
            valor_final += 1
    return valor_final
    
def coletaInputUsuario() -> list:
    numCommandos = int(input("Quantidade de comandos: "))
    commandos = []
    for x in range(numCommandos):
        commandos.append((input("Esquerda (E) ou Direita (D): ")).upper())
        
    return commandos
    
    
commandos = coletaInputUsuario()
valor = calculaPosicaoFinal(commandos)
print(f"O valor final é {valor}")



