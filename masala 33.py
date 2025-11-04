parol = input("Parol kiriting: ")

if len(parol) > 6 and "123" not in parol:
    print("Parol qabul qilindi")
else:
    print("Parol noto'g'ri! U 6 tadan uzun bo'lishi va '123' bo'lmasligi kerak.")
