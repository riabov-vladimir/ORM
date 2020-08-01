from pymongo import MongoClient
import re
from pprint import pprint


def find_by_name(name: str):
	"""
	Функция выводит в консоль все события с указанным аргументом :name: иполнителем
	:param name: case-insensitive название исполнителя
	:return: None
	"""

	name_pattern = re.compile(r'({})'.format(name), re.IGNORECASE)  # подстрахуемся на случай неточностей с регистром

	client = MongoClient()

	concerts_db = client['homework_concerts']

	shows_collection = concerts_db['shows']

	for show in shows_collection.find({'Исполнитель': name_pattern}):
		pprint(show)
