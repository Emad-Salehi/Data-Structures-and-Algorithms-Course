def condition_checker(ind, arr):
    diff1 = abs(arr[ind-1][0]-arr[ind][0])
    diff2 = abs(arr[ind-1][2]-arr[ind][2])
    return diff1, diff2

n = int(input())
a, b = input().split(), input().split()
output = [[]]*n
counter = 1
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

for i in range(n):
    output[i] = [a[i] , i + 1 , b[i]]
output.sort()

while (counter < len(output)):

    D1, D2 = condition_checker(counter, output)

    if D1 > D2:
        output.remove(output[counter])
        
    else:
        counter += 1

print(len(output))