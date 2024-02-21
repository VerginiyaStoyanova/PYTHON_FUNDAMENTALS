list_of_people = list(map(int, input().split()))
execute = int(input())
executed_persons = []
current_person = 0

while list_of_people:
    person_to_execute = (current_person + execute - 1) % len(list_of_people)
    executed_person = list_of_people.pop(person_to_execute)
    executed_persons.append(str(executed_person))
    current_person = person_to_execute

print('[' + ','.join(executed_persons) + ']')