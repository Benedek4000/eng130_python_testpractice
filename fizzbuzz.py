while True:
    try:
        length = int(input("enter fizzbuzz length: "))
        break
    except:
        print("invalid value")

while True:
    try:
        fizz = int(input("enter fizz: "))
        break
    except:
        print("invalid value")

while True:
    try:
        buzz = int(input("enter buzz: "))
        break
    except:
        print("invalid value")

for i in range(length):
    if (i+1) % fizz == 0:
        if (i+1) % buzz == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if (i+1) % buzz == 0:
            print("buzz")
        else:
            print(i+1)
