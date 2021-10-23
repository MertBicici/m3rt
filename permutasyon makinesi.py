per1 = int(input("permutasyon için 1.sayı:"))
deger = 1
for i in range(per1):
    deger = deger * (i+1)
 
print("Faktoriyel : ", deger)


per2 = int(input("permutasyon için 2.sayı:"))
deger2 = 1
for i in range(per1-per2):
    deger2 = deger2 * (i+1)
 
personuc = deger/ deger2

print("Permutasyon sonuc: ", personuc)