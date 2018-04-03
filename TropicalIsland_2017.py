def get_water_volume(island):
    M = len(island)
    # Число строк матрицы
    N = len(island[0])

    # Вторая строка и столбец, нумерация с нуля
    i = 1
    j = 1
    # Низина
    lowland = {}
    # Граница низины
    lowland_boundary = {}
    lowland_boundary_new = {}
    # Объём воды
    volume = 0

    for list_ in island[1:M - 1]:

        for element in list_[1:N - 1]:

            temp_lowland = {}

            def searching_cross(element, i, j):
                prep_volume = 0

                # print((i, j))
                if element < island[i][j - 1] \
                        and element < island[i - 1][j] \
                        and element < island[i][j + 1] \
                        and element < island[i + 1][j] and (i, j) not in lowland:
                    lowland[i, j] = element
                    # Разница между текущим элементом и его минимальным соседом
                    delta = min([island[i][j - 1],
                                 island[i - 1][j],
                                 island[i][j + 1],
                                 island[i + 1][j]]) - element
                    # Низина затопляется
                    lowland[i, j] += delta
                    island[i][j] += delta
                    prep_volume += delta

                if element >= island[i][j - 1] and (i, j) not in lowland:
                    lowland[i, j] = element
                    temp_lowland[i, j] = element
                    lowland_boundary[i - 1, j] = island[i - 1][j]
                    lowland_boundary[i, j + 1] = island[i][j + 1]
                    lowland_boundary[i + 1, j] = island[i + 1][j]
                    lowland_boundary[i, j - 1] = island[i][j - 1]
                    if j - 1 != 0:
                        return searching_cross(island[i][j - 1], i, j - 1)

                if element >= island[i - 1][j] and (i, j) not in lowland:
                    lowland[i, j] = element
                    temp_lowland[i, j] = element
                    lowland_boundary[i, j - 1] = island[i][j - 1]
                    lowland_boundary[i, j + 1] = island[i][j + 1]
                    lowland_boundary[i + 1, j] = island[i + 1][j]
                    lowland_boundary[i - 1, j] = island[i - 1][j]
                    if i - 1 != 0:
                        return searching_cross(island[i - 1][j], i - 1, j)

                if element >= island[i][j + 1] and (i, j) not in lowland:
                    lowland[i, j] = element
                    temp_lowland[i, j] = element
                    lowland_boundary[i, j - 1] = island[i][j - 1]
                    lowland_boundary[i - 1, j] = island[i - 1][j]
                    lowland_boundary[i + 1, j] = island[i + 1][j]
                    lowland_boundary[i, j + 1] = island[i][j + 1]
                    if j + 1 != N - 1:
                        return searching_cross(island[i][j + 1], i, j + 1)

                if element >= island[i + 1][j] and (i, j) not in lowland:
                    lowland[i, j] = element
                    temp_lowland[i, j] = element
                    lowland_boundary[i, j - 1] = island[i][j - 1]
                    lowland_boundary[i - 1, j] = island[i - 1][j]
                    lowland_boundary[i, j + 1] = island[i][j + 1]
                    lowland_boundary[i + 1, j] = island[i + 1][j]
                    if i + 1 != M - 1:
                        return searching_cross(island[i + 1][j], i + 1, j)

                # Минимальное число в границе низин
                for key, value in lowland_boundary.items():
                    if key not in temp_lowland:
                        lowland_boundary_new[key] = value

                try:
                    min_ = min(lowland_boundary_new.values())
                except ValueError:
                    pass
                else:
                    for key, value in temp_lowland.items():
                        if value > min_:
                            continue
                        delta = min_ - value
                        prep_volume += delta
                        lowland[key] += delta

                        island[key[0]][key[1]] += delta

                temp_lowland.clear()
                lowland_boundary_new.clear()
                lowland_boundary.clear()
                return prep_volume

            volume += searching_cross(element, i, j)

            j += 1

        j = 1
        i += 1

    # for x in island:
    #   print(x)
    while volume:
        return volume + get_water_volume(island)

    return volume

islands = [
    [
        [3, 2, 8, 5, 4, 7],
        [1, 2, 4, 3, 9, 7],
        [2, 4, 5, 5, 4, 9],
        [6, 6, 2, 2, 5, 4]
    ],
    [
        [4, 5, 3, 3, 4],
        [5, 9, 3, 7, 5],
        [5, 3, 2, 1, 8],
        [1, 7, 4, 1, 8],
        [8, 8, 1, 7, 6],
        [1, 6, 5, 4, 6],
        [4, 6, 8, 7, 9]
    ],
    [
        [3, 7, 7, 3],
        [9, 4, 9, 4],
        [6, 9, 1, 6],
        [8, 2, 3, 4],
        [9, 6, 5, 2],
    ],
    [
        [4, 6, 8, 3],
        [6, 1, 1, 4],
        [8, 8, 4, 8],
        [6, 4, 3, 3]
    ],
    [
        [2, 3, 5, 6, 2],
        [6, 6, 1, 3, 8],
        [1, 2, 5, 3, 7]
    ],
    [
        [7, 6, 4],
        [9, 8, 1],
        [5, 3, 8],
        [7, 2, 7],
        [2, 2, 6]
    ],
    [
        [7, 5, 6, 2],
        [6, 5, 3, 6],
        [6, 1, 2, 2],
        [7, 7, 8, 5],
        [7, 3, 5, 5],
        [7, 3, 7, 8]
    ],
    [
        [7, 4, 9, 2, 7],
        [7, 6, 2, 2, 2],
        [9, 1, 8, 5, 4],
        [4, 4, 4, 2, 4],
        [3, 1, 5, 7, 1]
    ],
    [
        [1, 3, 7],
        [1, 5, 6],
        [1, 3, 8],
        [1, 1, 1],
        [8, 2, 6],
        [3, 1, 1]
    ],
    [
        [5, 7, 2, 5],
        [2, 7, 1, 5],
        [6, 2, 1, 7],
        [2, 7, 5, 1]
    ],
    [
        [7, 8, 2, 1, 7],
        [5, 3, 5, 1, 8],
        [5, 9, 6, 2, 8],
        [4, 2, 3, 5, 6]
    ],
    [
        [5, 4, 4, 7, 1],
        [1, 6, 2, 2, 5],
        [6, 4, 5, 5, 9],
        [1, 1, 4, 2, 2]
    ],
    [
        [6, 4, 8],
        [3, 9, 9],
        [6, 1, 5],
        [2, 3, 2],
        [1, 5, 6]
    ],
    [
        [8, 9, 5, 1, 3, 9],
        [5, 7, 3, 9, 2, 8],
        [9, 5, 2, 3, 2, 2],
        [7, 8, 2, 7, 7, 1],
        [6, 9, 3, 8, 5, 6],
        [3, 5, 4, 4, 3, 3]
    ],
    [
        [4, 7, 4, 4, 3, 6],
        [7, 3, 8, 3, 2, 9],
        [7, 2, 3, 8, 6, 2],
        [3, 1, 6, 4, 6, 1],
        [4, 9, 9, 6, 9, 8],
        [8, 4, 3, 6, 3, 1]

    ],
    [
        [4, 5, 4],
        [3, 1, 5],
        [5, 4, 1]
    ],
    [
        [5, 7, 2, 5],
        [2, 7, 1, 5],
        [6, 2, 1, 7],
        [2, 7, 5, 1]
    ],
    [
        [5, 3, 4, 5],
        [6, 2, 1, 4],
        [3, 1, 1, 4],
        [8, 5, 4, 3]
    ],
    [
        [7, 4, 9, 2, 7],
        [7, 6, 2, 2, 2],
        [9, 1, 8, 5, 4],
        [4, 4, 4, 2, 4],
        [3, 1, 5, 7, 1]
    ],
    [
        [2, 2, 2],
        [2, 1, 2],
        [2, 1, 2],
        [2, 1, 2]
    ],
    [
        [4, 5, 4, 7, 8],
        [3, 6, 5, 3, 6],
        [5, 4, 1, 7, 10]
    ]
]

for island in islands:
    print(get_water_volume(island))
