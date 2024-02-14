def solution(my_string, queries):
    answer = ''
    
    for x in range(len(queries)):
        sub_querie = queries[x]
        
        start = sub_querie[0]
        end = sub_querie[1]
        
        front = my_string[0:start]
        mid = my_string[start:end+1]
        back = my_string[end+1:]
        
        mid = mid[::-1]
        
        my_string = front + mid + back
        
    return my_string