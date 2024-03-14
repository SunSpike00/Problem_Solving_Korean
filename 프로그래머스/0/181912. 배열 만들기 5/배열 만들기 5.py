def solution(intStrs, k, s, l):
    answer = []
    
    intStrs_list = [i[s:s+l] for i in intStrs]
    answer = [int(i) for i in intStrs_list if int(i) > k]
    
    return answer