import random

pc_num = random.randint(0, 100)
count = 1
game_count = 0
print(pc_num)
best_result = 101
best_game=0
while True:
    game_count += 1
    while True:
        if count == 6:
            print("попытки израсходованы. Вы проиграли")
            break
        n = int(input("введите число"))
        if pc_num == n:
            print(f"вы угадали за {count} раз")
            if best_result > count:
                best_result = count
                best_game=game_count
            break
        elif pc_num < n:
            print("загаданное число меньше")
        else:
            print("загаданное число больше")
        count += 1
    again = input("введите y если хотите сыграть еще? ")
    if again != "y":
        break
print(f"ваш лучший результат {best_result} был в игре № {best_game}\n"
      f"количество сыгранных партий {game_count}")
