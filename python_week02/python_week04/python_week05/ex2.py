import ex1

while True:
    print('\nโปรแกรมที่ต้องการใช้')
    print("1 = %3 , 2 = รวมค่าบวก ลบ , 0 = ออกจากโปรแกรม")
    a = int(input('เลือก :'))
    if a == 1:
        while True:
            print('\nโปรแกรม %3')
            print('พิมพ์ 0 เพื่อต้องการออก')
            a = 1
            b = int(input('ใส่คำปลาย :'))
            c = ex1.test(a,b)
            if b == 0:
                break
            print(f'{c}\n')

    elif a == 2 :
        b = 0
        c = 0
        while True:
            print('\nโปรแกรมรวมค่า')      
            print('พิมพ์ 0 เพื่อต้องการออก')  
            a = int(input('ใส่เลข :'))
            if a == 0:
                print(f'ผลรวมของค่าบวก = {c}')
                print(f'ผลรวมของค่าลบ = {c}')
                break
            b,c = ex1.sum(a,b,c)
            print(f'ผลบวก = {b}, ผลลบ = {c}')
    elif a == 0:
        print('คุณได้ออกจากระบบแล้ว tant you')
        break
    else :
        print('ป้อนตัวเลขให้ถูกต้อง')