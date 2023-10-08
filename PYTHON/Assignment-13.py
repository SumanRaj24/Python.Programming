"""
#q5
a,b,c=int(input("enter number 'a'")), int(input("enter number 'b'")) , int(input("enter number 'c'"))
if a>b and a>c:
    print("Grater'A'")
elif b>a and b>c:
    print("Grater'B'")   
else:
    print("Grater'C'")     
"""


#q4
year=int(input("enter a year"))
if year%100:
    if year%400==0:
        print("Leap year")
    else:
        print("Non Leap year")    
else:
    if year%4==0:
       print("Leap year")
    else:
       print("non Leap year")    
    
    
    
    
#q3
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(b*b-4*a*c>0):
   print("Real Distinet Roots");
elif(b*b-4*a*c<0):
    print("imaganiary Roots");  
else:
    print("Equal Roots");
    
      
"""
#q2
x=int(input("enter a number"))
if(x>0):
   print("positive numbwe");
elif(x>=0):
    print("zero number");  
else:
    print("negitive number");   
"""


"""
#q1
x=int(input("enter a number"))
if(99<x and x<1000):
   print("three digit numbwe");
else:
    print("not three digit number");  
""" 