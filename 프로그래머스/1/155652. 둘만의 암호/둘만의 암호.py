def solution(s, skip, index):
    answer = ''
    n = 0
    list_skip = list(skip)
    
    print(list_skip)
    
    for spell in s:
        check_spell = ord(spell)
        while n < index:
            check_spell += 1
            
            if check_spell > 122:
                check_spell = 97
                
            if chr(check_spell) in list_skip:
                continue
            else:
                n += 1
        n = 0
        answer += chr(check_spell)

    return answer