## README.md

# Rober: Intelligent Terrain Navigation System

Rober is a robot simulation that explores and navigates through a generated terrain, searching for optimal paths using various search algorithms like Hill Climbing, A*, Greedy Search, and more. The robot must avoid obstacles and traverse different elevation levels, with the goal of finding water sources marked on the map. 

This project demonstrates the application of search algorithms provided by the `simpleai` library and highlights how heuristic-based decision-making can optimize navigation in complex environments.

---

## Table of Contents
1. [Project Structure](#project-structure)  
2. [Dependencies](#dependencies)  
3. [Usage](#usage)  
4. [Algorithms Implemented](#algorithms-implemented)  
5. [Authors](#authors)

---

## Project Structure

```
.
├── Rober.py               # Defines the Rober robot class and search logic
├── Terreno.py             # Creates and displays the terrain environment
├── rober4 av3.py          # Main script to execute different search algorithms
├── README.md              # Documentation for the project
```

- **Rober.py**: Contains the core logic for the robot, including how it moves and interacts with the terrain.
- **Terreno.py**: Generates the terrain, placing water, obstacles, and different elevation levels.
- **rober4 av3.py**: Main script that demonstrates the usage of several search algorithms.

---

## Dependencies

This project relies on the following libraries:

- **simpleai**: For implementing search algorithms.  
  Install with:
  ```bash
  pip install simpleai
  ```
- **colorama**: For colored console output.  
  Install with:
  ```bash
  pip install colorama
  ```

---

## Usage

1. Clone this repository or download the files.

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python rober4\ av3.py
   ```

4. Enable or disable different search algorithms by commenting/uncommenting the relevant sections in `rober4 av3.py`. Example:

   ```python
   result = ss.hill_climbing(rober)  # Enable Hill Climbing search
   ```

---

## Algorithms Implemented

This project demonstrates the following algorithms from the `simpleai` library:

1. **Hill Climbing**: Greedy search that aims to reach the highest value in the state space.
2. **Hill Climbing with Random Restarts**: Executes multiple hill climbs to escape local maxima.
3. **Simulated Annealing**: A probabilistic technique to explore the state space.
4. **A\***: Uses a heuristic function to find the shortest path to the goal.
5. **Breadth-First Search (BFS)**: Explores nodes layer by layer.
6. **Depth-First Search (DFS)**: Explores as deep as possible before backtracking.
7. **Greedy Search**: Chooses the path with the most promising heuristic value.
8. **Uniform Cost Search**: Finds the least-cost path to the goal.

---

## Authors

- **Nathan Isaac García Larios** - A01749595  
- **Ximena Serna Mendoza** - A01749870

---

This project is intended for educational purposes and demonstrates the power of search algorithms applied to intelligent navigation. Feel free to explore, modify, and extend the code for your own experiments!
