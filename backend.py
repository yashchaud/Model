
#Load the model
from tensorflow import keras
model = keras.models.load_model('model.h5')


# Save features from training
rnd_columns = list(X_train.columns)
joblib.dump(rnd_columns, 'rnd_columns.pkl')
print("Random Forest Model Colums Saved")