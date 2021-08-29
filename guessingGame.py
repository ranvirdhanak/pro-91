import random
rand = random.randint(1,9)




chances = 0



# While loop to count the number of chances

while chances < 5:
    number = int(input("guess the number: "))
    if rand == number:
# if number entered by user is same as the generated
# number by randint function then break from loop using loop
# control statement "break"
        print("CONGRATULATIONS YOU WON!!!")
        break
    elif number < rand:
        print("Guess a higher number")
    else:
        print("Guess a lower number")
    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)
