#Menghitung Body mass index (BMI) dan mengkategorikannya

weight_lb = float(input("Enter your weight in pounds: "))
height_in = float(input("Enter your height in inches: "))

bmi = (weight_lb * 703) / (height_in * height_in)

if(bmi < 18.5):
    category = "Underweight"
elif(bmi <= 24.9):
    category = "Normal"
elif(bmi <= 29.9):
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is   : {bmi:.2f}")
print(f"Weight status : {category}")