#Code adapted from University of South Alabama course ISC  629 course: Python Flask Workshop 
#https://github.com/mahesh6420/flask-lab
import pymongo

class Database:

    def get_database(self):
       
        # db_client = pymongo.MongoClient('localhost', 27017)
        db_client = pymongo.MongoClient("mongodb+srv://admin:R6jSnQCHotD0dl1O@cluster0.eojsgnw.mongodb.net/?retryWrites=true&w=majority")
        
        pima_ml_db = db_client.pima_ml_db

        return pima_ml_db