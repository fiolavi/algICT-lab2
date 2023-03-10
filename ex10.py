def merge_sort(n):
    if len(n) == 1:
        return n
    mid = len(n) // 2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    if left[-1] <= right[0]:
        return left + right
    return merge_sort_unity(left, right)

def merge_sort_unity(list1, list2):
    unity_list = []
    count1 = 0
    count2 = 0
    while count1 < len(list1) and count2 < len(list2):
        if list1[count1] < list2[count2]:
            unity_list.append(list1[count1])
            count1 += 1
        else:
            unity_list.append(list2[count2])
            count2 += 1
    if count1 < len(list1):
        unity_list += list1[count1:]
    if count2 < len(list2):
        unity_list += list2[count2:]
    return unity_list

f = open("input.txt")
m = int(f.readline())
n = list(map(int, f.readline().split( )))

mf = open("output.txt", "w+")
mf.write(f'{merge_sort(n)} ')
mf.close()
