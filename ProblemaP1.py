# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 2

import sys, math

# Función solución
def grafosConectados(data):
    num,indexG=1,0 #numeros de componentes conectados y el mayor indice anterior
    subGraphs=[] #subcomponentes conectados
    subGraphs.append([data[indexG],math.inf])
    for i in range(1,len(data)):#Se generan los subcomponentes conectados
        if data[i]>data[indexG]:
            subGraphs.append([data[i],math.inf])
            num=num+1
            indexG=i
        else:
            if data[i]<subGraphs[len(subGraphs)-1][1]:
                subGraphs[len(subGraphs)-1][1]=data[i]
    men=math.inf
    for i in range(len(subGraphs)-1,0,-1):#Sobre conectan los subcomponentes conectados
        if subGraphs[i][1]<men:
            men=subGraphs[i][1]
        if subGraphs[i-1][0]>men:
            num=num-1
    return num


def main():
    input = sys.stdin.readline
    numberCases = int(input())  # Número de casos de prueba
    solutions = []
    for c in range(numberCases):
        data = list(map(int, (input().split())))
        # Se llama a la función solución con los datos anteriores
        sol = grafosConectados(data)
        solutions.append(sol)
    # Output
    for i in solutions:
        print(i)


main()
