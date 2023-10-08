s1=input("enter a string")
for e in s1:
    if e>='a' and e<='z' and e>='A' and e<='Z':
       pass
    else:
        print("string has at least one character which is not an alphabet ")
        break
else:
    print("string contains only alphabet")
        