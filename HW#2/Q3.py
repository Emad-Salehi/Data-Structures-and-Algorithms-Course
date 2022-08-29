def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def findFirstOccurrence(nums, target):
    (left, right) = (0, len(nums) - 1)

    result = -1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            right = mid - 1

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return result

n, t = input().split()
n, t = int(n), int(t)

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

Nums = []
for i in range(t):
    x, y = input().split()
    Nums.append((int(x),int(y)))

sorted_nums = a[:]
mergeSort(sorted_nums)

dic_repetition = {}
new_a = []
for i in a:
    if i in dic_repetition:
        dic_repetition[i] += 1
    
    else:
        dic_repetition[i] = 1
    
    new_a.append((i, dic_repetition[i]))

    
def calc_f(num):
    a_x = new_a[num - 1][0]
    ith_itter = new_a[num - 1][1]

    index = findFirstOccurrence(sorted_nums, a_x)

    return index + ith_itter
    

for num in Nums:
    print(calc_f(num[0]), calc_f(num[1]))


    