
narxlar = [12000, 8000, 15000, 9000]
narx = int(input("Iltimos, bir narx kiriting: "))

if narx in narxlar:
    narxlar.remove(narx)
    print(f"{narx} ro'yxatdan o'chirildi.")
else:
    narxlar.append(narx)
    print(f"{narx} royxatga qo'shildi.")
print("Yakuniy ro'yxat:", narxlar)
