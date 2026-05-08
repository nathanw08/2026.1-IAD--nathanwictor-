try:
    entrada = input("Digite a Pontuação: ")
    pontuacao = float(entrada)

    
    if pontuacao < 0.0 or pontuacao > 1.0:
        print("Pontuação Inválida")
    
    
    elif pontuacao >= 0.9:
        print("A")
    elif pontuacao >= 0.8:
        print("B")
    elif pontuacao >= 0.7:
        print("C")
    elif pontuacao >= 0.6:
        print("D")
    else:
        print("F")

except:
    # entradas que não são números (ex: "perfeito")
    print("Pontuação Inválida")