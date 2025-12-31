N, M = map(int, input().split())
ans = 0
lamp = []

for i in range(N) :
    lamp.append(input())

K = int(input())
    
for i in range(N) :
    zero_count = 0
    for j in lamp[i] :
        if j == '0' :
            zero_count += 1
    
    same_count = 0
    for k in range(N) :
        if lamp[k] == lamp[i] :
            same_count += 1
    
    if zero_count == K or (zero_count < K and (K - zero_count) % 2 == 0) :
        ans = max (ans, same_count)

print(ans)