l,u,s,d=0,0,0,0
x=input("enter the password:")
if(len(x)>=6):
    for i in x:
        if(i.isdigit()):
            d+=1
        if(i.isupper()):
            u+=1
        if(i.islower()):
            l+=1
        if(i=='$'or i=='@' or i=='#'):
              s+=1
if(l>=1 and s>=1 and u>=1 and d>=1 and l+u+d+s==len(x)):
    print("ACCEPTED")
else:
    print("NOT ACCEPTED")
