def calcular_ajuste(valor):
    if valor > 150:
        return valor * 1.08
    else:
        return valor * 0.96
def iniciar_sistema():
    total_previsto = int(input("Quantidade de leituras planejadas: "))
    soma_ajustada = 0
    leituras_realizadas = 0
    menor_pressao = float('inf')
    qtd_verde = 0
    consecutivas_vermelhas = 0
    travado = False
    for i in range(total_previsto):
        pressao_bruta = float(input(f"Leitura {i+1} (UPC): "))
        leituras_realizadas += 1
        p_ajustada = calcular_ajuste(pressao_bruta)
        soma_ajustada += p_ajustada
        if p_ajustada < menor_pressao:
            menor_pressao = p_ajustada
        if 120 <= p_ajustada <= 180:
            print("Status: ZONA VERDE")
            qtd_verde += 1
            consecutivas_vermelhas = 0
        elif p_ajustada > 250:
            print("Status: ZONA VERMELHA")
            consecutivas_vermelhas += 1
        else:
            print("Status: ZONA AMARELA")
            consecutivas_vermelhas = 0
        if consecutivas_vermelhas == 2:
            travado = True
            print("!!! EMERGÊNCIA: DUPLO PICO DETECTADO. TRAVANDO SISTEMA !!!")
            break

    # Cálculos Finais e Exibição de Métricas (Média, %, etc.)
    # (implementar conforme as regras do projeto)

iniciar_sistema()