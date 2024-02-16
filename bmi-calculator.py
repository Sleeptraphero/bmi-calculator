# BMI Calculator
# BMI-Formel = Körpergewicht (in kg) geteilt durch Körpergröße (in m) zum Quadrat

# BMI < 18,5 	        Untergewicht
# BMI 18,5 – 24,9 	    Normalgewicht
# BMI 25 – 29,9 kg/m2 	Übergewicht
# BMI 30 – 34,9 kg/m2 	Adipositas Grad I
# BMI 35 – 39,9 kg/m2 	Adipositas Grad II
# BMI ≥ 40 kg/m2 	    Adipositas Grad III 

weight = float(input("Bitte gib dein Gewicht in kg ein: "))
height = float(input("Bitte gib deine Größe in cm ein: "))
name = input("Bitte gib deinen Namen an: ")

def calculate_bmi(weight_kg, height_cm):
    BMI = ((weight_kg/(height_cm/100)**2))
    
    print("Hallo " + name + "!\nDein BMI ist: " + str(round(BMI, 2)))

    if BMI >0:
        if(BMI < 18.5):
            print("Du hast untergewicht.")
        elif(BMI < 24.9):
            print("Du hast Normalgewicht.")
        elif(BMI < 29.9):
            print("Du hast übergewicht.")    
        elif(BMI < 34.9):
            print("Du hast Adipositas Grad I")
        elif(BMI < 39.9):
            print("Du hast Adipositas Grad II")
        elif(BMI > 40):
            print("Du hast Adipositas Grad III.")
        else:
            print("Bitte gib gültige Werte an")

calculate_bmi(weight, height)
