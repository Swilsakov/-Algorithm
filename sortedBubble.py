# Сортировка пузырьком

# Ввод с задания
# n = int(input())
# mas = list(map(int,input().split()))

mas = [5,6,2,9,1,6,4,6,3]
n = len(mas)
count = 0

for run in range(n-1):
    for i in range(n-1-run):
        # print(f'Сравнивается {mas[i]} c {mas[i+1]}')
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]
    # print(mas)

# for i in mas:
#     print(i, end=' ')
print(*mas)
print("Количество перемещений:", count)