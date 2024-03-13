from simpleai.search import SearchProblem, hill_climbing,  hill_climbing_random_restarts, simulated_annealing
import random
from random import randint
import math
from simpleai.search.local import _exp_schedule

def crear_mapa(f, c, n):
    mapa = []
    
    for i in range(f):
        fila = []
        for j in range(c):
            if i == 0 or i == f-1 or j == 0 or j == c-1:
                fila.append("«") 
            else:
                terreno = random.randint(0, n) 
                if terreno == 0:
                    fila.append(str(terreno)) 
                elif terreno == n:
                    fila.append("@") 
                else:
                    obstaculo = random.randint(0, 9)
                    if obstaculo < 1:
                        fila.append("X") 
                        
                    else:
                        fila.append(str(terreno)) 
                       
        mapa.append(fila)
    
    rf = random.randint(1, f-2)
    rc = random.randint(1, c-2)
    while mapa[rf][rc] in ["X", "@"]:
        rf = random.randint(1, f-2)
        rc = random.randint(1, c-2)
    mapa[rf][rc] = "¶"
    
    return mapa, (rf, rc)

class RoverProblem(SearchProblem):
    def __init__(self, initial_state, mapa):
        super().__init__(initial_state)
        self.mapa = mapa
        self.water_pos = self._buscar_agua_mas_cercana()
        self.shallowest_pos = self._buscar_lugar_menos_profundo()
        self.deepest_pos = self._buscar_lugar_mas_profundo()
        
    def generate_random_state(self):
        return crear_mapa(len(self.mapa), len(self.mapa[0]), 9)[1]
        
    def _buscar_agua_mas_cercana(self):
        agua_pos = None
        agua_dist = None
        r, c = self.initial_state
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j] == "@":
                    dist = abs(i - r) + abs(j - c)
                    if agua_pos is None or dist < agua_dist:
                        agua_pos = (i, j)
                        agua_dist = dist
        return agua_pos
    
    def _buscar_lugar_menos_profundo(self):
        agua_pos = None
        profundidad = None
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j].isdigit():
                    prof = int(self.mapa[i][j])
                    if profundidad is None or prof < profundidad:
                        agua_pos = (i, j)
                        profundidad = prof
        return agua_pos

    def _buscar_lugar_mas_profundo(self):
        agua_pos = None
        profundidad = 0
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j].isdigit():
                    prof = int(self.mapa[i][j])
                    if prof > profundidad:
                        agua_pos = (i, j)
                        profundidad = prof
        return agua_pos

    def is_goal(self, state):
        return state == self.water_pos
    
    def is_goal_shallowest(self, state):
        return state == self.shallowest_pos

    def is_goal_deepest(self, state):
        return state == self.self.deepest_pos 
        
    def actions(self, state):
        acciones = []
        filas, columnas = len(self.mapa), len(self.mapa[0])
        r, c = state
        if r > 0 and self.mapa[r - 1][c] != "X":  
            acciones.append(("arriba", (-1, 0)))
        if r < filas - 1 and self.mapa[r + 1][c] != "X":  
            acciones.append(("abajo", (1, 0)))
        if c > 0 and self.mapa[r][c - 1] != "X":  
            acciones.append(("izquierda", (0, -1)))
        if c < columnas - 1 and self.mapa[r][c + 1] != "X":  
            acciones.append(("derecha", (0, 1)))
        return acciones

    def result(self, state, action):
        accion, (dr, dc) = action
        r, c = state
        nueva_r, nueva_c = r + dr, c + dc
        return nueva_r, nueva_c

    def value(self, state):
        return 1
    
    def cost(self,state, action, state2=None):
        x1, y1 = state
        x2, y2 = self.result(state, action)
        terreno = self.mapa[x2][y2]

        # Verificar si el rover puede moverse en el terreno
        if terreno == "X":
            return float('inf')
        elif terreno.isdigit():
            return float(terreno)
        else:
            return 1.0

    def find_rover(self):
        for fila in range(len(self.mapa)):
            for col in range(len(self.mapa[0])):
                if self.mapa[fila][col] == "¶":
                    return fila, col
                

    def heuristic(self, state):
        # Busca el lugar menos profundo
        pos_actual = state
        profundidad_actual = int(self.mapa[pos_actual[0]][pos_actual[1]])
        distancia_shallowest = float('inf')
        
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j] == str(self.shallowest_water_pos[0]):
                    distancia = abs(i-pos_actual[0])+abs(j-pos_actual[1])
                    if distancia < distancia_shallowest:
                        distancia_shallowest = distancia

        return profundidad_actual / distancia_shallowest
    
    

def temperature(k):
    return math.exp(-0.01 * k)



mapa, initial_state = crear_mapa(15, 30, 6)
problem = RoverProblem(initial_state, mapa)

print("Busqueda local hill_climbing")
result = hill_climbing(problem)
print("Coordenadas del lugar mas profundo:", problem.deepest_pos)
print("Coordenadas del lugar menos profundo:", problem.shallowest_pos)


for fila in mapa:
    print("".join(fila))
    
    
print("Busqueda local hill_climbing restarts")
result = hill_climbing_random_restarts(problem, 100)
print("Coordenadas del lugar mas profundo:", problem.deepest_pos )
print("Coordenadas del lugar menos profundo:", problem.shallowest_pos)

for fila in mapa:
    print("".join(fila))
    
print("Busqueda local Simulated Annealing")
result = simulated_annealing(problem,schedule = temperature)
print("Coordenadas del lugar mas profundo:", problem.deepest_pos )
print("Coordenadas del lugar menos profundo: ", problem.shallowest_pos)

for fila in mapa:
    print("".join(fila))