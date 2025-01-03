def get_grade(s1, s2, s3):
    g = (s1+s2+s3)/3
    if g >=0 and g<60:
        return "F"
    if g >=60 and g<70:
        return "D"
    if g >=70 and g<80:
        return "C"
    if g >=80 and g<90:
        return "B"
    if g >=90 and g<=100:
        return "A"
    
print(get_grade(95, 90, 93))