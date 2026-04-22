# 1
# Згенерувати два списки випадкових цілих чисел:
# list_1 — 8 елементів з діапазону [-3, 5]
# list_2 — 10 елементів з діапазону [2, 10]
# На їх основі:
# - створити кортеж tuple_1, де від’ємні елементи list_1 замінені на модулі;
# - створити список чисел, що є в обох списках;
# - створити кортеж без дублікатів із чисел, що є в обох списках;
# - створити список чисел, що є в list_2 і відсутні в list_1;
# - створити кортеж парних чисел, що є в обох списках;
# - створити список чисел, що є в list_1, відсутні в list_2 і більші за 3.

import random

print("==" * 80)
print("Task 7")

list_1_task7 = []
list_2_task7 = []

for _ in range(8):
    list_1_task7.append(random.randint(-3, 5))

for _ in range(10):
    list_2_task7.append(random.randint(2, 10))

print(f"list_1: {list_1_task7}")
print(f"list_2: {list_2_task7}")

# tuple_1 (модулі)
tuple_1_task7 = []
for val_a in list_1_task7:
    if val_a < 0:
        tuple_1_task7.append(-val_a)
    else:
        tuple_1_task7.append(val_a)

tuple_1_task7 = tuple(tuple_1_task7)
print(f"tuple_1: {tuple_1_task7}")

# спільні числа (з повторами)
common_list_task7 = []
for val_b in list_1_task7:
    if val_b in list_2_task7:
        common_list_task7.append(val_b)

print(f"Спільні числа: {common_list_task7}")

# спільні без дублікатів (кортеж)
common_unique_task7 = []
for val_c in list_1_task7:
    if val_c in list_2_task7 and val_c not in common_unique_task7:
        common_unique_task7.append(val_c)

common_unique_task7 = tuple(common_unique_task7)
print(f"Спільні без дублікатів (tuple): {common_unique_task7}")

# є в list_2, але нема в list_1
only_list2_task7 = []
for val_d in list_2_task7:
    if val_d not in list_1_task7:
        only_list2_task7.append(val_d)

print(f"Є в list_2, але нема в list_1: {only_list2_task7}")

# парні спільні (кортеж)
even_common_task7 = []
for val_e in list_1_task7:
    if val_e in list_2_task7 and val_e % 2 == 0:
        if val_e not in even_common_task7:
            even_common_task7.append(val_e)

even_common_task7 = tuple(even_common_task7)
print(f"Парні спільні (tuple): {even_common_task7}")

# є в list_1, нема в list_2 і > 3
only_list1_gt3_task7 = []
for val_f in list_1_task7:
    if val_f not in list_2_task7 and val_f > 3:
        only_list1_gt3_task7.append(val_f)

print(f"Є в list_1, нема в list_2 і > 3: {only_list1_gt3_task7}")