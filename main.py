# main.py

# Abrir um arquivo .txt e ler seu conteúdo em uma lista
with open('./tasks/aleatorio_1k.txt', 'r') as file:  # Substitua 'your_file.txt' pelo nome do seu arquivo
    lines = file.readlines()  # Ler todas as linhas em uma lista

# Extrair todos os números das linhas e colocá-los em uma lista
numeros = [int(num) for line in lines for num in line.split() if num.isdigit()]  # Selecionar todos os números

# Aplicar o algoritmo de ordenação (usando o método sort)
numeros.sort()  # Ordenar a lista de números

# Imprimir a lista ordenada
print(numeros)  # Exibir a lista de números ordenados
