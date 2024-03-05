def solution(data, ext, val_ext, sort_by):
    answer = []
    
    # ext 정보의 기준
    # val_ext 뽑아낼 정보의 기준 값
    # sort_by 정렬할 기준의 문자열
    
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑아서 sort_by에 해당하는 값을 기준으로 오름차순 정렬
    
    for code, date, maximum, remain in data:
        
        if ext == "code":
            if code < val_ext:
                answer.append([code, date, maximum, remain])
                
        elif ext == "date":
            if date < val_ext:
                answer.append([code, date, maximum, remain])
                
        elif ext == "maximum":
            if maximum < val_ext:
                answer.append([code, date, maximum, remain])
                
        elif ext == "remain":
            if remain < val_ext:
                answer.append([code, date, maximum, remain])
    
    if sort_by == "code":
        answer.sort(key=lambda x:x[0])
    elif sort_by == "date":
        answer.sort(key=lambda x:x[1])
    elif sort_by == "maximum":
        answer.sort(key=lambda x:x[2])    
    elif sort_by == "remain":
        answer.sort(key=lambda x:x[3])
    
    return answer