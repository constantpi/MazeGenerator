import random
from copy import deepcopy
from collections import deque
def CanGo(i,j):
    ans=[]
    for k in range(4):
        x=hoko[k][0]
        y=hoko[k][1]
        if(maze[i+x][j+y]+maze[i+2*x][j+2*y]==2):
            ans.append(k)
    return ans

def BlankList():
    ans=[]
    for i in range(1,m):
        for j in range(1,m):
            if(maze[i*2][j*2]):
                continue
            ans.append([i*2,j*2])
    return ans

def Dig(basho):
    i=basho[0]
    j=basho[1]
    cango=CanGo(i,j)
    if(len(cango)==0):
        return
    go=hoko[random.choice(cango)]
    for k in range(2):
        i+=go[0]
        j+=go[1]
        maze[i][j]=0
    Dig([i,j])

def CanDig():
    blank=BlankList()
    ans=[]
    for b in blank:
        if(len(CanGo(b[0],b[1]))):
            ans.append(b)
    return ans

m=5
n=2*m+1

maze=[[1]*n for i in range(n)]
hoko=[[0,1],[-1,0],[0,-1],[1,0]]
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i+1==n or j+1==n):
            maze[i][j]=0
maze[2][2]=0

for i in range(n*n):

    candig=CanDig()
    if(len(candig)==0):
        break
    Dig(random.choice(candig))

for ma in maze:
    print(ma)
Maze=[]
print()
for ma in maze[1:n-1]:
    Maze.append(ma[1:n-1])

for ma in Maze:
    for block in ma:
        if(block):
            print("#",end="")
        else:
            print(" ",end="")
    print()

solveMaze=deepcopy(maze)
d=deque()
d.append([2,2])
solveMaze[2][2]=10
while(len(d)):
    now=d.popleft()
    i=now[0]
    j=now[1]
    for k in range(4):
        x=hoko[k][0]
        y=hoko[k][1]
        if(maze[i+x][j+y]+maze[i+2*x][j+2*y]):
            continue
        if(solveMaze[i+2*x][j+2*y]):
            continue
        d.append([i+2*x,j+2*y])
        solveMaze[i+2*x][j+2*y]=solveMaze[i][j]+1

answerPath=[[n-3,n-3]]
i=n-3
j=n-3
for t in range(n*n):
    if(solveMaze[i][j]==10):
        break
    for k in range(4):
        x=hoko[k][0]
        y=hoko[k][1]
        if(solveMaze[i+x*2][j+y*2]==solveMaze[i][j]-1):
            answerPath.append([i+x,j+y])
            answerPath.append([i+x*2,j+y*2])
            i+=x*2
            j+=y*2

answerPath.reverse()

for ma in solveMaze:
    print(ma)
for ans in answerPath:
    print(ans)
