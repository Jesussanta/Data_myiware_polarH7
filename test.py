person= []
n = [2484,2839,4491,5492,5802,8862,9876,10970]

for t in range (len (n)):
    l=[]
    z=n[t]
    for i in range(7):        
        x=z+i*31
        l.append(x)
    person.append(l)
    print(l)

