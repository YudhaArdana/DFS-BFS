graph = {
    '1' : ['4','2'],
    '2' : ['1', '5', '8', '7'],
    '3' : ['10', '9', '4', '2'],
    '4' : ['1', '3'],
    '5' : ['2', '6', '7'],
    '6' : ['5'],
    '7' : ['5', '2', '8'],
    '8' : ['2', '7'],
    '9' : ['3'],
    '10' : ['3']
}

visited = set() 

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '1')