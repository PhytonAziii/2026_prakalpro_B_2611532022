# Nama: Malika Azizah Muskhir
# Nim: 2611532022
# Question 5

username = input("Username: ")

# A
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# B
# NIM valid jika terdiri atas 10 karakter dan semua digit
# Jika valid tampilkan Valid
# intake year 20xx dengan xx adalah dua digit pertama NIM
# jika invalid tampilkan Invalid

nim = input("Masukkan NIM: ")
if len(nim) == 10 and nim.isdigit():
    print("Valid")
    print("Tahun masuk: 20" + nim[:2])
else:
    print("Invalid NIM")