#Dictionaries and Sets

# dictionaries store data in the form of pairs in the way of key and its value

student = {
    'name': 'Sameer',
    'age': 20,
    'city':'Gujrat',
    'score': 95
}

print(student['name'])
print(student['age'])  #normal way
#print(student['rollno'])       it gives error

# safe way if we are accessing the key which is not available
print(student.get('rollno'))   # will output none if not defined
print(student.get('score'))


# way to access all keys , values and whole data

print(student.keys())
print(student.values())
print(student.items())

print(student)

#traversing through the loop

for key, value in student.items():
    print(f"{key}: {value}")


# _________ADD and UPDATE_________

student['grade'] = 'A'  # adds new key and value
student['score'] = 96   #updates the existing value

print(student)


#________Deleting___

removed = student.pop('age')
print(f"Removed: {removed}")
print(student)

#Check if key exists or not

if 'dob' in student:
    print('Exists')
else:
    print('does not exist')



#___________Nested Dictionaries______________
school = {
    'class 10': {
        'Sameer': {
            'name': 'sameer',
            'age': 20
        },
        'Ali': {
            'name':'ali',
            'age': 22
        }
    },

    'Class11':{
        'Usman':{
            'name':'usman',
            'age': 23
        },
        'Alia':{
            'name':'alia',
            'age':24
        }
    }
}
print(school['class 10']['Sameer']['age'])
print(school['class 10']['Sameer'].keys())
print(school['class 10']['Sameer'].values())
print(school['class 10']['Sameer'].items())

for key,value in school['class 10']['Sameer'].items():
    print(f"{key}: {value}")
removed = school['class 10']['Sameer'].pop('age')
print(removed)
school['class 10']['Sameer']['age'] = 20
print(school['class 10']['Sameer'])



#______________Comprehension of dictionaries__________________
squares ={i: i*i for i in range (1,11)}
print(squares)

words ={'sameer', 'ali', 'usman'}
word_lengths = {word : len(word) for word in words}
print(word_lengths)
same = {s_word: s_word == 'sameer' for s_word in words}
print(same)


#______________Sets_________________
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union — dono mein se sab:
print(set_a | set_b)            # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a.union(set_b))       # same

# Intersection — dono mein common:
print(set_a & set_b)            # {4, 5}
print(set_a.intersection(set_b))

# Difference — a mein hai b mein nahi:
print(set_a - set_b)            # {1, 2, 3}
print(set_a.difference(set_b))

# Symmetric difference — dono mein unique:
print(set_a ^ set_b)            # {1, 2, 3, 6, 7, 8}

# ── ADD & REMOVE ─────────────────────────────
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.remove("banana")         # error agar exist na kare
fruits.discard("grape")         # no error agar exist na kare
print(fruits)