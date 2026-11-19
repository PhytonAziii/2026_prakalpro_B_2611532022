last_digit = 2
daily_limit = 30000 + last_digit * 1000
expenses = []

# Membaca 7 pengeluaran
for i in range(7):
    expense = int(input(f"Day {i+1}: "))
    expenses.append(expense)

# Menghitung total dan mencari pengeluaran tertinggi
total = 0
highest = expenses[0]
highest_day = 1
above_limit = 0

for i in range(7):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        above_limit += 1

average = total / 7

# Menampilkan hasil
print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print("Highest: day", highest_day, f"({highest})")
print("Days above limit:", above_limit)