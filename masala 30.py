mevalar = {"Olma":5000, "Banan":10000, "Anor":12000}
umumiy = 0

print("Mevalar mavjud: Olma, Banan, Anor")
print("To'xtatish uchun 'exit' deb yozing")

while True:
    nom = input("Qaysi meva kerak? ").title()
    if nom.lower() == "exit":
        break
    if nom not in mevalar:
        print("Bunday meva mavjud emas!")
        continue
    try:
        miqdor = int(input(f"{nom} necha dona? "))
        if miqdor <= 0:
            print("Musbat son kiriting!")
            continue
    except:
        print("To'g'ri son kiriting!")
        continue
    umumiy += mevalar[nom] * miqdor
    print(f"{nom} qo'shildi. Hozirgi umumiy: {umumiy} so'm")

print(f"Xaridingiz tugadi. Umumiy summa: {umumiy} so'm")
