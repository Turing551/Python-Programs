from collections import deque
def initialize():
    q = deque()
    # A
    s = ""
    q.append(['.', '*', '*'])
    q.append(['*', '*', '.'])
    q.append(['.', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'A'
    q.clear()
    #E
    q.append(['*', '*', '*'])
    q.append(['*', '*', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'E'
    q.clear()
    
    #I
    q.append(['*', '.', '*'])
    q.append(['*', '*', '*'])
    q.append(['*', '.', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'I'
    q.clear()
    #O
    q.append(['*', '*', '*'])
    q.append(['*', '.', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'O'
    q.clear()
    #U
    q.append(['*', '*', '*'])
    q.append(['.', '.', '*'])
    q.append(['*', '*', '*'])
    s = ''.join(map(str, q))
    vowels[s] = 'U'
    q.clear()
     return vowels
vowels = {}
vowels = initialize()
n = int(input())
x = []
for i in range(n):
    x.append(['.', '.', '.'])
for i in range(3):
    l = []
    l = list(input())
    for j in range(n):
        x[j][i] = l[j]
    
constellation = ""
star = deque()
for i in range(n):
    if len(star) ==3:
        s = ''.join(map(str, star))
        if s in vowels:
            constellation += vowels[s]
            star.clear()
        else:
            star.popleft()
    if x[i]==['#', '#', '#']: 
        star.clear()
        constellation += '#'
        continue
    star.append(x[i])
if len(star)==3:
    s = ''.join(map(str, star))
    if s in vowels:
        constellation += vowels[s]
        
print(constellation, end="")
