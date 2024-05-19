Nested loops part 2
==================
Divider 1
------
````ruby
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
````
-----
````ruby
n = int(input())
while n > 9:
    tot = 0
    while n > 0:
        last = n % 10
        tot += last
        n = n//10
    n = tot
print(n)
````
----
````ruby
n = int(input())
tot = 0
for i in range(1, n + 1):
    cnt = 1
    for j in range(1, i + 1):
        cnt = cnt * j
    tot = tot + cnt
   
print(tot)
````
----
