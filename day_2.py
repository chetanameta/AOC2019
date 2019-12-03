lst = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 6, 19, 23, 2, 23, 6, 27, 1, 5, 27, 31, 1, 10,
       31, 35, 2, 6, 35, 39, 1, 39, 13, 43, 1, 43, 9, 47, 2, 47, 10, 51, 1, 5, 51, 55, 1, 55, 10, 59, 2, 59, 6, 63, 2,
       6, 63, 67, 1, 5, 67, 71, 2, 9, 71, 75, 1, 75, 6, 79, 1, 6, 79, 83, 2, 83, 9, 87, 2, 87, 13, 91, 1, 10, 91, 95, 1,
       95, 13, 99, 2, 13, 99, 103, 1, 103, 10, 107, 2, 107, 10, 111, 1, 111, 9, 115, 1, 115, 2, 119, 1, 9, 119, 0, 99,
       2, 0, 14, 0]


#for part 1 only
# lst[1] = 12
# lst[2] = 2


def get_alarm(lst1):
    for i in range(0, len(lst1) - 1, 4):
        # print(i)
        if lst1[i] == 1:
            lst1[lst1[i + 3]] = lst1[lst1[i + 1]] + lst1[lst1[i + 2]]
        if lst1[i] == 2:
            lst1[lst1[i + 3]] = lst1[lst1[i + 1]] * lst1[lst1[i + 2]]
        if lst1[i] == 99:
            break
    return lst1


# part 1
# print(get_alarm(lst))

# part2
for i in range(0, 99):

    for j in range(0, 99):
        lst1 = lst[::]
        lst1[1] = i
        lst1[2] = j
        lst2 = get_alarm(lst1)
        print(lst2)
        if lst2[0] == 19690720:
            break

    if lst2[0] == 19690720:
        print(i)
        print(j)
        print(100 * i + j)
        break
