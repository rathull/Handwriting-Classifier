import numpy as np
import pickle
import matplotlib.pyplot as plt
from random import randint
import tensorflow as tf
np.random.seed(42)
model = tf.keras.models.load_model('./')

def predict(img):
    images = np.array([np.zeros((84, 84)), img])

    tmp_imgs = images.reshape(84, 84, 2)
    new_images = np.array(tf.image.resize(
            tmp_imgs,(28,28), 
            method='bilinear', 
            preserve_aspect_ratio=False,
            antialias=True
        )
    ).reshape(2, 28, 28)

    predictions = model.predict(
        new_images.reshape(
            (2,784)
        )
    )
    labels = np.zeros_like(predictions)
    labels[
        np.arange(len(predictions)), 
        predictions.argmax(1)
    ] = 1
    return np.where(labels[1] == 1)[0][0]