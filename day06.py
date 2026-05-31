#__________________OOP IN PYTHON__________________
class student:
    def __init__(self, name , age , score):
        self.name = name
        self.age = age
        self.score = score
    
    def getgrade(self):
        if self.score>= 80:
            return 'A'
        elif self.score>= 70:
            return 'B'
        else:
            return 'F'
    
s1 = student('sameer',20,95)
print(s1.getgrade())







# ── CLASS VARIABLES VS INSTANCE VARIABLES ────
class Student:
    # Class variable — sab objects share karte hain
    school_name = "AI Academy"
    total_students = 0

    def __init__(self, name, age, score):
        # Instance variables — har object ka apna
        self.name = name
        self.age = age
        self.score = score
        Student.total_students += 1    # class variable update

    def get_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        elif self.score >= 60: return "D"
        else: return "F"

# Class variable — class se access:
print(Student.school_name)      # AI Academy
print(Student.total_students)   # 0

s1 = Student("Sameer", 22, 95)
s2 = Student("Ali", 20, 82)
s3 = Student("Zain", 21, 78)

print(Student.total_students)   # 3 — har object ne increment kiya

# Instance se bhi access ho sakta hai:
print(s1.school_name)           # AI Academy

# ── __str__ AND __repr__ ──────────────────────
# __str__  — user ke liye readable output
# __repr__ — developer ke liye detailed output

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        elif self.score >= 60: return "D"
        else: return "F"

    def __str__(self):
        # print(s1) pe yeh chalta hai
        return f"Student: {self.name} | Score: {self.score} | Grade: {self.get_grade()}"



s1 = Student("Sameer", 22, 95)
print(s1)           # Student: Sameer | Score: 95 | Grade: A

# List mein bhi:
students = [Student("Sameer", 22, 95), Student("Ali", 20, 82)]
for s in students:
    print(s)        # __str__ call hoga



#__________BASIC INHERITANCE_________________
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name} and my age is {self.age} years."
    def __str__(self):
        return f"Person[{self.name} | {self.age}]"
    

class student(person):
    def __init__(self,name,age,score,id):
        super().__init__(name,age)
        self.score = score 
        self.id = id
    def __str__(self):
        return f"Student[{self.name} | {self.age} | {self.score} | {self.id}]"
    def get_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 80: return "B"
        elif self.score >= 70: return "C"
        elif self.score >= 60: return "D"
        else: return "F"


s1 = student('sameer',14,56,34)
print(s1)
        
#_________METHOD OVERRIDING ___________
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def speak(self):          # override parent method
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):          # override parent method
        return f"{self.name} says: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"

animals = [Dog("Bruno"), Cat("Whiskers"), Duck("Donald")]
for animal in animals:
    print(animal.speak())    # polymorphism — same method, different behavior


# ── ENCAPSULATION — data protect karna ───────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance      # __ = private — direct access nahi
        self.__transactions = []      # private list

    # Getter — balance read karna
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__transactions.append(f"Deposit: +{amount}")
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds. Balance: {self.__balance}")
        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: -{amount}")
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def get_history(self):
        if not self.__transactions:
            return "No transactions yet"
        return "\n".join(self.__transactions)

    def __str__(self):
        return f"Account[{self.owner}] Balance: {self.__balance}"

# Test karo:
acc = BankAccount("Sameer", 1000)
print(acc)                          # Account[Sameer] Balance: 1000
print(acc.deposit(500))             # Deposited 500. New balance: 1500
print(acc.withdraw(200))            # Withdrew 200. New balance: 1300
print(acc.balance)                  # 1300 — property se

# Private access try karo:
# print(acc.__balance)              # AttributeError — private hai
print(acc._BankAccount__balance)    # 1300 — name mangling — exists but discouraged

# Error handling:
try:
    acc.withdraw(5000)
except ValueError as e:
    print(f"Error: {e}")

print(acc.get_history())