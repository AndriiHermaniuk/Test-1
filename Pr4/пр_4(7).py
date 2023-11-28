array = [3, -5, 0, 8, -2, 4, -6, 7, -1, 9, 0, -4]
modified_array = [abs(x) if x < 0 else x for x in array]
print("Заданий масив:", array)
print("Отриманий масив:", modified_array)
