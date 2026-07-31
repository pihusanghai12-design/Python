
snack_box1 = {"Burger", "Pizza", "sandwich", "Momo", "Fench fries"}
snack_box2 = {"cookies", "sandwich", "juice", "sandwich"}
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)

snack_box1.add("Chips")
print("Snack Box 1 after adding chips:", snack_box1)

# PART 3: Find snacks common to both boxes
common_snacks = snack_box1.intersection(snack_box2)
print("Snacks in both boxes:", common_snacks)


import array as arr
snack_counts = arr.array('i', [3, 5, 2, 4])
print("Snack counts array:", snack_counts)


snack_counts.insert(0, 3)
snack_counts.append(6)
print("Snack counts after adding items:", snack_counts)


count_of_4 = snack_counts.count(4)
print("Number of times 4 appears:", count_of_4)


snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)


