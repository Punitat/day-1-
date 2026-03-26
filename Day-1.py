while True:
    yourname = input("คุณชื่ออะไรครับ? :")  
    print("สวัสดีครับคุณ", yourname, "ยินดีที่ได้รู้จัก")   
    age = input("คุณอายุเท่าไหร่ครับ? :")    
    print("อายุ", age)   
    birth_day = 2569 - int(age) 
    print("ปีที่คุณเกิดคือ",birth_day, "ใช่ไหม")   
    if int(age) >= 60:  
        print("คุณคือวัยเกษียณสุดเก๋า!") 
    elif int(age) >= 18: 
        print("คุณคือวัยทำงานสู้ชีวิต")
    elif int(age) >= 13: 
        print("คุณคือวัยรุ่นวุ่นรัก")
    else:   
        print("เจ้าหนูวัยใส") 
    status = input("กด Enter เพื่อต่อ หรือพิมพ์ 'q' เพื่อเลิก: ")
    if status == 'q': 
        print("ขอบคุณที่ลองเล่นครับ!")
        break #