# ! pip install streamlit
# ! pip install streamlit-option-menu
# from tqdm.notebook import trange
# from IPython.display import Image, display
# from big_sleep import Imagine
import streamlit as st
from streamlit_option_menu import option_menu
import meat, fish, chicken
from PIL import Image
import pandas as pd 
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Embedding,Dropout, Bidirectional
from tensorflow.keras import regularizers
from tensorflow.keras.losses import sparse_categorical_crossentropy




st.set_page_config(page_title="Recipe Generator", page_icon=":tada:")

selected = option_menu(
    menu_title = "ECS7022P Computational Creativity - Recipe Generator",
    options = ["Main Menu", "Meat", "Chicken", "Fish"],
    icons= ["book","book","book"],
    orientation = "horizontal",
    default_index=0
)


if selected == "Main Menu":
    st.title("Hi there!")
    st.write("Hope, you are going to hardly believe your eyes when you read the recipe the generator prepared ONLY for you!")
    st.write("You may go through the whole code from [__here__] (https://github.com/enesbasbug/).")

#
# MEAT
if selected == "Meat":
    ingr = meat.meat_meal()[0]
    recp = meat.meat_meal()[1]
    st.title("Recipe:")
    st.write("Ingredients: ", ingr)
    st.write("__Recipe:__ ",)


# 
# CHICKEN
if selected == "Chicken":
    ingr = chicken.chicken_meal()[0]
    recp = chicken.chicken_meal()[1]
    st.title("Recipe:")    
    st.write("Ingredients: ", ingr)
    st.write("__Recipe:__ ",recp)


#
# FISH
if selected == "Fish":
    ingr = fish.fish_meal()[0]
    recp = fish.fish_meal()[1]
    st.title("Recipe:")
    st.write("Ingredients: ", ingr)
    st.write("__Recipe:__ ",recp)
