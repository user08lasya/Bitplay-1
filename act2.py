def setOrNot(number,n):
    mark = 1<<(n-1)
    if number & mark:
        print("\nSET")
    else:
        print("\nNOT SET")
number = int(input("Enter number: "))
n = int(input("Enter bit number: "))
setOrNot(number,n)