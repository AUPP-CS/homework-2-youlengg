from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)
print("""\n                                                                                                                                                                                                                                                                                 
     __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __ 
    |__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __|
     _                                                                                                    _  
    | |                                                                                                  | |  
    | |                                                                                                  | | 
    |_|                                                                                                  |_| 
     _     ____   __  __  ___    ____     _     _      ____  _   _  _         _   _____  ___   ____       _  
    | |   | __ ) |  \/  ||_ _|  / ___|   / \   | |    / ___|| | | || |       / \ |_   _|/ _ \ |  _ \     | | 
    | |   |  _ \ | |\/| | | |  | |      / _ \  | |   | |    | | | || |      / _ \  | | | | | || |_) |    | | 
    |_|   | |_) || |  | | | |  | |___  / ___ \ | |___| |___ | |_| || |___  / ___ \ | | | |_| ||  _ <     |_| 
     _    |____/ |_|  |_||___|  \____|/_/   \_\|_____|\____| \___/ |_____|/_/   \_\|_|  \___/ |_| \_\                                                                                                _  
    | |                                                                                                  | | 
    | |                                                                                                  | | 
    |_|                                                                                                  |_| 
     __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __  __ __ 
    |__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __||__ __|
                                                                                                                                                                                                                                                                                                                                                                                                           
\n""")

#First, showing user some instruction.
print("💪💪💪 Welcome to Good Health BMI Calculator 💪💪💪")
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
print("To know your Body Mass Index, Please follow through these below instructions. ⬇️  ⬇️  ⬇️  💡 💡 💡")
print("\n1️⃣  .Enter your name. 💬")
print("\n2️⃣  .Enter your weight in kg. ⏲️")
print("\n3️⃣  .Enter your height in meter. 📏")
print("\n4️⃣  .See your result. 📋")
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

# Add your code here
while True:
    #Asking user for three input, name, weight, and height.
    user_name = input("\n👉👉👉  Enter your name💬 💬 💬: ")
    user_weight = input("👉👉👉  Enter your weight in kg ⏲️  ⏲️  ⏲️ : ")
    user_height = input("👉👉👉  Enter your height in meter📏 📏 📏: ")
    
    #variable 'returned' represent 1 or 2 return values base on the return from the function.
    returned = bmi_check(user_weight, user_height)

    # Here we check the type of returned value to see how many values returned.
    # In this case if the returned value is in tuple type, it mean that function retured multiple value packed together. (For our code now, function returned 2 values).
    if type(returned) == tuple:
        # then we create new variable which is status and result_bmi is to unpakced the tuple to two different values and store in status, and result_bmi
        # we store in status and result_mbi becuase we already know that the 2 value that function returned is status and the calculated mbi result.
        # the concept of placing status infront of result_mbi is because in our logic code the status is in fitst order, and result is in second order.
        status, result_bmi = returned
        
        # printing different result base on user's status
        if status == 'underweight':
            print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("|                                                                                                            |")
            print(f'     💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪. You should eat more healthy calories.🥗 🥗 ')
            print("|                                                                                                            |")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        elif status == 'normal':
            print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("|                                                                                                            |")
            print(f'     💪💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪💪. Nice, keep maintain your normal bmi. 💪 ✅ ')
            print("|                                                                                                            |")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        elif status == 'overweight':
            print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("|                                                                                                            |")
            print(f'                     💪💪💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪💪💪.')
            print("|                                                                                                            |")
            print("                              You should do more pysical activity 💪 🏃")
            print("|                                                                                                            |")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        elif status == 'obese':
            print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("|                                                                                                            |")
            print(f'                     💪💪💪💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪💪💪💪.')
            print("|                                                                                                            |")
            print("                You should eat healthy reduced-calorie diet ad exercise reqularly 💪 🏃 🏋")
            print("|                                                                                                            |")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        elif status == 'extremely obese':
            print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            print("|                                                                                                            |")
            print(f'                   💪💪💪💪💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪💪💪💪💪.')
            print("|                                                                                                            |")
            print("                You should balance diet, more exercise and monitor your progress 💪 🏃 ⚽ 🏀 🏋")
            print("|                                                                                                            |")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    # but if first condition isn't True, then it mean that the function only return one value since in bmi_calc function sometime it returns only one value base on user's input

    # so here we come to check what is that one valued returned, looking at bmi_calc.py, there are two possible values, which are invalid input, and unrealistic information
    
    # if the returned value is 'invalid input', the code will print invalid input
    elif returned == 'invalid input':
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("|                                                                                |")
        print('                         ❌❌❌ Invalid input ❌❌❌')
        print("|                                                                                |")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    # if that one returned value is unrealistic information, the code will print unrealistic information
    elif returned == 'unrealistic information':
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("|                                                                                |")
        print('                    🚫🚫🚫  Unrealistic information  🚫🚫🚫')
        print("|                                                                                |")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    # here is the condition for the loop, we ask user if they wish to continue or not.
    check_condition = input('\n🔄🔄🔄 Do you want to start again? 🔄🔄🔄 y/n: ').lower()

    # if check condition not equal to n, it means that user don't want to stop, so the code return True to continue the loop.
    if check_condition != 'n':
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("\nLoading… 🔜")
        print("\n⏳ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ 100% ⏳")
        print("\nRestarted🔄✅")
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        True
    
    # if user don't want to continue, we'll print message and break the loop.
    else:
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("\nThank you for using our app 🥰 🥰 🥰")
        break