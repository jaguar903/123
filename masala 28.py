import sys, getpass

maxs = {"Olma":5000,"Banan":10000,"Anor":12000,"Nok":15000,"Tarvuz":16000,"Apelsin":20000,"Kivi":8000}
print("Mini marketga xush kelibsiz!")
print("Mavjud:", ", ".join(f"{k}({v})" for k,v in maxs.items()))

tanlangan = {}
for i in range(3):
    while True:
        nom = input(f"{i+1}-chi mahsulot: ").title()
        if nom in maxs: break
        print("Mavjud emas.")
    while True:
        try:
            m = int(input(f"{nom} nechta? "))
            if m>0: break
        except: pass
        print("Musbat butun son kiriting.")
    tanlangan[nom] = tanlangan.get(nom,0) + m

chegirma = 0
jami = sum(maxs[n]*q for n,q in tanlangan.items())
if jami > 100000:
    chegirma = int(jami * 0.10)
    jami -= chegirma

print("\n--- Hisob ---")
for n,q in tanlangan.items():
    narx = maxs[n]
    print(f"{n}: {q} dona x {narx} = {narx*q} so'm")
print(f"Chegirma: {chegirma} so'm")
print(f"To'lanishi kerak: {int(jami)} so'm")

kart_bal = {"Uzcard":300000,"Humo":200000}
kart_pin = {"Uzcard":"1111","Humo":"2222"}

typ = input("\nTo'lov (Naqt/Karta): ").strip().lower()
if typ == "naqt":
    print("Naqt qabul qilindi. Rahmat!")
else:
    while True:
        k = input("Karta turi (Uzcard/Humo): ").title()
        if k in kart_bal: break
    knum = input("Karta raqami kiriting: ").strip()
    if len(knum) < 12 or not knum.isdigit():
        print("Karta raqami noto'g'ri. Dastur to'xtadi."); sys.exit()
    ok = False
    for i in range(3):
        if getpass.getpass("PIN: ") == kart_pin[k]:
            ok = True; break
        print("PIN xato.")
    if not ok:
        print("PIN 3 marta xato. To'lov amalga oshmadi.")
    else:
        if kart_bal[k] >= jami:
            kart_bal[k] -= int(jami)
            print(f"To'lov muvaffaqiyatli. Qolgan balans: {kart_bal[k]} so'm")
        else:
            print(f"Hisobda yetarli pul yo'q ({kart_bal[k]} so'm).")
