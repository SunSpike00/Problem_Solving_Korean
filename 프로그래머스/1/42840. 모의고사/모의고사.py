def solution(answers):
    
    answer_trio = {i : 0 for i in range(1, 4)}
    answer_patter = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    player_one = 0
    player_two = 0
    player_three = 0

    for answer in answers:

        if answer_patter[0][player_one] == answer:
            answer_trio[1] += 1

        if answer_patter[1][player_two] == answer:
            answer_trio[2] += 1

        if answer_patter[2][player_three] == answer:
            answer_trio[3] += 1

        player_one += 1
        player_two += 1
        player_three += 1

        if player_one == len(answer_patter[0]):
            player_one = 0

        if player_two == len(answer_patter[1]):
            player_two = 0

        if player_three == len(answer_patter[2]):
            player_three = 0
    
    return [key for key, value in answer_trio.items() if value == max(answer_trio.values())]
