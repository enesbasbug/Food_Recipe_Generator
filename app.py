# ! pip install streamlit
# ! pip install streamlit-option-menu

import streamlit as st
from streamlit_option_menu import option_menu
import fish, meat, chicken


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
    st.write("You may go through the whole code from __here__. ( ADD LINK THROUGH GITHUB )")

#
# MEAT
if selected == "Meat":
    st.title("Recipe:")
    st.write("Ingredients: ", meat.meat_meal()[0])
    st.write("__Recipe:__ ",meat.meat_meal()[1])

# 
# CHICKEN
if selected == "Chicken":
    st.title("Recipe:")    
    st.write("Ingredients: ", chicken.chicken_meal()[0])
    st.write("__Recipe:__ ",chicken.chicken_meal()[1])

#
# FISH
if selected == "Fish":
    st.title("Recipe:")
    st.write("Ingredients: ", fish.fish_meal()[0])
    st.write("__Recipe:__ ",fish.fish_meal()[1])


