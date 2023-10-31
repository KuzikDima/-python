numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифмети
numbers [4] = 0
su_m = sum(numbers)
le_n = len(numbers)
numbers [4] = su_m / le_n
print("Измененный список:", numbers)
