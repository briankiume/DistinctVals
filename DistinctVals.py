def find_distinct(a):
    distinct = []
    for i in a:
        if i not in distinct:
            distinct.append(i)

    distinct_len = len(distinct)

    return distinct_len


print(find_distinct([2, 1, 1, 2, 3, 1]))
