from pymongo.mongo_client import MongoClient



class Database:
    def __init__(self) -> None:
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.imoveis

    def bulk_create(self, collection: str, data: list):
        return self.db[collection].insert_many(data)

    def create(self, collection: str, data: dict):
        return self.db[collection].insert_one(data)

    def read(self, collection: str, data: dict):
        return self.db[collection].find(data)


