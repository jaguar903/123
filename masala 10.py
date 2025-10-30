son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
son3 = int(input("3-sonni kiriting: "))

sonlar = [son1, son2, son3]

birinchi = sonlar.pop(0)  
sonlar.append(birinchi)    


yigindi = sonlar[0] + sonlar[1]


print("0 va 1-indexdagi sonlarning yig'indisi:", yigindi)
print("Yakuniy ro'yxat:", sonlar)
