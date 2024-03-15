def solution(my_string, is_suffix):
    answer = 0
    dic = []
    
    for i in range(len(my_string)):
        dic.append(my_string[i:])
    
    for i in dic:
        if i == is_suffix:
            answer += 1
    
    return answer