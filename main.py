import streamlit as st
import os
from PIL import Image
from helper import *
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
sns.set()
import zipfile
import constants
import shutil

get_top_page_content(st)

decoder = load_model()

#display_image_sequence(x_start,y_start,x_end,y_end,no_of_imgs, decoder)
#display_image_sequence(0,-3,-2,1,9, decoder, st)


with st.form("my_form"):
    x_start = int(st.number_input("X_inicial", min_value=-4, max_value=3, value=0, step=1))
    y_start = int(st.number_input("Y_inicial", min_value=-4, max_value=4, value=0, step=1))
    x_end = int(st.number_input("X_final", min_value=-4, max_value=3, value=0, step=1))
    y_end = int(st.number_input("Y_final", min_value=-4, max_value=4, value=0, step=1))
    images_number = int(st.number_input("Número de imágenes", min_value=0, max_value=20, value=5, step=1))

    submitted = st.form_submit_button("Submit")
    if submitted:
        display_image_sequence(x_start,y_start,x_end,y_end, images_number, decoder, st)