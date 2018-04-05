'''
Created on Jul 6, 2017

@author: bhatsubh
'''
from database import Database

class Author:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    
    @staticmethod
    def check_user(username,password):
        user_details = Database.find_one(collection="authors", query={'username' : username,'password' : password})
        if user_details is not None:
            user_obj = Author(user_details['username'],user_details['email'],user_details['password'])
            return user_obj
        else:
            return None
        
    @staticmethod
    def check_username(username):
        if Database.find_one(collection="authors", query={'username' : username}):
            return True
        else:
            return False
        
    @staticmethod
    def create_user(username,email,password):
        user = Author(username,email,password)
        user._save_to_mongo()
        return user
    
    
    @classmethod
    def create_json(cls,username,email,password):
        return {
            'username' : username,
            'email' : email,
            'password' : password
            }
        
    def _save_to_mongo(self):
        user_json = Author.create_json(username=self.username, email=self.email, password=self.password)
        Database.insert(collection="authors", data=user_json)
        
