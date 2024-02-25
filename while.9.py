n = int(input("enter the rnumber: "))
s=1
while n < 0:
    n = int(input("enter tHE NUMBER : "))

if n==0:
    print("the factories is:1 ")

else:
    for i in range(1,n+1):
        s=s*i
        i=i+1
    print(s)
