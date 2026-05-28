# #______list___________
# #list is like array in c++, the difference is in c++ we store same type of data and in python we can store multiple type of data in the same list and array's size is fixed but the size of list is dynamic

# fruits = ['strawberry', 'apple', 'mango', 'banana', 'orange'] 

# #indexing
# #indexing means accessing the elements at different indexes of the list, it works same as array
# print(fruits[0])
# print(fruits[-1])# last element
# print(fruits[-2])# second last element


# #slicing
# #fruits[start, stop, step]  stop is exclusive and is not printed, step is not mandatory
# print(fruits[0:3])
# print(fruits[0:4:2]) #at step of 2
# print(fruits[:5])
# print(fruits[::-1]) # reverse

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # predict karo pehle, phir run karo:
# print(numbers[2:7]) #30,40,50,60,70
# print(numbers[-3:]) #prints last 3
# print(numbers[::3]) # goes at step of 3
# print(numbers[1:8:2]) #goes from 20 to 80 at step of 2

# #_______List methods________#

# # Adding new element
#students = ['sameer', 'ali', 'zain', 'hassan']
# # .appemd() adds the element at the end and .insert() adds at specific index we mention
# students.append('usman')
# print(students)
# students.insert(2,'ahsan')
# print(students)


# #__________Removing the elements____________

# # two ways to remove 
# # by matching the value: we use .remove(value)
# # by index:  we use pop(index)
# students.pop(2)
# print (students)
# students.remove('hassan')
# print(students)


# #_________Sorting & reversing_______
# data = [2,4,34,22,44,66,23,98,12]
# print(data)
# data.sort() # sorts in ascending order
# print(data)
# data.sort(reverse = True) # sorts in reverse (descending order)
# print(data)
# data.reverse() # just reverses the data but don not sort it
# print(data)



# #Searching

# fruit = ['apple','banana', 'banana','guava']
# print(fruit.index('banana'))
# print(fruit.count('banana'))


# # copying the elements of list

# original = [2,4,5]
# copy = original.copy()
# print(copy)
# copy.append(3)
# copy.insert(2,33)
# print(copy)
# print(original)

#list comprehension

#lists provides us a way to use loops in condensed and comprehended way

# #normal

# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

# #this same thing can be done in one line

# squares = [i*i for i in range(1,11)]
# print(squares)

# # with condition

# cubes = [ i**3 for i in range(1, 13) if i%2 == 0]
# print (cubes)


# scores = [45,60,39,95,80,74,34]
# passed = [i for i in scores if i>=50]
# print (passed)
# grades = [s for s in scores if s>60]
# print(grades)
# passing_grades = [f"Grade: {s}" for s in scores if s >= 60]
# print(passing_grades)






#____Tuples____

#tuple is immutable data structure which means if it is created it cannot be changed its constant


rgb_red = (255, 0, 0)             # tuple — yeh value change nahi honi
shopping_cart = ["milk", "bread"] # list — items add/remove honge

# ── TUPLE METHODS ────────────────────────────
colors = ("red", "blue", "green", "blue", "red")
print(colors.count("blue"))       # 2
print(colors.index("green"))      # 2

# ── NAMED TUPLES — bonus concept ─────────────
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])
s1 = Student("Sameer", 22, "A")
print(s1.name)                    # Sameer — index ki jagah name se access
print(s1.grade)                   # A


print(s1)                         # Student(name='Sameer', age=22, grade='A') — pretty print


