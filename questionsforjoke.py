import random
Username = input("HelloHi! What is your name?")
number1 = random.randint(1, 30)
number2 = random.randint(31, 60)
number3 = random.randint(61, 100)
guess= int(input("What is your favourite number?:"))
joke1 = ("What do you call an ant that fights crime? A Vigilante.")
joke2 = ("What is brown, hairy and wears sunglasses? A coconut")
joke3 = ("What did the Dalmatian say after lunch? That hit the spot")
if guess<number1:
    print (joke1)
elif guess<number2:
    print (joke2)
elif guess<number3:
    print (joke3)
else:
    print("Sorry, try again later")