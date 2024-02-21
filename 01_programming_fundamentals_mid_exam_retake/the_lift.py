def is_there_empty_space(current_state):
    return any(value != 4 for value in current_state)


def find_a_place_in_the_lift(state_ot_the_lift, queue):
    if is_there_empty_space(state_ot_the_lift):
        for index, wagon in enumerate(state_ot_the_lift):
            free_places = 4 - wagon
            if queue >= free_places:
                queue -= free_places
                state_ot_the_lift[index] += free_places
            else:
                state_ot_the_lift[index] += queue
                queue = 0
                break

    return state_ot_the_lift, queue


def print_the_state(final_lift_state, final_state_of_queue):
    free_space = is_there_empty_space(final_lift_state)
    if final_state_of_queue == 0 and free_space:
        print("The lift has empty spots!")
        print(" ".join(str(number) for number in final_lift_state))
    elif final_state_of_queue != 0 and not free_space:
        print(f"There isn't enough space! {final_state_of_queue} people in a queue!")
        print(" ".join(str(number) for number in final_lift_state))
    elif final_state_of_queue == 0 and not free_space:
        print(" ".join(str(number) for number in final_lift_state))


people_on_queue = int(input())
current_state_of_the_lift = list(map(int, input().split()))

lift_state, remaining_queue = find_a_place_in_the_lift(current_state_of_the_lift, people_on_queue)

print_the_state(lift_state, remaining_queue)