import os
pedidos = {} 
entregadores = {}  

def limpar_tela():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear && printf "\e[3J"')
        os.system('clear')

def contar_pedidos_ativos(id_entregador, pedidos):
    total = 0

    for dados_pedido in pedidos.values():
        if (dados_pedido[5] == id_entregador and dados_pedido[4] != "Entregue"):
            total += 1

    return total

def ordenarPedidos(pedidos):
    pedidos_ordenados = []
    for id_pedido, dados_pedido in pedidos.items():
        if dados_pedido[2] == "Alta":
            pedidos_ordenados.append((id_pedido, dados_pedido))

    for id_pedido, dados_pedido in pedidos.items():
        if dados_pedido[2] == "Normal":
            pedidos_ordenados.append((id_pedido, dados_pedido))

    return pedidos_ordenados

def gerarIdPedido(pedidos, nome_cliente):
    chaves_pedidos = pedidos.keys()
    inicial_cliente = nome_cliente[0]
    maior_id = 0
    for chave_id in chaves_pedidos:
        
        int_chave_id = int(chave_id[1:])
        
        if int_chave_id > maior_id:
            maior_id = int_chave_id
    
    maior_id += 1
    id_pedido = inicial_cliente + str(maior_id).zfill(4)
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

def selecioneStatus():
    retStatus = ""
    while retStatus == "":
        print("-------STATUS-------")
        print("| 1 - Pendente       |")
        print("| 2 - Em trânsito    |")
        print("| 3 - Entregue       |")
        print("--------------------\n")

        status = input("Digite o status do pedido: ")
        match status:
            case "1":
                retStatus = "Pendente"
            case "2":
                retStatus = "Em trânsito"
            case "3":
                retStatus = "Entregue"
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

        veiculo = input("Selecione o tipo de veículo: ")
        match veiculo:
            case "1":
                retVeiculo = "Carro"
            case "2":
                retVeiculo = "Van"
            case "3":
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

def gerar_id_entregador(entregadores):
    chaves_entregadores = entregadores.keys()
    
    maior_id = 0
    for chave_id in chaves_entregadores:
        int_chave_id = int(chave_id)
        
        if int_chave_id > maior_id:
            maior_id = int_chave_id
    
    maior_id += 1
    return str(maior_id).zfill(4)

def busca_entregador_disp (entregadores, pedidos):
    periodos_sistema = ["Manhã", "Tarde", "Noite"]

    for periodo in periodos_sistema:
        print(f"\nENTREGADORES DISPONÍVEIS - {periodo}")
        print("=======================================================================")

        possui_disponivel = False
        for id_entregador, dados_entregador in entregadores.items():
            nome = dados_entregador[0]
            veiculo = dados_entregador[1]
            pedidos_ativos = contar_pedidos_ativos(id_entregador, pedidos)
            periodos = dados_entregador[3]

            limite_pedidos = qtdPedidosMaximo(veiculo)
            vagas_restantes = limite_pedidos - pedidos_ativos

            if periodo in periodos and vagas_restantes > 0:
                possui_disponivel = True

                print(f"ID: {id_entregador:<10} Nome: {nome:<20} Veículo: {veiculo:<10} Vagas: {vagas_restantes}")

        if not possui_disponivel:
            print("Nenhum entregador disponível.")
        print("========================================================================")


def selecionar_consulta(entregadores, pedidos):
    ret_consulta = ""
    while ret_consulta == "":
        limpar_tela()
        print("--------------CONSULTA--------------")
        print("| 1 - Pedidos Pendentes            |")
        print("| 2 - Pedidos Entregues            |")
        print("| 3 - Buscar Pedido por ID         |")
        print("| 4 - Entregador Disponível        |")
        print("| 5 - Todas as Entregas Realizadas |")
        print("|     por um Entregador            |")
        print("| 0 - Voltar                       |")
        print("------------------------------------\n")

        consulta = input("Digite o que você deseja consultar: ")
        match consulta:
            case "1":
                limpar_tela()
                print("========PEDIDOS PENDENTES========\n")
                buscaPedidos(pedidos, "Pendente")
                verificaVoltar()
            case "2":
                limpar_tela()
                print("========PEDIDOS ENTREGUES========\n")
                buscaPedidos(pedidos, "Entregue")
                verificaVoltar()
            case "3":
                limpar_tela()
                print("========BUSCA PEDIDO PELO ID========\n")
                idPedido = selecionar_pedido(pedidos)
                buscaPedidoID(pedidos, idPedido)
                verificaVoltar()
            case "4": 
                limpar_tela()
                busca_entregador_disp(entregadores, pedidos)
                verificaVoltar()
            case "5":
                limpar_tela()
                print("========BUSCA ENTREGAS FEITAS POR ENTREGADOR========\n")
                idEntregador = busca_entregador(entregadores)
                buscaEntregas(idEntregador, pedidos)
                verificaVoltar()
            case "0":
                break
            case _:
               input("Opção inválida! Clique Enter e tente novamente.")
        
                
    return ret_consulta 

def buscaEntregas(id_entregador, pedidos):
    possui_entregas = False

    for id_pedido, dados_pedido in ordenarPedidos(pedidos):
        status = dados_pedido[4]
        entregador = dados_pedido[5]

        if status == "Entregue" and entregador == id_entregador:
            possui_entregas = True
            exibePedido(id_pedido, dados_pedido)

    if not possui_entregas:
        print("\nOps! Este entregador não possui entregas realizadas.\n")

def buscaPedidos(pedidos, tipo):
    possui_pedido = False
    for id_pedido, dados_pedido in ordenarPedidos(pedidos):
        if dados_pedido[4] == tipo:
            possui_pedido = True
            exibePedido(id_pedido, dados_pedido)

    if not possui_pedido:
        print(f"\nOps! Não encontramos pedidos {tipo}s\n")

def buscaPedidoID(pedidos, id):
    pedido = pedidos.get(id)
    if pedido is None:
        print(f"\nOps! Não encontramos nenhum pedido com o ID {id}s\n")
    else:
        exibePedido(id, pedido)

def exibePedido(id_pedido, dados_pedido):
    entregador = dados_pedido[5]
    if entregador is None:
        entregador = "Não Definido"
        
    print("=============================================================================")
    print(f"ID: {id_pedido:<5}  Cliente: {dados_pedido[0]:<30}")
    print(f"Prioridade: {dados_pedido[2]:<35}  Status: {dados_pedido[4]:<35}")
    print(f"Período: {dados_pedido[6]:<40}  Entregador: {entregador:<35}")
    print(f"Endereço: {dados_pedido[1]}")
    print(f"Descrição: {dados_pedido[3]}")
    print("=============================================================================")
    
def verificaVoltar():
    voltar = ""
    while voltar not in ["S"]:
        voltar = input("Você deseja voltar ao menu anterior? (S) ").upper()
        if voltar not in ['S']:
            print("Digite uma opção válida")
            continue

        if voltar == "S":
            break    

    limpar_tela()

def selecionePeriodo():
    print("--------------PERIODOS --------------")
    print("| 1 - Manhã                          |")
    print("| 2 - Tarde                          |")
    print("| 3 - Noite                          |")
    print("------------------------------------\n")
    periodo_valido = False
    while periodo_valido == False:
        periodo = input("Selecione o periodo: ")
        match periodo:
            case "1":
                periodo = "Manhã"
            case "2":
                periodo = "Tarde"
            case "3":
                periodo = "Noite"
            case _:
                print("Selecione um periodo válido")
                continue
        periodo_valido = True
    return periodo

def qtdPedidosMaximo(veiculo):
    if veiculo == "Moto":
        return 2
    elif veiculo == "Carro":
        return 4
    else:
        return 6
    
def selecionar_pedido(pedidos):
    pedido_selecionado = None

    while pedido_selecionado is None:
        pedido = input("Insira o ID do pedido: ")
        if pedido in pedidos:
            pedido_selecionado = pedido
        else:
            print("Ops! Pedido não encontrado ou cancelado.")

            tentar_novamente = input("Deseja tentar novamente? (S/N): ").upper()
            if tentar_novamente == "N":
                return None

    return pedido_selecionado

def busca_entregador(entregadores):
    entregador_selecionado = None
    while entregador_selecionado is None:
        entregador = input("Insira o ID do entregador: ")
        if entregador in entregadores:
            entregador_selecionado = entregador
        else:
            print("Ops! Entreagador não encontrado. Insira um ID válido!")

    return entregador_selecionado

def entregadoresDisponiveis(id_pedido, pedidos, entregadores):
    dados_pedido = pedidos[id_pedido]
    periodo_pedido = dados_pedido[6]
    limpar_tela()
    print("\nENTREGADORES DISPONÍVEIS:\n")

    encontrou = False
    entregadoresDisp = []
    for id_entregador, dados_entregador in entregadores.items():
        nome = dados_entregador[0]
        veiculo = dados_entregador[1]
        pedidos_ativos = contar_pedidos_ativos(id_entregador, pedidos)
        periodos = dados_entregador[3]

        
        limite_pedidos = qtdPedidosMaximo(veiculo)
        periodo_ok = periodo_pedido in periodos
        capacidade_ok = pedidos_ativos < limite_pedidos

        if periodo_ok and capacidade_ok:
            encontrou = True
            vagas_restantes = limite_pedidos - pedidos_ativos
            entregadoresDisp.append(id_entregador)

            print("--------------------------------------------------------------------------------------------")
            print(f"ID: {id_entregador:<5}  Nome: {nome:<20} | Veículo: {veiculo:<25}")
            print(f"Pedidos ativos: {pedidos_ativos:<25} | Capacidade máxima: {limite_pedidos:<25} | Vagas restantes: {vagas_restantes:<5}")
            print(f"Períodos disponíveis: {periodos}")
            print("--------------------------------------------------------------------------------------------")


    if not encontrou:
        print("Nenhum entregador disponível.")

    return entregadoresDisp

def cadastrarPedido():
    print("FLUXO NORTE\n")
    print("CADASTRAR PEDIDO\n")
    nomeCliente = ""
    endereco    = ""
    descricao   = ""
    status      = "Pendente"
    periodoEntrega = ""
    while nomeCliente == "":
        nomeCliente = str(input("Digite o nome do cliente: "))

    while endereco == "":
        endereco    = input("Digite o endereço do pedido: ")
    
    while descricao == "":
        descricao   = input("Digite a descrição do pedido: ")

    print("\nSelecione o periodo de entrega: ")
    periodoEntrega = selecionePeriodo()

    prioridade = selecionePrioridade()
    id     = gerarIdPedido(pedidos, nomeCliente)

    pedidos[id] = [nomeCliente, endereco, prioridade, descricao, status, None, periodoEntrega]
    print(pedidos)
    
    limpar_tela()
    print("\nPEDIDO CADASTRADO")
    print(f" -> ID Pedido: {id}                  ")
    print(f" -> Nome Cliente: {nomeCliente}      ")
    print(f" -> Endereço: {endereco}             ")
    print(f" -> Descrição: {descricao}           ")
    print(f" -> Prioridade: {prioridade}         ")
    print(f" -> Status: {status}                 ")
    print(f" -> Periodo de Entrega: {periodoEntrega}")
    print(f" -> Entregador: Não selecionado      ")
    print("\n\n")

def cancelaPedido(idPedido):
    id_entregador = pedidos[idPedido][5]
    if id_entregador is not None:
        if id_entregador in entregadores:
            if idPedido in entregadores[id_entregador][2]:
                entregadores[id_entregador][2].remove(idPedido)

    del pedidos[idPedido]
    print(f"\nPedido {idPedido} cancelado com sucesso!")

def removeAssociacao(idPedido):
    id_entregador = pedidos[idPedido][5]
    if id_entregador is not None:
        if id_entregador in entregadores:
            if idPedido in entregadores[id_entregador][2]:
                entregadores[id_entregador][2].remove(idPedido)

        pedidos[idPedido][5] = None 
        print(f"\nAssociacao do entregador {id_entregador} ao pedido {idPedido} removido com sucesso!")
    else:
        print("\nEste pedido não possui nenhum entregador associado á ele!")
    verificaVoltar()

def confirmaCancelar(idPedido):
    confirma = ""
    while confirma == "":
        confirma = input("Você tem certeza que deseja cancelar esse pedido? (S/N): ").upper()
        if confirma not in ['S', 'N']:
            print("\nDigite uma opção válida!")
            continue

        if confirma == "S":
            cancelaPedido(idPedido)
            verificaVoltar()
        else:
            break

def atualizarPedido():
    print("FLUXO NORTE\n")
    print("ATUALIZAR PEDIDO\n")
    opcao = ""
    while opcao != "0":
        limpar_tela()
        print("-----------------------SELECIONE-------------------------")
        print("| 1 - Alterar Status Pedido                             |")
        print("| 2 - Cancelar Pedido                                   |")
        print("| 3 - Associar Entregador á Pedido                      |")
        print("| 4 - Remover associação de entregador á pedido         |")
        print("| 0 - Cancelar Atualização                              |")
        print("---------------------------------------------------------")

        opcao = input("Selecione a opção desejada: ")
        match opcao:
            case "1":
                print("\nALTERAR STATUS PEDIDO\n")
                idPedido = selecionar_pedido(pedidos)
                idPedido = selecionar_pedido(pedidos)
                if idPedido is None:
                    continue
                status = selecioneStatus()
                pedidos[idPedido][4] = status
                print("Status do pedido alterado com sucesso!")
                verificaVoltar()
            case "2":
                print("\nCANCELAR PEDIDO\n")
                idPedido = selecionar_pedido(pedidos)
                if idPedido is None:
                    continue

                confirmaCancelar(idPedido)
                verificaVoltar()
            case "3":
                print("\nASSOCIAR ENTREGADOR Á PEDIDO\n")
                idPedido = selecionar_pedido(pedidos)
                if idPedido is None:
                    continue

                entregadoresDisp = entregadoresDisponiveis(idPedido, pedidos, entregadores)
                id_entregador = busca_entregador(entregadores)
                associaEntregador(id_entregador, idPedido, entregadoresDisp)
                verificaVoltar()
            case "4":
                idPedido = selecionar_pedido(pedidos)
                if idPedido is None:
                    continue

                removeAssociacao(idPedido)
                verificaVoltar()
            case "0":
                print("CANCELANDO ATUALIZAÇÃO\n")
                limpar_tela()

                continue
            case _:
                print("Opção inválida! Tente novamente")

def associaEntregador(id_entregador, idPedido, entregadoresDisponiveis):
    if id_entregador in entregadoresDisponiveis:
        if pedidos[idPedido][5] is not None:
            removeAssociacao(idPedido)

        pedidos[idPedido][5] = id_entregador
        if idPedido not in entregadores[id_entregador][2]:
            entregadores[id_entregador][2].append(idPedido)

        print(f"\nPedido {idPedido} será entregue pelo Entregador {entregadores[id_entregador][0]}!")
    else:
        print("Entregador indisponível!")

def cadastrarEntregador():
    print("FLUXO NORTE\n")
    print("CADASTRAR ENTREGADOR\n")
    id              = gerar_id_entregador(entregadores)
    nomeEntregador  = ""
    veiculo         = ""
    idsPedido       = []
    disponibilidade = []
    while nomeEntregador == "":
        nomeEntregador = input("Digite o nome do entregador: ")

        if nomeEntregador == "":
            print("Digite um nome válido!")
        
    veiculo = selecioneVeiculo()

    print("Selecione o primeiro período de trabalho deste entregador: ")
    periodo1 = selecionePeriodo()
    disponibilidade.append(periodo1)
    
    periodo2 = periodo1
    while periodo2 == periodo1:            
        print("Selecione o segundo período de trabalho deste entregador: ")
        periodo2 = selecionePeriodo()
        if periodo2 == periodo1:
            print("O segundo periodo não pode ser o mesmo do primeiro. Tente novamente")

    disponibilidade.append(periodo2)
    
    entregadores[id] = [nomeEntregador, veiculo, idsPedido, disponibilidade]
    limpar_tela()
    print("\nENTREGADOR CADASTRADO")
    print(f" -> ID Entregador: {id}              ")
    print(f" -> Nome Entregador: {nomeEntregador}")
    print(f" -> Veículo: {veiculo}              ")
    print(f" -> Pedidos: Este entregador ainda não possui nenhum pedido para entrega")
    print(f" -> Disponibilidade: {disponibilidade}")
    print("\n\n")

def menuInicial():
    print("----------SELECIONE-----------")
    print("| 1 - Cadastrar Pedido       |")
    print("| 2 - Atualizar Pedido       |")
    print("| 3 - Cadastrar Entregador   |")
    print("| 4 - Consultar              |")
    print("| 0 - Finalizar Sistema      |")
    print("------------------------------")

opcao = "-1"
while opcao != "9":
    limpar_tela()
    print("FLUXO NORTE\n")
    menuInicial()

    opcao = input("Selecione a opção desejada: ")
    match(opcao):
        case "1":
            limpar_tela()
            cadastrarPedido()
            verificaVoltar()
        case "2":
            limpar_tela()
            atualizarPedido()
        case "3":
            limpar_tela()
            cadastrarEntregador()
            verificaVoltar()
        case "4":
            limpar_tela()
            selecionar_consulta(entregadores, pedidos)
        case "0":
            limpar_tela()
            print("\nFINALIZAR SISTEMA\n")
            if verificaFinalizar():
                opcao = "9" 
            continue
        case _:
            limpar_tela()
            print("Ops! Opção inválida, tente novamente.")
            opcao = "-1"
            verificaVoltar()
