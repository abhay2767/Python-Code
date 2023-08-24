num = int(input("Enter the number "))

match num:
    case 0:
        print("number is zero")
    case 3:
        print("Number is three")
    case 9:
        print("Number is Nine")
    case _ if num <= 100: #Default case use _
        print("Number is Under 100")
    case _ if num >= 100 and num <= 200:
        print("Number is between 100 to 200")
    case _ if num == 250:
        print("Number is 250")
print("Exit")