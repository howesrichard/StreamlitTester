import streamlit as st
import random
import pandas as pd
# import matplotlib.pyplot as plt

st.markdown('# This is the test dashboard')

col1, col2, col3, col4, col5 = st.columns(5)
for col in [col1, col2, col3, col4, col5]:
    col.markdown('### This is a column')
col1.markdown('### Column 1')
col2.write('Column 2')
# put a border around the columns
col1.markdown('---')
# put a box in col2
col2.markdown('### This is a box')

st.sidebar.text('Hello and welcome to the sidebar')
myRadioChoice = st.sidebar.radio('Choose:',[1,2])
st.write('You chose the following in the radio: ' + str(myRadioChoice))
mySliderVal = st.sidebar.slider('Slide me', min_value=0, max_value=10, value=5)
st.write('The value in the slider bar is: ' + str(mySliderVal))

names = ['a','b','c','d','e','f','g','h','i','j']
numbers = [random.randint(1,mySliderVal) for i in range(10)]

# plot a bar chart with names on x-axis and values on y-axis
#import matplotlib.pyplot as plt
#plt.bar(names,numbers)
#st.pyplot(plt)# show the plot in the streamlit app

# create a streamlit form to get user input
with st.sidebar.form(key='myForm'):
    myText = st.text_input('Enter some text')
    mySlider = st.slider('Slide me', min_value=0, max_value=10, value=5)
    myRadio = st.radio('Choose:',[1,2])
    mySubmit = st.form_submit_button(label='Submit')
    if mySubmit:
        st.write('You submitted the following:')
        st.write('Text: ' + myText)
        st.write('Slider: ' + str(mySlider))
        st.write('Radio: ' + str(myRadio))

if mySubmit:
    st.write ('# This is a header')
    st.write ('Text: ' + myText)

goNow = st.button('Go Now')
if goNow:
    st.write('You pressed the button')


tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
tab1.markdown('### This is tab 1')
tab2.markdown('### This is tab 2')