my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nummer2 = []
for nummer in my_list:
    if nummer not in nummer2:
        nummer2.append(nummer)
my_list = nummer2[:]
print("Nummer i listan", my_list)