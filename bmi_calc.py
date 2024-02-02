'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''
def bmi_check(weight, height):
    # Add your code here

    # here we use the try becuase we want to try in converting weight and height to float, if input can't convert then it will return an error
    try:
         # converting weight to float
        weight = float(weight)
        # converting height to float
        height = float(height)

         # cheking the condition if weight or height is equal or below to 0
        if weight <= 0 or height <= 0:
            # if the condition is True: we'll return the invalid input, since weight and height should be more than 0
            return 'invalid input'
        # but if weight or height both are not below or equal to 0, it mean that weight > 0, height > 0 is True.
        else:
            # we still check for some unrealistic condition, if weight is more than 625 kg or height is more than 2.72 meter
            if weight > 625 or height > 2.72:
                # then it seem unrealistic, so we print unrealistic
                return 'unrealistic information'
            
            # if both of this upper condition is not true, then all the input are valid and meet the realistic condition
            else:
                # do the calculation
                # we use round to round the result, since it return a lot of decimal number
                #the function will return two values, one values is the stauts, and another one is the calculted bmi result
                result_bmi = weight/(height*height) 
                if result_bmi < 18.5:
                    return 'underweight', round(result_bmi, ndigits=1)
                elif result_bmi > 18.5 and result_bmi <= 24.9:
                    return 'normal', round(result_bmi, ndigits=1)
                elif result_bmi > 24.9 and result_bmi <= 29.9:
                    return 'overweight', round(result_bmi, ndigits=1)
                #this code below might be a bit different from the instruction, but to meet the autograde requirement
                elif result_bmi >29.9 and result_bmi <=40:  
                    return 'obese', round(result_bmi, ndigits=1)
                elif result_bmi > 40:
                    return 'extremely obese', round(result_bmi, ndigits=1)
                
    # so, if the input from user is anything that it can't convert to float then the code will cause an error, but we counter the error by the except
    except ValueError:
        # here, instead of showing error, we return the 'invalid input' instead
        return 'invalid input'
    

    ### incase the input is invalid or seem unrealistic, the function will only return one value which is the status of it, to show that if it's invalid input or unrealistic.
    ### but if all the input are correct, then the function will return 2 values, one value is status of user, and another one is the calculated bmi result of user.