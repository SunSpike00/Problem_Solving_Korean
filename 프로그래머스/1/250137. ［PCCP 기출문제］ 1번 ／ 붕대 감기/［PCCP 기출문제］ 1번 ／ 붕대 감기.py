from collections import deque

def solution(bandage, health, attacks):
    queue = deque(attacks)
    
    max_health = health
    attack = queue.popleft()
    
    time = 1
    success = 0
    attack_count = 1
    
    while True:
        
        # last attack
        if attack[0] == time and attack_count == len(attacks):
            
            if health - attack[1] <= 0:
                health = -1
                break
            
            health -= attack[1]
            success = 0
            break
            
        # attack
        elif attack[0] == time and attack_count < len(attacks):
            
            if health - attack[1] <= 0:
                health = -1
                break
            
            health -= attack[1]
            success = 0
            attack_count += 1
            attack = queue.popleft()
        
        # normal
        else:
            
            if health + bandage[1] <= max_health:
                health += bandage[1]
            else:
                health = max_health
            
            success += 1
            
            if success == bandage[0]:
                if health + bandage[2] <= max_health:
                    health += bandage[2]
                else:
                    health = max_health
                success = 0
                
        time += 1
    
    return health