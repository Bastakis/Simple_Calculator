q = False
x=""

while q == False:
    i=float(input("gimme the 1st number:"))
    a=input("put the operation:")
    b=float(input("gimme the 2nd number:"))

    if a=="+":
       print(i+b)
    elif a=="-":
       print(i-b)
    elif a == "*":
        print(i * b)
    elif a == "/":
         print(i / b)
    else:
        print("you didnt put valid operation symbol")

    print(x)

    while x!="False" and x !="True":
        x = input("Would you like another operation press True or False:")
        if x == "False":
            q = True
        elif x =="True":
            q = False
        else:
            print("You need to type True or False")

print("Thanks for your time!")