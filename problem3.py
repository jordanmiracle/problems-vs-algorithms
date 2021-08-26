def rearrange_digits(input_list):

    freq = [0 for _ in range(10)]
    for i in input_list:
        freq[i] += 1

    first_num = 0
    second_num = 0
    first = True
    for i in range(10):
        while freq[9 - i] > 0:
            if first:
                first_num *= 10
                first_num += 9 - i
                first = False
            else:
                second_num *= 10
                second_num += 9 - i
                first = True
            freq[9 - i] -= 1
    return (first_num, second_num)


def mergesort(input_list):
    l = len(input_list)
    if l <= 1:
        return input_list

    mid = l // 2
    left = mergesort(input_list[:mid])
    right = mergesort(input_list[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1

    sorted_list += left[l:]
    sorted_list += right[r:]

    return sorted_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case_0 = [[1, 2, 3, 4, 5], [542, 31]]
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]

test_case_2 = [[9], [9, 0]]
test_case_3 = [[], [0, 0]]

print(rearrange_digits(test_case_0[0]))
# expected output: (531, 42)
test_function(test_case_0)
print('----------------------')

print(rearrange_digits(test_case_1[0]))
# expected output: (964, 852)
test_function(test_case_1)
print('----------------------')

print(rearrange_digits(test_case_2[0]))
# expected output: (9,0)
test_function(test_case_2)
print('----------------------')

print(rearrange_digits(test_case_3[0]))
# expected output: (0,0)
test_function(test_case_3)
print('----------------------')