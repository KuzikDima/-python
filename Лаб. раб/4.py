users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

wassup = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
wassup ["Общее количество"] = len(users)
wassup ["Уникальные посещения"] = len(set(users))

print(wassup)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
