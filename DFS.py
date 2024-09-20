# Function to perform DFS traversal
def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()  # Initialize an empty set to track visited vertices
    
    visited.add(start_vertex)
    print(start_vertex, end=' ')  # Print the current vertex
    
    # Recursively visit all adjacent vertices that have not been visited
    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call DFS starting from vertex 'A'
dfs(graph, 'A')
