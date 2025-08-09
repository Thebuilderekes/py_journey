import random

customers = ["john", "james", "jose"]
winner = random.choice(customers)

prompt = "do you want topinng with that?"

check = input(prompt)

if(check == 'yes'):
     print(winner + " asked for topping")

