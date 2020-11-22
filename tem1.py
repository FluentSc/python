
def Callatz(n):
    res=0
    tem=[]
    
    while n!=1:
        if n%2==0:
            n=int(n/2)
        else:
            n=int((3*n+1)/2)
        res+=1
        tem.append(n)
    #print(tem)
    return tem

ns=input("s--: ").split(' ')

nc=[]
for i in range(len(ns)):
    ns[i]=int(ns[i])
    nc.append(Callatz(ns[i]))

res=[]

for i in range(len(ns)):
    tem_nc=nc[:]
    tem_nc.pop(i)
    tem_nch=[]
    for j in tem_nc:
        for k in j:
            if k not in tem_nch:
                tem_nch.append(k)
    if ns[i] not in tem_nch:
        res.append(ns[i])
print(res)