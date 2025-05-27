def solution(s):
    if s[0] == ")" : return False
    
    left = 0

    for brace in s :
        if brace == "(" : left += 1
        else : left -= 1
        
        if left < 0 :
            break
        
    
    return left == 0
    
    
        