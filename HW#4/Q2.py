n, m = input().split()
n, m = int(n), int(m)

A = input().split()
B = input().split()

A_hashed = [0]*n
B_hashed = [0]*m

for i in range(n):
    if i==0:
        A_hashed[i] = hash(A[i])
    else:
        A_hashed[i] = A_hashed[i-1] + hash(A[i])

for i in range(m):
    if i==0:
        B_hashed[i] = hash(B[i])
    else:
        B_hashed[i] = B_hashed[i-1] + hash(B[i])

q = int(input())
querys = []
for i in range(q):
    l, s, t, m = input().split()
    l, s, t, m = int(l), int(s), int(t), int(m)
    querys.append([l,s,t,m])

for query in querys:
    l, s, t, m = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    if (l==0 and t!=0):
        if (A_hashed[s]==(B_hashed[m]-B_hashed[t-1])):
            print('YES')

        else:
            print('NO')

    elif (l!=0 and t==0):
        if ((A_hashed[s]-A_hashed[l-1])==B_hashed[m]):
            print('YES')

        else:
            print('NO')

    elif (l==0 and t==0):
        if (A_hashed[s]==B_hashed[m]):
            print('YES')

        else:
            print('NO')
    
    else:
        if ((A_hashed[s]-A_hashed[l-1])==(B_hashed[m]-B_hashed[t-1])):
            print('YES')

        else:
            print('NO')