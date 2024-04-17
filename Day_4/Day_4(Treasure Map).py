row1 = ["🏻", "🏻", "🏻"]
row2 = ["🏻", "🏻", "🏻"]
row3 = ["🏻", "🏻", "🏻"]

map = [row1, row2, row3]
print(f"{map[0]}\n{map[1]}\n{map[2]}")
loc = int(input("Enter the location : "))-11

i = loc % 10
j = loc // 10

map[j][i] = "☠️"

print(f"{map[0]}\n{map[1]}\n{map[2]}")
