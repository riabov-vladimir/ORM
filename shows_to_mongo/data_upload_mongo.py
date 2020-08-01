from pymongo import MongoClient


def data_upload_mongo(shows_list: list) -> list:
	"""

	:param shows_list:
	:return: для нашей программы возврат функции мог остаться и None, но так её при случае можно будет отпринтить
	и получить идентификаторы добавленных документов
	"""

	client = MongoClient()

	concerts_db = client['homework_concerts']

	shows_collection = concerts_db['shows']

	shows = shows_collection.insert_many(shows_list).inserted_ids

	print(f'В базу данных добавлено {len(shows)} мероприятий.')

	return shows
