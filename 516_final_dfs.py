import random
class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0:
                    count += 1
        return count

    def insert_node(self):
        for i in range(len(self.maps)):
            self.maps[i].append(-1)
        self.maps.append([-1]*(self.nodenum) + [0])
        self.nodenum += 1

    def insert_edge(self, x, y, weight):
        if x < 0 or x >= self.nodenum or y < 0 or y > self.nodenum or weight <= 0 or x == y:
            return
        else:
            self.maps[x][y] = self.maps[y][x] = weight
            self.edgenum += 1
   
    def depth_first_search(self):
        res = []
        visited = [False]*self.nodenum
        def dfs(i):
            res.append(i)
            visited[i] = True
            for j in range(self.nodenum):
                if self.maps[i][j] > 0 and visited[j] == False:
                    dfs(j)
                    
        if self.nodenum > 0:
            dfs(s0)

        return res


#compute Cmax of equation (1)
def computeCmax(Coefficient):
    C1=Coefficient[0]
    C2=Coefficient[1]
    C3=Coefficient[2]
    C=Coefficient[3]
    cmax=0
    for d1 in range(0,2):
        for d2 in range(0,2):
            for d3 in range(0,2):
                for d in range(0,2):
                    ctotal=C1*d1+C2*d2+C3*d3+d
                    cabs=abs(ctotal)
                    if(cabs>cmax):
                        cmax=cabs

    return(cmax)

#input a number C, translate it into binary digit, and output the length of the new 2-digit number
def returnKc(number):

    C=int(number)
    res=[]
    while(C!=0):
        quotient=C//2
        remainder=C%2
        res.append(remainder)
        C=quotient
        
    Kc=len(res)
    res.reverse()
    
    return Kc


#translate C into 2-digit form, and output the i-digit bumber of C
def returnbi(number,i):

    C=int(number)
    res=[]
    while(C!=0):
        quotient=C//2
        remainder=C%2
        res.append(remainder)
        C=quotient

    res.append(0)
    res.reverse()
    ser=res[i-1]
    return ser


#for the input, state is [carry,i], a is(a1,a2,a3), and C is the coefficient of (1)
def isMoveState(state,a,Coefficient):
    #coefficient of equation (1)
    C1=Coefficient[0]
    C2=Coefficient[1]
    C3=Coefficient[2]
    C=Coefficient[3]

    node1=state
    node2=[0,0]
    #newstate is [carry',i']
    Cmax=computeCmax(Coefficient)
    Cmin=0-Cmax
    #get the present state [carry,i], and corresponding kc and bi
    i=node1[1]
    kc=returnKc(C)
    bi=returnbi(C,i)
    #get the instruction (a1,a2,a3)
    a1=a[0]
    a2=a[1]
    a3=a[2]
    
    R=C1*a1+C2*a2+C3*a3+bi+node1[0]
    #only when R is divisble by 2, and both carry and carry' are in bounded, the transition can happen
    if(R%2==0):
        node2[0]=R//2
        
        if(node2[0]>=Cmin and node2[0]<=Cmax):
            if(i>=0 and i<=kc):
               node2[1]=node1[1]+1
               
            else:
               node2[1]=node1[0]              
    else:
        node2=node1
    
    return(node1,node2,a)


def createalphabet():
    alphabet=[]
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                tup=(i,j,k)
                alphabet.append(tup)
                k=k+1
            k=0
            j=j+1
        j=0
        i=i+1
    return alphabet

def canmove(node1,node2,Coefficient):
    alpha=createalphabet()
    la=len(alpha)
    A=[]
    for i in range(la):
        node1,newstate,a=isMoveState(node1,alpha[i],Coefficient)
        if(newstate==node2):
            A.append(a)
    return(A)

def createGraph(coefficient):
    kc=returnKc(coefficient[3])
    cmax=computeCmax(coefficient)
    imax=kc+1
    cmin=0-cmax
    node=[]
    edge=[]
    for i in range(cmin,cmax+1):
        for j in range(1,imax+1):
            tup=[i,j]
            node.append(tup)
    ln=len(node)
    for i in range(ln):
        edge.append([[]]*ln)
    for i in range(ln):
        for j in range(ln):
            if(i!=j):
                edge[i][j]=canmove(node[i],node[j],coefficient)
    return(node,edge,ln)
    

def getindex(state,node):
    l=len(node)
    for i in range(l):
        if(node[i]==state):
            return i
        
def checkinornot(list,node):
    l=len(list)
    for i in range(l):
        if(list[i]==node):
            return 1
        
def getchild(node1,node,edge):
    ln=len(node)
    index=getindex(node1,node)
    total=edge[index]
    child=[]
    for i in range(ln):
        if(total[i]!=[]):
            child.append(i)
    return child

def M(coefficient,M0,Maccept):
    node,edge,ln=createGraph(coefficient)
    E=[]
    N=[]
    walk=[]
    list=[]
    s0=getindex(M0,node)
    sf=getindex(Maccept,node)
    for i in range(ln):
        E.append([0]*ln)

    for i in range(ln):
        for j in range(ln):
            if(edge[i][j]!=[]):
                E[i][j]=1

    for i in range(ln):
        N.append(i)
    graph=Graph(E)
    walk=graph.depth_first_search()
    lw=len(walk)
    infinish=0
    for i in range(lw):
        if(walk[i]==sf):
            infinish=i
            
    walk2=[]

    for i in range(infinish+1):
        walk2.append(walk[i])
    lw2=len(walk2)
    if(lw2==1):
        return None
    else:
        return(N,E)    
    for i in range(lw2):
        index=walk2[i]
        index2=walk[i+1]
        list.append(node[index])

def isvisited(number,visit,node):
    l=len(visit)
    for i in range(l):
        if(visit[i]==node[number]):
            return 1
        else:
            return 0

    
#=================================Algorithm 1 =======================

coefficient=(-3,0,4,17)
M0=[0,1]
Maccept=[0,6]
node,edge,ln=createGraph(coefficient)
s0=getindex(M0,node)
N,E=M(coefficient,M0,Maccept)

list=M(coefficient,M0,Maccept)
print(list)
l=len(list)
print(l)

for i in range(l-1):
    for j in range(i+1,i+2):
        i1=list[i]
        i2=list[j]
        print(edge[i1][i2])


M0=[0,1]
dict={}
for i in range(ln):
    dict[N[i]]=[E[i]]
print(dict)











    

























    


