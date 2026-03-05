src = [1,2] 
pvt = []
dst = []


steps = 0;
def hanoi(s, p, d):

    global steps
    global src
    global pvt
    global dst
    steps += 1;

    if len(s) == 0: 
        return

    hanoi(d,s,p)
    d.insert( 0, s.pop(0) )
    print(steps) 
    print(src)
    print(pvt)
    print(dst)  
    hanoi(p,s,d) 

while len(src) > 0:
    hanoi(src,pvt,dst)

print(src)
print(pvt)
print(dst)
print(steps)   
