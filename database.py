'''
Created on Jul 6, 2017

@author: bhatsubh
'''

import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']
      
    @staticmethod  
    def insert(collection,data):
        Database.DATABASE[collection].insert(data)
        
    @staticmethod  
    def find(collection,query):
        return [data for data in Database.DATABASE[collection].find(query)]
    
    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find_one(query)
    
    @staticmethod
    def update(collection,filter,query):
        Database.DATABASE[collection].update(filter,query)
