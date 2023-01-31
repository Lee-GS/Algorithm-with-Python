num = input()
while num !=0:
    if (num == 0):
        break
    num = list(num)
    num2 = list(reversed(num))
    if (num == num2):
        print("yes")
    else:
        print("no")
    num = input()
    