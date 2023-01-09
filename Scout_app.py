import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


# here we define some of the front end elements of the web page like the font and background color,
# the padding and the text to be displayed
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i4.hurimg.com/i/hurriyet/75/0x0/61debc8f4e3fe103ecc6535c.jpg");
             background-position: 61% -10%;
             background-size: 25%, 25%, 45%;
             background-repeat: repeat-x; 
             background-attachment: scroll;
             


    Copy to Clipboard


         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


# this line allows us to display the front end aspects we have defined in the above code

# Display Auto Scout Model

col1, col2, col3 = st.columns([1,6,1])
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("https://www.autoscout24.com/cms-content-assets/1tkbXrmTEPPaTFel6UxtLr-c0eb4849caa00accfa44b32e8da0a2ff-AutoScout24_primary_solid.png")

with col3:
    st.write("")


df = pd.read_csv('C:/Users/Asus/Desktop/Project Autoscout MLD/final_scout_not_dummy2.csv')

# Loading the models to make predictions
final_model = pickle.load(open("C:/Users/Asus/Desktop/Project Autoscout MLD/final_model", "rb"))

# User input variables that will be used on predictions
st.sidebar.title("Please Enter the Features for Auto Scout Model")
make_model = st.sidebar.selectbox("Car Model", ('Audi A3', 'Audi A1', 'Opel Insignia', 'Opel Astra', 'Opel Corsa',
       'Renault Clio', 'Renault Espace', 'Renault Duster'))
km = st.sidebar.number_input("Km", 0.0, 320000.0,  10000.0, 1000.0)
hp_kW = st.sidebar.number_input("Hp (Horse Power)", 40, 239, 40, 1)
age = st.sidebar.radio("Age", (0,1,2,3))
Type = st.sidebar.selectbox("Type", ('Used', 'New', 'Pre-registered', 'Employee"s car', 'Demonstration'))
Gears = st.sidebar.selectbox("Gears", (5,6,7,8))
Gearing_Type = st.sidebar.selectbox("Gearing_Type",('Manual', 'Automatic', 'Semi-automatic'))
Safety_Security_Package = st.sidebar.selectbox("Safety_Security_Package", ('Safety Premium Package', 'Safety Premium Plus Package',
       'Safety Standard Package'))

# Converting user inputs to dataframe 

my_dict = {
    "make_model": make_model,
    "km": km,
    "hp_kW": hp_kW ,
    "age": age,
    "Gearing_Type": Gearing_Type,
    "Gears": Gears,
    "Type":Type,
    'Safety_Security_Package':Safety_Security_Package
}
df_input = pd.DataFrame.from_dict([my_dict])

# defining the function which will make the prediction using the data
def prediction(model, input_data):

	prediction = model.predict(input_data)
	return prediction

# Making prediction and displaying results
if st.button("Predict"):
    result = prediction(final_model, df_input)[0]
    
        
try:
    st.success(f"{make_model} Prediction Price is **{round((result),2)}€**")
    if make_model == "Audi A3":
    	st.image(Image.open("car_images/a3.jpg"))
    elif make_model == "Audi A1":
        st.image(Image.open("car_images/a1.jpg"))
    elif make_model == "Opel Insignia":
        st.image(Image.open("car_images/insignia.jpg"))
    elif make_model == "Opel Astra":
        st.image(Image.open("car_images/astra.jpg"))
    elif make_model == "Opel Corsa":
        st.image(Image.open("car_images/corsa.jpg"))
    elif make_model == "Renault Clio":
        st.image(Image.open("car_images/clio.jpg"))
    elif make_model == "Renault Espace":
        st.image(Image.open("car_images/espace.jpg"))
    elif make_model == "Renault Duster":
        st.image(Image.open("car_images/duster.jpg"))
except NameError:
    st.write("Please **Predict** button to display the result!")
    
except NameError:
    st.write("Please **Predict** button to display the car price prediction!")



    


