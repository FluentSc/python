def pr(a):
    res=[]
    tem=[]
    while a!=0:
        tem.append(a%10)
        a=a//10
    tem_sum=0
    for i in tem:
        tem_sum+=i
    while tem_sum!=0:
        res.append(tem_sum%10)
        tem_sum=tem_sum//10
    res=res[::-1]
    return res

a=int(input())
a=pr(a)
PinYin=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
for i in range(len(a)):
    a[i]=PinYin[a[i]]
for i in range(len(a)-1):
    print(a[i],end=' ')
print(a[len(a)-1],end='')