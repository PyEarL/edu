# message = input("Tell me something, ans I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = input('How old are you? ')
age = int(age)
print(age)

height = input('How tall are you, in santimeters? ')
height = int(height)
if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little taller.")

number = input("Enter a number, and I'll tell you if it's even ot odd: ")
number = int(number)
if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
