def solution(n, w, num):
    answer = 0
    
    boxNum = 1
    dir = 1
    
    maxHeight = n // w + 2
    
    row = 0
    col = 0
    
    list = [[0] * w for _ in range(maxHeight)]
    
    for i in range(maxHeight):
        if boxNum > n:
            break
        
        if dir == 1:
            width = range(w)
        
        else :
            width = range(w - 1, -1, -1) # 이러면 0까지 감
            
        for j in width:
            if boxNum > n:
                break
            list[i][j] = boxNum
            if boxNum == num:
                row = i
                col = j
                
            boxNum += 1
        dir = 1 - dir
    
    for i in range(row, maxHeight):
        if list[i][col] != 0:
            answer += 1
        else:
            break
    return answer