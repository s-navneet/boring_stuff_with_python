def collatz(number):
    if(number%2==0):
        print(number//2)
        return(number//2)
    else:
        number=(number*3)+1
        print(number)
        return number

number=0

while(number!=1):
    try:
        number=int(input())
        number=collatz(number)
    except ValueError:
        print("must enter an integer")

