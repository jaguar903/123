
soz1 = input("1-so'zni kiriting: ")
soz2 = input("2-so'zni kiriting: ")
soz3 = input("3-so'zni kiriting: ")
royxat = [soz1, soz2, soz3]

royxat.append(soz1)

royxat.insert(0, soz2)

orta_index = len(royxat) // 2
royxat.insert(orta_index, soz3)

del royxat[2]

print("Yakuniy ro'yxat:", royxat)
