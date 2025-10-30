
narxlar = [23000, 12000, 7500]
print("Boshlang'ich ro'yxat:", narxlar)

yangi_oxiri = int(input("Ro'yxat oxiriga qo'shmoqchi bo'lgan narxni kiriting: "))
narxlar.append(yangi_oxiri)

yangi_boshi = int(input("Ro'yxat boshiga qo'shmoqchi bo'lgan narxni kiriting: "))
narxlar.insert(0, yangi_boshi)

narxlar.pop()

print("Yakuniy ro'yxat:", narxlar)
