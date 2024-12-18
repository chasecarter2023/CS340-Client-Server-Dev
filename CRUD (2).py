#CHASE CARTER Wednesday, November 27,20204
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34386
        DB = 'AAC'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)  # data should be dictionary            
#CHASE CARTER Wednesday, November 27,20204           
            return insertSuccess.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty") 
# Make the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            data = self.database.animals.find( {}, {"_id": False})
        return [doc for doc in data]

# Make the U in CRUD.
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData})
        else:
            return "{}"
        return result.raw_result
    
# Make the D in CRUD.
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return result.raw_result