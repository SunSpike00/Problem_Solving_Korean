def solution(n):
    answer = 0
    
    for num in range(1,n):
        if n%num==1 and answer==0:
            answer = num
        
        if n%num==1 and num<answer:
            answer = num
    
    return answer