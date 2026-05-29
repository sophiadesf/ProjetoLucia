import util as util
print("FLUXO NORTE\n")
pedidos = {} # {"idPedido": ["Nome Cliente", "Endereço", "Prioridade", "Descricao", "status", "id_entregador"]
entregadores = {} # {"idEntregador": ["Nome Entregador", "Veículo", [], [periodo1, periodo2], carga_max]}
opcao = -1
numero_id_pedidos_atual = 0
numero_id_entregadores_atual = 0

while opcao != "0":
    print("-----------SELECIONE-----------")
    print("| 1 - Cadastrar Pedido        |")
    print("| 2 - Atualizar Pedido        |")
    print("| 3 - Cadastrar Entregador    |")
    print("| 4 - Consultar               |")
    print("| 5 - Relatórios Operacionais |") # fazer menu INTEIRO
    print("| 0 - Finalizar Sistema       |")
    print("-------------------------------")

    opcao = input("Selecione a opção desejada: ")
    match(opcao):
        case "1":
            util.limpar_tela()
            print("FLUXO NORTE\n")
            print("CADASTRAR PEDIDO\n")
            nomeCliente   = ""
            endereco      = ""
            descricao     = ""
            status        = "Pendente"
            id_entregador = ""

            while nomeCliente == "":
                nomeCliente = input("Digite o nome do Cliente: ")
            while endereco == "":
                endereco    = input("Digite o endereço de Entrega: ")
            
            while descricao == "":
                descricao   = input("Digite a descrição do Pedido: ")

            id_entregador = util.selecionar_entregador(entregadores)
            
            prioridade = util.selecionePrioridade()

            numero_id_pedidos_atual +=1
            id = util.gerarIdPedido(nomeCliente, numero_id_pedidos_atual)

            pedidos[id] = [nomeCliente, endereco, prioridade, descricao, status, id_entregador]
            
            util.limpar_tela()
            print("\nPEDIDO CADASTRADO")
            util.display_pedido(pedidos, id)

            continue
        case "2":
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
            while opcao != "0":
                print("-------------------------------------------------")
                print("| 1 - Alterar Status Pedido                     |")
                print("| 2 - Cancelar Pedido                           |")
                print("| 3 - Associar Entregador á Pedido              |")
                print("| 4 - Remover associação de entregador á pedido |")
                print("| 0 - Cancelar Atualização                      |")
                print("-------------------------------------------------")

                opcao = input("Selecione a opção desejada: ")
                match opcao:
                    case "1":
                        print("ALTERAR STATUS PEDIDO\n")
                        pass
                    case "2":
                        print("CANCELAR PEDIDO\n")
                        pass
                    case "3":
                        idPedido = util.selecionar_pedido(pedidos)
                        id_entregador = util.selecionar_entregador(entregadores)

                    case "4":
                        print("ALTERAR STATUS PEDIDO\n")
                        pass
                    case "0":
                        print("CANCELANDO ATUALIZAÇÃO\n")
                        util.limpar_tela()
                        continue
                    case _:
                        print("Opção inválida! Tente novamente")

        case "3":
            util.limpar_tela()
            print("FLUXO NORTE\n")
            print("CADASTRAR ENTREGADOR\n")
            numero_id_entregadores_atual+=1
            id              = util.gerar_id_entregador(numero_id_entregadores_atual)
            nomeEntregador  = ""
            veiculo         = ""
            ids_pedidos     = []
            entregas        = 0
            disponibilidade = "Disponível"

            while nomeEntregador == "":
                nomeEntregador = input("Digite o nome do entregador: ")
        
            disponibilidade = util.definir_disponibilidade()

            veiculo = util.selecioneVeiculo()
            
            carga_max = util.carga(veiculo)

            entregadores[id] = [nomeEntregador, veiculo, ids_pedidos, disponibilidade, entregas, carga_max]
            util.limpar_tela()
            print("\nENTREGADOR CADASTRADO")
            print(f" -> ID Entregador: {id}              ")
            print(f" -> Nome Entregador: {nomeEntregador}")
            print(f" -> Veículo: {veiculo}              ")
            print(f" -> Pedidos: Este entregador ainda não possui nenhum pedido para entrega")
            print(f" -> Disponibilidade: {disponibilidade}")
            print("\n\n")
            continue
       
        case "4":
            util.selecionar_consulta(entregadores)
    
        case "0":
            util.limpar_tela()
            print("\nFINALIZAR SISTEMA\n")
            if util.verificaFinalizar():
                break
        case _:
            print("Ops! Opção inválida, tente novamente.")