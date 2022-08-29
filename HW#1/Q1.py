n = int(input())
a, b = input().split()
a, b = [int(a), int(b)]
array = input().split()

count = 0
for i in range(a, b+1):
    if i == b:
        break
    else:
        if array[i] == array[i+1]:
            count += 1

print(count)