#Libraries importing:
from datetime import date, datetime

#starting code
print ("********************** Welcome in UMBRELLA's car wash!! **********************")
print ("Navigation Bar:")
print ("\n\t 1- Home ***** 2- Services ***** 3- Who are us? ***** 4- complaint")
print ("\n\t")
print ("**************** Plese Select one choice from navBar selections ****************")

userInput= input ("Enter number of selection/Type the name of selection: \t")

# check if userInput is exsit or not
if userInput == "1" or userInput == "Home":
    print("Hi, we are UMBRELLA's car wash \n known as UM\n we are seek to make every car clean and well work\n")

elif userInput == "2" or userInput == "Services":
    print("\n 1- Normal wash\n 2- VIP Wash\n 3- ALL wash")
    servicesInput= input("Enter the of selection above:\t ")

    if servicesInput == "1":
        print (" Normal Wash contains:\t Exterior car wash, wheels and seats = 10KD")

        #Let user choose or NO:
        selctionA= input ("Want to try ? please answr with Yes or NO \t")

        if selctionA == "Yes" or selctionA =="YES":
            
            hours = int(input('Enter the hour: '))
            minutes = int(input('Enter the minutes: '))
            year = int(input('Enter a year: '))
            month = int(input('Enter a month: '))
            day = int(input('Enter a day: '))
            
            dt = datetime(year, month, day, hours, minutes)

            print("\n\n")
            print(dt)
            print ("\n Thanks for Reservation \n\n\t\tSee U")

        else:
            print("\n\n")
            print ("You're Welcome <3")
        


        
    elif servicesInput == "2":
        print (" VIP Wash contains:\t  Exterior car wash, wheels, seats, machine, repump the pumber and wheels, polishand fix the scratches= 25KD for big cars and buses otherwise, 15KD")

        #Let user choose or NO:
        selctionB= input ("Want to try ? please answr with Yes or NO \t")

        if selctionB == "Yes" or selctionB =="YES":
            
            hoursB = int(input('Enter the hour: '))
            minutesB = int(input('Enter the minutes: '))
            yearB = int(input('Enter a year: '))
            monthB = int(input('Enter a month: '))
            dayB = int(input('Enter a day: '))
            
            dtB = datetime(year, month, day, hours, minutes)

            print("\n\n")
            print(dtB)
            print ("\n Thanks for Reservation \n\n\t\tSee U")

        else:
            print("\n\n")
            print ("You're Welcome <3")
            
    elif servicesInput == "3":
        print (" ALL Wash contains:\t  Exterior car wash, wheels, seats, machine, repump the pumber and wheels, polish the scratches,Thermal shading and thermal insulation = 30KD for big cars and buses otherwise, 25KD ")

        #Let user choose or NO:
        selctionC= input ("Want to try ? please answr with Yes or NO \t")

        if selctionC == "Yes" or selctionC =="YES":
            
            hoursC = int(input('Enter the hour: '))
            minutesC = int(input('Enter the minutes: '))
            yearC = int(input('Enter a year: '))
            monthC = int(input('Enter a month: '))
            dayC = int(input('Enter a day: '))
            
            dtC = datetime(year, month, day, hours, minutes)

            print("\n\n")
            print(dtC)
            print ("\n Thanks for Reservation \n\n\t\tSee U")

        else:
            print("\n\n")
            print ("You're Welcome <3")

elif userInput == "3" or userInput == "Who are us":
    print("We are UMBRELLA's car wash \n known as UM\n we are seek to make every car clean and well work\n")
    #Let user choose or NO:
    selctionD= input ("Want to try ? please answr with Yes or NO \t")

    if selctionD == "Yes" or selctionD =="YES":
            
            hoursD = int(input('Enter the hour: '))
            minutesD = int(input('Enter the minutes: '))
            yearD = int(input('Enter a year: '))
            monthD = int(input('Enter a month: '))
            dayD = int(input('Enter a day: '))
            
            dtD = datetime(year, month, day, hours, minutes)

            print("\n\n")
            print(dtD)
            print ("\n Thanks for Reservation \n\n\t\tSee U")

    else:
            print("\n\n")
            print ("You're Welcome <3")

elif userInput == "4" or userInput == "complaint":
    print("Who is making you getting mad!!\n")
    input ("Type your complaint:\t")

    print ("\n\n Sorry for hear that :( \n We will fix it ")

    

else:
    print ("It's not exsit :(")
