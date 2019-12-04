from itertools import groupby


def get_digits(digit):
    return [int(d) for d in str(digit)]


# part 1
def check_digit_order(digit):
    digits = get_digits(digit)
    if sorted(digits) == digits:
        return True
    return False


# part 1
def check_consecutive_no(digit):
    digits = get_digits(digit)
    l = [digits[i] == digits[i + 1] for i in range(len(digits) - 1)]
    return any(l)


# part 2
def check_larger_group(digit):
    digits = get_digits(digit)
    counts = [sum(1 for _ in group) for _, group in groupby(digits)]
    counts = list(filter(lambda x: x % 2 == 0, counts))
    ret = False
    if counts:
        for i in counts:
            ret = False if i > 2 and len(counts) == 1 else True
    return ret


def get_pass_number(lst):
    # part 1
    lst = list(filter(check_digit_order, lst))
    lst = list(filter(check_consecutive_no, lst))
    # part 1
    # return len(lst)

    # part 2
    lst = list(filter(check_larger_group, lst))
    return len(lst)


input_no = range(248345, 746315)
count = get_pass_number(input_no)
print(count)
