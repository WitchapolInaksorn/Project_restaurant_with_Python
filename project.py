import random
# menu หลัก
def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.รายการสั่งอาหาร")
    print("2.รายการสั่งเครื่องดื่ม")
    print("3.รายสุ่มอาหาร")
    print("4.รายสุ่มเครื่องดื่ม")
    print("0.ออกจากโปรแกรม")

# menu 1 รายการสั่งอาหาร
def menu_food() :
    while True :
        print("\n[รายการสั่งอาหาร]")
        if work == 0 :
            return 0
        elif work == 1 :
            list_food()
        else : 
            pass

# menu 2 รายการสั่งเครื่องดื่ม
def menu_drink() :
    while True :
        print("\n[รายการสั่งเครื่องดื่ม]")
        if work == 0 :
            return 0
        elif work == 2 :
            list_drink()
        else :
            pass

# menu 3 รายสุ่มอาหาร
def menu_foodrand() :
    while True :
        print("\n[รายการสุ่มอาหาร]")
        if work == 0 :
            return 0
        elif work == 3 :
            rand_food()
        else :
            pass

# menu 4 รายสุ่มเครื่องดื่ม
def menu_foodrand() :
    while True :
        print("\n[รายการสุ่มอาหาร]")
        if work == 0 :
            return 0
        elif work == 4 :
            rand_drink()
        else :
            pass

# function 1 รายการสั่งอาหาร
def list_food() :
    print("\n[เลือกเมนูอาหาร]")
    print("<<เมนูอาหารประเภทจานเดียว>>")
    print("กด 1 : ข้าวผัดรวมมิตร 50 บาท  ","กด 2 : ข้าวผัดคะน้าหมูกรอบ 50 บาท  ","กด 3 : ข้าวผัดกะเพราหมูสับ 40 บาท  ","กด 4 : ข้าวหมูทอดกระเทียม 40 บาท")
    print("<<เมนูอาหารประเภทผัด/ทอด>>")
    print("กด 5 : ทอดมันกุ้ง 55 บาท  ","    กด 6 : กุ้งชุบแป้งทอด 55 บาท  ","     กด 7 : ผัดผงกะหรี่ 65 บาท  ","       กด 8 : ผัดฉ่าทะเล 65 บาท  ")
    print("<<เมนูอาหารประเภทต้ม>>")
    print("กด 9 : ต้มจืดหมูสับ 50 บาท  ","  กด 10 : ต้มโคล้งหม้อไฟ 50 บาท  ","   กด 11 : ซุปเปอร์ตีนไก่หม้อไฟ 60 บาท  "," กด 12 : ต้มยำทะเล 60 บาท  ")
    print("กด 0 : เมื่อคุณยืนยันจะสั่งเมนู")

    sum_food = 0
    item = 1
    while item > 0 :
        item = int(input("เลือกเมนูอาหาร : "))
        if item == 1 or item == 2 :
            sum_food += 50
        elif item == 3 or item == 4 :
            sum_food += 40
        elif item == 5 or item == 6 :
            sum_food += 55
        elif item == 7 or item == 8 :
            sum_food += 65
        elif item == 9 or item == 10 :
            sum_food += 50
        elif item == 11 or item == 12 :
            sum_food += 60
        elif item == 0 :
            break
        else :
            print("ไม่มีอาหารที่คุณเลือก")
    print("รวมราคาทั้งหมด",sum_food,"บาท")
    while sum_food != 0 :
        print("\n<<เมนูคิดเงิน>>") 
        cash = int(input("เงินสด : "))
        if cash < sum_food :
            print("ยอดเงินของคุณไม่เพียงพอ กรุณากรอกใหม่อีกครั้ง")
        elif cash >= sum_food :
            change = cash - sum_food
            break
    print("เงินทอน ", change , "บาท")

# function 2 รายการเครื่องดื่ม
def list_drink() :
    print("\n[เลือกเมนูเครื่องดื่ม]")
    print("<<เมนูเครื่องดื่มประเภทร้อน>>")
    print("กด 1 : อเมริกาโน่ 30 บาท  ","      กด 2 : เอสเพรสโซ่ 30 บาท  ","      กด 3 : มอคค่า 30 บาท  ","        กด 4 : ลาเต้ 30 บาท  ")
    print("<<เมนูเครื่องดื่มประเภทเย็น")
    print("กด 5 : ชาไทยเย็น 30 บาท ","       กด 6 : ชาเขียวเย็น 30 บาท ","       กด 7 : นทสดเย็น 30 บาท ","       กด 8 : โอวัลตินเย็น 30 บาท ")
    print("<<เมนูเครื่องดื่มประเภทปั่น>>") 
    print("กด 9 : นมหมีโอวัลตินปั่น 35 บาท ","  กด 10 : นมหมีสตอเบอรี่ปั่น 35 บาท ","   กด 11 : นมหมีน้ำผึ้งปั่น 40 บาท ","   กด 12 : นมหมีบราวชูก้าปั่น 40 บาท ")
    print("กด 0 : เมื่อคุณยืนยันจะสั่งเมนู")
    sum_food = 0
    item = 1
    while item > 0 :
        item = int(input("เลือกเมนูอาหาร : "))
        if item == 1 or item == 2 :
            sum_food += 30
        elif item == 3 or item == 4 :
            sum_food += 30
        elif item == 5 or item == 6 :
            sum_food += 30
        elif item == 7 or item == 8 :
            sum_food += 30
        elif item == 9 or item == 10 :
            sum_food += 35
        elif item == 11 or item == 12 :
            sum_food += 40
        elif item == 0 :
            break
        else :
            print("ไม่มีเครื่องดื่มที่คุณเลือก")
    print("รวมราคาทั้งหมด",sum_food,"บาท")
    while sum_food != 0 :
        print("\n<<เมนูคิดเงิน>>") 
        cash = int(input("เงินสด : "))
        if cash < sum_food :
            print("ยอดเงินของคุณไม่เพียงพอ กรุณากรอกใหม่อีกครั้ง")
        elif cash >= sum_food :
            change = cash - sum_food
            break
    print("เงินทอน ", change , "บาท")

# function 3 รายการสุ่มอาหาร
def rand_food():
    print("\n[รายการสุ่มอาหาร]")
    randfood = ["ข้าวผัดกะเพราหมูสับ","ข้าวผัดรวมมิตร","ข้าวผัดคะน้าหมูกรอบ","ข้าวผัดพริกแกง","ข้าวไข่เจียวหมูสับ","ข้าวหมูทอดกระเทียม","ผัดมาม่า","สุกี้น้ำทะเล","ต้มยำทะเล","ผัดซีอิ๋ว","ราดหน้าทะเลกรอบ","แกงจืดเต้าหู้หมูสับ","ผัดไทยทะเล"]        
    guess = random.randint(0,len(randfood)-1)
    print(f'ยินดีด้วยคุณสุ่มได้ : {randfood[guess]}')

# function 4 รายการสุ่มเครื่องดื่ม
def rand_drink():
    print("\n[รายการสุ่มเครื่องดื่ม]")
    randdrink = ["ชาไทย","ชาเขียว","ชาเขียว","โกโก้","กาแฟเย็น","สตรอเบอรี่โยเกิร์ต","โอวัลตินเย็น","นมสด","ชามะนาว","โอเลี้ยง","ช็อคโกแลตเย็น","แดงมะนาวโซดา","บลูฮาวายเย็น"]  
    guess = random.randint(0,len(randdrink)-1)
    print(f'ยินดีด้วยคุณสุ่มได้ : {randdrink[guess]}')   

#ทักทาย
def meet(name) :
    print(f'<<ร้านข้าวfood4u>>\n ยินดีต้อนรับคุณ {name}')
    print()

#ขอบคุณ
def farewell(name) :
    print()
    print(f"ขอบคุณ คุณ {name} ที่อุดหนุน\n")
    print("-----ร้าน food4u-----")

#ชื่อ
name = input("ชื่อลูกค้า : ")
meet(name)

#วนLoopรับค่า menu หลัก
while True :
    mainmenu()
    work=int(input("เลือกหัวข้อเพื่อทำงาน : "))
    if work == 0 :
        farewell(name)
        break
    elif work==1:
        if list_food() == 0:
            farewell(name)
            break
    elif work==2:
        if list_drink() == 0:
            farewell(name)
            break
    elif work==3:
        if rand_food() == 0:
            farewell(name)
            break
    elif work==4:
        if rand_drink() == 0:
            farewell(name)
            break
    else :
        pass
