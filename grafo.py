from collections import defaultdict


def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["B", "C"], ["B", "G"],
        ["E", "F"], ["G", "F"],
        ["C", "D"], ["D", "H"],
        ["D", "G"]
    ]
    graph = defaultdict(list)
    
    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
         
        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph

def coberturaGrafo(graph):
    #new_graph = defaultdict(list)
    new_graph = graph.copy()
    result = set()
    for vertex in new_graph.keys():
        if new_graph.get(vertex) != []:
            result.add(vertex)
            for edge in new_graph.get(vertex):
                new_graph[vertex] = new_graph.get(vertex).pop(edge)
                new_graph[edge] = new_graph.get(edge).pop(vertex)
    return result
            

if __name__ == "__main__":
    graph = build_graph()
     
    print(graph)
    print(coberturaGrafo(graph))