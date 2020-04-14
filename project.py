import pymongo
import requests
from datetime import datetime

class DatabaseConnection():
	def __init__(self, address="mongodb://localhost:27017/"):
		self.database_address = address
		self.database_client = pymongo.MongoClient(self.database_address)
		self.db = self.database_client["lt_project"]
	def write_data(self, data):
		if(data is list):
			self.db.insert_many(data)
		else:
			self.db.insert(data)
	def read_data(self, collection):
		return self.db[collection]
	def update_data(self, collection):
		pass


class DataCollector():
	def __init__(self, dbc, url_gen):
		self.database_connection = dbc
		self.url_generator = url_gen
	def collect_data(self):
		collected_data = []
		for url, page_type in url_generator:
			encapsulated_page = {"type":page_type, "page":, "collection_time":}
			page = requests.get(url)
			encapsulated_page[page]=page
			encapsulated_page[collection_time]=str(datetime.now())
			collected_data.append(encapsulated_page)
		self.database_connection.write_data(collected_data)



class Controller():
	def __init__(self):
