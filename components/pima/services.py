from nis import cat
import pickle
from db import Database

class Pima:
    def __init__(self):
        self.database = Database().get_database()
        self.model = pickle.load(open('static/saved_voting.pkl', 'rb'))

    def predict(self, features) :
        try :
            has_diabetes = self.model.predict([features])
            self.save_one(features, has_diabetes[0])
            print(has_diabetes[0])
            return has_diabetes[0] # return 0 or 1
        except:
            print('except error from predict')
            pass
    def save_one(self, features, result):
        model_prediction = {
            "features": str(features),
            "result": str(result)
        }
        print(model_prediction)
        return self.database.pima_predictions.insert_one(model_prediction)

    def get_all(self):
        all_predictions = self.database.pima_predictions.find({})
        if all_predictions:
            return list(all_predictions)
        else:
            return {'error': 'No data available'}