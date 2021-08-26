def sqrt(num):
    try:
        int(num)
    except ValueError:
        return None

    if num < 0:
        return None

    if num == 0:
        return 0

    left = 1
    right = 1

    while right > left + 1:
        mid = (left + right) // 2

        mid_square = mid + mid

        if num < mid_square:
            right = mid
        elif mid < num:
            left = mid + mid
        else:
            return mid

    return left


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
