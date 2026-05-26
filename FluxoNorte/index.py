import util as util
print("FLUXO NORTE\n")
pedidos = {} # {"idPedido": ["Nome Cliente", "Endereço", "Prioridade", "Descricao", "status", "id_entregador"]}
entregadores = {} # {"idEntregador": ["Nome Entregador", "Veículo", [], "Disponibilidade"]}
opcao = -1
while opcao != 9:
    print("----------SELECIONE-----------")
    print("| 1 - Cadastrar Pedido       |")
    print("| 2 - Editar Pedido          |")
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
            id          = util.geraIdPedido()
            nomeCliente = ""
            endereco    = ""
            descricao   = ""
            prioridade  = "Pendente"

            while nomeCliente == "":
                nomeCliente = input("Digite o nome do cliente: ")

            while endereco == "":
                endereco    = input("Digite o endereço do pedido: ")
            
            while descricao == "":
                descricao   = input("Digite a descrição do pedido: ")
    
            
            status = util.selecioneStatus()

            util.menuEntregadores(entregadores)
            entregadorSelecionado = None
            while entregadorSelecionado is None:
                entregador = input("Insira o ID do entregador: ")
                if entregador in entregadores:
                    entregadorSelecionado = [entregador, entregadores[entregador][0]]
                else:
                    print("Ops! Entregador não encontrado. Insira um ID válido")
            
            pedidos[id] = [nomeCliente, endereco, prioridade, descricao, status, entregadorSelecionado[0]]
            entregadores[entregadorSelecionado[0]][2].append(id)
            util.limpar_tela()
            print("\nPEDIDO CADASTRADO")
            print(f" -> ID Pedido: {id}                  ")
            print(f" -> Nome Cliente: {nomeCliente}      ")
            print(f" -> Endereço: {endereco}             ")
            print(f" -> Descrição: {descricao}           ")
            print(f" -> Prioridade: {prioridade}         ")
            print(f" -> Status: {status}                 ")
            print(f" -> Entregador: {entregadorSelecionado[0]}  - {entregadorSelecionado[1]}")
            print("\n\n")
            continue
        case 2:
            pass
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
            pass
        case 0:
            util.limpar_tela()
            print("\nFINALIZAR SISTEMA\n")
            if util.verificaFinalizar():
                opcao = 9 
            continue
        case _:
            util.limpar_tela()
            print("Ops! Opção inválida, tente novamente.")


