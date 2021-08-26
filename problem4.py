def sort_012(input_list):

    index = 0
    x_index = 0
    a_index = len(input_list) - 1

    while index <= a_index:
        if input_list[a_index] == 2:
            a_index -= 1
            continue
        if input_list[index] == 0:
            input_list[index] = input_list[x_index]
            input_list[x_index] = 0
            index += 1
            x_index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[a_index]
            input_list[a_index] = 2
            a_index -= 1
        else:
            index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

## Test cases

#Test 1
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
print('\n')# Test 2
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
print('\n')# Test 3
print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')# Test 4
print(sort_012([0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 2, 2, 0]))
test_function([0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 2, 2, 0])
print('\n')
print(sort_012([2, 2, 2, 2, 2, 2]))
test_function([2, 2, 2, 2, 2, 2])

print(sort_012([]))
test_function([])
