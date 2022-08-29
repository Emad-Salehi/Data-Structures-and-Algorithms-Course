from cmath import inf

n = int(input())
inputs = []
min = inf

for i in range(n):
    a, c = input().split()
    a, c = int(a), int(c)

    inputs.append([a, c, i+1])

for i in range(0, n):
    for j in range(i,-1,-1): 
        if ((j != 0) and (inputs[j][0] > inputs[j-1][0]) and (inputs[j][1] != 0)):
            inputs[j][1] -= 1
            t = inputs[j-1]
            inputs[j-1] = inputs[j]
            inputs[j] = t
        
        else:
            break

output = ''
for i in range(n):
    output += str(inputs[i][2]) +' '

print(output)

    