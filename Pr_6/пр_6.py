import math

def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        numbers = file.readline().split()
        if len(numbers) < 1:
            raise ValueError("Недостатньо даних у файлі")

        x = float(numbers[0])
        x_rad = math.radians(x)
        t = (x * math.sin(x_rad) ** 5 - math.cos(x_rad) / math.cos(x_rad + 3.23) + 7)
        y = 1 + 1 / t ** 2 + 1
    return x, t, y

try:
    result = data()
    result_str = f"x: {result[0]}\n t: {result[1]}\n y: {result[2]}"
    print(result_str)

    with open("output.txt", 'w') as f:
        f.write(result_str)
except ValueError as e:
    print(f"Помилка: {e}")
