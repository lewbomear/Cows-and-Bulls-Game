import random

number = random.sample(range(0, 10), 4)
number_str = ''.join(map(str, number))

game_active = True

while game_active:
    while True:
        user_input = input("Input a four-digit number: ")

        if user_input.isdigit() and len(user_input) == 4:
            break
        else:
            print("Please enter a valid four-digit number.")

    user_number = [int(digit) for digit in user_input]

    bull_count = sum(1 for i, digit in enumerate(user_number) if digit == number[i])
    cow_count = sum(1 for digit in user_number if digit in number and digit != number[user_number.index(digit)])

    if bull_count == 4:
        game_active = False

    print(f"Bulls: {bull_count}, Cows: {cow_count}")

print(f"Congratulations! You've guessed the correct number: {number_str}")
