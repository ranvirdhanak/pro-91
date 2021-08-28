number = input("guess the number: ")

print(number)

number = 0

for i in number:
    number = number + 1


print(number)

# While loop to count the number of chances

while chances < 5:

if guess == number:
# if number entered by user is same as the generated
# number by randint function then break from loop using loop
# control statement "break"
print("CONGRATULATIONS YOU WON!!!")
break

if not chances < 5:
print("YOU LOSE!!! The number is", number)
