import random
from cache.funcoes import faz_jogada, guardar_dado, imprime_cartela, remover_dado
from funcoes import *


cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def rolar_dados(qtd):
    dados = []
    for _ in range(qtd):
        dados.append(random.randint(1, 6))
    return dados


for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print("Dados rolados:", dados_rolados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input(">")

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input(">"))
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)

        
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input(">"))
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)

        
        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(5 - len(dados_guardados))
                rerrolagens += 1

        
        elif opcao == "4":
            imprime_cartela(cartela)

        
        elif opcao == "0":
            while True:
                print("Digite a combinação desejada:")
                categoria = input(">")

                
                if categoria in ["1","2","3","4","5","6"]:
                    cat = int(categoria)
                    if cartela['regra_simples'][cat] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break

                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        break

                else:
                    print("Combinação inválida. Tente novamente.")

            break  

       
        else:
            print("Opção inválida. Tente novamente.")



imprime_cartela(cartela)

total = 0

soma_simples = 0
for i in cartela['regra_simples']:
    if cartela['regra_simples'][i] != -1:
        soma_simples += cartela['regra_simples'][i]
        total += cartela['regra_simples'][i]

for i in cartela['regra_avancada']:
    if cartela['regra_avancada'][i] != -1:
        total += cartela['regra_avancada'][i]

if soma_simples >= 63:
    total += 35

print(f"Pontuação total: {total}")