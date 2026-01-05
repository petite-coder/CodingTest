def solution(triangle):
    res = []
    
    for row in triangle:
        res = [
            curr + max(left, right)
            for left, right, curr in zip(
                [0] + res,
                res + [0],
                row
            )
        ]
        
    return max(res)


"""
* 동적 계획법(DP)
* zip: 같은 인덱스의 값끼리 튜플 형태로 묶음
    e.g. zip([0, 10, 15], [10, 15, 0], [8, 1, 0])
        [0, 10, 8] -> 첫 번째 인덱스끼리
        [10, 15, 1] -> 두 번째 인덱스끼리
        [15, 0, 0] -> 세 번째 인덱스끼리
        [left, right, curr] 
"""

"""
처음 썼던 코드
def solution(triangle):

    tr_end = len(triangle)-1

    for i, row in enumerate(triangle):
        if i != tr_end:
            triangle[i+1][0] += row[0] 
            triangle[i+1][-1] += row[-1]

        for idx, num in enumerate(row, start=1):
            if i!=0 and idx<len(row)-1:
                c = triangle[i-1][idx-1] 

                d = triangle[i-1][idx] 

                triangle[i][idx] += c if c>d else d

    return max(triangle[-1])
"""
    
      