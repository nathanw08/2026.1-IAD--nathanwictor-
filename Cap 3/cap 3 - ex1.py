
horas = float(input("Digite as Horas: "))
taxa = float(input("Digite a taxa: "))

if horas > 40:
    
    horas_normais = 40
    horas_extras = horas - 40
    pagamento = (horas_normais * taxa) + (horas_extras * taxa * 1.5)
else:
    
    pagamento = horas * taxa

# resultado
print(f"Pagamento: {pagamento}")