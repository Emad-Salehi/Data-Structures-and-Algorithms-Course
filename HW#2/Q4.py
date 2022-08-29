n = int(input())
Inputs = []
edge_num = 0
edges = []

for i in range(n):
    d, Xor = input().split()
    d = int(d)
    Xor = int(Xor)
    Inputs.append([i,d,Xor])

if n == 1:
    print('NOT POSSIBLE')
    
else:
    while Inputs != []:
        for node in Inputs:
            if ((node[1] == 0) and ((node[2] == 0))):
                Inputs.remove(node)

            elif node[1] == 1:
                
                edges.append((node[0], node[2]))
                edge_num += 1
                for item in Inputs: 
                    if item[0] == node[2]:
                        item[1] -= 1
                        item[2] = item[2]^node[0]
                        break
                Inputs.remove(node)
            
            if ((node[2] < 0) or (node[1] < 0)):
                print('NOT POSSIBLE')
                exit()
                
    print(edge_num)
    for edge in edges:
        if edge[0] < edge[1]:
            print(edge[0], edge[1])
        else:
            print(edge[1], edge[0])