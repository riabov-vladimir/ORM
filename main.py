from shows_to_mongo.read_data import read_data
from shows_to_mongo.data_upload_mongo import data_upload_mongo


shows_list = read_data()   # подготовили данные для работы с MongoDB

data_upload_mongo(shows_list)  # загружаем полученные данные в MongoDB
