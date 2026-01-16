def main():
    clean_values()
    tickets_by_type = {}

    for key, value in types.items():
            tickets_by_type[value] = tickets[key]

    print(tickets_by_type)
        


def clean_values():
    used = []
    for key,value in tickets.items():
        new_value = []
        for type in value:
            if type not in used:
                used.append(type)
                new_value.append(type)
        tickets[key] = new_value




types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

if __name__ == '__main__':
    main()

"""{
    'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
    'Критический': ['UI_19', 'API_65', 'E2E_45'],
    'Значительный': ['E2E_2'],
    'Незначительный': ['E2E_9'],
    'Тривиальный': ['API_61']
} """