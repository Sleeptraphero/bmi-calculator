# BMI Calculator
# BMI Formula = Body weight (in kg) divided by height (in m) squared

# BMI < 18.5 	    Underweight
# BMI 18.5 – 24.9 	Normal weight
# BMI 25 – 29.9   	Overweight
# BMI 30 – 34.9   	Obesity Grade I
# BMI 35 – 39.9   	Obesity Grade II
# BMI ≥ 40        	Obesity Grade III

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))
name = input("Please enter your name: ")

def calculate_bmi(weight_kg, height_cm):
    BMI = ((weight_kg/(height_cm/100)**2))
    
    print("Hello " + name + "!\nYour BMI is: " + str(round(BMI, 2)))

    if BMI >0:
        if(BMI < 18.5):
            print("You are underweight.")
        elif(BMI < 24.9):
            print("You have normal weight.")
        elif(BMI < 29.9):
            print("You are overweight.")    
        elif(BMI < 34.9):
            print("You have Obesity Grade I")
        elif(BMI < 39.9):
            print("You have Obesity Grade II")
        elif(BMI > 40):
            print("You have Obesity Grade III.")
        else:
            print("Please provide valid values.")

calculate_bmi(weight, height)