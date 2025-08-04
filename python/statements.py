# positive & negative

a=int(input())
if a>0:
    print("positive")
else:
    print("not positive")
    print("end")

# walking

a=int(input())
if a > 50:
    print("person is go to grnd floor")
else:
    print("person is go to 1st floor")

# luckey

n=input()
if n[0] == n[len(n)-1]:
    print("luckey")
else:
    print("super luckey")

# vote

a=int(input())
if a>50:
    print("ground")
elif 50>a>=18:
    print("1st floor")
else:
    print("not eligible for vote")

# winding mission

token=int(input())  #10 20 else:invalid
brand=input()   # 20 = = mazza sprite cocola waterbottel
if token == 10:
    print("chips")
elif token == 20:
    if brand=="mazza":
        print("mazza")
    elif brand=="sprint":
        print("sprite")
    else:
        print("invalid brand")
else:
    print("invalid token")

# count

a=int(input())
counter=0
while counter<3:
    a=a+1
    print(a)
    counter = counter+1
    
# palindrom

n="abcba"
s=n[::-1]
if n==s:
    print("palindrom")
else:
    print("not palindron")

# prime number

n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")
