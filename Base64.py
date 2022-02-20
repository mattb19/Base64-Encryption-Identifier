def Identify(str):
    condition1 = False
    numChar = 0
    for i in str:
        numChar += 1
    if numChar%4 == 0:
        condition1 = True


    condition2 = False
    good = True
    for i in str:
        x = i.isalpha()
        y = i.isdigit()
        if x == True:
            None
        elif y == True:
            None
        elif i == '+':
            None
        elif i == '/':
            None
        else:
            good = False
            print("okay")
            break


    if good == True:
        condition2 = True

    if condition2 == True and condition1 == True:
        return True
    else:
        return False


def main():
    str = input()
    test = Identify(str)
    if test == True:
        print("This string is possibly encrypted in Base64")
    else:
        print("This string is 100% not encrypted in Base64")
if __name__ == "__main__":
    main()