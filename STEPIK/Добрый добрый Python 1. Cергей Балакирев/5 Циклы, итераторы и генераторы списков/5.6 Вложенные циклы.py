# Большой подвиг 6.
# Вводится список целых чисел в одну строку через пробел.
# Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).

data = list(map(int, input().split()))

for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i] > data[j]:
            data[j], data[i] = data[i], data[j]

print(*data)




