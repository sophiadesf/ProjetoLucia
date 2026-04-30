print("\n SEUC-4 \n")
print("--------------------------------")
numeroLeituras = int(input("Digite o número de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))

soma_leituras = 0
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
        leitura_ajustada = leitura * 1.04

    if leitura_ajustada >= 120 and leitura_ajustada <= 180:
        qtd_zona_verde += 1
        zona = "🟢 VERDE"
    elif leitura < 250:
        zona = "🟡 AMARELA"
    else:
        zona = "🔴 VERMELHA"

    print("\n-------------------------------------\n")
    print(f"Pressão ajustada: {leitura_ajustada:0.2f}\n")
    print(f"Zona UPC:         {zona}\n")
    print("-------------------------------------\n")

    if zona == "🔴 VERMELHA":
        if vermelha_anterior:
            print("⚠️ INTERROMPER ESCOAMENTO IMEDIATO!")
            print("\nPor questões de segurança o escoamento deve ser interrompido imediatamente. Houve duas leituras na zona vermelha.")
            print("-------------------------------------\n")
            houve_travamento = True
            break

        vermelha_anterior = True
    else:
        vermelha_anterior = False
    

        