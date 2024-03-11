import math
import numpy

def solution(number, limit, power):
    
    # 정수 limit와 제한수치를 초과한 기사가
    # 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때
    
    number_list = []
    tmp_list = []
    
    for x in range(1, number+1):
        for y in range(1, int(math.sqrt(x))+1):
            if x % y == 0:
                tmp_list.append(y)
                
                if x // y != y:
                    tmp_list.append(x // y)
        
        number_list.append(len(tmp_list))
        tmp_list.clear()
    
    np_array = numpy.array(number_list)
    np_array = numpy.where(np_array > limit, power, np_array)
    
    number_list = list(np_array)
    return int(sum(number_list))