def gcd(a, b):
    r = 0
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

def solution(arr):
    
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    
    return answer




