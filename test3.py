import random

secret_number = random.randint(1,99)

while True:
    guess = int(input("Вгадайте число від 1 до 99\n"))
    if guess == secret_number:
        print("Ви угадали загадане число")
        break
    elif guess < secret_number:
        print("Ви не угадали загадане число, агадане число є більше")
    else:
        print("Ви не угадали загадане число, агадане число є менше")