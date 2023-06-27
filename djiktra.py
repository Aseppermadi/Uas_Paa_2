import sys
import time

# Representasi graph dalam bentuk dictionary
graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'C': 8, 'D': 12},
    'C': {'D': 11, 'E': 3, 'G': 9},
    'D': {'E': 11, 'F': 10},
    'E': {'F': 6},
    'G': {'E': 7, 'F': 9},
    'H': {}
}

def tsp(graph, start, visited, current_path, current_cost, shortest_path, shortest_cost):
    visited[start] = True
    current_path.append(start)
    
    if len(current_path) == len(graph):
        current_path.append(start)
        current_cost += graph[start][current_path[-2]]
        if current_cost < shortest_cost[0]:
            shortest_path[0] = current_path.copy()
            shortest_cost[0] = current_cost
        current_path.pop()
        current_cost -= graph[start][current_path[-1]]
        
    for neighbor, distance in graph[start].items():
        if not visited[neighbor]:
            current_cost += distance
            tsp(graph, neighbor, visited.copy(), current_path, current_cost, shortest_path, shortest_cost)
            current_cost -= distance
            
    current_path.pop()
    visited[start] = False

# Main program
choice = input("Enter algorithm choice (TSP/Dijkstra): ")

if choice.lower() == "tsp":
    start_time = time.time()
    shortest_path = [[]]
    shortest_cost = [sys.maxsize]
    visited = {node: False for node in graph}
    tsp(graph, 'A', visited, [], 0, shortest_path, shortest_cost)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("\n*** TSP (Traveling Salesman Problem) ***")
    print("Shortest Path:", shortest_path[0])
    print("Shortest Cost:", shortest_cost[0])
    print("Elapsed Time:", elapsed_time, "seconds")
    
elif choice.lower() == "dijkstra":
    start_time = time.time()
    shortest_distance = dijkstra(graph, 'A', 'F')
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print("\n*** Dijkstra ***")
    print("Shortest Distance:", shortest_distance)
    print("Elapsed Time:", elapsed_time, "seconds")

else:
    print("Invalid choice. Please choose either 'TSP' or 'Dijkstra'.")
