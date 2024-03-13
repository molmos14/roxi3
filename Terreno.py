import simpleai.search as ss
# la libreria simpleai nos permite hacer uso de algoritmos de busqueda
import random
# la libreria random nos permite generar numeros aleatorios
from colorama import Fore, Style
# la libreria colorama nos permite darle color a la salida de la consola

class Terreno(ss.SearchProblem):
    def __init__(self, filas, columnas, porcentaje_agua, porcentaje_obstaculos):
        self.filas = filas
        self.columnas = columnas
        self.porcentaje_agua = porcentaje_agua
        self.porcentaje_obstaculos = porcentaje_obstaculos
        self.matriz = [[' ' for _ in range(columnas + 2)] for _ in range(filas + 2)]
        self.agua_encontrada = 0
        self.obstaculos_encontrados = 0
        self.niveles_agua = set()
        self.generar_terreno()
        self.rober = None  # Rober instance
        self.initial_state = (0, 0, 0)

    def generar_terreno(self):
        for i in range(1, self.filas + 1):
            for j in range(1, self.columnas + 1):
                # Asignar nivel topográfico
                nivel = random.randint(1, 6)
                # Asignar agua
                if random.random() < self.porcentaje_agua:
                    # Definir los porcentajes de probabilidad para cada nivel de agua
                    if random.random() < 0.6:  # 60% para nivel 1
                        nivel_agua = 1
                    elif random.random() < 0.3:  # 30% para nivel 2
                        nivel_agua = 2
                    else:  # 10% para nivel 3
                        nivel_agua = 3
                    self.matriz[i][j] = '-'
                    self.agua_encontrada += 1
                    # self.niveles_agua.add(nivel_agua)
                # Asignar obstáculo
                elif random.random() < self.porcentaje_obstaculos:
                    self.matriz[i][j] = '*'
                    self.obstaculos_encontrados += 1
                else:
                    self.matriz[i][j] = nivel

        # Agregar límites alrededor del mapa
        for i in range(self.filas + 2):
            self.matriz[i][0] = '#'
            self.matriz[i][self.columnas + 1] = '#'
        for j in range(self.columnas + 2):
            self.matriz[0][j] = '#'
            self.matriz[self.filas + 1][j] = '#'

    def mostrar_terreno(self, rx=None, ry=None):
        for i in range(self.filas + 2):
            for j in range(self.columnas + 2):
                # If the current position is the robot's position, print 'R'
                if rx is not None and ry is not None and rx == i and ry == j:
                    print(Fore.GREEN + 'R', end=' ')
                elif self.matriz[i][j] == '-':
                    print(Fore.LIGHTCYAN_EX + self.matriz[i][j], end=' ')
                elif self.matriz[i][j] == '*':
                    print(Fore.BLACK + self.matriz[i][j], end=' ')
                elif isinstance(self.matriz[i][j], int):
                    # Colores para los números según su valor
                    if self.matriz[i][j] <= 1:
                        print(Fore.LIGHTYELLOW_EX + str(self.matriz[i][j]), end=' ')
                    elif self.matriz[i][j] <= 2:
                        print(Fore.LIGHTYELLOW_EX + str(self.matriz[i][j]), end=' ')
                    elif self.matriz[i][j] <= 3:
                        print(Fore.YELLOW + str(self.matriz[i][j]), end=' ')
                    elif self.matriz[i][j] <= 4:
                        print(Fore.LIGHTRED_EX + str(self.matriz[i][j]), end=' ')
                    elif self.matriz[i][j] <= 5:
                        print(Fore.RED + str(self.matriz[i][j]), end=' ')
                    else:
                        print(Fore.MAGENTA + str(self.matriz[i][j]), end=' ')
                else:
                    print(Fore.WHITE + str(self.matriz[i][j]), end=' ')
            print()
        print(Style.RESET_ALL)

