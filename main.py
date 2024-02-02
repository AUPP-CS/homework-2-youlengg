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
print("To know your Body Mass Index, Please follow through these below instructions. ⬇️  ⬇️  ⬇️")
print("1️⃣  .Enter your name.")
print("2️⃣  .Enter your weight in kg.")
print("3️⃣  .Enter your height in meter.")
print("4️⃣  .See your result.")
print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

# Add your code here
while True:
    #Asking user for three input, name, weight, and height.
    user_name = input("\n👉👉👉  Enter your name📋📋📋: ")
    user_weight = input("👉👉👉  Enter your weight in kg ⏲️ ⏲️ ⏲️ : ")
    user_height = input("👉👉👉  Enter your height in meter📏📏📏: ")
    
    #variable returned represent 2 return values from the function
    returned = bmi_check(user_weight, user_height)

    # here we check the type of returned value , this case if the returned value is tuple mean that it retured multiple value packed together.
    if type(returned) == tuple:
        # then we create new variable which is status and result_bmi is to unpakced the tuple to two different values and store in status, and result_bmi    
        status, result_bmi = returned

        #print the result
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("|                                                                                |")
        print(f'       💪💪💪 {user_name}, you are {status} and your bmi is: {result_bmi} 💪💪💪 ')
        print("|                                                                                |")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    # but if first condition isn't True, then it mean that the function only return one value since in bmi_calc function sometime it returns only one value base on user's input

    # so here we come to check what is that one valued returned, looking at bmi_calc.py, there are two possible values, which are invalid input, and unrealistic information
    
    # if the returned value is 'invalid input', the code will print invalid input
    elif returned == 'invalid input':
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("|                                                                                |")
        print('                         ❌❌❌ Invalid input ❌❌❌')
        print("|                                                                                |")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    # the same, if that one returned value is unrealistic information, the code will print unrealistic information
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
        print("\n🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁🔁... restarted")
        print("\n")
        True
    
    # if user wish not to continue, we'll print message and break the loop.
    else:
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        print("\nThank you for using our app 🥰 🥰 🥰")
        break