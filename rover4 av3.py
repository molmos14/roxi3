"""
    Nathan Isaac García Larios - A01749595
    Ximena Serna Mendoza - A01749870
"""
import Rober
import Terreno
import simpleai.search as ss
from simpleai.search import astar, greedy, uniform_cost
from simpleai.search.local import  hill_climbing_random_restarts, hill_climbing, hill_climbing_stochastic
from simpleai.search.viewers import ConsoleViewer

# la libreria simpleai nos permite hacer uso de algoritmos de busqueda

# Create terrain object
terreno = Terreno.Terreno(15, 30, 0.05, 0.1)
# Create Rober instance with the terrain as an argument
rober = Rober.Rober(terreno)

# Búsquedas locales
#print("Estado inicial:")
#print(rober.initial_state)
# terreno.mostrar_terreno()
#output = ss.hill_climbing(rober)
#output = ss.hill_climbing_random_restarts(rober,500) #el que corre mejor
#output = ss.simulated_annealing(rober,temperature)
#output = ss.simulated_annealing(rober,_exp_schedule)

# print("Robert está en: " + str(rober.robot_nivel))
#terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
#terreno.matriz[rober.robot_x][rober.robot_y] = ' '  # Restore original position

#BFS
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por BFS:")
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# print("Robert está en: ")
# result = ss.breadth_first(rober)
# terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# terreno.matriz[rober.robot_x][rober.robot_y] = rober.robot_nivel  # Restore original position

#DFS
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por DFS:")
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# result = ss.depth_first(rober,True)
# print("Robert está en: " + str(rober.robot_nivel))
# terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# terreno.matriz[rober.robot_x][rober.robot_y] = rober.robot_nivel  # Restore original position

# A*
print("Estado inicial:")
print(rober.initial_state)
print("Camino encontrado por A*:")
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
result = astar(rober)
print("Robert está en: " + str(rober.robot_nivel))
# terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# terreno.matriz[rober.robot_x][rober.robot_y] = rober.robot_nivel  # Restore original position
if result is not None and result.path() != 'NoneType':
    print(f"\nNumero de movimientos: {len(result.path())-1}")
    # print(result.path())
for action, next_state in result.path():
    print(f"Heurística {action}: {rober.heuristic(next_state)}")
    print(f"Costo de {action}: {rober.cost(next_state, action)}")


# Greedy
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por Greedy:")
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# result = greedy(rober, True)
# print("Robert está en: " + str(rober.robot_nivel))
# terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# terreno.matriz[rober.robot_x][rober.robot_y] = rober.robot_nivel  # Restore original position
# print(f"\nNumero de movimientos: {len(result.path()) - 1}")


# # Uniform Cost Search
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por Uniform Cost Search:")
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# result = uniform_cost(rober,True)
# print("Robert está en: " + str(rober.robot_nivel))
# terreno.matriz[rober.robot_x][rober.robot_y] = 'R'  # Update rover position
# terreno.mostrar_terreno(rober.robot_x, rober.robot_y)
# terreno.matriz[rober.robot_x][rober.robot_y] = rober.robot_nivel  # Restore original position
# for action, next_state in result.path():
#     print(f"Heurística: {rober.heuristic(next_state)}")
# for action, next_state in result.path():
#     print(f"Costo de {action}: {rober.cost(None, action, next_state)}")

#las diferenciAS CON ROVER3 es la definicion del costo y la imprenta