import streamlit

streamlit.title('🥣my new healthy diner')
streamlit.header('🍞Favorite Breakfast')
streamlit.text('🥑omega 3 & blueberry oatmeal')
streamlit.text('🥗kale, spinach & rocket smoothie')
streamlit.text('🐔Hard-Boil Free-Range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.AP-SOUTHEAST-1.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
