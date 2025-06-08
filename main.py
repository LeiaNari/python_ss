import random

min_number = 1
max_number = 100
max_attempts = 7

print("Вітаю! Я загадав число від 1 до 100.")
print(f"Спробуйте вгадати його за {max_attempts} спроб.")

computer_number = random.randint(min_number, max_number)

for attempt in range(1, max_attempts + 1):
    print(f"Ваша спроба №{attempt}")
    guess = int(input("Введіть ваше припущення: "))

    if guess < computer_number:
        print("Занадто маленьке!")
    elif guess > computer_number:
        print("Занадто велике!")
    else:
        print(f"Ви вгадали. Це число {computer_number}.")
        break

else:
    print("На жаль, ви не вгадали. Спроби закінчились.")
    print(f"Я загадав число {computer_number}.")
