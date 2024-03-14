import simpleai.search as ss
# la libreria simpleai nos permite hacer uso de algoritmos de busqueda
import random
# la libreria random nos permite generar numeros aleatorios
import math
# la libreria math nos permite hacer operaciones matematicas

class Rober(ss.SearchProblem):
    def __init__(self, Terreno):
        # Inicializa el robot en una posición aleatoria
        self.robot_x = 0
        self.robot_y = 0
        self.robot_nivel = 0
        self.Terreno = Terreno  # Terreno en el que se encuentra el robot
        self.colocar_robot()  # Colocar el robot en una posición aleatoria
        self.costo = 0
        # Estado inicial
        self.initial_state = (self.robot_x, self.robot_y, self.robot_nivel)


    def colocar_robot(self):
        # Coloca el robot en una posición aleatoria
        self.robot_x = random.randint(1, self.Terreno.filas)
        self.robot_y = random.randint(1, self.Terreno.columnas)
        self.robot_nivel = random.randint(1, 6)
        self.Terreno.matriz[self.robot_x][self.robot_y] = 'R'

    def actions(self, state):
        # Devuelve las acciones que se pueden ejecutar en un estado
        acciones = []
        if state is not None:
            x, y, nivel = state
        else:
            x, y, nivel = self.robot_x, self.robot_y, self.robot_nivel

        print("Posición actual: ", x, y, nivel)
        if x - 1 < 0 or x + 1 > self.Terreno.filas or y - 1 < 0 or y + 1 > self.Terreno.columnas:
            arriba = self.Terreno.matriz[x][y]
            abajo = self.Terreno.matriz[x][y]
            derecha_arriba = self.Terreno.matriz[x][y]
            derecha_abajo = self.Terreno.matriz[x][y]
            izquierda_arriba = self.Terreno.matriz[x][y]
            izquierda_abajo = self.Terreno.matriz[x][y]
        else:
            arriba = self.Terreno.matriz[x - 1][y]
            abajo = self.Terreno.matriz[x + 1][y]
            derecha_arriba = self.Terreno.matriz[x - 1][y + 1]
            derecha_abajo = self.Terreno.matriz[x + 1][y + 1]
            izquierda_arriba = self.Terreno.matriz[x - 1][y - 1]
            izquierda_abajo = self.Terreno.matriz[x + 1][y - 1]

        caracteres = ["R", "#", "*", "-", " "]

        num = abs(nivel - int(arriba)) if isinstance(arriba, str) and arriba.isdigit() else 0
        if arriba not in caracteres and arriba != '*' and arriba != '#':
            if arriba != '-' and num <= 1:
                acciones.append('⬆')

        elif arriba == "-":
            acciones.append('⬆')

        num = abs(nivel - int(abajo)) if isinstance(abajo, str) and abajo.isdigit() else 0
        if abajo not in caracteres and abajo != '*' and abajo != '#':
            if abajo != '-' and num <= 1:
                acciones.append('⬇')

        elif abajo == "-":
            acciones.append('⬇')

        num = abs(nivel - int(derecha_arriba)) if isinstance(derecha_arriba, str) and derecha_arriba.isdigit() else 0
        if derecha_arriba not in caracteres and derecha_arriba != '*' and derecha_arriba != '#':
            if num <= 1:
                acciones.append('⬈')

        elif derecha_arriba == "-":
            acciones.append('⬈')

        num = abs(nivel - int(derecha_abajo)) if isinstance(derecha_abajo, str) and derecha_abajo.isdigit() else 0
        if derecha_abajo not in caracteres and derecha_abajo != '*' and derecha_abajo != '#':
            if num <= 1:
                acciones.append('⬊')

        elif derecha_abajo == "-":
            acciones.append('⬊')

        num = abs(nivel - int(izquierda_arriba)) if isinstance(izquierda_arriba, str) and izquierda_arriba.isdigit() else 0
        if izquierda_arriba not in caracteres and izquierda_arriba != '*' and izquierda_arriba != '#':
            if num <= 1:
                acciones.append('⬉')

        elif izquierda_arriba == "-":
            acciones.append('⬉')

        num = abs(nivel - int(izquierda_abajo)) if isinstance(izquierda_abajo, str) and izquierda_abajo.isdigit() else 0
        if izquierda_abajo not in caracteres and izquierda_abajo != '*' and izquierda_abajo != '#':
            if num <= 1:
                acciones.append('⬋')

        elif izquierda_abajo == "-":
            acciones.append('⬋')

        print(acciones)
        return acciones

    def heuristic(self, state):
        # Heurística: distancia euclidiana al estado objetivo
        print(state)
        if not isinstance(state, int):
            print(state)
            goal_x, goal_y, _ = state
            current_x, current_y, _ = (self.robot_x, self.robot_y, self.robot_nivel)
            return math.sqrt((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2)
        else:
            return 1

    def cost(self, state, action, state2 = None):
        # Incrementa el costo si el nivel del robot y el nivel del estado objetivo son diferentes
        if state is not None:
            x2, y2, _ = self.result(state, action)
        else:
            x2, y2 = self.robot_x, self.robot_y
        next_level = self.Terreno.matriz[x2][y2]
        current_level = self.robot_nivel
        caracteres_especiales = ["#", "*", "R", "-", " "]

        if next_level in caracteres_especiales:
            return 0
        elif next_level == current_level:
            self.costo += current_level
            return current_level
        elif next_level > current_level:
            self.costo += next_level
            return next_level
        
        self.costo = next_level
        return next_level

    def is_goal(self, state):
        # is_goal es True si el estado es el agua objetivo
        x, y, nivel = state
        return self.Terreno.matriz[x][y] == '-'


    def result(self, state, action):
        # Devuelve el estado resultante de ejecutar una acción en un estado
        if state is not None:
            x, y, nivel = state
        else:
            x, y, nivel = self.robot_x, self.robot_y, self.robot_nivel

        if action == '⬆':
            nivel = self.Terreno.matriz[x - 1][y]
            new_state = (x - 1, y, nivel)
        elif action == '⬈':
            nivel = self.Terreno.matriz[x - 1][y + 1]
            new_state = (x - 1, y + 1, nivel)
        elif action == '⬉':
            nivel = self.Terreno.matriz[x - 1][y - 1]
            new_state = (x - 1, y - 1, nivel)
        elif action == '⬇':
            nivel = self.Terreno.matriz[x + 1][y]
            new_state = (x + 1, y, nivel)
        elif action == '⬊':
            nivel = self.Terreno.matriz[x + 1][y + 1]
            new_state = (x + 1, y + 1, nivel)
        elif action == '⬋':
            nivel = self.Terreno.matriz[x + 1][y - 1]
            new_state = (x + 1, y - 1, nivel)
        else:
            return state

        new_x, new_y, new_nivel = new_state
        caracteres_especiales = ["#", "*", "R", "-", " "]
        try:
            # Intentar convertir a entero si no es un caracter especial
            if self.Terreno.matriz[new_x][new_y] not in caracteres_especiales:
                self.robot_nivel = int(self.Terreno.matriz[new_x][new_y])
        except ValueError:
            # Si hay error (ej: '-', agua), mantener el nivel anterior
            pass
        
        return new_state
    
    def temperature(self, k):
        return math.exp(-0.01 * k)
    
    def calculate_state_value(self, state):
        if state is not None:
            x, y, nivel = state
            return nivel
        else:
            return self.robot_nivel
    
    def value(self, state):
        if state is not None:
        # Calculate the value of the state
            value = self.calculate_state_value(state)
            if isinstance(value, str):
                # print("Value is a string, cannot compare.")
                return 0  # or any default value
            return value
        else:
            # print("State is None, cannot calculate value.")
            return 0  # or any default value
        
    def generate_random_state(self):
    # Generate a random state
        state = self.colocar_robot()
        return state