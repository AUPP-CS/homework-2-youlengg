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
    try: # here we use the try becuase we want to trying in convert weight and height to float
        weight = float(weight) # converting weight to float
        height = float(height) # converting height to float
        if weight <= 0 or height <= 0: # cheking the condition if weight or height is equal or below to 0
            return 'invalid input' # if the condition is True: we'll return the invalid input, since weight and height should be more than 0
        else: # but if the condition if false
            if weight > 625 or height > 2.72: # we still check for some unrealistic condition, if wight is more than 625 kg or height is more than 2.72 meter 
                return 'unrealistic information' # then it seem unrealistic, so we print unrealistic
            else: # if not then all the input are valid and meet the realistic condition
                result_bmi = weight/(height*height) # so, we do the calculation
                if result_bmi < 18.5:
                    return 'underweight', round(result_bmi, ndigits=2)
                elif result_bmi > 18.5 and result_bmi <= 24.9:
                    return 'normal', round(result_bmi, ndigits=1)
                elif result_bmi > 24.9 and result_bmi <= 29.9:
                    return 'overweight', round(result_bmi, ndigits=1)
                elif result_bmi >29.9 and result_bmi <=40:
                    return 'obese', round(result_bmi, ndigits=2)
                elif result_bmi > 40:
                    return 'extremely obese', round(result_bmi, ndigits=1) # we use round to round the result, since it return a lot of decimal
    except ValueError: # so, if the input from user is anything that it can't convert to float then the code will cause an error, but we counter the error by the except
        return 'invalid input' # here, instead of showing error, we return the 'invalid input' instead