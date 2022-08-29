from cmath import inf
MAX_VAL = 1000001

def update(i, add, BIT):
    while (i > 0 and i < len(BIT)):
        BIT[i] += add
        i = i + (i & (-i))

def sum(i, BIT):
	ans = 0
	while (i > 0):
		ans += BIT[i]
		i = i - (i & (-i))
	return ans

def insertElement(x, BIT):
	update(x, 1, BIT)

def deleteElement(x, BIT):
	update(x, -1, BIT)

def findRank(x, BIT):
	return sum(x, BIT)

BIT = [0]*MAX_VAL

num = int(input())
output = []
min_key = inf

for i in range(num):
    user_input = input()
    if user_input[0] == '?':
        key1, key2 = user_input[2], user_input[4]
        key1 = int(key1)
        key2 = int(key2)
        if key1 == min_key:
            output.append(findRank(key2, BIT))
        else:
            output.append(findRank(key2, BIT) - findRank(key1, BIT))

    elif user_input[0] == '+':
        key = user_input[2]
        key = int(key)
        if key < min_key:
            min_key = key
        insertElement(key, BIT)

    else:
        key = user_input[2]
        key = int(key)
        deleteElement(key, BIT)

for i in output:
    print(i)
