print("Ali")

#fibonacci series

a = 0
b = 1
while a<10:
    print (a)
    a = b
    b = a+b

# type of data
name = 'Ali'
age = 18
height = 6.6
is_married = False
print(type(name))
print(type(age))
print(height)
print(type(is_married))

# type conversions
print(int(height))


#Problem 1: The Road Trip SplitterThe Scenario: 
# You and a friend went on a road trip. 
# You need to write a program that calculates how much gas money they owe you.
# Your Task: Write a Python script that does the following:
# Take Input: Ask the user for three things:The total distance driven (in miles or kilometers).
# The vehicle's fuel efficiency (miles per gallon or liters per 100km).
# The current price of gas per gallon/liter.
# Convert & Calculate: * Remember that user input always starts as a string! Convert these inputs to floats.
# Calculate the total cost of the gas used. (Formula: $(\text{Distance} \div \text{Efficiency}) \times \text{Price}$)
# Divide that total cost by 2 (since you're splitting it with your friend).
# Output: Use an f-string to print a message telling your friend exactly how much they owe you. Format it nicely so it looks like currency (e.g., "$24.5").
distance = float(input("Enter the total distance covered in (kms): "))
fuel_efficiency = float(input("Enter fuel efficiency per litre: "))
price =float(input("Enter the price per litre: "))
cost = (distance/fuel_efficiency)*price
split_cost = cost/2
print(f"Your friend owes you ${split_cost:.2f} for the gas used on the road trip.")


# Problem 2: The Digital ID Badge Generator
# The Scenario: You are building a quick registration tool for a tech conference. It needs to collect user data and format it into a standardized badge layout.

# Your Task: Write a Python script that does the following:

# Take Input: Ask the user for:

# Their first name.

# Their year of birth.

# Whether they are a speaker at the event (they should type True or False).

# Convert & Process: * Keep the name as a string.

# Convert the birth year to an integer, and calculate their approximate age (assume the current year is 2026).

# Convert their speaker status into a boolean type.

# Output: Use a single, multi-line f-string to print out a badge that looks exactly like this:

# Plaintext
# ==================================
# CONFERENCE BADGE: [Name Here]
# Age: [Calculated Age Here]
# VIP Speaker Access: [True/False Here]
# ==================================
first_name = input("Enter your first name: ")
birth_year = int(input("Enter birth year: "))
age = int(2026 - birth_year)
if(age>18):
    vip_access = True
else:
    vip_access = False

print(f"""Conference Badge: {first_name}
    Age: {age}
      VIP Speaker Access: {vip_access}""")




# ── IF / ELIF / ELSE ─────────────────────────
score = int(input("Enter your score: "))

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("Fail")

# ── OPERATORS ────────────────────────────────
x = 10
y = 20

print(x > y)           # False
print(x < y)           # True
print(x == y)          # False
print(x != y)          # True

# logical
print(x > 5 and y > 5) # True  — both must be true
print(x > 15 or y > 15)# True  — one must be true
print(not x > 15)      # True  — flips the result



#--------------------For loop------------------------
for i in range (10):
    print (i)

for i in range (0,10):
    print (i)

for i in range (1,50,2 ): #third argument gives the step first is strting second is ending 2nd and 3rd is exclusive
    print(i)


#---------------------while loop---------------------
i= 1
while (i <= 10):
    if i == 5:
        i= i+1
        continue #continue will skip 5 and go on
    if i == 9 :
        break  #break will stop the loop
    print (i)
    i = i+1


# #Computer picks a random number between 1 and 100
# User keeps guessing until they get it right
# After each wrong guess: tell them "Too high" or "Too low"
# Count the number of attempts
# When they win: print how many attempts it took
# If they guess wrong 10 times: game over, reveal the number

import random
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter the number between 1 to 100: "))
    attempts += 1
    if (guess < 1 or guess > 100):
        print("Invalid input, please enter a number between 1 and 100.")
        continue
    if (attempts == 10):
        print("Game over!!!!") 
        print (f"The number is: {secret}")
        break
    elif(guess< secret):
        print("too low")
    elif (guess> secret):
        print ("too high")
    elif(guess == secret):
        print(f"You guessed it right!!!! in {attempts} attempts")
        break
    