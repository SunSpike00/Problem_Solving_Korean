def solution(n):
    
    tmp = 0
    num = 1
    answer = 1
    
    if n == 3:
        return 2
    
    while num <= n:

        for i in range(num, n):
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
            else:
                tmp += i

        num += 1
        tmp = 0
    
    return answer