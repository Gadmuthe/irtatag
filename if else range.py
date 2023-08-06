for num in range(-2, 2):
    if num < 0:
        if num * 2 == 0:
            print(str(num) + "is negative and even")
    else:
        print(str(num) + "is negative and odd")
        if num == 0:
            print(str(num) + "is zero")
else :
    if num % 2 == 0:
        print(str(num) + "is positive and even") 
    else:
        print(str(num) + "is posiitve and odd")