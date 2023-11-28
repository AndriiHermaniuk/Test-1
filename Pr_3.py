import random
print("Відгадайте число!")
a = random.randint(0, 101)
b = 0
while True:
    c = int(input("Введіть число: "))
    b += 1
    if c == a:
        print(f"Вітаємо, ви відгадали загадане число, це: {a}")
        print(f"Кількість спроб: {b}")
        break
    elif c < a:
        print("Трішки більше!")
    else:
        print("Трішки менше!")
print("Гра завершена!")
