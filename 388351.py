def solution(schedules, timelogs, startday):
    answer = 0
    startday -= 1
    sat = (5 - startday) % 7
    sun = (6 - startday) % 7
    
    for i in range(len(schedules)):
        schedules[i] += 10
        if (schedules[i] % 100) >= 60:
            schedules[i] = schedules[i] + 100 - 60
    
    for i in range(len(schedules)):
        success = 1
        for j in range(7):
            if time_cal(timelogs[i][j], schedules[i]) > 0:
                if (j != sat and j != sun):
                    success = 0
                    break
        if success == 1:
            answer += 1
        
    return answer

def time_cal(num1, num2):
    num1_h = num1 // 100
    num2_h = num2 // 100
    num1_m = num1 % 100
    num2_m = num2 % 100
    
    ans_h = num1_h - num2_h
    ans_m = 0
    if (num1_m - num2_m < 0) :
        ans_h = ans_h - 1
        ans_m = 60 + (num1_m - num2_m)
    else: 
        ans_m = num1_m - num2_m
        
    return ans_h * 60 + ans_m