def rotated_array_search(input_list, number, mid=0):

    l = len(input_list)
    low_num = 0
    high_num = l
    while low_num <= high_num:
        pivot = (low_num+high_num) // 2
        if input_list[l-1] > input_list[0] or pivot == l-1:
            pivot = 0
            break
        if input_list[pivot] < input_list[pivot-1]:
            break
        elif input_list[pivot] < input_list[0] :
            high_num = pivot
        elif input_list[pivot] > input_list[0]:
            low_num = pivot


    pivot = 0
    if input_list[pivot] <= number <= input_list[l - 1]:
        low_num = pivot
        high_num = l
    else:
        low_num = 0
        high_num = pivot

    while low_num <= high_num:
        pivot = (low_num+high_num) // 2
        if input_list[pivot] == number:
            return pivot
        elif input_list[pivot] < number:
            low_num = pivot+1
        else:
            high_num = pivot-1
    return -1


def linear_search(input_list, number):
    for index, item in enumerate(input_list):
        if item == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8], 10])