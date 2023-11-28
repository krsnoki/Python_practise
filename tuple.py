tup = (12, 23, 36, 24)

for i in range(0, len(tup)):
    print(tup[i], end=" ")

print("\n")

li = ["up", "down", "left", "right"]
t = [12, 23, 36, 24]
li.append(t)

tup = tuple(li)
print(tup)