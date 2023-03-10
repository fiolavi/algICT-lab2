import time
import os

t_start = time.perf_counter()
def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

def merge(A, list, left, mid, right):
    count = i = left
    j = mid + 1
    inversCount = 0
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            list[count] = A[i]
            i = i + 1
        else:
            list[count] = A[j]
            j = j + 1
            inversCount += (mid - i + 1)
        count = count + 1
    while i <= mid:
        list[count] = A[i]
        count = count + 1
        i = i + 1
    for i in range(left, right + 1):
        A[i] = list[i]
    return inversCount
def mergesort(A, list, left, right):
    if right <= left:
        return 0
    mid = left + ((right - left) // 2)
    inversCount = 0
    inversCount += mergesort(A, list, left, mid)
    inversCount += mergesort(A, list, mid + 1, right)
    inversCount += merge(A, list, left, mid, right)
    return inversCount

f = open("input.txt")
m = int(f.readline())
A = list(map(int, f.readline().split( )))
list = A.copy()

result = mergesort(A, list, 0, len(A) - 1)
mf = open("output.txt", "w+")
mf.write(f'{result} ')
mf.close()

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")
f.close()
