

#5
x=input("enter a number")
match x:
    case x if x in "mysirg":
        print("One")
    case x if x in "education":
        print("Two")
    case x if x in "service":
        print("Three")        

"""
#q4
x=eval(input("enter a number"))
match x:
     case x if type(x)==int:
         print("monday")
     case x if type(x)==float:
         print("tuesday")
     case x if type(x)==complex:
         print("Wednesday") 
     case x if type(x)==bool:
         print("Thursday")      
  """     
               

"""
#q3
print("1.Odd and even")
print("2.positive and Negative")
print("3.Simple Interest")
print("4.Roots of Quatice Equation")
x=int(input("Enter your choice"))
match x:
    case 1:
        print("enter a number")
        n=int(input())
        print("Even" if n%2==0 else "Odd number")
              
    case 2:
        print("enter a number")
        n=int(input())
        print("Positive"if n>0 else"Non-positive")
        
        
    case 3:
        print("principle Rate and Time")
        priciple,Rate,Time=float(input()),float(input()),float(input()),
        si=priciple*Rate*Time/100
        print("Simple Interast is", si)
        
    case 4:
        print("enter value a b and c")
        a,b,c=int(input()),int(input()),int(input())   
        r1=(-b+(b*b-4*a*c)**0.5)/2*a
        r2=(-b-(b*b-4*a*c)**0.5)/2*a 
        print("Roots are:,r1 and r2")
    case _:
        print("Invalid choice")              
"""

"""
#q2
x=int(input("enter a three digit number"))
match x:
     case x if x>0:
         print("Positive number")
     case x if x<0:
         print("negitive number")
     case x:
         print("Zero number")

"""         

"""
#q1
x=int(input("enter a three digit number"))
match x:
     case x if x>99 and x<1000:
         print("three digit number")
     case x:
         print("not three digit number")      
 """