#@author: Aditya Ravikumar
from dj import graph
import string
def dijkstra(graph, source, destination, visited=[], dist={}, pre={} ):
    neighbour = None
    # calculates a shortest path tree routed in source.
    if source == destination:
        # Build the shortest path and display it.
        pred = destination
        path = []
        while pred != None:
            path.append(pred)
            pred = pre.get(pred, None)
            'graph'[::-1]
        print('shortest path from: '+(source)  + str(path) + " Total Cost =" + str(dist[destination]))
    else:
        # if the vertex is not visited, distance from source will be 0.
        if not visited:
            dist[source] = 0
        # visit the neighbors
        for neighbor in graph[source]:
            if neighbour not in visited:
                new_dist = dist[source] + graph[source][neighbor]
                if new_dist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = new_dist
                    pre[neighbor] = source
        # mark as visited
        visited.append(source)
        #print(visited[::-1])
        # Recurse when all neighbors have visited and select the non visited node with lowest distance 'x'
        unvisited = {}
        #initial condition
        if source not in graph:
            raise TypeError('The shortest path cannot be found')
        if destination not in graph:
            raise TypeError('The destinaton of the shortest path cannot be found')
        for k in graph:
            if k not in visited:
                unvisited[k] = dist.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, destination, visited, dist, pre)
        #graph[::-1]

if __name__ == "__main__":
    graph = {'a': {'b': 1, 'c': 6},
         'b': {'a': 1, 'd': 2, 'e': 7},
         'c': {'a': 6, 'e': 1},
         'd': {'b': 2, 'e': 1},
         'e': {'b': 7, 'c': 1, 'd': 1},
         }
    print("Dijkstras Algorithum  \n")
    print("Matrix List Representation")
    numberWidth = len(str(max(max(v.values()) for v in graph.values())))

    # function to format the numbers
    formatNumber = lambda x: str(x).rjust(numberWidth)
    keys = sorted(graph.keys())
    rows = [' '.join(map(formatNumber, [''] + keys))]

    for r in keys:
        row = [r]
        for k in keys:
            row.append(graph[r].get(k, '0'))
        rows.append(' '.join(map(formatNumber, row)))

    print('\n'.join(rows))
#graph[::-1]

dijkstra(graph, 'a', 'e')
#graph[::-1]
dijkstra(graph, 'a', 'c')
#dijkstra(graph, 'a', 'd')
#dijkstra(graph, 'a', 'b')

#def init(self):
    #my_file_handle = open("C:\Users\Aditya\PycharmProjects\slgo_presentation.txt")
    #my_file_handle.read()
    #k = int(input("Enter the source vertex"))
    #print("Dijkstras algorithum  \n")
    #n = int(input("Enter the number of elements in row"))
    #m = int(input("Enter the number of elements in column"))
    # print("enter the values of the matrix")
    #matrix = [[0 for x in range(m)] for x in range(n)]
    #for i in range(n):
        #for j in range(m):
            #matrix[i][j] = int(input("enter the values of the matrix"))
    #print(matrix)
    #dijkstra(matrix, n, m)


    #graph = {'a': { 'b': 1, 'c': 6 },
             #'b': {'a': 1, 'd': 2, 'e': 7},
             #'c': {'a': 6, 'e': 1},
             #'d': {'b':2 , 'e': 1},
             #'e': {'b': 7, 'c': 1  , 'd': 1},
             #}

    #dijkstra(graph, 'b', 'd')
    #dijkstra(graph, 'a', 'c')

