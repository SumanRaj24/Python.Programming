#A-27 Q1
"""
s1=input("enter a string")
print(' '.join(s1.split(' ')[::-1]))
"""

#A-27 Q2
"""
s1=input("enter a string")
l1=[]
for word in s1.split(' '):
    try:
        l1.append(float(word))
    except:
        pass   
 """        

#A-27 Q3
"""
s1=input("enter a string")
print("palindrome" if s1==s1[::-1] else "not a parindrome")
#A-27 Q4
#A-27 Q5
"""

#A-27 Q4
"""
s1=input("enter a string")
print(s1.upper())
"""


#A-27 Q5
s1=input("enter a string")
i=0
index=0
maxlength=-1
for e in s1.split(' '):
    if maxlength<len(e):
        maxlength=len(e)
        index=i
    i+=1
print("max length word",s1.split(' ')[index],"is ",maxlength)        