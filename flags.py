prompt = "\nTell me something, ans I will repeat it back to you:"
prompt += "\nEnter 'exit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'exit':
        active = False
    else:
        print(message)

prompt_2 = "\nPlease enter the name of a city you have visited:"
prompt_2 += "\n(Enter 'exit' when you are finished.)"
while True:
    city = input(prompt_2)

    if city == 'exit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
        