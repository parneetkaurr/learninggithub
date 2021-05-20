def Q2_moveTower(n,source,destination,temp):
    if n>=1:
           Q2_moveTower(n-1,source,temp,destination)
           Q2_moveDisk(n-1,source,destination)
           Q2_moveTower(n-1,temp,destination,source)

def Q2_moveDisk(n,s,d):
    print("Move disk",n+1,"from",s,"to",d)

n=int(input("Enter number of disks:"))
Q2_moveTower(n,'A','C','B')
    
    
