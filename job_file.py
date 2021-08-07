from pprint import pprint


def merging_files(file_list):
    temp_list = []
    for files in file_list:
        temp_dict = {}
        with open(files, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            temp_dict['Имя файла'] = files
            temp_dict['Количество строк'] = str(len(lines))
            temp_dict['Содержимое файла'] = lines
            temp_list.append(temp_dict)
    result_list = sorted(temp_list, key=lambda i: i['Количество строк'])
    with open('result.txt', 'w', encoding='utf-8') as file:
        for i in result_list:
            file.write(i['Имя файла'] + '\n')
            file.write(i['Количество строк'] + '\n')
            for j in i['Содержимое файла']:
                file.write(j.strip() + '\n')


my_list = ['1.txt', '2.txt', '3.txt']
pprint(merging_files(my_list))
