def solution(x):
    
    str_x = str(x)
    
    div_value = 0
    
    for i in range(len(str_x)):
        div_value += int(str_x[i])
    
    if x % div_value == 0:
        return True
    
    return False