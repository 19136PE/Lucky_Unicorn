import random

#Main Routine Goes Here
balance = 100
#testing loop to generate 20 tokens
#chosen = random.choice(tokens)
for item in range(0, 20):
    token_number = random.randint(1, 100)
    if 1 <= token_number <= 10:
        chosen = "Unicorn"
    elif 11 <= token_number <= 42.0:
        chosen = "Donkey"
    else:
        if token_number % 2 == 0:
            chosen = "Horse"
        else:
            chosen = "Zebra"
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5
    print("token_number: {}, You Have ${} Left".format(chosen, balance ))
