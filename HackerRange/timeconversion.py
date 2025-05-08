# def timeConversion(s):
#     PmAm = s[-2:]
#     hours = s[:2]
#     rest = s[2:-2]
#     if PmAm == "PM":
#         if hours == "12":
#             hours = "12"
#         elif hours == "11":
#             hours = "23"
#         elif hours == "10":
#             hours = "22"
#         elif hours == "09":
#             hours = "21"
#         elif hours == "08":
#             hours = "20"
#         elif hours == "07":
#             hours = "19"
#         elif hours == "06":
#             hours = "18"
#         elif hours == "05":
#             hours = "17"
#         elif hours == "04":
#             hours = "16"
#         elif hours == "03":
#             hours = "15"
#         elif hours == "02":
#             hours = "14"
#         elif hours == "01":
#             hours = "13"
        
#     if PmAm == "AM":
#         if hours == "12":
#             hours = "00"
#         elif hours == "11":
#             hours = "11"
#         elif hours == "10":
#             hours = "10"
#         elif hours == "09":
#             hours = "09"
#         elif hours == "08":
#             hours = "08"
#         elif hours == "07":
#             hours = "07"
#         elif hours == "06":
#             hours = "06"
#         elif hours == "05":
#             hours = "05"
#         elif hours == "04":
#             hours = "04"
#         elif hours == "03":
#             hours = "03"
#         elif hours == "02":
#             hours = "02"
#         elif hours == "01":
#             hours = "01"
        
#     return hours+rest


#Código Mejorado

def timeConversion(s):
    PmAm = s[-2:]  # AM o PM
    hours = int(s[:2])  # Convertimos las horas a entero
    rest = s[2:-2]  # Minutos y segundos se quedan igual

    if PmAm == "AM":
        hours = 0 if hours == 12 else hours  # 12 AM -> 00
    else:  # PM
        hours = hours if hours == 12 else hours + 12  # 12 PM se mantiene igual, el resto suma 12

    return f"{hours:02}{rest}"  # Formateamos la hora con dos dígitos

    
s = "07:05:45PM"
print(timeConversion(s))