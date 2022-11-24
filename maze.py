import random
from copy import deepcopy
from collections import deque

class MazeGen:
    def __init__(self,m):
        self.m=m
        self.n=2*self.m+1

        self.maze=[[1]*self.n for i in range(self.n)]
        self.hoko=[[0,1],[-1,0],[0,-1],[1,0]]
        for i in range(self.n):
            for j in range(self.n):
                if(i==0 or j==0 or i+1==self.n or j+1==self.n):
                    self.maze[i][j]=0
        self.maze[2][2]=0

        self.answerPath=[]
    
    def CanDigDirection(self,i,j):
        ans=[]
        for k in range(4):
            x=self.hoko[k][0]
            y=self.hoko[k][1]
            if(self.maze[i+x][j+y]+self.maze[i+2*x][j+2*y]==2):
                ans.append(k)
        return ans

    def BlankList(self):
        ans=[]
        for i in range(1,self.m):
            for j in range(1,self.m):
                if(self.maze[i*2][j*2]):
                    continue
                ans.append([i*2,j*2])
        return ans

    def Dig(self,basho):
        i=basho[0]
        j=basho[1]
        cango=self.CanDigDirection(i,j)
        if(len(cango)==0):
            return
        go=self.hoko[random.choice(cango)]
        for k in range(2):
            i+=go[0]
            j+=go[1]
            self.maze[i][j]=0
        self.Dig([i,j])

    def CanDig(self):
        blank=self.BlankList()
        ans=[]
        for b in blank:
            if(len(self.CanDigDirection(b[0],b[1]))):
                ans.append(b)
        return ans


    def Generate(self):
        for i in range(self.n*self.n):

            candig=self.CanDig()
            if(len(candig)==0):
                break
            self.Dig(random.choice(candig))

    
    # Maze=[]
    # print()
    # for ma in maze[1:n-1]:
    #     Maze.append(ma[1:n-1])

    # for ma in Maze:
    #     for block in ma:
    #         if(block):
    #             print("#",end="")
    #         else:
    #             print(" ",end="")
    #     print()

    def Solve(self):
        solveMaze=deepcopy(self.maze)
        d=deque()
        d.append([2,2])
        solveMaze[2][2]=10
        while(len(d)):
            now=d.popleft()
            i=now[0]
            j=now[1]
            for k in range(4):
                x=self.hoko[k][0]
                y=self.hoko[k][1]
                if(self.maze[i+x][j+y]+self.maze[i+2*x][j+2*y]):
                    continue
                if(solveMaze[i+2*x][j+2*y]):
                    continue
                d.append([i+2*x,j+2*y])
                solveMaze[i+2*x][j+2*y]=solveMaze[i][j]+1

        
        i=self.n-3
        j=self.n-3
        self.answerPath.append([i,j])
        for t in range(self.n**2):
            if(solveMaze[i][j]==10):
                break
            for k in range(4):
                x=self.hoko[k][0]
                y=self.hoko[k][1]
                if(self.maze[i+x][j+y]+self.maze[i+2*x][j+2*y]):
                    continue
                if(solveMaze[i+x*2][j+y*2]==solveMaze[i][j]-1):
                    self.answerPath.append([i+x,j+y])
                    self.answerPath.append([i+x*2,j+y*2])
                    i+=x*2
                    j+=y*2

        self.answerPath.reverse()

    def __str__(self):
        moji=""
        for i in range(self.n):
            for j in range(self.n):
                if(self.maze[i][j]==1):
                    moji+="#"
                else:
                    moji+=" "
            moji+="\n"
        return moji


if(__name__=="__main__"):
    mazegen=MazeGen(20)
    mazegen.Generate()
    # mazegen.maze=[[0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,0],[0,1,0,1,0,1,0,0,0,1,0],[0,1,0,1,0,1,0,1,0,1,0],[0,1,0,1,0,0,0,1,0,1,0],[0,1,0,1,1,1,1,1,0,1,0],[0,1,0,1,0,0,0,0,0,1,0],[0,1,0,1,0,1,0,1,1,1,0],[0,1,0,0,0,1,0,0,0,1,0],[0,1,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0]]
    mazegen.Solve()
    print(mazegen)
    ans=mazegen.answerPath
    maze=mazegen.maze
    for ma in maze:
        print(ma)
    for a in ans:
        maze[a[0]][a[1]]=2
    print()
    for ma in maze:
        print(ma)
    for i in range(mazegen.n):
        for j in range(mazegen.n):
            if(maze[i][j]==1):
                print("#",end="")
            elif(maze[i][j]==2):
                print(".",end="")
            else:
                print(" ",end="")
        print()