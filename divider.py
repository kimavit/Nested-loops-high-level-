a = int(input())
b = int(input())
cnt = 0
max = 0

for i in range(a, b+1):
    total = 0
    for j in range(1, i+1):
        if i % j == 0:
            total += j
        if total >= cnt:
            cnt = total
            max = i
print(max, cnt)
