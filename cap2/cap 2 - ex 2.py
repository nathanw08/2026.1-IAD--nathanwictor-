# 1. Solicita os dados e converte para números decimais (float)
horas = float(input('Digite as horas: '))
taxa = float(input('Digite a taxa: '))

# 2. Calcula o valor total multiplicando um pelo outro
pagamento = horas * taxa

# 3. Exibe o resultado final
print('Valor a ser pago:', pagamento)