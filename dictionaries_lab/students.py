data = input()
courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_name: student_id}
    else:
        courses[course_name][student_name] = student_id

    data = input()

course_name = data.replace("_", " ")
students = courses[course_name]

for student_name, student_id in students.items():
    print(f"{student_name} - {student_id}")