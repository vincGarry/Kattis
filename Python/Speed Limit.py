a=1
while(a>0):
    b = []
    total=0
    a=int(input())
    if(a<0):
        break
    for x in range(a):
        c=input().split()
        d=int(c[0])
        e=int(c[1])
        b.append(e)
        if(x==0):
            total= total+(d*e)
        else : total = total+(d*(e-b[x-1]))
    print(str(total)+" miles")