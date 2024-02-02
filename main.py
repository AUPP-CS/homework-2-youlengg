from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)
print("\n Welcome to our app!")
print("\n ------------------------------------------------------")
# Add your code here
while True:
    user_name = input("Your name: ")
    user_weight = input("Your weight: ")
    user_height = input("Your height: ")
    returned = bmi_check(user_weight, user_height) #returned represent 2 return values from the function
    if type(returned) == tuple:    # here we check the type of returned value , this case if it is tuple mean that it retured more than one value
        status, result_bmi = returned # then create new variable which is status and result_bmi is to unpakced the tuple to two different value which is represent by status and result_bmi
        print(f'Your status is: {status} and your bmi is: {result_bmi}') 
    elif returned == 'invalid input': # but if it's invalid then the function will only return one value since in bmi_calc we only give it to returned one value
        print('Invalid input') # if the returned value is 'invalid input', it will print invalid input
    elif returned == 'unrealistic information': # the same, if it's unrealistic information, it also return only 1 value
        print('Unrealistic information') # and it will print unrealistic information

    check_condition = input('Do you want to start again? y/n: ') # here is the condition for the loop, we ask user if they wish to continue
    if check_condition != 'n': # if check condition not equal to n, which mean user don't want to stop
        True # then it will return the True for the loop to continue
    else:
        print("Thank you for using our app!")
        break # else, the loop will break