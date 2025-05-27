def solution(s):
    if s[0] == ")" : return False
    
    left = 0

    for brace in s :
        if brace == "(" : left = left+1
        else : left = left-1
        
        if left < 0 :
            return False
        
        
    if left != 0 : return False
    else : return True
    
    
        