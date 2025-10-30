print("Bankomatga xush kelibsiz")

print("Bankomat 2 ta kartani qo`llab quvatlaydi 1) Humo 2) Uzcard")
turi = input("Qanday karta kiritasiz>> ")
if turi == "humo" or turi == "uzcard":
    karta = input("Karta raqamini kiriting: ")
    if len(karta) != 12:
        print("karta raqami 12 ta bo`lishi kerak")
    else:
        pin = input("karta parolini kiriting: ")
        print("parolni tog`ri kiritingiz")
        if turi == "uzcard":
            hisob = 500_000
        else:
            hisob = 300_000

            for i in range(5):
                print("xizmatlar:")
                print("1) pin kodni o`zgartirish")
                print("2) xisobni ko'rish")
                print("3) xisobdan pul yechish")
                print("4) chiqish")

                xizmatlar = int(input("xizmt raqamini kiriting: "))

                if xizmatlar == 1:
                    eski_parol = input("eski parolni kiriting: ")

                    if eski_parol != ping:
                        print("parol xato")
                    else:
                        yangi_parol = input  ("yangi parol kiriting: ")
                        if len(yangi_parol) ==4:
                            print("parol o'zgardi")
                            pin = yangi_parol

                elif xizmatlar == 2:
                    print(f"xisobingizda {hisob} so'm mavjud") 

                elif xizmatlar == 3:    
                    print("yechishingiz mumkin bo'lgan sumalar")
                    print("1) 50000")
                    print("2) 200000")
                    print("3) 400000")
                    print("4) boshqa summa")

                    tanla = input("summalardan birini tanlang: ") 

                    if tanla == "1":
                        ayir = 50000
                    elif tanla == "2":
                        ayir = 200000
                    elif tanla == "3":
                        ayir = 400000
                    elif tanla == "4":
                        kirit = input("xoxlagan summani kiriting: ")
                        ayir = int(kirit)
                    else:
                        print("noto'g'ri tanlov qildingiz!") 
                        ayir = 0
                        break

                    if ayir > hisob:
                        print("hisobingizda mablag' yetarli emas!")

                    else:
                        hisob = hisob - ayir

                        print(f"hisobingizda {hisob} so'm qoldi")

                elif xizmatlar == 4:
                    print("foydalanganingiz uchun rahmat")
                else:
                    print("noto'g'ri karta turini kiritdingiz")                                     