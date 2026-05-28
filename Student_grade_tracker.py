#     Requirements — poori system banao:

# Student add kar sako — naam aur marks
# Sab students aur unke grades dekh sako
# Class average calculate ho
# Highest aur lowest scorer ka naam aur marks dikhao
# Grade assign ho automatically:

# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# 60 se kam → F


# Passing students ki list alag dikhao (60+)
# Failing students ki list alag dikhao
# Scores ko sort karke dikhao — ascending aur descending dono
# Ek student ko remove kar sako naam se
# CLI loop — quit type karne tak chalta rahe

from collections import namedtuple
Student = namedtuple("Student", ['name', 'score'])
s1 = Student('Sameer', 90)
s2 = Student('Ali', 80)
s3 = Student('Sumaira', 70)
s4 = Student('Sameera', 60)
s5 = Student('Samia', 50)
s6 = Student('Samra', 40)
s7 = Student('Sami', 45)
s8 = Student('Saim', 55)

Students = [s1, s2, s3, s4, s5, s6, s7, s8]

def add_student():
    while True:
        name = input("Enter student name: ")
        score_input = input("Enter student score: ")
        if not score_input.isdigit():
            print("Score must be a number. Please try again.")
            continue
        score = int(score_input)
        new_student = Student(name, score)
        Students.append(new_student)
        print(f"{new_student.name} with score {new_student.score} added successfully!!")
        again = input("Do you want to add another student(yes/no): ")
        if again.lower() != 'yes':
            break

def sort_scores_ascending():
    sorted_students = sorted(Students, key=lambda x: x.score)
    for student in sorted_students:
        print(f"{student.name}: {student.score}")

def sort_scores_descending():
    sorted_students = sorted(Students, key=lambda x: x.score, reverse=True)
    for student in sorted_students:
        print(f"{student.name}: {student.score}")

def show_all_students_and_grades():

    get_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    for student in Students:
        grade = get_grade(student.score)
        print(f"{student.name}: {student.score} ({grade})")

def show_passing_students():   
    for student in Students:
        if student.score>= 60:
            print(f"{student.name}: Passed")

def show_failing_students():
    for student in Students:
        if student.score < 60:
            print(f"{student.name}: Failed")

def show_class_average():
    if not Students:
        return
    total = 0
    for student in Students:
        total += student.score
    average = total / len(Students) 
    print(f"The average score is: {average:.2f}")

def show_highest_and_lowest():
    if not Students:
        print("No students available.")
        return

    highest_scorer = max(Students, key=lambda s: s.score)
    lowest_scorer = min(Students, key=lambda s: s.score)

    print(f"Highest Scorer: {highest_scorer.name} with score {highest_scorer.score}")
    print(f"Lowest Scorer: {lowest_scorer.name} with score {lowest_scorer.score}")

def remove_student_by_name():
    name_to_remove = input("Enter the name of the student to remove: ")
    for student in Students:
        if student.name == name_to_remove:
            Students.remove(student)
            print(f"{student.name} removed successfully!!")
            return
    print(f"No student found with the name {name_to_remove}.")

def main():
    while True:
      
      print("\n=== Student Grade Tracker ===")
      print("1. Add Student")
      print("2. Show All Students and Grades")
      print("3. Show Class Average")
      print("4. Show Highest and Lowest Scorer")
      print("5. Show Passing Students")
      print("6. Show Failing Students")
      print("7. Sort Scores Ascending")
      print("8. Sort Scores Descending")
      print("9. Remove Student by Name")
      print("10. Quit")

      choice = input("Enter your choice: ")

      if choice == '1':
            add_student()
      elif choice == '2':
            show_all_students_and_grades()
      elif choice == '3':
            show_class_average()
      elif choice == '4':
            show_highest_and_lowest()
      elif choice == '5':
            show_passing_students()
      elif choice == '6':
            show_failing_students()
      elif choice == '7':
            sort_scores_ascending()
      elif choice == '8':
            sort_scores_descending()
      elif choice == '9':
            remove_student_by_name()
      elif choice == '10':
            print("Goodbye!")
            break
      else:
            print("Invalid choice, please try again.")
main()