num = int(input("enter a number :"))
revnum = 0

while(num>0):
    lastdigit = num%10
    revnum = (revnum*10)+lastdigit
    num//= 10

print("Reverse number:",revnum)