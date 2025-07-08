def solution(record):
    answer = []
    users = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    for i in range(len(record)):
        record[i] = record[i].split()
    
    for rc in record:
        cmd, uid = rc[0], rc[1]
        
        if cmd in ("Enter", "Change"):
            users[uid] = rc[2]
    
    for rc in record:
        if not rc[0] == "Change": 
            answer.append(users[rc[1]] + printer[rc[0]] )

    return answer


''' 첫 풀이
def solution(record):
    answer = []
    users = {}
    lines = []
    
    for rc in record:
        splited = rc.split()
        cmd, uid = splited[0], splited[1]
        
        if cmd in ("Enter", "Change"):
            users[uid] = splited[2]
        
        if cmd == "Enter":
            lines.append([uid,"들어왔습니다."]) 
        elif cmd == "Leave":
            lines.append([uid,"나갔습니다."]) 
    
    for uid, cmd in lines:
        answer.append(users[uid] + "님이 " + cmd)
     
    return answer
'''