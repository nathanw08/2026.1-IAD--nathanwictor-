try:
    horas = float(input("Digite as Horas: "))
    taxa = float(input("Digite a taxa: "))

    if horas > 40:
        pagamento = (40 * taxa) + ((horas - 40) * taxa * 1.5)
    else:
        pagamento = horas * taxa
    
    print(f"Pagamento: {pagamento}")

except:
    print("Erro, por favor utilize uma entrada numérica")