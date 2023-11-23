print("Hello world")

import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

names = ['a','b','c','d','e','f','g','h','i','j']
numbers = [random.randint(1,100) for i in range(10)]
print(numbers)

# Plot a bar chart with names on x-axis and values on y-axis
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

