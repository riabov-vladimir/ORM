from pymongo import MongoClient


def data_upload_mongo(shows_list: list) -> list:

	client = MongoClient()

	concerts_db = client['homework_concerts']

	shows_collection = concerts_db['shows']

	print(repr(shows_collection))

	shows = shows_collection.insert_many(shows_list).inserted_ids

	print(f'В базу данных добавлено {len(shows)} мероприятий.')

	return shows
