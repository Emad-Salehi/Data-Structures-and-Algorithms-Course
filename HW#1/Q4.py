dp = [[-1 for i in range(1001)]
          for j in range(1001)]
 
def ispal(s, i, j):
     
    if (i > j):
        return 1
 
    if (dp[i][j] != -1):
        return dp[i][j]
 
    if (s[i] != s[j]):
        dp[i][j] = 0
        return dp[i][j]
         
    dp[i][j] = ispal(s, i + 1, j - 1)
     
    return dp[i][j]

def convert(a, b):
	return str(a) + str(b);

def minpalparti_memo(input, i, j, memo):

	if (i > j):
		return 0
	
	ij = convert(i, j)

	if (ij in memo):
		return memo[ij]
	
	if (i == j):
		memo[ij] = 0
		return 0
	if (ispal(input, i, j)):
		memo[ij] = 0
		return 0
	minimum = 1000000000
	
	for k in range(i, j):
		left_min = 1000000000
		right_min = 1000000000
		left = convert(i, k)
		right = convert(k + 1, j)

		if (left in memo):
			left_min = memo[left]
		
		if (right in memo):
			right_min = memo[right]
		
		if (left_min == 1000000000):
			left_min = minpalparti_memo(input, i, k, memo)
		if (right_min == 1000000000):
			right_min = minpalparti_memo(input, k + 1, j, memo)

		minimum = min(minimum, left_min + 1 + right_min)
	memo[ij] = minimum
	
	return memo[ij]

string = input()
memo = dict()
print(minpalparti_memo(string, 0, len(string) - 1, memo))
	
