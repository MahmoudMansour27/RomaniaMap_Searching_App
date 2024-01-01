import heapq
import matplotlib.pyplot as plt
from math import sqrt

# graphs
romania_graph_with_cost = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}, 
    'Zerind': {'Arad': 75, 'Oradea': 71}, 
    'Oradea': {'Zerind': 71, 'Sibiu': 151}, 
    'Timisoara': {'Arad': 118, 'Lugoj': 111}, 
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70}, 
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75}, 
    'Dobreta': {'Mehadia': 75, 'Craiova': 120}, 
    'Craiova': {'Dobreta': 120, 'Rimnicu': 146, 'Pitesti': 138}, 
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}, 
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151}, 
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211}, 
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101}, 
    'Bucharest': {'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}, 
    'Urziceni': {'Hirsova': 98, 'Bucharest': 85, 'Vaslui': 142}, 
    'Giurgiu': {'Bucharest': 90}, 
    'Hirsova': {'Urziceni': 98, 'Eforie': 86}, 
    'Eforie': {'Hirsova': 86}, 
    'Vaslui': {'Urziceni': 142, 'Iasi': 92}, 
    'Iasi': {'Vaslui': 92, 'Neamt': 87}, 
    'Neamt': {'Iasi': 87}
    }

romania_graph = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'], 
    'Zerind': ['Arad', 'Oradea'], 
    'Oradea': ['Zerind', 'Sibiu'], 
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'], 
    'Timisoara': ['Arad', 'Lugoj'], 
    'Lugoj': ['Timisoara', 'Mehadia'], 
    'Mehadia': ['Lugoj', 'Dobreta'], 
    'Dobreta': ['Mehadia', 'Craiova'], 
    'Craiova': ['Dobreta', 'Rimnicu', 'Pitesti'], 
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'], 
    'Fagaras': ['Sibiu', 'Bucharest'], 
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'], 
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'], 
    'Giurgiu': ['Bucharest'], 
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'], 
    'Hirsova': ['Urziceni', 'Eforie'], 
    'Eforie': ['Hirsova'], 
    'Vaslui': ['Iasi', 'Urziceni'], 
    'Iasi': ['Vaslui', 'Neamt'], 
    'Neamt': ['Iasi']
    }

romania_map_points = {
    'Arad': (91, 492), 
    'Bucharest': (400, 327), 
    'Craiova':( 253, 288),
    'Dobreta': (165, 299), 
    'Eforie': (562, 293), 
    'Fagaras': (305, 449),
    'Giurgiu': (375, 270), 
    'Hirsova': (534, 350), 
    'Iasi': (473, 506),
    'Lugoj': (165, 379), 
    'Mehadia': (168, 339), 
    'Neamt': (406, 537),
    'Oradea': (131, 571), 
    'Pitesti': (320, 368), 
    'Rimnicu': (233, 410),
    'Sibiu': (207, 457), 
    'Timisoara': (94, 410), 
    'Urziceni': (456, 350),
    'Vaslui': (509, 444), 
    'Zerind': (108, 531)
    }

# uninformed search
def breadth_first_search(start, goal, graph = romania_graph):
    explored = []
    frontier = [(start, [start])]
    
    while frontier:
        cur_node, path = frontier.pop(0)
        
        if cur_node == goal:
            return path
        
        explored.append(cur_node)
        
        for child in graph[cur_node]:
            if child not in explored:
                temp_path = path + [child]
                frontier.append((child, temp_path))
                
                
    return None


def uniform_cost_search(start, goal, graph = romania_graph_with_cost):
    # cost, cur, path
    cost_ordered_queue = [(0, start, [start])]
    explored = []
    
    while cost_ordered_queue:
        cur_cost, cur_node, cur_path = heapq.heappop(cost_ordered_queue)
        
        if cur_node == goal:
            return (cur_path+[cur_node], cur_cost)
        
        if cur_node in explored:
            continue
        
        else:
            explored.append(cur_node)
            
        for child, child_cost in graph[cur_node].items():
            if child not in explored:
                total_cost = cur_cost + child_cost
                temp_path = cur_path + [cur_node]
                heapq.heappush(cost_ordered_queue, (total_cost, child, temp_path)) # shof hena
     
    
    return None


def deepth_first_search(start, goal, graph = romania_graph):
    stack = [(start, [start])]
    explored = []
    
    while stack:
        cur_node, path = stack.pop()
        
        if cur_node == goal:
            return path
        
        if cur_node in explored:
            continue
        
        explored.append(cur_node)
        
        for child in reversed(graph[cur_node]):
            if child not in explored:
                stack.append((child, path + [child]))
                
    return None


def deepth_limit_search(start, goal, limit_depth, graph = romania_graph): # 3del el limit
    stack = [(start, [start], 0)]
    explored = []
    
    while stack:
        cur_node, cur_path, cur_depth = stack.pop()
        
        if cur_node == goal:
            return cur_path
        
        if cur_depth < limit_depth:
            
            if cur_node in explored:
                continue
            
            explored.append(cur_node)
            
            for child in reversed(graph[cur_node]):
                if child not in explored:
                    stack.append((child, cur_path + [child], cur_depth+1))
                
    return None
    

def iterative_deeping_DLS(start, goal, graph = romania_graph, maxdepth = 25):
    limit = 0
    
    while True:
        path = deepth_limit_search(start, goal, limit, graph)
        
        if path is not None:
            return path
        
        limit += 1
        
        if maxdepth == limit:
            return None
    
    return None
    
# ********************************************************************************
# idea for BFS for Bidirectional search, step by step for to functions and stored in global variables
def breadth_first_search_bi(start, goal, graph = romania_graph):
    global explored
    global frontier
    
    explored = []
    frontier = [(start, [start])]
    
    while frontier:
        cur_node, path = frontier.pop(0)
        
        if cur_node == goal:
            return path
        
        explored.append(cur_node)
        
        for child in graph[cur_node]:
            if child not in explored:
                temp_path = path + [child]
                frontier.append((child, temp_path))
                
                
    return None
# ********************************************************************************


def bidirectional_search(start, goal, graph = romania_graph):
    forward_queue = [(start, [start])]
    backward_queue = [(goal, [goal])]
    
    explored_forward = []
    explored_backward = []
    
    # forward and backward paths
    forward_paths = {start: [start]}
    backward_paths = {goal: [goal]}
    
    while forward_queue and backward_queue:
        # forward search
        cur_forward, path_forward = forward_queue.pop(0)
        explored_forward.append(cur_forward)
        
        if cur_forward in explored_backward:
            backward_path = backward_paths[cur_forward]
            backward_path.pop()
            return forward_paths[cur_forward] + backward_path[::-1]
    
        for forward_child in graph[cur_forward]:
            if forward_child not in explored_forward:
                forward_queue.append((forward_child, path_forward+[forward_child]))
                forward_paths[forward_child] = path_forward + [forward_child]
                
        # backward search
        cur_backward, path_backward = backward_queue.pop(0)
        explored_backward.append(cur_backward)
        
        if cur_backward in explored_forward:
            forward_path = forward_paths[cur_backward]
            forward_path.pop()
            return forward_path + backward_paths[cur_backward][::-1]
        
        for backward_child in graph[cur_backward]:
            if backward_child not in explored_backward:
                backward_queue.append((backward_child, path_backward+[backward_child]))
                backward_paths[backward_child] = path_backward + [backward_child]
                
    return None


# ----------------------
# romania map graph points
def romania_map_points_visualize(map_points = romania_map_points):
    city_x_values = []
    city_y_values = []
    for city in romania_map_points:
        points = romania_map_points[city]
        city_x_values.append(points[0])
        city_y_values.append(points[1])
    
    plt.scatter(city_x_values, city_y_values)
    plt.show()


def calculate_huristic(goal, points = romania_map_points):
    huristic_values = {}
    goal_points = points[goal]
    
    for city in romania_map_points:
        point_b = romania_map_points[city]
        euclidean_distance = sqrt((point_b[0]-goal_points[0])**2+(point_b[1]-goal_points[1])**2)
        huristic_values[city] = euclidean_distance
    
    return huristic_values
        
# informed search
def greedy_best_first_search(start, goal, heuristic, graph = romania_graph):
    queue = [(heuristic[start], start, [start])]
    explored = []
    
    while queue:
        huristic, cur_node, path = queue.pop(0)
        
        if cur_node == goal:
            return path 
        
        explored.append(cur_node)
        
        if cur_node in graph:
            childern = graph[cur_node]
            for child in childern:
                if child not in explored:
                    temp_path = path + [child]
                    queue.append((heuristic[child], child, temp_path))
        queue.sort()
    
    return None


def a_start_search(start, goal, heuristic, graph = romania_graph_with_cost):
    queue = [(0, start, [start])]
    explored = []
    
    while queue:
        cur_cost, cur_node, cur_path = heapq.heappop(queue)
        
        if cur_node == goal:
            return cur_path
        
        explored.append(cur_node)
        
        if cur_node in graph:
            childern = graph[cur_node]
            for child, cost in childern.items():
                if child not in explored:
                    temp_path = cur_path + [child]
                    temp_cost = cur_cost + cost
                    total_cost = temp_cost + heuristic[child]
                    heapq.heappush(queue, (total_cost, child, temp_path))
                    
    
    return None    
        
        
        
        
        
        
        
        
        
