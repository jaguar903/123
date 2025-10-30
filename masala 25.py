import random
import time

def send_otp_sim(phone):
    """OTP ni simulyatsiya qilib yaratadi va terminalga chiqaradi (dev-mode)."""
    code = f"{random.randint(100000, 999999)}"
    print(f"[DEBUG] SMS yuborildi {phone} raqamiga. OTP: {code}")
    return code

print("Bankomatga xush kelibsiz\n")

print("Bankomat 2 ta kartani qo`llab-quvvatlaydi: 1) humo  2) uzcard")
turi = input("Qanday karta kiritasiz (humo/uzcard) >> ").strip().lower()

if turi not in ("humo", "uzcard"):
    print("Noto'g'ri karta turi. Dastur tugaydi.")
    exit()

karta = input("Karta raqamini kiriting (12 raqam) : ").strip()
if len(karta) != 12 or not karta.isdigit():
    print("Karta raqami 12 ta raqamdan iborat bo'lishi kerak. Dastur tugaydi.")
    exit()

phone = input("Hozirgi SMS bilan bog'langan telefon raqami (masalan +998901234567) kiriting: ").strip()

pin = input("Karta parolini kiriting (4 ta raqam): ").strip()
if len(pin) != 4 or not pin.isdigit():
    print("Parol 4 ta raqam bo'lishi kerak. Dastur tugaydi.")
    exit()

if turi == "uzcard":
    hisob = 500_000
else:
    hisob = 300_000
while True:
    print("\nXizmatlar:")
    print("1) Pin kodni o`zgartirish")
    print("2) Hisobni ko'rish")
    print("3) Hisobdan pul yechish")
    print("4) SMS bilan bog'langan telefonni o'zgartirish")
    print("5) Chiqish")

    try:
        xizmatlar = int(input("Xizmat raqamini kiriting: "))
    except ValueError:
        print("Iltimos, raqam kiriting.")
        continue

    if xizmatlar == 1:
        eski_parol = input("Eski parolni kiriting: ").strip()
        if eski_parol != pin:
            print("Parol xato.")
        else:
            yangi_parol = input("Yangi 4 xonali parol kiriting: ").strip()
            if len(yangi_parol) == 4 and yangi_parol.isdigit():
                pin = yangi_parol
                print("Parol muvaffaqiyatli o'zgardi.")
            else:
                print("Parol 4 ta raqam bo'lishi kerak. O'zgarmadi.")

    elif xizmatlar == 2:
        print(f"Hisobingizda {hisob} so'm mavjud.")

    elif xizmatlar == 3:
        print("Yechishingiz mumkin bo'lgan summalar:")
        print("1) 50000")
        print("2) 200000")
        print("3) 400000")
        print("4) Boshqa summa")

        tanla = input("Summalardan birini tanlang (1/2/3/4): ").strip()
        if tanla == "1":
            ayir = 50000
        elif tanla == "2":
            ayir = 200000
        elif tanla == "3":
            ayir = 400000
        elif tanla == "4":
            try:
                kirit = input("Xohlagan summani kiriting: ").strip()
                ayir = int(kirit)
            except ValueError:
                print("Noto'g'ri summa kiritildi.")
                continue
        else:
            print("Noto'g'ri tanlov qildingiz!")
            continue

        if ayir > hisob:
            print("Hisobingizda mablag' yetarli emas!")
        else:
            hisob -= ayir
            print(f"Operatsiya muvaffaqiyatli. Hisobingizda {hisob} so'm qoldi.")

    elif xizmatlar == 4:
        if turi == "humo":
            print("Eslatma: HUMO kartalar uchun SMS bilan bog'langan raqamni o'zgartirish cheklangan.")
            continue

        print("Uzcard aniqlandi. Telefon raqamini o'zgartirish uchun OTP yuboramiz.")
        yangi_phone = input("Yangi telefon raqamini kiriting (masalan +998901234567): ").strip()
        otp = send_otp_sim(yangi_phone)
        attempts = 3
        verified = False
        while attempts > 0:
            kir_otp = input("SMSdagi 6 xonali kodni kiriting: ").strip()
            if kir_otp == otp:
                verified = True
                break
            else:
                attempts -= 1
                print(f"Noto'g'ri kod. Qolgan urinishlar: {attempts}")
        if verified:
            phone = yangi_phone
            print(f"Telefon raqami muvaffaqiyatli o'zgartirildi. Yangi raqam: {phone}")
        else:
            print("SMS kod tekshirilmadi. Telefon raqami o'zgarmadi.")

    elif xizmatlar == 5:
        print("Foydalanganingiz uchun rahmat. Xayr!")
        break

    else:
        print("Noto'g'ri tanlov. Qayta urinib ko'ring.")
