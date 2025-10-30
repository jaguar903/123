a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))


yigindi = a + b
ayirma = a - b
kopaytma = a * b


if b != 0:
    bolinma = a / b
else:
    bolinma = "Bo'lish mumkin emas (0 ga bo'linmaydi)"

print(f"Yig'indisi: {yigindi}")
print(f"Ayirmasi: {ayirma}")
print(f"Ko'paytmasi: {kopaytma}")
print(f"Bo'linmasi: {bolinma}")