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
    options = ["Main Menu", "Meat π₯©", "Chicken π", "Fish π"],
    icons= ["book","book","book"],
    orientation = "horizontal",
    default_index=0
)


if selected == "Main Menu":
    st.title("π₯¬π₯ππ₯© Hi there! π¦π₯ππ")
    st.write("You may simply choose above what kind of dish you would like to eat.")
    st.write("Bon AppΓ©tit π₯¬π₯ππ₯©π¦π₯ππ")
    st.write("You may go through the whole code from [__here__] (https://github.com/enesbasbug/Food_Recipe_Generator).")

#
# MEAT
if selected == "Meat π₯©":

    st.write("It just takes some time, please wait :) (around 30 secs)")
    ingr = meat.meat_meal()[0]
    recp = meat.meat_meal()[1]
    st.title("π₯π₯© Recipe: π₯¬π₯")
    st.write("__Recipe:__ ", recp)
    st.write("Bon AppΓ©tit π₯¬π₯ππ₯©π¦π₯ππ")
    st.write("For another meat π₯© recipe, please refresh the page.")
    st.write("Ingredients: ", ingr)
    



# 
# CHICKEN
if selected == "Chicken π":

    st.write("It just takes some time, please wait :) (around 30 secs)")
    ingr = chicken.chicken_meal()[0]
    recp = chicken.chicken_meal()[1]
    st.title("π₯π Recipe: π₯¬π₯")
    st.write("__Recipe:__ ", recp)
    st.write("Bon AppΓ©tit π₯¬π₯ππ₯©π¦π₯ππ")
    st.write("For another chicken π recipe, please refresh the page.")
    st.write("Ingredients: ", ingr)



#
# FISH
if selected == "Fish π":

    st.write("It just takes some time, please wait :) (around 30 secs)")
    ingr = fish.fish_meal()[0]
    recp = fish.fish_meal()[1]
    st.title("π₯π Recipe: π₯¬π₯")
    st.write("__Recipe:__ ", recp)
    st.write("Bon AppΓ©tit π₯¬π₯ππ₯©π¦π₯ππ")
    st.write("For another fish π recipe, please refresh the page.")
    st.write("Ingredients: ", ingr)
