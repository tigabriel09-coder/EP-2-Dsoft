
import random

def rolar_dados(qtd):
    resultados = []
    
    for _ in range(qtd):
        valor = random.randint(1, 6)
        resultados.append(valor)
    
    return resultados

    
