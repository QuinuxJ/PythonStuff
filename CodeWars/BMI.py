def bmi(weight, height):
    bmic = weight / height**2
    if bmic <= 18.5: return "Underweight"
    if bmic <= 25.0: return "Normal"
    if bmic <= 30.0: return "Overweight"
    if bmic > 30: return "Obese"
    

print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(100, 1.77)) 
    