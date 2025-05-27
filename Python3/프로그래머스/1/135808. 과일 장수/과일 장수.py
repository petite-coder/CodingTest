from collections import deque

def solution(k, m, score):
    # 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score
    # (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수)
    
    lenS = len(score)
    rest = lenS % m 
    
    if lenS / m < 1 : return 0
    
    score.sort()
    score = score[rest:]

    res = 0
    for i in range(0, len(score), m) :
        res += score[i] * m 
    
    return res
    
    