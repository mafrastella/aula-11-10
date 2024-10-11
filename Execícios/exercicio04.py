temperaturas = [
    [22, 25, 28, 32], 
    [20, 23, 26, 30],  
    [18, 22, 25, 29]   
]

def transpor_matriz(matriz):
    
    return [list(linha) for linha in zip(*matriz)]

def exibir_matriz(matriz):

    for linha in matriz:
        print(linha)

matriz_transposta = transpor_matriz(temperaturas)

print("Matriz Transposta:")
exibir_matriz(matriz_transposta)
