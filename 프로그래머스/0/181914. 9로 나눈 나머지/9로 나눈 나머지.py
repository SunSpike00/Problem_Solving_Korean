def solution(number):
    answer = 0
    
    number_list = list(map(int, number))
    answer = sum(number_list) % 9
    
    
    return answer