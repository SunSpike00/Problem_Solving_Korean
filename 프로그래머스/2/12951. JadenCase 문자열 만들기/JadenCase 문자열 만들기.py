def solution(s):
    a = list(s.lower().title())
    
    for i in range(len(a)):
        if a[i].isdigit():
            if not a[i+1].isdigit():
                a[i+1] = a[i+1].lower()
    
    return ''.join(a)