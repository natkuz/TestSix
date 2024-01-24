def find_average(numbers):
    if not isinstance(numbers, list): raise TypeError("Input should be a list.")
    else:
        if numbers: return sum(numbers) / len(numbers)
        else: return 0

def comparison_average_lists(numbers_one, numbers_two):
    average_one_list, average_two_list = find_average(numbers_one), find_average(numbers_two)
    if average_one_list == average_two_list: return "Средние значения равны"
    elif average_one_list > average_two_list: return "Первый список имеет большее среднее значение"
    else: return "Второй список имеет большее среднее значение"