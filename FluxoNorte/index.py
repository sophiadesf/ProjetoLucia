import util as util
print("FLUXO NORTE\n")
pedidos = {} # {"idPedido": ["Nome Cliente", "Endereço", "Prioridade", "Descricao", "status", "id_entregador"]
print(pedidos)
entregadores = {} # {"idEntregador": ["Nome Entregador", "Veículo", [], [periodo1, periodo2]]}
opcao = -1
while opcao != 9:
    print("----------SELECIONE-----------")
    print("| 1 - Cadastrar Pedido       |")
    print("| 2 - Atualizar Pedido       |")
    print("| 3 - Cadastrar Entregador   |")
    print("| 4 - Consultar              |")
    print("| 0 - Finalizar Sistema      |")
    print("------------------------------")

    opcao = int(input("Selecione a opção desejada: "))
    match(opcao):
        case 1:
            util.limpar_tela()
            print("FLUXO NORTE\n")
            print("CADASTRAR PEDIDO\n")
            nomeCliente = ""
            endereco    = ""
            descricao   = ""
            status      = "Pendente"

            while nomeCliente == "":
                nomeCliente = str(input("Digite o nome do cliente: "))

            while endereco == "":
                endereco    = input("Digite o endereço do pedido: ")
            
            while descricao == "":
                descricao   = input("Digite a descrição do pedido: ")
    
            
            prioridade = util.selecionePrioridade()
            id     = util.gerarIdPedido(pedidos, nomeCliente)

            pedidos[id] = [nomeCliente, endereco, prioridade, descricao, status, -1]
            print(pedidos)
            
            util.limpar_tela()
            print("\nPEDIDO CADASTRADO")
            print(f" -> ID Pedido: {id}                  ")
            print(f" -> Nome Cliente: {nomeCliente}      ")
            print(f" -> Endereço: {endereco}             ")
            print(f" -> Descrição: {descricao}           ")
            print(f" -> Prioridade: {prioridade}         ")
            print(f" -> Status: {status}                 ")
            print(f" -> Entregador: Não selecionado      ")
            print("\n\n")
            continue
        case 2:
            util.limpar_tela()
            print("FLUXO NORTE\n")
            print("ATUALIZAR PEDIDO\n")
            pedidoSelecionado = {}
            while pedidoSelecionado is None:
                idPedido = input("Digite o id do pedido que você deseja selecionar: ")
                for id_ped in pedidos.keys():
                    if (idPedido == id_ped):
                        pedidoSelecionado = pedidos[id_ped]
                        print(f"Pedido #{id_ped} encontrado. Selecione o que deseja atualizar:")
                        continue
                
                    print("Pedido não encontrado! Insira um id válido")
                
            opcao = -1
            while opcao != 0:
                print("-------------------------------------------------")
                print("| 1 - Alterar Status Pedido                     |")
                print("| 2 - Cancelar Pedido                           |")
                print("| 3 - Associar Entregador á Pedido              |")
                print("| 4 - Remover associação de entregador á pedido |")
                print("| 0 - Cancelar Atualização                      |")
                print("-------------------------------------------------")

                opcao = int(input("Selecione a opção desejada: "))
                match opcao:
                    case 1:
                        print("ALTERAR STATUS PEDIDO\n")
                        pass
                    case 2:
                        print("CANCELAR PEDIDO\n")
                        pass
                    case 3:
                        print("ASSOCIAR ENTREGADOR Á PEDIDO\n")
                        pass
                    case 4:
                        print("ALTERAR STATUS PEDIDO\n")
                        pass
                    case 0:
                        print("CANCELANDO ATUALIZAÇÃO\n")
                        util.limpar_tela()
                        continue
                    case _:
                        print("Opção inválida! Tente novamente")

        case 3:
            util.limpar_tela()
            print("FLUXO NORTE\n")
            print("CADASTRAR PEDIDO\n")
            id              = util.gerar_id_entregador(entregadores)
            nomeEntregador  = ""
            veiculo         = ""
            idsPedido       = []
            disponibilidade = "Disponível"

            while nomeEntregador == "":
                nomeEntregador = input("Digite o nome do entregador: ")

            veiculo = util.selecioneVeiculo()
            
            entregadores[id] = [nomeEntregador, veiculo, idsPedido, disponibilidade]
            util.limpar_tela()
            print("\nENTREGADOR CADASTRADO")
            print(f" -> ID Entregador: {id}              ")
            print(f" -> Nome Entregador: {nomeEntregador}")
            print(f" -> Veículo: {veiculo}              ")
            print(f" -> Pedidos: Este entregador ainda não possui nenhum pedido para entrega")
            print(f" -> Disponibilidade: {disponibilidade}")
            print("\n\n")
            continue
       
        case 4:
            util.selecionar_consulta(entregadores)
    
        case 0:
            util.limpar_tela()
            print("\nFINALIZAR SISTEMA\n")
            if util.verificaFinalizar():
                opcao = 9 
            continue
        case _:
            util.limpar_tela()
            print("Ops! Opção inválida, tente novamente.")


