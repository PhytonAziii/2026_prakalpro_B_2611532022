
schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a
busiest_day = ""
max_courses = 0

for day in schedule:
    count = len(schedule[day])

    if count > max_courses:
        max_courses = count
        busiest_day = day

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 6b
course = input("Enter course name: ")
total = 0

for day in schedule:
    if course in schedule[day]:
        total += 1

print(f"{course}: {total} days")