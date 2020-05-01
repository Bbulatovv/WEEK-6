class Participants:
    score = 0
    secondName = ''
par = []

N = int(input())

for i in range(N):
    properties = list(input().split())
    p = Participants()
    p.secondName = properties[0]
    p.points = int(properties[1])
    par.append(p)
    
par.sort(key=lambda part: -part.points)

for p in par:
    print(p.secondName)
