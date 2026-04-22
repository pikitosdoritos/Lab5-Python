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
print("Task 1")

list_1 = []
list_2 = []

for _ in range(8):
    list_1.append(random.randint(-3, 5))

for _ in range(10):
    list_2.append(random.randint(2, 10))

print(f"list_1: {list_1}")
print(f"list_2: {list_2}")

# tuple_1 (модулі)
tuple_1 = []
for num_a in list_1:
    if num_a < 0:
        tuple_1.append(-num_a)
    else:
        tuple_1.append(num_a)

tuple_1 = tuple(tuple_1)
print(f"tuple_1: {tuple_1}")

# спільні числа
common_list = []
for num_b in list_1:
    if num_b in list_2:
        common_list.append(num_b)

print(f"Спільні числа: {common_list}")

# спільні без дублікатів
common_unique = []
for num_c in list_1:
    if num_c in list_2 and num_c not in common_unique:
        common_unique.append(num_c)

common_unique = tuple(common_unique)
print(f"Спільні без дублікатів (tuple): {common_unique}")

# є в list_2, але нема в list_1
only_list2 = []
for num_d in list_2:
    if num_d not in list_1:
        only_list2.append(num_d)

print(f"Є в list_2, але нема в list_1: {only_list2}")

# парні спільні
even_common = []
for num_e in list_1:
    if num_e in list_2 and num_e % 2 == 0:
        if num_e not in even_common:
            even_common.append(num_e)

even_common = tuple(even_common)
print(f"Парні спільні (tuple): {even_common}")

# є в list_1, нема в list_2 і > 3
only_list1_gt3 = []
for num_f in list_1:
    if num_f not in list_2 and num_f > 3:
        only_list1_gt3.append(num_f)

print(f"Є в list_1, нема в list_2 і > 3: {only_list1_gt3}")


# 2
# Дано список значень різних типів даних.
# Створити словник, де ключами є елементи списку,
# а значеннями — назви їх типів даних.
# У словнику можуть бути присутні дані одного типу.
# Надрукувати вміст словника у вигляді:
# <class 'тип'> значення1 значення2 ...

print("==" * 80)
print("Task 2")

data_list = [
    1952, 1000000,
    10.45, 5.5,
    (2+3j),
    False,
    "pythonguide.pp.ua",
    (1, -6),
    [3, 15],
    {'Class C': ['Volkswagen Golf', 'Ford Focus'],
     'Class F': ['Audi A8', 'Bentley', 'Maybach'],
     'E': ['Toyota Camry']},
    None
]

grouped = {}

for item in data_list:
    type_name = type(item).__name__

    if type_name not in grouped:
        grouped[type_name] = []

    grouped[type_name].append(item)

for type_name in grouped:
    print(f"<class '{type_name}'>", end=" ")
    for val in grouped[type_name]:
        print(val, end=" ")
    print()
    
# 3
# Написати програму для створення словника з рядка для підрахунку кількості букв.
# Ключі — букви, значення — кількість входжень.
# Ігнорувати пробіли та пунктуацію, великі/малі літери однакові.
# Вивести:
# - довжину словника і всі пари ключ-значення;
# - кількість входжень букв a, j;
# - найчастішу і найрідшу букву;
# - додати відсутні букви зі значенням 0.

print("==" * 80)
print("Task 3")

text = """Take the first step in faith. You don't have to see the whole staircase,
just take the first step. Only two things are infinite — the universe and human stupidity,
and I'm not sure about the former"""

letter_counts = {}

# підрахунок букв
for ch in text:
    if ch.isalpha():
        ch_low = ch.lower()
        if ch_low in letter_counts:
            letter_counts[ch_low] += 1
        else:
            letter_counts[ch_low] = 1

# додати відсутні букви
for code in range(ord('a'), ord('z') + 1):
    letter = chr(code)
    if letter not in letter_counts:
        letter_counts[letter] = 0

# довжина і пари
print(f"Довжина словника: {len(letter_counts)}")
for key in letter_counts:
    print(f"{key}: {letter_counts[key]}")

# a, j
print(f"a: {letter_counts['a']}")
print(f"j: {letter_counts['j']}")

# найчастіша і найрідша
max_letter = None
min_letter = None

for key in letter_counts:
    if max_letter is None or letter_counts[key] > letter_counts[max_letter]:
        max_letter = key
    if min_letter is None or letter_counts[key] < letter_counts[min_letter]:
        min_letter = key

print(f"Найчастіша літера: {max_letter} ({letter_counts[max_letter]})")
print(f"Найрідша літера: {min_letter} ({letter_counts[min_letter]})")

# 4
# Дано два словники з ключами (букви) і значеннями (цілі числа).
# - надрукувати спільні пари «ключ-значення»;
# - надрукувати ключі, що є в першому словнику, але відсутні в другому;
# - об’єднати два словники в один.

print("==" * 80)
print("Task 4")

dict_a = {'x': 1, 'y': 2, 'z': 3}
dict_b = {'w': 10, 'x': 1, 'y': 2}

# 1) спільні пари
common_pairs = {}

for key_a in dict_a:
    if key_a in dict_b and dict_a[key_a] == dict_b[key_a]:
        common_pairs[key_a] = dict_a[key_a]

print("Спільні пари:", common_pairs)

# 2) ключі, що є в dict_a, але нема в dict_b
only_keys = []

for key_b in dict_a:
    if key_b not in dict_b:
        only_keys.append(key_b)

print("Ключі тільки з dict_a:", end=" ")
for k in only_keys:
    print(k, end=" ")
print()

# 3) об’єднання словників
merged_dict = {}

for key_c in dict_a:
    merged_dict[key_c] = dict_a[key_c]

for key_d in dict_b:
    merged_dict[key_d] = dict_b[key_d]

print("Об'єднаний словник:", merged_dict)