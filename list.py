list = [1, 2, 3, 4, 5, "Kalyani", 2.5, 0]
print("Actual list: ", list)

#copying list
l2 = list.copy()

#string reversal
for i in range(0, len(list)):
    list[i] = l2[-(i+1)]

print("List reversed: ", list)

list = []
for i in range(0, 4):
    list.append(int(input("enter list element:")))

print("List:", list)
