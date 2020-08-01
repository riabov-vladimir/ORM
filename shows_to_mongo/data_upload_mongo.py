from pymongo import MongoClient


def data_upload_mongo(shows_list: list, db='homework_concerts', collection='shows') -> list:
	"""
	Функция загрузки данных в MongoDB
	:param db: название базы данных
	:param collection: название коллекций
	:param shows_list: список словарей
	:return: для нашей программы возврат функции мог остаться и None, но так её при случае можно будет отпринтить
	и получить идентификаторы добавленных документов
	"""

	client = MongoClient()

	concerts_db = client[db]

	shows_collection = concerts_db[collection]

	shows_collection.drop()  # делаю дроп базы, для удобства работы с файлом main.py

	shows = shows_collection.insert_many(shows_list).inserted_ids

	print(f'В базу данных добавлено {len(shows)} мероприятий.')

	return shows
