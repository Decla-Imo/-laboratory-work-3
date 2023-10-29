# TODO Напишите функцию find_common_participants

def find_common_participants(x, y):
    common_participants = x + "|" + y
    common = common_participants.split(',')

    duplicates_particiants = []
    for item in common:
        if common.count(item) > 1 and item not in duplicates_particiants:
            duplicates_particiants. append(item)

    print(list.sort(duplicates_particiants))






participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group,participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
