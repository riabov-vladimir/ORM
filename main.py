from shows_to_mongo.read_data import read_data
from shows_to_mongo.data_upload_mongo import data_upload_mongo
from shows_to_mongo.find_by_name import find_by_name
from shows_to_mongo.find_cheapest import find_cheapest

shows_list = read_data()   # подготовили данные для работы с MongoDB

data_upload_mongo(shows_list)  # загружаем полученные данные в MongoDB

find_by_name('fest')  # найдем концерты исполнителя, в названии которого есть неточности регистра

find_cheapest()  # выводим все события отсортированные во возрастанию цены (вовремя догадался привести цены к int)

