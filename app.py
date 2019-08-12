#!/usr/bin/env python
# coding: utf-8

# Autor:   Ricardo Galiardi
# 
# Base:    Uso do algorítmo de Dijkstra (teoria dos Grafos)
#          Foram usadas peças de vários modelos já existentes
#          para elaboração do código.
#          
# Versões: Python 3.7
#
# Arquivo: Arquivo principal para execução em shell - App
# 
# Execução do Modo - App:
#       * Como executar a aplicação;
#         
#       * Estrutura dos arquivos/pacotes;
#         Uso da biblioteca Pandas e Flask
#         
#       * Explique as decisões de design adotadas para a solução;
#         Foram usadas rotinas básicas de python e flask para aplicação
#         desse exercício. 
#         Python: foi utilizado para criação do código e aplicação da 
#         teoria dos gráfos aplicada ao algorítmo de Dijkstra
#         Flask: foi utilizado para criação dos endpoints rest para iteração
#         do usuário via interface web.
#         
#       * Descreva sua APÌ Rest de forma simplificada;
#         Com base no Flask para Python, a api utiliza duas rotinas básicas
#         uma para consulta da melhor rota dada uma partida e um destino.
#         E a segunda para adicionar uma nova rota a lista de rotas já existentes
#         importadas no inicio do programa.
# 

# Definição e importação das bibliotecas
import sys
import time
import route
import webapp

# Definição do arquivo de rotas
def loadfile():
    load = input("Carregue o arquivo de rotas: ")

    if not load:
        print("Arquivo de rotas não definido!")
        sys.exit

    route.clearscreen()
    routes = route.read_routes(load)

    route.flights = route.Graph(routes)
    route.edges = len(route.flights.edges)

    if route.edges == 0:
        print("O arquivo selecionado não possui rotas, \n Por favor, seleciona um arquivo válido.")
        loadfile()

# Menu
def menu():
    #os.system('cls' if os.name == 'nt' else 'clear')

    print("*****************MAIN MENU*******************\n")
    print("Você pode selecionar entre " + str(route.edges) + " rotas válidas.\n")

    #time.sleep(1)
    print("""
    W: Carregar WebApi
    V: Verificar a melhor rota
    I: Incluir uma nova rota
    R: Remover uma rota existente 
    L: Limpar tela
    F: Finalizar""")
    option()

# Escolha da opção do menu
def option():
    print("")
    choice = route.inputvalid("[a-zA-Z]{1,}", "Por favor, escolha uma opção: ")

    if choice == "W":
        webapp.run()
        
    elif choice == "V":
        source = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é a origem: ")
        dest = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é o destino: ")

        if source and dest:
            ret = route.flights.dijkstra(source, dest)
            print("\n" + ret + "\n")
        else:
            print("Valores digitados não são válidos, tente novamente!")

        option()
    elif choice == "I":
        source = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é a origem: ")
        dest = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é o destino: ")
        cost = route.inputvalid("[\d]*$", "Defina qual é o valor: ")

        if source and dest and cost:
            ret = route.flights.add_edge(source, dest, int(cost))
            print("\n" + ret + "\n")
        else:
            print("Valores digitados não são válidos, tente novamente!")

        option()
    elif choice == "R":
        source = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é a origem: ")
        dest = route.inputvalid("[a-zA-Z]{3,}", "Defina qual é o destino: ")

        if source and dest:
            ret = route.flights.remove_edge(source, dest)
            print("\n" + ret + "\n")
        else:
            print("Valores digitados não são válidos, tente novamente!")
            
        option()
    elif choice == "L":
        route.clearscreen()
        menu()
    elif choice == "F":
        route.clearscreen()
        sys.exit
    else:
        print("Você deve selecionar uma opção válida V,I,R,L ou F.")
        print("Por favor, tente novamente!")
        option()

# Chamada principal
if __name__ == '__main__':
    route.clearscreen()
    loadfile()
    menu()