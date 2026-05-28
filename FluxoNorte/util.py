import os
def limpar_tela():
    os.system('cls')

# precisamos adicionar opções de "cancelar e voltar ao o menu anterior" em todos os menus

# entregadores podem entregar multiplos (2, 4 ou 6, depende do veiculo) pedidos,
# mas cada pedido só pode ser entregue por um entregador.


# geração de id "corrigida" pelo Thomas
def gerarIdPedido(nome_cliente, numero_id_atual):
    inicial_cliente = str(nome_cliente[0]).upper()

    id_pedido = inicial_cliente + str(numero_id_atual).zfill(4)
    return id_pedido

def selecionePrioridade():
    retPrioridade = ""
    while retPrioridade == "":
        print("-----PRIORIDADE-----")
        print("| 0 - Normal       |")
        print("| 1 - Alta         |")
        print("--------------------\n")

        prioridade = input("Digite a prioridade do pedido: ")
        match prioridade:
            case "0":
                retPrioridade = "Normal"
            case "1":
                retPrioridade = "Alta"
            case _:
                print("Opção inválida! Tente novamente.")
                
                
    return retPrioridade

#atualização de status 
def selecioneStatus():
    retStatus = ""
    while retStatus == "":
        print("-------STATUS-------")
        print("| 1 - Pendente       |")
        print("| 2 - Em trânsito    |")
        print("| 3 - Entregue       |")
        print("--------------------\n")

        status = int(input("Digite o status do pedido: "))
        match status:
            case 1:
                retStatus = "Pendente"
            case 2:
                retStatus = "Em trânsito"
            case 3:
                retStatus = "Entregue"
            case _:
                print("Opção inválida! Tente novamente.")

    return retStatus

#quero adicionar a carga do veiculo, mas não sei fazer o sistema usar
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


def menu_entregadores(entregadores, texto_pesquisa):
    print("-------SELECIONE-------")
    for ent in entregadores.keys():
        if texto_pesquisa in entregadores[ent][0] or texto_pesquisa in ent:
            print(f"|ID {ent} - {entregadores[ent][0]}")
    print("-----------------------")

def menu_pedidos(pedidos, texto_pesquisa):
    print("-------SELECIONE-------")
    for id in pedidos.keys():
        if texto_pesquisa in pedidos[id][0] or texto_pesquisa in id:
            print(f"|ID {id} de {pedidos[id][0]}, descrição: {pedidos[id][3]}")
    print("-----------------------")


#gerar_id_entregadores feito pelo Thomas
def gerar_id_entregador (numero_id_atual):
    return str(numero_id_atual).zfill(4)

#função disponibilidade feito pelo Thomas
def definir_disponibilidade ():
    retDisponibilidade = ""
    while retDisponibilidade == "":
        print("-------SELECIONE------")
        print("| 1 - Diponível      |")
        print("| 2 - Indisponível   |")
        print("----------------------\n")

        disponibilidade = int(input("Selecione a disponibilidade do entregador: "))
        match disponibilidade:
            case 1:
                retDisponibilidade = "Disponível"
            case 2:
                retDisponibilidade = "Indisponível"
            case _:
                print("Opção inválida! Tente novamente.")

    return retDisponibilidade

def carga(veiculo):
    if veiculo == "Moto":
        carga_max = 2
    if veiculo == "Carro":
        carga_max = 4
    if veiculo == "Van":
        carga_max = 6
    return carga_max

#função busca entregador disponivel feita pelo Thomas
def busca_entregador_disp (entregadores):
    print("--------RESULTADO-DA-CONSULTA--------")
    print("\tOs entregadores:")
    entregadores_disp = False
    for id, dados_entregador in entregadores.items():
        if (dados_entregador[3] == "Disponível"):
            entregadores_disp = True
            print(f"\tID:{id} // Nome: {dados_entregador[0]}")
    
    if (entregadores_disp):
        print("\tEstão Disponíveis")
    else:
        print("\tEstão Indisponíveis")


#função da consulta feita pelo Thomas
def selecionar_consulta(entregadores): #add pedidos como parametro depois
    ret_consulta = ""
    while ret_consulta == "":
        print("--------------CONSULTA--------------")
        print("| 0 - Pedidos Pendentes            |")
        print("| 1 - Pedidos Entregues            |")
        print("| 2 - Buscar Pedido por ID         |")
        print("| 3 - Entregador Disponível        |")
        print("| 4 - Todas as Entregas Realizadas |")
        print("|     por um Entregador            |")
        print("------------------------------------\n")

        consulta = int(input("Digite o que você deseja consultar: "))
        match consulta:
            case 0:
                ret_consulta = "Pedidos Pendentes" #chamar função de pedidos pendentes
            case 1:
                ret_consulta = "Pedidos Entregues" #chamar função de pedidos entregues
            case 2:
                ret_consulta = "Buscar Pedido por ID" # ... busca de pedido por ID
            case 3: 
                busca_entregador_disp(entregadores)
                break
            case 4:
                ret_consulta = "Todas as Entregas Realizadas por um Entregador"
            case _:
                print("Opção inválida! Tente novamente.")
                
    return ret_consulta 

def selecionar_entregador_por_id (entregadores):
    id_correto = None
    while id_correto == None and id_correto != "0":
        print("(digite 0 para voltar ao menu anterior)")
        opcao = input("Digite o ID do Entregador selecionado:")
        if opcao in entregadores:
            id_correto = opcao 
        elif (id_correto != "0"):
            print("Ops! Entregador não encontrado ou Removido. Insira um ID válido!")
    return id_correto



def selecionar_entregador(entregadores):
    id_entregador = None
    while id_entregador is None:
        print("---------------------SELECIONE-------------------")
        print("| Digite 1 para selecionar Entregador (pelo ID) |")
        print("| Digite 2 para pesquisar Entregador            |")
        print("| Digite 0 para pular cadastro de Entregador    |")
        print("-------------------------------------------------")
        opcao = input("Digite aqui:")
        match opcao:
            case "1":
                id_entregador = selecionar_entregador_por_id(entregadores)
            case "2":
                id_entregador = pesquisar_entregador(entregadores)
            case "0":
                break
    return id_entregador


    
def pesquisar_entregador(entregadores):
    entregadorSelecionado = None
    while entregadorSelecionado is None:
        limpar_tela()
        texto_pesquisado = input("Pesquise o Entregador pelo Nome ou ID: ")
        print ("(digite 0 para sair da pesquisa)")
        menu_entregadores(entregadores, texto_pesquisado)
        print("Digite 0 para continuar Pesquisa")
        print("Digite 1 para selecionar Entregador (por ID)")
        opcao = input("Digite aqui: ")
        match opcao:
            case "0":
                continue
            case "1":
                id_correto = ""
                while id_correto == "" and id_correto != "0":
                    print("(digite 0 para voltar ao menu anterior)")
                    opcao = input("Digite o ID do Entregador selecionado:")
                    if opcao in entregadores:
                        id_correto = opcao
                        entregadorSelecionado = id_correto
                    else:
                        print("Ops! Entregador não encontrado ou Removido. Insira um ID válido!")

    return entregadorSelecionado


def selecionar_pedido(pedidos):
    menu_pedidos(pedidos)
    pedido_selecionado = None
    while pedido_selecionado is None:
        pedido = input("Insira o ID do pedido: ")
        if pedido in pedidos:
            pedido_selecionado = pedido
        else:
            print("Ops! Pedido não encontrado ou Cancelado. Insira um ID válido!")

    return pedido_selecionado

# feito por thomas
def display_pedido(pedidos, id):
    print(f" -> ID Pedido: {id}                  ")
    print(f" -> Nome Cliente: {pedidos[id][0]}")
    print(f" -> Endereço: {pedidos[id][1]}")
    print(f" -> Prioridade: {pedidos[id][2]}")
    print(f" -> Descrição: {pedidos[id][3]}")
    print(f" -> Status: {pedidos[id][4]}")
    if(pedidos[id][5] == ""):
        print(f" -> Entregador: Não selecionado")
    else:
        print(f" -> Entregador: {pedidos[id][5]}")
    
    print("\n\n")
            