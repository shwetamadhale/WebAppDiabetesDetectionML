#Description: Program will detect if someone has diabetes using Machine Learning and Python

#Importign libraries
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st
#Diabetes Detection
#creating title and subtitle form web app
st.write("""
To Detect if someone has Diabetes, using Machine Learning and Python
""")


#Get the data
df = pd.read_csv('C:/Users/madha/PycharmProjects/DiabetesWebAppML/diabetes.csv')

#set a subheader
st.subheader('Data Information : ')

#show the data as a table
st.dataframe(df)

#show statistics on the data
st.write(df.describe())

#show the data as chart
chart = st.bar_chart(df)

#split the data into independent 'X' and dependent 'Y' variables
#x is dataset y is for outcome
X = df.iloc[:, 0:8].values
Y = df.iloc[:, -1].values

#split dataset into 75% training and 25% testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#user input for features
def get_user_input():
    pregnancies = st.sidebar.slider('pregnancies', 0, 17, 3)
    glucose = st.sidebar.slider('glucose', 0, 199, 117)
    blood_pressure = st.sidebar.slider('blood_pressure', 0, 122, 72)
    skin_thickness = st.sidebar.slider('skin_thickness', 0, 99, 23)
    insulin = st.sidebar.slider('insulin', 0.0, 846.0, 30.0)
    bmi = st.sidebar.slider('bmi', 0.0, 67.1, 32.0)
    dpf = st.sidebar.slider('dpf', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('age', 21, 81, 29)

    #store a dictionary into a variable
    user_data = { 'pregnancies' : pregnancies,
                  'glucose' : glucose,
                  'blood_pressure' : blood_pressure,
                  'skin_thickness' : skin_thickness,
                  'insulin' : insulin,
                  'bmi' : bmi,
                  'dpf' : dpf,
                  'age' : age
               }

    #transform the data into dataframe
    features = pd.DataFrame(user_data, index = [0])
    return features

#store the user input in a variable
user_input = get_user_input()

#set a subheader and display the users input
st.subheader('User Input : ')
st.write(user_input)

#Create and train the model
RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train, Y_train)


#show the model metrics, accuracy
st.subheader("Model Testing Accuracy Score : ")
st.write(str(accuracy_score(Y_test, RandomForestClassifier.predict(X_test))* 100 )+ '%')

#store the predictions
prediction = RandomForestClassifier.predict(user_input)

#set a subheader and display the classification
st.subheader('Classification : ')
st.write(prediction)