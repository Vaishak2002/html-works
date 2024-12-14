num=int(input("enter tye num"))

original=num

count=len(str(num))
tot=0

while(num!=0):

    digit=num%10
    digit=digit**count
    tot=tot+digit
    num=num//10

if tot==original:

    print("is armstrong")

else:
    
    print("not armstrong")

