"""
Завдання 3:

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

"""
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def find_timing_incoming_by_group_number(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logging.info(f"Value timingExbytes/incoming for group {group_number}: {incoming.text}")
                        return incoming.text
        logging.info(f"The group with number {group_number} is not found.")
        return None

    except ET.ParseError as e:
        logging.error(f"Parsing error XML: {e}")
    except Exception as e:
        logging.error(f"There is an error: {e}")


file_path = r'E:\QA_Automation_Python\lesson11\xml_file\groups.xml'

group_number = 2
find_timing_incoming_by_group_number(file_path, group_number)
