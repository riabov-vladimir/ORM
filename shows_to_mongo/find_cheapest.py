from pymongo import MongoClient
import pymongo


def find_cheapest():

	client = MongoClient()

	concerts_db = client['homework_concerts']

	shows_collection = concerts_db['shows']

	for show in shows_collection.find().sort('Цена', pymongo.ASCENDING):
		print(show)
