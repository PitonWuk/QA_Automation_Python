"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу
виведіть через логер на рівні еррор у файл json__<your_second_name>.log

"""
import os
import json
import logging


logging.basicConfig(
    filename='json__zavadskyi.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def validate_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except json.JSONDecodeError as e:
        logging.error(f"Not valid JSON in file {file_path}: {e}")
        return False


def validate_json_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path) and filename.endswith('.json'):
            is_valid = validate_json_file(file_path)
            if is_valid:
                print(f"File {filename} is valid to JSON.")
            else:
                print(f"File {filename} is not valid to JSON.")


directory_path = 'E:\QA_Automation_Python\lesson11\JSON_files'

validate_json_in_directory(directory_path)