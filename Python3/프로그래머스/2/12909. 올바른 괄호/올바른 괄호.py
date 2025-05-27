def solution(s):
    pair = list()
    
    for brace in s :
        if brace == "(" : pair.append(brace)
        else : 
            try : pair.pop()
            except IndexError :
                return False
    
    return len(pair) == 0
                
    
    
    """
    처음 썼던 코드
    left = 0

    for brace in s :
        if brace == "(" : left += 1
        else : left -= 1
        
        if left < 0 :
            break
        
    
    return left == 0
    """
    
        