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

print("Estado inicial:")
print(rober.initial_state)
output = ss.hill_climbing(rober)
output = ss.hill_climbing_random_restarts(rober,500) #el que corre mejor
output = ss.simulated_annealing(rober, rober.temperature)
output = ss.simulated_annealing(rober, rober.heuristic)
print("Robert está en: " + str(rober.robot_nivel))

#BFS

# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por BFS:")
# print("Robert está en: ")
# result = ss.breadth_first(rober)

#DFS

# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por DFS:")
# result = ss.depth_first(rober,True)
# print("Robert está en: " + str(rober.robot_nivel))


# A*

# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por A*:")
# result = astar(rober)
# print("Robert está en: " + str(rober.robot_nivel))
# if result is not None and result.path() != 'NoneType':
#     print(f"\nNumero de movimientos: {len(result.path())-1}")
#     for action, next_state in result.path():
#         print(f"Heurística {action}: {rober.heuristic(next_state)}")
#         print(f"Costo de {action}: {rober.cost(next_state, action)}")
# else:
#     print("No hay camino")


# Greedy
    
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por Greedy:")
# result = greedy(rober, True)
# print("Robert está en: " + str(rober.robot_nivel))
# if result is not None and result.path() != 'NoneType':
#     print(f"\nNumero de movimientos: {len(result.path()) - 1}")
# else:
#     print("No hay camino")

# Uniform Cost Search
    
# print("Estado inicial:")
# print(rober.initial_state)
# print("Camino encontrado por Uniform Cost Search:")
# result = uniform_cost(rober,True)
# print("Robert está en: " + str(rober.robot_nivel))
# if result is not None:
#     print(f"\nNumero de movimientos: {len(result.path()) - 1}")
#     for action, next_state in result.path():
#         print(f"Heurística: {rober.heuristic(next_state)}")
#         print(f"Costo de {action}: {rober.cost(next_state, action)}") 