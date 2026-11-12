# Nama: Malika Azizah Muskhir
# Nim: 2611532022
# Question 3

# soal3.py (A)
text = "Informatika"
print(text[-1])
print(text.upper())
print(text[0:20])

#soal3.py (B)
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)