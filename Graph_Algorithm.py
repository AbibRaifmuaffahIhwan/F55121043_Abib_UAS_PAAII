import itertools
import time
import heapq

def calculate_distance(points, order):
    distance = 0
    for i in range(len(order) - 1):
        city1 = order[i]
        city2 = order[i+1]
        distance += points[city1][city2]
    return distance

def tsp(points):
    start_time = time.time()
    num_cities = len(points)
    best_distance = float('inf')
    best_order = None

    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(range(num_cities))

    # Iterate through each permutation and calculate the distance
    for order in all_permutations:
        distance = calculate_distance(points, order)
        if distance < best_distance:
            best_distance = distance
            best_order = order

        # Print the current iteration and distance
        print("Iteration:", order, "| Distance:", distance)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nBest Order:", best_order)
    print("Best Distance:", best_distance)
    print("Execution Time:", execution_time, "seconds")

def dijkstra(graph, start_node):
    start_time = time.time()
    num_nodes = len(graph)
    distances = {node: float('inf') for node in range(num_nodes)}
    distances[start_node] = 0
    visited = set()
    heap = [(0, start_node)]
    path = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        visited.add(current_node)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

        # Print the current iteration and distances
        print("Iteration:", current_node, "| Distances:", distances)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nShortest Distances:", distances)
    print("Execution Time:", execution_time, "seconds")

def Program_Utama():
    points = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print("================== Ujian Akhir  Semester ==================");
    print("========== Perancangan dan Analisis Algoritma II ==========");
    print("================= Abib  Raifmuaffah Ihwan =================");
    print("======================= F551 21 043 =======================");
    print("========================= Kelas B =========================");
    print("1. TSP");
    print("2. Djikstra");
    pilihan = input("Silahkan Pilih Algoritma Shortest Path : ")
    if pilihan == "1":
        print("\nAlgoritma TSP")
        tsp(points)
    elif pilihan == "2":
        print("\nAlgoritma Djikstra");
        # Contoh grafik
        graph = {
            0: {1: 4, 2: 2},
            1: {2: 3, 3: 2, 4: 3},
            2: {1: 1, 3: 4},
            3: {4: 2},
            4: {}
        }
        start_node = 0

        dijkstra(graph, start_node)
    else:
        print("\nPilihan Anda Tidak Tersedia");

Program_Utama()