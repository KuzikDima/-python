# TODO Напишите функцию find_common_participants
def find_common_participate (firstgroup, secondgroup):
    def group_lists (group):
        list_ = set(group.split("|"))
        return list_
    a = (group_lists(firstgroup))
    b = group_lists(secondgroup)
    return a.intersection(b)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participate(participants_first_group, participants_second_group))
