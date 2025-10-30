# Boshlang'ich ro'yxat
narxlar = [15000, 8500, 12000]

# Ro'yxat boshiga foydalanuvchidan qiymat kiritamiz
yangi_narx = int(input("Yangi narxni kiriting: "))
narxlar.insert(0, yangi_narx)  # boshiga qo'shamiz

# Oxirgi elementni o'chiramiz
narxlar.pop()

# Umumiy qiymatni hisoblaymiz
umumiy = sum(narxlar)

# Natijani chiqaramiz
print("Yangilangan ro'yxat:", narxlar)
print("Umumiy qiymat:", umumiy)
