"""
Завдання 1:

Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv

"""

import csv


def read_csv_file(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


def write_csv_file(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def remove_duplicates(file1_path, file2_path, result_path):
    data1 = read_csv_file(file1_path)
    data2 = read_csv_file(file2_path)
    combined_data = data1 + data2
    unique_data = [list(item) for item in set(tuple(row) for row in combined_data)]
    write_csv_file(result_path, unique_data)
    print(f"Result is in file: {result_path}")


file1 = 'r-m-c.csv'
file2 = 'rmc.csv'
result_file = 'zavadskyi.csv'

remove_duplicates(file1, file2, result_file)
