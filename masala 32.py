oylar = {
    1: "Yanvar", 2: "Fevral", 3: "Mart", 4: "Aprel",
    5: "May", 6: "Iyun", 7: "Iyul", 8: "Avgust",
    9: "Sentabr", 10: "Oktyabr", 11: "Noyabr", 12: "Dekabr"
}

oy = int(input("1 dan 12 gacha bo'lgan oy raqamini kiriting: "))

if oy in oylar:
    print(f"{oy}-chi oy: {oylar[oy]}")
else:
    print("Noto'g'ri raqam! 1-12 oralig'ida kiriting.")
