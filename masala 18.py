
baho = int(input("0 dan 100 gacha bo'lgan raqam kiriting: "))
if 0 <= baho <= 55:
    print("Qoniqarsiz")
elif 56 <= baho <= 70:
    print("Qoniqarli")
elif 71 <= baho <= 85:
    print("Yaxshi")
elif 86 <= baho <= 100:
    print("A'lo")
else:
    print("Iltimos, 0 dan 100 gacha bo'lgan raqam kiriting.")
