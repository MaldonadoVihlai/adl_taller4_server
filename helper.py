import numpy as np
import tensorflow as tf
from pathlib import Path
from tensorflow.keras.models import load_model
import streamlit as st
import constants, keras, re, glob, cv2, os
import matplotlib.pyplot as plt
from keras.layers import Input, Dense, Conv2DTranspose, Flatten, Reshape
from keras.models import Model

@st.experimental_singleton()
def load_model(model_path = constants.MODEL):
    return keras.models.load_model('model/' + model_path)


model = load_model()


def get_top_page_content(st):
    #st.image(constants.IMAGE_BANNER)
    st.title(
        'Generador de imagenes aleatorio')
    st.markdown('Asigne los valores con las coordenadas de inicio y fin para las imágenes aleatorias, así como la cantidad de imágenes.')
    st.image(constants.SCATTERPLOT_IMAGE)
    st.markdown('**Nota:** Tenga encuenta que: \
    0: T-shirt/top, 1: Trouser, 2: Pullover, 3: Dress, 4: Coat, 5: Sandal, 6: Shirt, 7: Sneaker, 8: Bag, 9: Ankle boot')

def get_scatter_plot(encoder, X_train_new, y_train):
    encoded = encoder.predict(X_train_new)
    plt.figure(figsize=(14,12))
    plt.scatter(encoded[:,0], encoded[:,1], s=2, c=y_train, cmap='hsv')
    plt.colorbar()
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

def display_image_sequence(x_start,y_start,x_end,y_end,no_of_imgs, decoder, st):
    x_axis = np.linspace(x_start,x_end,no_of_imgs)
    y_axis = np.linspace(y_start,y_end,no_of_imgs)
    print(list(zip(x_axis,y_axis)))
    
    x_axis = x_axis[:, np.newaxis]
    y_axis = y_axis[:, np.newaxis]
    
    new_points = np.hstack((x_axis, y_axis))
    new_images = decoder.predict(new_points)
    new_images = new_images.reshape(new_images.shape[0], new_images.shape[1], new_images.shape[2])
    
    # Display some images
    fig, axes = plt.subplots(ncols=no_of_imgs, sharex=False,
                             sharey=True, figsize=(20, 7))
    counter = 0
    for i in range(no_of_imgs):
        axes[counter].imshow(new_images[i], cmap='gray')
        axes[counter].get_xaxis().set_visible(False)
        axes[counter].get_yaxis().set_visible(False)
        counter += 1
    st.pyplot(fig)
    #plt.show()