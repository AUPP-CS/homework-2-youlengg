# HW2 BMI Calculator

You're working in a clinic and your supervisor has asked you to create a program that calculates a patient's BMI. This program will be used to keep record your patient's health, by following the conditions below:

- < 18.5, underweight
- 18.5 - 24.9, normal
- 25 - 29.9, overweight
- 30 - 34.9, obese
- 35 <, extremely obese

BMI Fomula:

```python
BMI = weight in kg/(height in m)^2
```

<br>

## Requirements

1. Create the **bmi_check** function that takes 2 parameters, **weight as float** and **height as float**.

2. **bmi_check** needs to return **2 values**; it needs to return a **result** and the **bmi**.

3. The **result** should return the weight status as underweight, normal, overweight, obsese, and extremely obsese with its **bmi** score.

4. Unrealistic weight or height should return “unrealistic information."

5. Any invalid parameter to the function should return “invalid input.”

<br>

### Task: You will be writing a Python function that calculates a user's BMI and returns their BMI result into the console.

<br>

### Instruction:

> - Ask for user input
>   > Input:
>   >
>   > - user's name
>   > - user's weight
>   > - user's height
> - Do a calcualtion by fomula provided above
> - Print output

> - Then display an option **`Y/N`**, for user to whether contiune or stop.

### Expected Output:

- Output: 1
  ![image](https://github.com/AUPP-CS/homework_2/assets/80062829/fee1819e-a135-439d-a17c-cd3166f5be47)


> If user pick "y" for yes.

- Output: 2
  ![image](https://github.com/AUPP-CS/homework_2/assets/80062829/f54c3776-4e49-45ad-9639-76cdf09a52f6)

### Hint
> - Make use of different loops (while, try)

### Reminders
> - Comment your code to prove you understand the logic if you're using concepts from the internet 
> - Make sure to have pytest installed by following the instructions in Canvas.
> - Run pytest to ensure your code passes all the tests to recieve a full score.


<br><br>

<h1 style="text-align: center;">*** Be Creative ***</h1>
