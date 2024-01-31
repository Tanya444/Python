# for i in range(start,endnotincluded,stepsize)
def digsum(n):
    dsum=0
    for i in str(n):
        dsum+=int(i)
    return dsum
list=[123,456,343]
newlist=[digsum(ele) for ele in list if ele & 1]
print(newlist)

if(3 > 1):
    if(20<10):
        print("12")
        if(True):
            print("above condition true")

d=dict()
d['name']='tanya'
d['topic']='python'
for i in d:
    print(i,d[i])    
#continue-beginning of loop, break-out of loop, 
#else block just after for/while is executed only when the loop is NOT terminated by a break statement.
for i in range(1,4):
    if(i==3): 
        break
    print(f"{i}")
else:
    print("no break executed")

#looping techniques in python gfg