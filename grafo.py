import pandas as pd
import random # usar as funções dessa biblioteca para definir o peso das arestas e escolher as linhas dentro do dataframe

df = pd.read_csv("https://raw.githubusercontent.com/flaviasoares/Grafo/main/directory.csv", encoding="UTF-8")
# print(df.columns.values) # mostra quais são as instâncias/colunas
total_colunas = len(df.columns) # quantidade de colunas
total_linhas = len(df) # quantidade de colunas

class Adjacente:
    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso
        self.adjacente = None
    
class Vertice:
    def __init__(self, data):
        self.data = data
        self.visitado = False
        self.adjacente = []
    
    def adiciona_adjacente(self, adjacente):
        self.adjacente.append(adjacente)
    
    def mostra_adjacentes(self):
        for i in self.adjacente:
            print(i.vertice.data, i.peso)

def menu():
    quantVertices = int(input("Digite a quantidade de vértices:\n"))
    
    for i in range(quantVertices):
        linha_aleatoria = random.randint(0, total_linhas)-1
        linha = df.iloc[linha_aleatoria]

        #AQUI chame a função para adicionar as linhas no grafo
        Vertice(linha)
    
    # AQUI chame a função para mostrar todos os vértices dentro do grafo
    mostra_adjacentes()
    vertice1 = input("Escolha o vértice inicial:\n")
    vertice2 = input("Escolha o vértice final:\n")
    
    # AQUI chame a função que vai calcular a menor distância entre esses nós
    menu()
menu()