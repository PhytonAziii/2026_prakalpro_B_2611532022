# Membuat peta kursi bioskop
number_of_rows = 4
seats_per_row = 5

cinema = [["."] * seats_per_row for _ in range(number_of_rows)]

seats_taken = 0

while True:
    # Menampilkan peta kursi
    for i in range(number_of_rows):
        print("Row", i + 1, ":", *cinema[i])

    row = int(input("Row (0 to stop): "))

    if row == 0:
        break

    seat = int(input("Seat: "))

    # Memeriksa nomor baris dan kursi
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")

    elif cinema[row - 1][seat - 1] == "X":
        print("Seat already taken.")

    else:
        cinema[row - 1][seat - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

# Menampilkan jumlah kursi yang sudah dipesan
print("Seats taken:", seats_taken)