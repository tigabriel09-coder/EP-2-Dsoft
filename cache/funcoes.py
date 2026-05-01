
import random

def rolar_dados(qtd):
    resultados = []
    
    for _ in range(qtd):
        valor = random.randint(1, 6)
        resultados.append(valor)
    
    return resultados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    
    dados_no_estoque.append(dado)
    
    dados_rolados.pop(dado_para_guardar)
    
    return [dados_rolados, dados_no_estoque]
    
