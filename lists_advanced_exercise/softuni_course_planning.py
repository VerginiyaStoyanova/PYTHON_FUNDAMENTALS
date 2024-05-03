def add_lesson(lessons, title):
    if title not in lessons:
        lessons.append(title)
    return lessons


def insert_lesson(lessons, title, title_index):
    if title not in lessons:
        lessons.insert(title_index, title)
    return lessons


def remove_lesson(lessons, title):
    if title in lessons:
        lessons.remove(title)
    if f'{title}-Exercise' in lessons:
        lessons.remove(f'{title}-Exercise')
    return lessons


def swap_lesson(lessons, title, swap_title):
    if title in lessons and swap_title in lessons:
        title_index = lessons.index(title)
        swap_index = lessons.index(swap_title)
        lessons[title_index], lessons[swap_index] = lessons[swap_index], lessons[title_index]
    if f'{title}-Exercise' in lessons:
        lessons.remove(f'{title}-Exercise')
        title_index = lessons.index(title)
        lessons.insert(title_index + 1, f'{title}-Exercise')
    if f'{swap_title}-Exercise' in lessons:
        lessons.remove(f'{swap_title}-Exercise')
        swap_index = lessons.index(swap_title)
        lessons.insert(swap_index + 1, f'{swap_title}-Exercise')
    return lessons


def exercise(lessons, title):
    if not f'{title}-Exercise' in lessons:
        if title in lessons:
            lessons.insert(lessons.index(title) + 1, f'{title}-Exercise')
        else:
            lessons.append(title)
            lessons.append(f'{title}-Exercise')
    return lessons


schedule_of_lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        schedule_of_lessons = add_lesson(schedule_of_lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        if 0 <= index < len(schedule_of_lessons):
            schedule_of_lessons = insert_lesson(schedule_of_lessons, lesson_title, index)
    elif action == "Remove":
        schedule_of_lessons = remove_lesson(schedule_of_lessons, lesson_title)
    elif action == "Swap":
        lesson_to_swap = command[2]
        schedule_of_lessons = swap_lesson(schedule_of_lessons, lesson_title, lesson_to_swap)
    elif action == "Exercise":
        schedule_of_lessons = exercise(schedule_of_lessons, lesson_title)

    command = input()

for index, lesson in enumerate(schedule_of_lessons):
    print(f"{index + 1}.{lesson}")