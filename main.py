def count_paths_floyd_warshall(matrix, src, dst):
    V = len(matrix)
    paths = [row[:] for row in matrix]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if paths[i][k] > 0 and paths[k][j] > 0:
                    paths[i][j] += paths[i][k] * paths[k][j]
                    
    return paths[src][dst]

if __name__ == "__main__":
    matrix_string = "0,1,1,1|0,0,0,1|0,0,0,1|0,0,0,0"
    graph = [[int(num) for num in row.split(",")] for row in matrix_string.split("|")]
    
    source = 0
    destination = 3
    
    total_paths = count_paths_floyd_warshall(graph, source, destination)
    print(f"Total paths from {source} to {destination}: {total_paths}")
