n = int(input("son kiriting: "))
yigindi = 0 

for i in range (1,n+1):
    if i % 2 != 0:
        continue
    yigindi += i
    print("juft sonlar yigindisi:", yigindi)

