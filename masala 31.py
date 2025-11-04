n = int(input("1 dan n gacha bo'lgan sonlar uchun n ni kiriting: "))

for i in range(1, n+1):
    if i % 5 == 0:
        continue  
    print(f"{i}2 = {i**2}")
