def isFire(k,s):
    if(k[0]+k[1]<=s[0] and k[0]+k[2]<=s[1] and k[0]+k[1]+k[2]<=s[2]):
        return 1



def isMax(k,s):
    
    mes=0
    i=k[0]
    j=k[1]
    m=k[2]
    for i in range(k[0],s[0]+1):
        for j in range(k[1],s[1]+1):
            for m in range(k[2],s[2]+1):
                t=isFire([i,j,m],s)
                if(t==1 and [i,j,m]!=k and i>=0 and j>=0 and m>=0):
                    mes=mes+1
                m+=1
                
            m=k[2]   
            t=isFire([i,j,m],s)
            if(t==1 and [i,j,m]!=k and i>=0 and j>=0 and m>=0):
                mes=mes+1
            j+=1
            
        j=k[1]
        t=isFire([i,j,m],s)
        if(t==1 and [i,j,m]!=k and i>=0 and j>=0 and m>=0):
            
            mes=mes+1
        i+=1
    
        
    if(mes==0):
        return 1
        
        

def isequation(k):
    e1=k[0]+k[1]-k[2]+k[3]+k[4]-k[5]+k[6]+k[7]-k[8]
    e2=k[1]-k[2]+k[4]-k[5]+k[7]-k[8]
    e3=k[0]+2*k[1]-2*k[2]+k[3]+2*k[4]-2*k[5]+k[6]+2*k[7]-2*k[8]

    in1=k[0]+k[1]
    in2=k[0]+k[2]
    in3=k[0]+k[1]+k[2]

    in4=k[0]+k[3]+k[4]
    in5=k[2]-k[1]+k[3]+k[5]
    in6=k[0]+k[1]-k[2]+k[3]+k[4]+k[5]

    in7=k[0]+k[3]+k[7]+k[8]
    in8=k[2]-k[0]+k[5]-k[4]+k[6]+k[8]
    in9=k[0]+k[1]-k[2]+k[3]+k[4]-k[5]+k[6]+k[7]+k[8]

    if(e1==0 and e2==0 and e3==0 and in1<=5 and in2<=5 and in3<=5 and in4 <=5 and in5<=5 and in6<=5 and in7 <=5 and in8<=5 and in9<=5):
        return 1

def combine(a,b,c):
    K=[0,0,0,0,0,0,0,0,0]
    for i in range(0,2):
        K[i]=a[i]
        i+=1
    for i in range(0,2):
        K[i+3]=b[i]
    for i in range(0,2):
        K[i+6]=c[i]
    return K

def changeSituation(k,s):
    Snew=[0,0,0]
    Snew[0]=s[0]-k[0]
    Snew[1]=s[1]+k[1]-k[2]
    Snew[2]=s[2]-k[0]-k[1]+k[2]
    return Snew

def find(k,s):
    for k[0] in range(0,5):
        for k[1] in range(0,5):
            for k[2] in range(0,5):
                t=isMax(k,s)
                Snew=S1=changeSituation(k,s)
                if(t==1):
                    return Snew
                k[2]+=1
            k[1]+=1
        k[0]+=1
        



    
k1=[0,0,0]
k2=[0,0,0]
k3=[0,0,0]
S0=[5,5,5]
S1=[5,5,5]
S2=[5,5,5]
S=[5,5,5]
KK=[0,0,0,0,0,0,0,0,0]
exist=0

#from S0 to S1，find the maximal-parallel (k1,k2,k3)
for k1[0] in range(0,5):
    for k1[1] in range(0,5):
        for k1[2] in range(0,5):
 
            t1=isMax(k1,S0)
            S1=changeSituation(k1,S0)
            if(t1==1 and S1>=[0,0,0]):
                
                
                if(S1<[0,0,0]):
                    continue
                
                #from S0 to S1，find he maximal-parallel K
                for k2[0] in range(0,5):
                    for k2[1] in range(0,5):
                        for k2[2] in range(0,5):
                            
                            t2=isMax(k2,S1)
                            S2=changeSituation(k2,S1)
 
                            if(t2==1 and S2>=[0,0,0]):
                                print(S2)
                               
                                #from S2 to S, find the maximal-parallel and check if it is satisfied the equations
                                for k3[0] in range(0,5):
                                    for k3[1] in range(0,5):
                                        for k3[2] in range(0,5):
                                            t2=isMax(k3,S2)
                                            S=changeSituation(k3,S2)

                                            KK=combine(k1,k2,k3)
                                            e=isequation(KK)
                                            if(t2==1 and e==1 and S>=[0,0,0]):
                                                print(KK)
                                                exist+=1
                                                                                           
                                            k3[2]=k3[2]+1
                                        k3[1]=k3[1]+1
                                    k3[0]=k3[0]+1
                            k2[2]=k2[2]+1
                        k2[1]=k2[1]+1
                    k2[1]=k2[1]+1
                    
            k1[2]=k1[2]+1
        k1[1]=k1[1]+1
    k1[0]=k1[0]+1

if(exist>0):
    print('YES')
else:
    print('NO')


        
    

