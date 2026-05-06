
def calcula_leitura_ajustada(leitura):
    if leitura > 150:
        return leitura * 1.08
    else:
        return leitura * 0.96
    
def retorna_zona(leitura_ajustada):
    if leitura_ajustada >= 120 and leitura_ajustada <= 180:
        return "🟢 VERDE"
    elif leitura_ajustada < 250:
        return "🟡 AMARELA"
    else:
        return "🔴 VERMELHA"

def processar_leitura(leitura):
    leitura_ajustada = calcula_leitura_ajustada(leitura)
    zona = retorna_zona(leitura_ajustada)

    print("\n-------------------------------------")
    print(f"⚙️ Pressão ajustada: {leitura_ajustada:0.2f}")
    print(f"🎯 Zona UPC:         {zona}")
    print("---------------------------------------\n")

    return leitura_ajustada, zona

def verificar_travamento(zona, vermelha_ant):
    travou = False 
    vermelha_anterior = False 
    if zona == "🔴 VERMELHA":
        if vermelha_ant:
            print("🚨 INTERROMPER ESCOAMENTO IMEDIATO!")
            travou = True
        vermelha_anterior = True
    else:
        vermelha_anterior = False

    return travou, vermelha_anterior

def exibir_resultados(soma, contador, qtd_verdes, numero_leituras, menor_valor, houve_travamento):
    media = soma / contador
    perc_verde = (qtd_verdes / contador) * 100
    perc_total = (contador / numero_leituras) * 100
    travou = "Não"

    if houve_travamento:
        travou = "Sim"
        tot_leituras_conc = f"📈 Total leituras até o travamento (%): {perc_total:0.2f}"
    else:
        tot_leituras_conc = f"📉 Total leituras até a conclusão (%): {perc_total:0.2f}"
        travou = "Não"

    print("----------- MÉTRICAS FINAIS -----------")
    print(f"🔁 Média final: {media:0.2f}")
    print(f"⬇️ Menor pressão registrada: {menor_valor:0.2f}")
    print(f"✅ Leituras na zona verde (%): {perc_verde:0.2f}")
    print(f"🚨 Houve travamento? "+travou)
    print(tot_leituras_conc)
    print("---------------------------------------\n")


print("\n ⚙️ SEUC-4 \n")
opcao = -1 
while not opcao == 0:
    print("----------SELECIONE UMA OPÇÃO----------")
    print("1️⃣ - Iniciar Leitura")
    print("0️⃣ - Finalizar programa")
    print("---------------------------------------\n")

    opcao = int(input("👉 Selecione a opção desejada: "))
    match opcao:
        case 1:
            print("\n---------------------------------------\n")
            numero_leituras = int(input("🔢 Digite o número de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
            print("\n")

            soma = 0
            contador = 0
            menor_pressao = None
            qtd_zona_verde = 0
            vermelha_anterior = False
            houve_travamento = False

            for i in range(numero_leituras):
                leitura = float(input(f"Digite a pressão da leitura {i+1}º : "))
                leitura_ajustada, zona = processar_leitura(leitura)

                if leitura_ajustada >= 120 and leitura_ajustada <= 180:
                    qtd_zona_verde += 1

                soma += leitura_ajustada
                contador += 1

                houve_travamento, vermelha_anterior = verificar_travamento(zona, vermelha_anterior)

                if menor_pressao == None or leitura_ajustada < menor_pressao:
                    menor_pressao = leitura_ajustada

                if houve_travamento:
                    break

            exibir_resultados(soma, contador, qtd_zona_verde, numero_leituras, menor_pressao, houve_travamento)
        case 0:
            print(f"\n✖️ Finalizando programa....\n")
            print("---------------------------------------\n")
        case _:
            print("🚨 Digite uma opção válida! \n")