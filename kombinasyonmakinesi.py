kom1 = int(input("Kombinasyon için 1.sayı:"))
komfak1 = 1
for i in range(kom1):
    komfak1 = komfak1* (i+1)

kom2 = int(input("Kombinasyon için 1.sayı:"))
komfak2 = 1
for i in range(kom2):
    komfak2 = komfak2* (i+1)

kom2_kom1fak = 1
for i in range(kom1-kom2):
    kom2_kom1fak = kom2_kom1fak* (i+1)

komsonuç = komfak1/(komfak2*kom2_kom1fak)

print("kombinasyon:", komsonuç)
