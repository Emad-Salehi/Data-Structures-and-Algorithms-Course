def find_answer(b, m):
    unique_b = []
    for k in range(m):
        if b[k] not in unique_b:
            unique_b.append(b[k])
            ind = k

        else:
            continue
    
    #print(ind)

    before_index = 0
    after_index = ind + 1
    while after_index <= m-1:
        
        if b[after_index] == b[before_index]:
            after_index += 1
            before_index += 1

        else:
            ind = after_index - before_index
            after_index = ind + 1
            before_index = 0

        #print('ind', ind)
        #print('before ind', before_index)
        #print('after ind', after_index)
        

    a = b[:ind+1]

    return ind+1, a

t = int(input())
K = []
A = []

for i in range(t):
    m = int(input())
    b = input().split()
    for j in range(m):
        b[j] = int(b[j])

    k, a = find_answer(b, m)

    K.append(k)
    A.append(a)
    
for i in range(len(K)):
    print(K[i])

    print(*A[i])