import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    loc_index = __data_columns.index(location.lower())
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[loc_index] = 1
    return np.round(__model.predict([x])[0],2)

def load_saved_model():
    global  __data_columns
    global __locations
    with open("model/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open('model/home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns