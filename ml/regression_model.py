import pickle

#LOAD ML MODEL
loaded_model = pickle.load(open('./models/model.sav', 'rb'))

#LOAD SCALER 
loadedscaler = pickle.load(open('./models/SB.pkl', 'rb'))