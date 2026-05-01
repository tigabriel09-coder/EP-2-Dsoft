
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
    
def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    
    dados_rolados.append(dado)
    dados_no_estoque = (
        dados_no_estoque[:dado_para_remover] +
        dados_no_estoque[dado_para_remover + 1:])
    
    return [dados_rolados, dados_no_estoque]
def calcula_pontos_regra_simples(dados):
    pontos = {}
    for i in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == i:
                soma += dado
        pontos[i] = soma
    return pontos
def calcula_pontos_soma(dados):
    total = 0 #define
    for dado in dados:
        total += dado
    return total 
def calcula_pontos_sequencia_baixa(dados):
    conjunto = set(dados)
    
    if 1 in conjunto and 2 in conjunto and 3 in conjunto and 4 in conjunto:
        return 15
    if 2 in conjunto and 3 in conjunto and 4 in conjunto and 5 in conjunto:
        return 15
    if 3 in conjunto and 4 in conjunto and 5 in conjunto and 6 in conjunto:
        return 15
    
    return 0