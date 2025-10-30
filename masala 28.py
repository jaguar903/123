print("Mini marketga xush kelibsiz!")

maxsulotlar = {
    "Olma": 5000,
    "Banan": 10000,
    "Anor": 12000,
    "Nok": 15000,
    "Tarvuz": 16000,
    "Apelsin": 20000,
    "Kivi": 8000
}

print("Bizda mavjud maxsulotlar:")
for nom, narx in maxsulotlar.items():
    print(f" - {nom}: {narx} so'm/kg")

tanlangan = {}

for i in range(3):
    while True:
        a = input(f"{i+1}-chi maxsulotni tanlang: ").title()
        if a in maxsulotlar:
            break
        else:
            print("Bunday mahsulot mavjud emas, boshqa tanlang.")
    
    while True:
        try:
            miqdor = int(input(f"{a} dan necha dona kerak? "))
            if miqdor > 0:
                break
            else:
                print("Iltimos, musbat son kiriting.")
        except ValueError:
            print("Iltimos, to'g'ri son kiriting.")
    
    tanlangan[a] = miqdor

print("Siz tanlagan mahsulotlar:")
umumiy_summa = 0
for nom, miqdor in tanlangan.items():
    narx = maxsulotlar[nom]
    summa = narx * miqdor
    umumiy_summa += summa
    print(f" - {nom}: {miqdor} dona x {narx} so'm = {summa} so'm")

if umumiy_summa > 100000:
    chegirma = umumiy_summa * 0.10
    umumiy_summa -= chegirma
    print(f"Umumiy summa 100,000 so'mdan oshgani uchun 10% chegirma qo'llanildi: -{int(chegirma)} so'm")

while True:
    tolov = input("To'lov turini tanlang (Naqt/Karta): ").strip().lower()
    if tolov in ["naqt", "karta"]:
        break
    else:
        print("Iltimos, faqat 'Naqt' yoki 'Karta' deb yozing.")

print(f"To'lov turi: {tolov.capitalize()}")
print(f"To'lanadigan summa: {int(umumiy_summa)} so'm")
print("\nXaridingiz uchun rahmat!")


if umumiy_summa > 100000:
    chegirma = umumiy_summa * 0.10
    umumiy_summa -= chegirma
    print(f"\nUmumiy summa 100,000 so'mdan oshgani uchun 10% chegirma qo'llanildi: -{int(chegirma)} so'm")

print(f"\nTo'lanadigan summa: {int(umumiy_summa)} so'm")

