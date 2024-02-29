def solution(phone_number):
    answer = ''
    
    s = answer.rjust(len(phone_number[:-4]), '*')
    answer = s + phone_number[-4:]
    
    return answer