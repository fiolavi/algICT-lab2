import time
import os

t_start = time.perf_counter()
def memory_usage_psutil():
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

f = open("1.csv")
a = []
for i in f.readlines():
    b = i.strip().split(";")
    a.append((b[0], float(b[1])))
c = [0]
for i in range(1, len(a)):
    c.append(a[i][1] - a[i - 1][1])

def sdfsf(a, low, high):
    if low == high:
        return (a[low], low, high)
    mid = (low + high) // 2
    left = sdfsf(a, low, mid)
    right = sdfsf(a, mid + 1, high)
    m = ghghgh(a, low, mid, high)
    if left[0] >= right[0] and left[0] >= m[0]:
        return left
    elif right[0] >= left[0] and right[0] >= m[0]:
        return right
    else:
        return m

def ghghgh(a, low, mid, high):
    l_max = -10**1001
    l_sum = 0
    l_index = 0
    for i in range(mid, low - 1, -1):
        l_sum += a[i]
        if l_sum > l_max:
            l_max = l_sum
            l_index = i
    r_max = -10**1001
    r_sum = 0
    r_index = 0
    for i in range(mid + 1, high + 1):
        r_sum += a[i]
        if r_sum > r_max:
            r_max = r_sum
            r_index = i
    return (l_max + r_max, l_index, r_index)

t = sdfsf(c, 0, len(c) - 1)

mf = open("output.txt", "w+")
mf.write(f'{a[t[1]][0]}, {a[t[2]][0]}, {t[0]}')
mf.close()

print("Время:", time.perf_counter() - t_start)
print("Память:", memory_usage_psutil(), "мб")
f.close()
