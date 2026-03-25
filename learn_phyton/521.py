students = {"Петров": 3, "Іванов": 4, "Сидоров": 5, "Смирнов": 2, "Козлов": 4}
avg = sum(students.values())/len(students)
# for student in students:
#     if students[student]>avg:
#         print(student)
for name, grade in students.items():
    if grade>avg:
        print(name)
