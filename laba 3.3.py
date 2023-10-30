#Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный
# предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) 10(лаб)
#Физкультура: 30(пр)
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

#Пустой словарь
subject_data = {}

with open('subjects.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    # Разделение строки на части
    parts = line.strip().split(': ')

    # Если строка разделилась на две части, то есть данные о занятиях
    if len(parts) == 2:
        subject_name = parts[0]  # Получение название предмета
        sessions_data = parts[1]  # Получение данных о занятиях

        # Разделение данных о занятиях на отдельные элементы
        sessions = sessions_data.split()

        lectures = 0
        practicals = 0
        labs = 0
        import re

        for session in sessions:
            # Используйте регулярное выражение для извлечения числа из строки
            match = re.match(r'(\d+)\((\w+)\)', session)
            if match:
                count, session_type = match.groups()
                count = int(count)

                if session_type == 'л':
                    lectures += count
                elif session_type == 'пр':
                    practicals += count
                elif session_type == 'лаб':
                    labs += count

        total_sessions = lectures + practicals + labs

        # Добавление данных в словарь
        subject_data[subject_name] = total_sessions

print(subject_data)