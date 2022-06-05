a=int(input())
c=0
while a!=0:
    c+=a//500
    a %= 500
    c+=a//100
    a%=100
    c+=a//50
    a%=50
    c+=a//10
    a%=10
print(c)