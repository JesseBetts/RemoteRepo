#age guessing machine
import random
max = 30
min = 15


print("Please enter your name:")
name = input()
print(f"Hello, {name}! I am going to guess your age!")

while True: 
    rnd = random.randint(min, max)
    print(f"Are you {rnd} years old?")
    user_input = input()
    
    if user_input == "y":
        print(f"I win! You are {name} and you are {rnd} years old!!")
        break
    else :
        print("Rats! I will try again.")
        print(f"Give me a hint. Are you older or younger than {rnd}?")
        hint =input()
        if hint == "older":
            min = rnd
        elif hint == "younger":
            max = rnd
      