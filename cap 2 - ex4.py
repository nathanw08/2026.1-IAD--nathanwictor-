# Passo 1: Solicita a temperatura ao usuário
# Usamos float() porque a temperatura pode ter casas decimais
celsius = float(input("Digite a temperatura em Celsius: "))

# Passo 2: Aplica a fórmula de conversão
fahrenheit = (celsius * 1.8) + 32

# Passo 3: Mostra o resultado formatado
print(f"{celsius}°C é igual a {fahrenheit}°F")