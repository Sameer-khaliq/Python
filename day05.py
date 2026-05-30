#____________File I/O Basics________________#

# ── FILE MODES ───────────────────────────────
# "r"  — read only (default) — file exist karni chahiye
# "w"  — write — file create karta hai, existing overwrite karta hai
# "a"  — append — end mein add karta hai
# "r+" — read + write
# "rb" — read binary — images, PDFs ke liye



# ── WRITING A FILE ───────────────────────────
# Context manager — with — automatically file band karta hai

with open('test.txt','w') as file:
    file.write(".Write() is used to write something in the file \n")
    file.write("'w' is used to create the new file \n")
    file.write("open() creates or opens the file based on next argument which can be 'r', 'w' , 'a', 'r+' etc.\n")


#______________READING THE ENTIRE FILE____________#
with open('test.txt','r') as file:
    data = file.read()
    print(data)


#__________READING LINE BY LINE FROM A FILE___________#
with open('test.txt', 'r') as file:
    for line in file:
        print(line.strip()) #strip() will remove \n

# ______________READING ALL LINES AS A LIST__________
with open('test.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    print(len(lines))

#___________APPENDING NEW LINES TO EXISTING FILE________
with open('test.txt', 'a') as file:
    file.write("'a' is used as argument for appending the new lines in the file\n")

with open('test.txt', 'r') as file:
    text = file.read()
    print(text)

#___________with___________
with open('test.txt', 'a') as file:
    file.write('with is the industry standard for file handling as it automatically closes the file and there is no need to write file.close()')
with open('test.txt', 'r') as file:
     text = file.read()
     print(text)



#__________FILE OPERATIONS____________



#_____________WRITING A LIST INTO FILE___________________

students = ['sameer', 'usman', 'ahsan', 'noor']
with open('students.txt','w') as file:
    for student in students:
        file.write(student + '\n')
with open('students.txt','r') as file:
    text = file.read()
    print(text)


#___________READING FILE AND CONVERTING IT TO LIST___________
with open('students.txt', 'r') as file:
    loaded_students = [line.strip() for line in file]
    print(loaded_students)

#______________CHECK IF FILE EXISTS_____________
import os 
if os.path.exists('students.txt'):
    print('File exists!!')
else:
    print("file does not exist!!")


#_________________FILE INFO______________

print(os.path.getsize('students.txt')) #return size in bytes
print(os.path.abspath('students.txt')) # returns complete/ absolute path

#_____________remove file____________
#print(os.remove('students.txt')) # will delete the file

# till now  i have studied file opening , reading , writing, converting list to file , file to list, checking file size , path and existence

#__________STRUCTURED FILES(CSV)_________

contacts =[
    ('sameer','03001234567','sam@gamil.com'),
    ('sami','03011234567','sami@gamil.com'),
    ('sameera','03021234567','sameera@gamil.com'),
    ('saim','03031234567','saim@gamil.com'),
]

with open('info.txt','w') as file:
    for name,contact,email in contacts:
        file.write(f"{name},{contact},{email}\n")

with open('info.txt','r') as file:
    print(file.read())




#____________EXCEPTION HANDLING_____________


#____BASIC TRY/EXCEPT_________

try:
    number = int(input("Enter a number to divide with: "))
    result = 100/ number
    print(f"Result: {result}")
except ValueError:
     print("that's not the number buddy!!")
except ZeroDivisionError:
     print("Zero se kon karta hai division!!")


#_________MULTIPLE EXCEPTIONS__________
try:
    with open('try.txt','r') as file:
        content = file.read()
except FileExistsError:
    print("File does not exist")
except FileNotFoundError:
    print("Mujhe ni mili file")
except PermissionError:
    print("tere pass ni hai permission isse kholne ki")
except Exception as e:
    print(f"Unknown exception: {e}")



#________else and finally____________
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Success! Result is {result}")    # sirf success pe
finally:
    print("Execution completed.")


operand = int(input("Enter a number: "))
if operand == 0:
    raise ZeroDivisionError ("Cant be zero")
result = 100 /operand
print (result)


# ── REAL PATTERN — File operations with proper handling ──
def read_file_safe(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filepath}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None

def write_file_safe(filepath, content):
    try:
        with open(filepath, "w") as file:
            file.write(content)
            return True
    except PermissionError:
        print(f"Error: No permission to write to '{filepath}'")
        return False
    except Exception as e:
        print(f"Unexpected error writing file: {e}")
        return False

# Test karo:
content = read_file_safe("nonexistent.txt")
print(content)    # None — no crash

success = write_file_safe("output.txt", "Hello World")
print(success)