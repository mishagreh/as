from itertools import product


def filter_count_sort_entries():

    file = '/home/bit/Downloads/Copy of Задание №1 - Данные.csv'
    with open(file, 'r') as read:
        data = read.read().split('\n')

    # 3 days of rank 1, 2 or 3 within the timeline

    entries = []
    for i in [i.split(',') for i in data]:
        count = 0
        for j in i:
            if j in ('1', '2', '3'):
                count += 1
            if count == 3:
                entries.append(','.join(i))
                break

    entries.sort()
    entries = [f'{len(entries)} of {len(data)-1}'] + [data[0]] + entries
    w_file = '/home/bit/pyproj/as/result.csv'
    with open(w_file, 'w') as write:
        write.write('\n'.join(entries))

    # 3 days in a row with entreis of rank 1, 2 and 3

    entries = []
    for i in data:
        for j in [f',{','.join(i)},' for i in tuple(product('123', repeat=3))]:
            if j in i:
                entries.append(i)
                break

    entries.sort()
    entries = [f'{len(entries)} of {len(data)-1}'] + [data[0]] + entries
    w_file = '/home/bit/pyproj/as/in_a_row.csv'
    with open(w_file, 'w') as write:
        write.write('\n'.join(entries))


filter_count_sort_entries()
