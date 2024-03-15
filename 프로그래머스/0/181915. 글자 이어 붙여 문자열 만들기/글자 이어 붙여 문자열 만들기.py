def solution(my_string, index_list):
    answer = ''
    text_list = []
    for i in range(len(index_list)):
        text_list.append(my_string[index_list[i]])
    
    answer = "".join(text_list)
    
    return answer