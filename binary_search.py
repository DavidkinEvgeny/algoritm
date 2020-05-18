def binary_search(list, item):
    '''Как в книге, но там был потерян операнд 2 в переменной mid'''
    low = 0
    hight = len(list) - 1
    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid -1
        else:
            low = mid + 1
    return None


# def binary_search(list, item):
#     '''Моя реализация функции'''
#     low = 0
#     hight = len(list) - 1
#     mid = len(list) // 2
#     while low <= hight:
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             hight = mid -1
#         else:
#             low = mid + 1
#         mid = (low + hight) // 2
#     return None


my_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(my_list, 9))