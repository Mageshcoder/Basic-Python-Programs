def tower(n,frod,trod,arod):
    if n==1:
        print("Move disk 1 from rod",frod,"to rod",trod)
        return
    tower(n-1,frod,arod,trod)
    print("MOve disk ",n,"from rod",frod,"to rod",trod)
    tower(n-1,arod,trod,frod)

n=3
tower(n,'A','C','B')
