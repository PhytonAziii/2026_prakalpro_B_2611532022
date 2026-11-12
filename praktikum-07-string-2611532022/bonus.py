# Nama: Malika Azizah Muskhir
# Nim: 2611532022
# Bonus

kalimat = input("Masukkan kalimat: ")
clean = kalimat.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")