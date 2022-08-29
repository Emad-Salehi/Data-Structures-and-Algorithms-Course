n = int(input())

edges = {}

for i in range(n-1):
    u, v = input().split()
    u, v = int(u), int(v)

    if u not in edges:
        edges[u] = [v]
    
    else:
        edges[u].append(v)
    
    if v not in edges:
        edges[v] = [u]
    
    else:
        edges[v].append(u)

print(edges)
candids = list(range(1,n+1))

for candid in candids:
    visited = []
    flag = True
    node = candid
    while len(visited) != n:
        degrees = []
        if len(edges[node]) != 1:
            visited.append(node)
            for neighbor in edges[node]:
                if neighbor not in visited:
                    degrees.append(len(edges[neighbor]))

            #print(degrees)
            if len(set(degrees)) != 1:
                print(-1)
                flag = False
                break

        else:
            visited.append(node)

if flag == True:
    print(1)