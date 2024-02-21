first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))
third_line = list(map(int, input().split()))

full_list = first_line + second_line + third_line

if any(all(full_list[index] == 1 for index in list_comb) for list_comb in
       [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):
    print("First player won")

elif any(all(full_list[index] == 2 for index in list_comb) for list_comb in
         [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]):
    print("Second player won")
else:
    print("Draw!")
