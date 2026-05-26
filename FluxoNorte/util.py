import os
def limpar_tela():
    os.system('clear')

def geraIdPedido():
    return 1

def selecionePrioridade():
    retPrioridade = ""
    while retPrioridade == "":
        print("-----PRIORIDADE-----")
        print("| 0 - Normal       |")
        print("| 1 - Alta         |")
        print("--------------------\n")

        prioridade = int(input("Digite a prioridade do pedido: "))
        match prioridade:
            case 0:
                retPrioridade = "Normal"
            case 1:
                retPrioridade = "Alta"
            case _:
                print("Opção inválida! Tente novamente.")
                
    return retPrioridade

def selecioneStatus():
    retStatus = ""
    while retStatus == "":
        print("-------STATUS-------")
        print("| 0 - Pendente      |")
        print("| 1 - Alta          |")
        print("--------------------\n")

        prioridade = int(input("Digite a prioridade do pedido: "))
        match prioridade:
            case 0:
                retStatus = "Normal"
            case 1:
                retStatus = "Alta"
            case _:
                print("Opção inválida! Tente novamente.")

    return retStatus

def selecioneVeiculo():
    retVeiculo = ""
    while retVeiculo == "":
        print("-------VEÍCULO-------")
        print("| 1 - Carro          |")
        print("| 2 - Van            |")
        print("| 3 - Moto           |")
        print("--------------------\n")

        prioridade = int(input("Selecione o tipo de veículo: "))
        match prioridade:
            case 1:
                retVeiculo = "Carro"
            case 2:
                retVeiculo = "Van"
            case 3:
                retVeiculo = "Moto"
            case _:
                print("Opção inválida! Tente novamente.")

    return retVeiculo

def verificaFinalizar():
    finalizar = False
    resposta_valida = False

    while not resposta_valida:
        print("Você tem certeza que deseja finalizar o sistema?")
        print("| S - Sim           |")
        print("| N - Não           |")
        print("--------------------\n")

        opcao = input("Selecione (S/N): ").upper()
        match opcao:
            case "S":
                finalizar = True
                resposta_valida = True

            case "N":
                finalizar = False
                resposta_valida = True

            case _:
                print("Opção inválida! Tente novamente.")
    return finalizar


def menuEntregadores(entregadores):
    print("-------SELECIONE-------")
    for ent in entregadores.keys():
        print(f"|ID {ent} - {entregadores[ent][0]}")
    print("-----------------------")

#gerar_id_entregadores feito pelo Thomas
def gerar_id_entregador (entregadores):
    chaves_entregadores = entregadores.keys()
    
    maior_id = 0
    for chave_id in chaves_entregadores:
        int_chave_id = int(chave_id)
        
        if int_chave_id > maior_id:
            maior_id = int_chave_id
    
    maior_id += 1
    return str(maior_id).zfill(4)
