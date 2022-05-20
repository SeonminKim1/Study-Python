
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image

WEIGHTS_PATH = 'static/weights/model.h5'

answers={0:'cat', 1:'dog'}

def get_classification_result(upload_path):

    img = image.load_img(upload_path, target_size=(256, 256))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    print(x.shape)

    model = keras.models.load_model(WEIGHTS_PATH)
    result = model.predict(x)
    print(result[0][0]) # 0.0 or 1.0
    return answers[result[0][0]]
