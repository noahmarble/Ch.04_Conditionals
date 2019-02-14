print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.upper() == "A" or user_input.lower() == "jedi master":
    sensitivity = 1000
elif user_input.upper() == "B" or user_input.lower() == "sith lord":
    sensitivity = 900
elif user_input.upper() == "C" or user_input.lower() == "droid":
    sensitivity = 0

print("sensativity is:",sensitivity)