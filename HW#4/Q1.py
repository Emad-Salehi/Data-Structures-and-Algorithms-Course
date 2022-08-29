def findDandZeros(a, b, n):
	mpp = {}
	count = 0

	for i in range(n):

		if (b[i] != 0 and a[i] != 0):
			val = (-1.0 * b[i]) / a[i]
			
			if val not in mpp:
				mpp[val] = 0
				
			mpp[val] += 1

		elif (b[i] == 0 and a[i] == 0):
			count += 1

	maxi = 0
	for item in mpp:
		maxi = max(mpp[item], maxi)

	for keys, values in mpp.items():
		if (values == maxi):
			break
	print(mpp)
	return maxi + count

n = int(input())
a, b = [], []

a = input().split()
b = input().split()

for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

print(findDandZeros(a, b, n))

