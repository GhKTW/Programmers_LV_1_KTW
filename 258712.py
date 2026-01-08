def solution(friends, gifts):
    n = len(friends)
    gift = [[0]*n for _ in range(n)]
    idx = {name: i for i, name in enumerate(friends)}
    for g in gifts:
        giver, receiver = g.split()
        gift[idx[giver]][idx[receiver]] += 1
    
    gift_meter = [0]*n
    for i in range(n):
        gift_meter[i] = sum(gift[i]) - sum(gift[j][i] for j in range(n))
    
    next_receive = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if gift[i][j] != gift[j][i]:
                if gift[i][j] > gift[j][i]:
                    next_receive[i] += 1
                else:
                    next_receive[j] += 1
            else:
                if gift_meter[i] > gift_meter[j]:
                    next_receive[i] += 1
                elif gift_meter[i] < gift_meter[j]:
                    next_receive[j] += 1
    
    return max(next_receive)