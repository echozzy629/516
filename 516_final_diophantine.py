
#compute Cmax of equation (1)
def computeCmax(C1,C2,C3,C):

    cmax=0
    for d1 in range(0,2):
        for d2 in range(0,2):
            for d3 in range(0,2):
                for d in range(0,2):
                    ctotal=C1*d1+C2*d2+C3*d3+d
                    cabs=abs(ctotal)
                    if(cabs>cmax):
                        cmax=cabs
                    
                    d=d+1
                d3=d3+1
            d2=d2+1
        d1=d1+1

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
    
    return res[i-1]


#for the input, state is [carry,i], a is(a1,a2,a3), and C is the coefficient of (1)
def isMoveState(state,a,Coefficient):
    #coefficient of equation (1)
    C1=Coefficient[0]
    C2=Coefficient[1]
    C3=Coefficient[2]
    C=Coefficient[3]
    
    #newstate is [carry',i']
    newstate=state
    newCarry=newstate[0]
    newi=newstate[1]
    #carry is bounded
    carry=state[0]
    Cmax=computeCmax(C1,C2,C3,C)
    Cmin=0-Cmax
    #get the present state [carry,i], and corresponding kc and bi
    i=state[1]
    kc=returnKc(C)
    bi=returnbi(C,i)
    #get the instruction (a1,a2,a4)
    a1=a[0]
    a2=a[1]
    a3=a[2]

    
    R=C1*a1+C2*a2+C3*a3+bi+carry
    #only when R is divisble by 2, and both carry and carry' are in bounded, the transition can happen
    if(R%2==0):
        newCarry=R//2
        if(newCarry>=Cmin and newCarry<=Cmax):
            if(i>=0 and i<=kc):
               newi=i+1
            else:
               newi=i
            

    newstate[0]=newCarry
    newstate[1]=newi
    
    return newstate

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


def FAM(cofficient,Minitial,Mfinal):
    #coefficient of equation (1)
    C1=Coefficient[0]
    C2=Coefficient[1]
    C3=Coefficient[2]
    C=Coefficient[3]

    input=[]
    A=createalphabet()
    la=len(A)

    kc=returnKc(C)
    M0=Minitial
    Maccept=Mfinal
    round=0

    while(M0!=Maccept):
        round+=1
        input.append(alphabet[random.choice(range(8))])
        i=len(input)
        A=input[i-1]
        M0=isMoveState(M0,A,coefficient)
        
            
        
    

#============================== Algorithm 1 =================================
coefficient=(-3,0,4,17)

input=[]
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

l=len(alphabet)

kc=returnKc(17)
M0=[0,1]
Maccept=[0,kc+1]
    
round=0
while(M0!=Maccept):
    round+=1
    #print('=================Round %d=================' %round)
    
    input.append(alphabet[random.choice(range(8))])
    i=len(input)
    A=input[i-1]
    M0=isMoveState(M0,A,coefficient)

#print(input)

    
    

#============================== Algorithm 2 =================================
Ma=[0,6]
order=[]
while(M0!=Ma):
    order.append(M0)
    print(order)
    child=getchild(M0,node,edge)
    lc=len(child)
    index2=child[random.choice(range(lc))]
    node2=node[index2]
    checkvisit=isvisited(index2,order,node)
    if(checkvisit==0):
        M0=node2
 #       M0=isMoveState(M0,A,coeddicient)
    
print(order)






E1=(3,-2,1,5)
Maccept=[0,3]
node,edge,ln=createGraph(E1)
s0=getindex(M0,node)
list1=M(E1,M0,Maccept)
l1=len(list1)
       
E2=(6,-4,2,9)
Maccept=[0,4]
node,edge,ln=createGraph(E1)
s0=getindex(M0,node)
list2=M(E2,M0,Maccept)

if(list1==None or list2==None):
    print('No answer')
else:
    for i in range(l1-1):
        for j in range(i+1,i+2):
           i1=list1[i]
           i2=list1[j]
            
    for i in range(l-1):
        for j in range(i+1,i+2):
           i1=list[i]
           i2=list[j]
















