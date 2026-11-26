absen = input(). split()
pengumpulan = input(). split()

belum = set(absen) - set(pengumpulan)

submitted= len(pengumpulan)
not_submitted = len (set(absen) - set(pengumpulan))

print ("submitted:", submitted, "students")
print ("not submitted:", not_submitted, "students")

for not_submitted in belum:
    print(not_submitted)
