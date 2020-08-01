import csv


def read_data(path='C:/Users/79055/PycharmProjects/ORM/data/artists.csv') -> list:
	"""
	Функция чтения данных из .csv файла

	:param path: путь к нашему файлу по умолчанию прописан в аргументы, но при желании можно обработать любой
	список концертов с идентичной структурой
	:return: возвращает список словарей по каждому мероприятию
	"""
	with open(path, encoding='utf-8') as f:
		rows = csv.reader(f, delimiter=",")
		shows_list = list(rows)

	init_doc = dict.fromkeys(['_id', *shows_list.pop(0)], None)
	shows_list_json = []
	count = 0
	for show in shows_list:
		count += 1
		temp_dict = init_doc.copy()
		temp_dict['_id'] = count
		temp_dict['Исполнитель'] = show[0]
		temp_dict['Цена'] = show[1]
		temp_dict['Место'] = show[2]
		temp_dict['Дата'] = show[3]
		shows_list_json.append(temp_dict)
	return shows_list_json
