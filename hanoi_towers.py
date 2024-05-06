game = {
    "A": [
        num
        for num in range(int(input("Введіть кількість елементів башти ===>  ")), 0, -1)
    ],
    "B": [],
    "C": [],
}

print(f"Початковий стан: {game}")


def move(start, end, game):
    print(f"Переміщуємо диск з колони {start} на колону {end}")
    game[end].append(game[start].pop())
    print(f"Проміжний стан: {game}")


def hanoi(amount, start, end, help):
    if amount == 1:
        move(start, end, game)
    else:
        hanoi(amount - 1, start, help, end)
        move(start, end, game)
        hanoi(amount - 1, help, end, start)


hanoi(len(game["A"]), "A", "C", "B")
print(f"Кінцевий стан: {game}")
