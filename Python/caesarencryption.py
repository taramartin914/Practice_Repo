message=input("Enter a message : ")
distance=int(input("Enter the distance : "))
for i in message:
    value=ord(i)+distance
    if value>ord('z'):
        value=value-26
    print(chr(value),end="")
