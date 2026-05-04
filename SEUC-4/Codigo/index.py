print("\n SEUC-4 \n")
opcao = -1 
while not opcao == 0:
    print("----------SELECIONE UMA OPÇÃO----------")
    print("1 - Iniciar Leitura")
    print("0 - Finalizar programa")
    print("---------------------------------------\n")

    opcao = int(input("Selecione a opção desejada: "))
    match opcao:
        case 1:
            numeroLeituras = int(input("Digite o número de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))

            soma = 0
            contador = 0
            menor_pressao = None
            qtd_zona_verde = 0

            vermelha_anterior = False
            houve_travamento = False

            for i in range(numeroLeituras):
                leitura = float(input(f"Digite a pressão da leitura {i+1}º : "))

                if leitura > 150:
                    leitura_ajustada = leitura * 1.08
                else:
                    leitura_ajustada = leitura * 0.96

                if leitura_ajustada >= 120 and leitura_ajustada <= 180:
                    qtd_zona_verde += 1
                    zona = "🟢 VERDE"
                elif leitura < 250:
                    zona = "🟡 AMARELA"
                else:
                    zona = "🔴 VERMELHA"

                print("\n-------------------------------------")
                print(f"Pressão ajustada: {leitura_ajustada:0.2f}")
                print(f"Zona UPC:         {zona}")
                print("---------------------------------------\n")

                if zona == "🔴 VERMELHA":
                    if vermelha_anterior:
                        print("⚠️ INTERROMPER ESCOAMENTO IMEDIATO!")
                        print("\nPor questões de segurança o escoamento deve ser interrompido imediatamente. Houve duas leituras na zona vermelha.")
                        print("---------------------------------------\n")
                        houve_travamento = True
                        break

                    vermelha_anterior = True
                else:
                    vermelha_anterior = False
                
                soma += leitura_ajustada
                contador += 1

                if menor_pressao == None or leitura_ajustada < menor_pressao:
                    menor_pressao = leitura_ajustada


            media = soma/contador
            if houve_travamento:
                travou = "Sim"
            else:
                travou = "Não"

            perc_zona_verde = (qtd_zona_verde/contador) * 100
            percentual_relizado = (contador/numeroLeituras) * 100
            print("----------- MÉTRICAS FINAIS -----------")
            print(f"Média final: {media:0.2f}")
            print(f"Menor pressão registrada: {menor_pressao:0.2f}")
            print(f"Leituras na zona verde (%): {perc_zona_verde:0.2f}")
            print(f"Houve travamento? {travou}")
            if houve_travamento: 
                print(f"Total leituras até o travamento (%): {percentual_relizado:0.2f}")
            else:
                print(f"Total leituras até a conclusão (%): {percentual_relizado:0.2f}")
            print("---------------------------------------\n")
        case 0:
            print(f"Finalizando programa....")
            print("---------------------------------------\n")
        case _:
            print("Digite uma opção válido!")