#import lib
import streamlit as st
import pandas as pd 
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import validators
import re
import plotly.express as px
import plotly.graph_objects as go
from plotly import subplots
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas_profiling
from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file




st.markdown("<h1 id='head'><center><span style='color: #B830ED; font-size: 45px;'>Welcome 👋👋</span><span >Udemy_Project</span></center></h1>", unsafe_allow_html=True)

st.markdown("![Udemy](https://business.udemy.com/wp-content/uploads/2021/10/logo-udemy-purple-animation.gif)")

#########################
st.markdown('<p style="color:#5b5b5b; font-size: 20px;"> top 5000 course on Udemy on the development category , scrapped 9/11/2022 and will b#updated every 3 to 6 months also the other categories will be added soon</p>',unsafe_allow_html=True)
st.markdown("[👉👉Udemy_dataSet](https://www.kaggle.com/datasets/mahmoudahmed6/udemy-top-5k-course-2022)")

st.markdown('<h2 style="color:red; font-size: 25px;">About DataSet🧐🧐</h2>',unsafe_allow_html=True)

st.markdown(
"""
The following list won't indent no matter what I try:

- course_name : the name of the course
- instructor. : the course instructor
- course_url. : the url of the course on udemy
- course_image : image of the course
- course_description : the course subtitle , contains information about the course content
- reviews_avg. : the avg reviews on the course
- reviews_count : how many reviews on each course
- course_durartion : the course duration in hours
- lectures_count. : how many lecture in each course
- level. : the course level on udemy
- price_after_discount : the course price in EGP after discount
- main_price. : the original course price
- course_flag. : the course flag like (best seller , hot , new … etc)
- students_count. : how many students in each course
""",unsafe_allow_html=True
)
st.markdown(
    """
    <p><span style="color:red; font-size: 23px;">Why do I work on this dataset?🤔🤔</span><br><span style="color:#d69a04; font-size: 23px;">because it's a new idea to work with this data and I wan't get more statistical insists from this data it helps lecturers to predict his own course price 🕵️‍♂️🕵️‍♂️</span></p>
    """,unsafe_allow_html=True
)

st.markdown('----')
st.title("This section to show dataset")
My_data=pd.read_csv("data.csv")
df=My_data.copy()

if st.button('Show Data Set'):
    st.write(df)
else:
    st.write("press 👆👆Button to show Data")


st.markdown('----')

st.title("This shape Before removing noisy Data")
if st.button('Show shape Befor'):
    st.write(df.shape)
    st.write(df.isnull().sum())

##############################################
NewData=pd.read_csv("Cleaned_Data.csv")

st.markdown('----')

st.title("This shape After cleaning the Data")
if st.button('show shape After '):
    st.write(NewData.shape)
    st.write(NewData.isnull().sum())
    st.write(NewData.describe())

st.markdown('----')

st.markdown("""
            
            <center style="color: #8B1A1B; font-size:30px;">Finaly we Clend data from missing Data🎉🎉</center>
            """,unsafe_allow_html=True)
###############################################
x=NewData['instructor'].value_counts().head(10)
fig1=px.bar(x,text_auto=True,y='instructor',title="top 10 instructor has course in udemy")
st.plotly_chart(fig1, theme=None, use_container_width=True)
###############################################
st.markdown('----')

st.write("there are campany and people are making courses in udemy🌟🌟")
inst_flag=NewData.groupby('course_flag')['instructor'].count()
fig2=px.bar(inst_flag,text_auto=True)
st.plotly_chart(fig2, theme=None, use_container_width=True)

#################################################################

st.markdown('----')

q2=NewData[NewData['course_flag']=='Bestseller']['instructor'].value_counts().head(10)
fig3=px.bar(q2,text_auto=True,x='instructor',title="top 10 instructor has course in udemy and them courses flag =Bestseller ")
st.plotly_chart(fig3, theme=None, use_container_width=True)


#################################################################
st.markdown('----')

st.write("As we saw data left skwenees and most bestseller take reviwe avg >=4.5")
fig4=px.scatter(NewData,x='reviews_avg',y='reviews_count',color='course_flag',symbol='course_flag',marginal_x='histogram')
st.plotly_chart(fig4, theme=None, use_container_width=True)

#################################################################
st.markdown('----')
st.write("There is a strongs linear relation betwen student counts and review count when the number student increase it's predict the number of review count increases but is outlier in data As shown in the figure")

fig5=px.scatter(NewData,x='reviews_count',y='students_count',color='reviews_avg',marginal_x='rug',marginal_y='box',trendline='ols')

st.plotly_chart(fig5, theme=None, use_container_width=True)

#################################################################
st.markdown('----')

st.write("in this figer, we saw relation between lecture count and course_duration based reviews_avg The number of each varies according to the orde And so in all Level")

fig6=px.scatter(NewData,x='lectures_count',y='course_duration',color="level",animation_frame='reviews_avg',trendline='ols')

st.plotly_chart(fig6, theme=None, use_container_width=True)

#################################################################
st.markdown('----')
fig7=px.pie(NewData,'level','reviews_count',title="number of reviwe based level of course",hole=.6)
st.plotly_chart(fig7, theme=None, use_container_width=True)


#################################################################
st.markdown('----')

st.write('Actually, I found that the size of the description affects the number of students who enroll in the course, and that depends on the price of the course, and that most of them are registered at the time of discounts')

fig8=px.scatter_3d(NewData,x='len descreption',y='students_count',z='amount of discount',color='level',animation_frame='reviews_avg')
st.plotly_chart(fig8, theme=None, use_container_width=True)

#################################################################
st.markdown('----')
st.write('Most of the discounts range between 80 and 90, and according to the price of the course. The lower the price, the lower the percentage')

fig9=px.scatter_3d(NewData,x='price_after_discount',y='main_price',z='amount of discount',color='level',animation_frame='reviews_avg')
st.plotly_chart(fig9, theme=None, use_container_width=True)
#################################################################

st.markdown("""
            <center style="color:#FFD700;font-size:25px">the insights form this project </center><br>
<ul style="color:#ff0000;font-size:18px">
    <li>most courses that have most student count not have 5 stars rating</li><br>
    <li>lecture count and course duration have Simple impact on main_price</li><br>
    <li>We knew that top 20 popular courses are long-term. Maybe so many people enroll the long-term courses because they think they can find the information they're looking for with these.</li><br>
    <li>What improvement can we improve if we leave the course price dependent on the reviws_avg and reviwe_count</li>
    <li>Most of the discounts range between 80 and 90, and according to the price of the course. The lower the price, the lower the percentage</li><br>
    <li>Actually, I found that the size of the description affects the number of students who enroll in the course, and that depends on the price of the course, and that most of them are registered at the time of discounts</li>
</ul>
<br>
            """,unsafe_allow_html=True)

st.markdown("![thank](https://www.funimada.com/assets/images/cards/big/thank-you-2.gif)")


















































































