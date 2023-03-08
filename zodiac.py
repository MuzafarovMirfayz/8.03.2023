def zodiac(sana):
    try:
        a = sana.split('.')[:2]
        if 0<int(a[0])<32 and 0<int(a[1])<13:
            if int(a[1])== 1:
                if 1 <= int(a[0]) <= 20:print("Uloq")
                else:print("Kova")
            elif int(a[1]) == 2:
                if int(a[0]) <= 29:
                    if 1<= int(a[0]) <= 19:print("Kova")
                    else:print("Baliq")
                else: print(f"fevralda {a[0]}-kun yo'q")
            elif int(a[1])== 3:
                if 1<= int(a[0]) <=20:print("Baliq")
                else:print("Qo'y")
            elif int(a[1]) == 4:
                if 1<= int(a[0]) <= 20:print("Qo'y")
                else:print("Toros")
            elif int(a[1])==5:
                if 1 <= int(a[0]) <= 21:print("Toros")
                else:print("Egizak")
            elif int(a[1])==6:
                if 1<= int(a[0]) <=21:print("Egizak")
                else:print("Saraton")
            elif int(a[1])==7:
                if 1<= int(a[0]) <=22:print("Saraton")
                else:print("Leo")
            elif int(a[1])==8:
                if 1<= int(a[0]) <= 21: print("leo") 
                else: print("Bokira")
            elif int(a[1])==9:
                if 1<= int(a[0]) <= 23: print("Bokira") 
                else: print("Tarozi")
            elif int(a[1])==10:
                if 1<= int(a[0]) <= 23: print("Tarozi") 
                else: print("Chayon")
            elif int(a[1])==11:
                if 1<= int(a[0]) <= 22: print("Chayon") 
                else: print("O'q otar")
            elif int(a[1])==12:
                if 1<= int(a[0]) <= 22: print("O'q otar") 
                else: print("Uloq")   
        else:
            print("Bunday sana mavjud emas")     
    except:
        print("Notogri ma'llumot kiritingiz")
zodiac(input())