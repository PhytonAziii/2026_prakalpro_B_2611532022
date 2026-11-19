menu = ["Nasi Goreng", "Mie Ayam", "Soto"]
days = 3
sales = []

# data penjualan
for i in range(days):
    row = []
    for j in range(len(menu)):
        value = int(input(f"Day {i+1}, {menu[j]}: "))
        row.append(value)
    sales.append(row)

# total penjualan setiap hari
print("Total per day:")
for i in range(days):
    total = 0
    for j in range(len(menu)):
        total += sales[i][j]
    print(f"Day {i+1}: {total}")

# total penjualan setiap menu
menu_totals = []

for j in range(len(menu)):
    total = 0
    for i in range(days):
        total += sales[i][j]
    menu_totals.append((menu[j], total))

print("Total per menu:", menu_totals)

# Mencari menu terlaris
best = menu_totals[0]

for item in menu_totals:
    if item[1] > best[1]:
        best = item

print("Best seller:", best)