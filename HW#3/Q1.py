maxn = 10000000
max_elem = 100000

segmentTree = [0 for i in range(maxn)]

def update(node, a, b, x, diff):
	global segmentTree

	if (a == b and a == x ):

		segmentTree[node] += diff
		return

	if (x >= a and x <= b):

		update(node * 2, a, (a + b)//2, x, diff)
		update(node * 2 + 1, (a + b)//2 + 1, b, x, diff)

		segmentTree[node] = segmentTree[node * 2] + segmentTree[node * 2 + 1]

def findKth(node, a, b, k):
	global segmentTree

	if (a != b):

		if (segmentTree[node * 2] >= k):
			return findKth(node * 2, a, (a + b)//2, k)

		return findKth(node * 2 + 1, (a + b)//2 + 1,
					b, k - segmentTree[node * 2])

	return a if (segmentTree[node]) else -1

def insert(x):
	update(1, 0, max_elem, x, 1)

def delete(x):
	update(1, 0, max_elem, x, -1)

def median():
	k = (segmentTree[1] + 1) // 2
	return findKth(1, 0, max_elem, k)

num = int(input())
output = []
for i in range(num):
    sign, key = input().split()
    key = int(key)

    if sign=='+':
        insert(key)
    
    else:
        delete(key)

    output.append(median())

for i in range(num):
    print(output[i])