from cmath import inf


n = int(input())

Arr1 = input().split()
for i in range(len(Arr1)):
    Arr1[i] = int(Arr1[i])

Arr2 = input().split()
for i in range(len(Arr2)):
    Arr2[i] = int(Arr2[i])

Arr3 = input().split()
for i in range(len(Arr3)):
    Arr3[i] = int(Arr3[i])

Arr1.sort()
Arr2.sort()
Arr3.sort()

final_lst = []
final_lst.append(Arr1[0])
final_lst.append(Arr2[0])
final_lst.append(Arr3[0])

all_lists = []

while ((Arr1 != []) and (Arr2 != []) and (Arr3 != [])):
    local_mininum = min(final_lst)

    all_lists.append(final_lst[:])

    if final_lst[0] == local_mininum:
        Arr1.remove(local_mininum)
        if Arr1 != []:
            final_lst[0] = Arr1[0]
        else:
            break

    elif final_lst[1] == local_mininum:
        Arr2.remove(local_mininum)
        if Arr2 != []:
            final_lst[1] = Arr2[0]
        else:
            break

    else:
        Arr3.remove(local_mininum)
        if Arr3 != []:
            final_lst[2] = Arr3[0]
        else:
            break

min_dis = inf
final = []
for lst in all_lists:
    diff = max(lst) - min(lst)
    if diff < min_dis:
        min_dis = diff

for lst in all_lists:
    diff = max(lst) - min(lst)
    if min_dis == diff:
        final.append(lst[:])

min_value = inf
if len(final) == 1:
    print(sum(final[0]))

else:
    for lst in final:
        new_value = lst[2]
        if new_value < min_value:
            min_value = new_value
            the_final_list = lst

    print(sum(the_final_list))


