print('โปรแกรมตัดเกรด')
try:
    score = int(input('กรุณากรอกเกรด :'))
except :
    score = 0
if score > 0 :
    grade = ''
    if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'   
elif score >= 60 :
    grade = 'D' 
elif :
    grade = 'E' 
    print('คุณได้รับเกรด',grade)
