def solution(a, b, c, d):

    numbers = [a, b, c, d]
    number_list = [0] * 7
    
    #오름차순 정렬
    for i in numbers:
        number_list[i] += 1
    
    number_count = numbers.count(number_list.index(max(number_list)))
    
    p = a if number_count == 4 else 0
    q = 0
    r = 0
    
    if number_count == 4:
        answer = p * 1111
        
    elif number_count == 3:
        for i in range(len(number_list)):
            if number_list[i] == 3:
                p = i
            
            if number_list[i] == 1:
                q = i
                
        answer = pow(10 * p + q, 2)
        
    elif number_count == 2:
        if 1 in number_list:
            for i in range(len(number_list)):
                if number_list[i] == 1:
                    if q == 0:
                        q = i
                    else:
                        r = i
                    
            answer = q * r
            
        else:
            for i in range(len(number_list)):
                if number_list[i] == 2:
                    if p == 0:
                        p = i
                    else:
                        q = i
                    
            answer = (p + q) * abs(p - q)
        
    else:
        for i in range(len(number_list)):
            if number_list[i] > 0:
                answer = i
                break
        
    return answer