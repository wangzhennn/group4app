import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image





#import the data


data=pd.read_csv('/work/Group4App/profiles.csv')

data.info()

data=data.drop(["essay0","essay1","essay2","essay3","essay4","essay5","essay6","essay7","essay8","essay9", "last_online", "diet", "offspring", "education", "body_type", "ethnicity", "income", "speaks"],axis=1)
# Drop all rows with free text and data we don't want

data[['city','state']] = data["location"].str.split(',',n=1,expand=True) #Split the location into city and state

data['pets'] = data['pets'].replace({'likes cats and likes cats':'no pets','likes cats':'no pets','likes dogs and dislikes cats':'no pets','likes dogs': 'no pets','dislikes dogs and dislikes cats': 'no pets','likes dogs': 'no pets','dislikes cats': 'no pets','dislikes dogs': 'no pets', 'dislikes dogs and likes cats':'no pets'})

data['pets'] = data['pets'].replace({'has dogs and likes cats':'has dogs', 'has dogs and dislikes cats':'has dogs'})

data['pets'] = data['pets'].replace({'likes dogs and has cats':'has cats', 'dislikes dogs and has cats':'has cats'})

data['pets'] = data['pets'].replace({np.nan:'no pets'})

data['height'] = data['height'] * 2.54 # Convert inches to CM

data['job'] = data['job'].replace({np.nan:'unknown'}) # Change the NaN's to unknown

data['drugs'] = data['drugs'].replace({np.nan:'unknown'}) # Change the NaN's to unknown

data['sign'] = data['sign'].replace({np.nan:'unknown'}) # Change the NaN's to unknown

#keeping only california

data = data[data.state ==' california'] 

st.set_page_config(page_title='OkCupid',page_icon="❤️")
alt.Chart(data).mark_point()

#st.header("Fun Facts about Dating")

#Info and Intro about OK Cupid

col7, col8, col9 = st.columns(3)

with col7: #logo of okcupid
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/OKCupid_Logo.svg/2560px-OKCupid_Logo.svg.png")

with col8:#interactive button
    if st.button('Fun facts about?'):

        st.write('🐼+🐻=❤️') #displayed when the button is clicked

    else:

        st.write('') #displayed when the button is unclicked


#with col8:
    #st.markdown("<h4 style='text-align: left; color: darkorange;'>What is the Site for? </h2>", unsafe_allow_html=True)
    #st.write('   🐼+🐻=❤️')

#map
#import data from github (longitude and latitude)

st.markdown("<h2 style='text-align: center; color: black;'> Have a look on it </h2>", unsafe_allow_html=True)
st.markdown("<h7 style='text-align: center; color: black;'> Observations are mainly based in California, primarily around the Bay Area </h2>", unsafe_allow_html=True)
url = 'https://raw.githubusercontent.com/LukaRado/long_lat/main/California.csv'
df = pd.read_csv(url,index_col=0,parse_dates=[0])

df1 = pd.merge(data, df, on="city")


df2 = df1.sample(25000)
st.map(df2)

st.markdown("<h2 style='text-align: center; color: black;'>Basic Information </h2>", unsafe_allow_html=True)

# You can call any Streamlit command, including custom components:
st.table(data.groupby('sex')['age'].mean())

st.image('/work/Group4App/age-gender.jpg', width=600)

col11, col12, col13 = st.columns(3)

with col11:
    chart = alt.Chart(data).mark_bar().encode(
    alt.X("age:Q", bin=True),
    y='count()',
    color = 'sex:N')   
    st.altair_chart(chart)

with col12:
    st.write()

with col13:
    st.write('')





#new thing 

st.markdown("<h1 style='text-align: center; color: black;'>Now for the fun stuff </h2>", unsafe_allow_html=True)
with st.container():
  
  st.header("Who drinks more?")
  st.write(pd.crosstab(data.sex, data.drinks, normalize='index'))

  



data.info()
#data.drugs.value_counts()
#Introduction (Text/Picture?) 
#Logic - boring to fun 
#Fun ideas: Status/drugs, Bubble-Chart (Drugs, Cities), Drugs/sign (Mike), (Shane)
#Jobs: Zach
#pets: Michelle 
#Luka: Geopandas, Coordinates - (Github) (Shane)
#Fun additional stuff like maybe some videos of austrian guys

#Test area Michelle
data.info()

col4, col5, col6 = st.columns(3)

with col4:
    st.write(' ')

with col5:
    st.image("data:image/jpeg;base64,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", width=150)

with col6:
    st.write(' ')


with st.container():
  st.header("Religion and Drinking")
  st.write(pd.crosstab(data.religion, data.drinks, normalize='index'))

with st.container():
  st.header("Pets and Drugs")
  st.write(pd.crosstab(data.pets, data.drugs, normalize='index'))

# add pictures

#st.image("https://free-url-shortener.rb.gy/url-shortener.png")

# center pictures 

#col4, col5, col6 = st.columns(3)

#with col4:
    #st.write(' ')

#with col5:
    #st.image("data:image/jpeg;base64,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")

#with col6:
    #st.write(' ')

#columns next to picture 
#st.write("a logo and text next to eachother")
#col1, mid, col2 = st.columns([10,5,60])
#with col1:
#    st.image("data:image/jpeg;base64,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",         width=150)
#with col2:
#   st.write(pd.crosstab(data.religion, data.drinks, normalize='index'))

#centered and colourful headline
#st.markdown("<h1 style='text-align: center; color: blue;'>Big headline</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: red;'>Fun Facts Dating </h2>", unsafe_allow_html=True)

#this one maybe

#chart = alt.Chart(data).mark_bar().encode(
   # alt.X("age:Q", bin=True),
    #y='drugs',
   # color = 'sex:N')   
#st.altair_chart(chart)

#Jobs and drugs 

with st.container():

  st.header(" Jobs and Drugs")

  st.image('/work/Group4App/jobanddrug.jpg', width=600)

  st.write(pd.crosstab(data.job, data.drugs, normalize='index'))



#st.video(https://www.youtube.com/watch?v=pFJ62vlZbls&ab_channel=scuffner)

#video_file = open('https://www.youtube.com/watch?v=pFJ62vlZbls&ab_channel=scuffner')
#video_bytes = video_file.read()
#st.video(video_bytes)

