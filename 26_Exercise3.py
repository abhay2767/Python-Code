""" Create a program capable of displaying question to the user like KBC:
Use List data type to store the question and their correct answer
Display the final amount the person is taking home after playing the game
 """

""" print("Wellcome to KBC")
Question = ["0- Who is prime Minister of India", "1- Who is President of India", "2- Who is Home Minister of Indai"]
Option_1 = ["0- Narendhra Modi","1- Kenjari Bal","2- Rahul Gandhi","3- Amit Shah"]
Answer_1 = 1;
Amout_1 = 100000;
Option_2 = ["0- Javahar lal Nehru","1- Kenjari Bal","2- Rabindhra Nath Govind","3- Shubhash Chandhra Bosh"]
Answer_2 = 3;
Amount_2 = 200000
Option_3 = ["0- Akhilesh Yadav","1- Rahul Gandhi","2- Lalu Prashad Yadav","3- Amit Shah"]
Answer_3 = 4;
Amout_3 = 500000

print(Question[0],"\n","Price is: ", Amout_1)
print(Option_1)
num = int(input("Enter Number: "))
if(num == Answer_1 ):
    print("Your answer is right: ",Option_1[0], "And you have won price of ",Amout_1)
    print("Press 1 to go ahed for next Question")
    choice = 1
    number = int(input("Enter CHoice: "))
    if(number == choice):
        print("Next Queston is: ",Question[1])
        print(Option_2)
        num = int(input("Enter Number: "))
        if(num == Answer_2):
            print("Your answer is right: ",Option_1[1], "And you have won price of ",Amout_1+Amount_2)
            print("Press 1 to go ahed for next Question")
            choice = 1
            number = int(input("Enter CHoice: "))
            if(number == choice):
                print(Question[2],"\n","Price is: ", Amout_3)
                print(Option_3)
                num = int(input("Enter Number: "))
                print("Your answer is right: ",Option_1[3], "And you have won price of ",Amout_1+Amount_2+Amout_3)
                #exit = 1
                Str = int(input("Type Exit to go out of the Game: "))

                while(Str!= 1):
                    Str = int(input("Try Again: "))
            else:
                print("You have out of Game afetr 2 right Answer with the price won: ",Amout_1+Amount_2)
        else:
            print("You are out of game after 1 right and 1 wrong Answer")
    else:
        print("You are out of the Game after 1 right answer with the price won: ",Amout_1)
else:
    print("Galat Jabab: ",Option_1[num]) """
questions = [
    ["Who is prime Minister of India","Narendhra Modi","Kenjari Bal","Rahul Gandhi","Amit Shah",2],
    ["Who is President of India","Javahar lal Nehru","Kenjari Bal","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Home Minister of India","Javahar lal Nehru","Kenjari Bal","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Chief Minister of Utter Pradesh","Javahar lal Nehru","Aadhitya Nath yogi","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Chief Minister of Utter Pradesh","Javahar lal Nehru","Aadhitya Nath yogi","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Chief Minister of Utter Pradesh","Javahar lal Nehru","Aadhitya Nath yogi","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Chief Minister of Utter Pradesh","Javahar lal Nehru","Aadhitya Nath yogi","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is Chief Minister of Utter Pradesh","Javahar lal Nehru","Aadhitya Nath yogi","Rabindhra Nath Govind","Amit Shah",2],
    ["Who is prime Minister of India","Narendhra Modi","Kenjari Bal","Rahul Gandhi","Amit Shah",2],
    ["Who is President of India","Javahar lal Nehru","Kenjari Bal","Rabindhra Nath Govind","Amit Shah",2],
    ]

levels = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"Q- {question[0]}")
    print(f"a. {question[1]},               b. {question[2]}")
    print(f"c. {question[3]},               d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or (0) to Quit the game: "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct Answer, You have won Rs. {levels[i]}")
        if(i == 0):
            money = 1000
        elif(i == 1):
            money = 2000
        elif(i == 2):
            money = 4000
        elif(i == 3):
            money = 8000
        elif(i == 4):
            money = 16000
        elif(i == 5):
            money = 32000
        elif(i == 6):
            money = 64000
        elif(i == 7):
            money = 128000
        elif(i == 8):
            money = 256000
        elif(i == 9):
            money = 512000
        elif(i == 10):
            money = 1024000
            questions[i+1] 
    else:
        print("Wrong Aswer")
        break
print(f"You take money home total Rs. {money}")