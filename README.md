# Diabetes Prediction Web App Using Machine Learning

A Python-based web application using Streamlit to predict the likelihood of diabetes using machine learning.

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Implementation Steps](#implementation-steps)
- [Example Code](#example-code)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Background
This project implements a diabetes prediction system using a machine learning model trained on patient health data. The system allows users to input health parameters and receive a prediction of their likelihood of having diabetes.

## Install
To set up the project, clone the repository and install the required dependencies.

```sh
$ git clone https://github.com/your-username/diabetes-predictor.git
$ cd diabetes-predictor
$ pip install -r requirements.txt
```

## Usage
1. Ensure you have the dataset (`diabetes.csv`) in the project directory.
2. Run the Streamlit web application:
   ```sh
   streamlit run WebApp.py
   ```
3. Input patient details via the web interface and receive a prediction.

## Features
- **Machine Learning Model**: Uses Random Forest Classifier for predictions.
- **User Input via Streamlit**: Allows users to input health details interactively.
- **Data Visualization**: Displays dataset insights and statistics.
- **Model Accuracy Display**: Shows the accuracy of the trained model.

## Technologies Used
- **Python Libraries**: Pandas, NumPy, Scikit-learn, Streamlit
- **Machine Learning**: Random Forest Classifier for prediction
- **Web Framework**: Streamlit for interactive UI
- **Data Analysis**: Exploratory data analysis with Pandas

## Implementation Steps
1. **Load Data**: Read the diabetes dataset using Pandas.
2. **Data Preprocessing**: Handle missing values and scale features if necessary.
3. **Feature Engineering**:
   - Select relevant health indicators (glucose, insulin, BMI, etc.).
   - Allow user input through Streamlit sliders.
4. **Train Machine Learning Model**:
   - Split data into training and testing sets.
   - Train a Random Forest Classifier.
5. **Model Evaluation**:
   - Compute accuracy of the trained model.
   - Display the score on the Streamlit app.
6. **Web App Deployment**:
   - Collect user input.
   - Use the trained model to predict diabetes likelihood.
   - Display results interactively.
