first=(input("enter first number"))
operator=input("enter operater (+,-,*,/,%)")
secound=(input("enter secound number"))

first=int(first)
secound=int(secound)

if operator == '+':
    print(first + secound)
    
elif operator == '-':
    print(first - secound)
    
elif operator == '*':
    print(first * secound)

elif operator == '/':
    print(first / secound) 
    
elif operator == '%':
    print(first % secound)   
    
else:
    print("Invalid operater")                