start=int(input("enter a number"))
end=int(input("enter a number"))
for x in range(start,end,1):
   for i in range(2,x):
      if(x%i==0):
       break
   else:
       print(x, end=' ')



"""
#q4
n=int(input("enter a number"))
r1=range(1,n+1,1)
for e in r1:
    print(e**3,end=' ')
"""


"""
#q3
n=int(input("enter a number"))
r1=range(1,n+1,1)
for e in r1:
    print(e*e,end=' ')
"""


"""
#q2
n=int(input("enter a number"))
r1=range(1,2*n,2)
for e in r1:
    print(e,end=' ')
    """


"""
#q1
n=int(input("enter a number"))
r1=range(2,2*n+1,2)
for e in r1:
    print(e,end=' ')
    """