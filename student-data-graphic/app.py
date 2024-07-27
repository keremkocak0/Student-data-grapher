import pandas as pd
import plotly.express as px

students_df = pd.read_csv('C:/Users/kerem/studentsfinalfr.csv')

attribute = input("Choose an attribute (name, gender, age): ").strip()
class_name = input("Choose a class (Class1, Class2, Class3, Class4, Class5): ").strip()

if attribute not in ['name', 'gender', 'age']:
    print("Invalid attribute. Please choose from 'name', 'gender', 'age'.")
    exit()
if class_name not in ['Class1', 'Class2', 'Class3', 'Class4', 'Class5']:
    print("Invalid class. Please choose from 'Class1', 'Class2', 'Class3', 'Class4', 'Class5'.")
    exit()

grades_column = class_name

if attribute == 'gender':
    data = students_df[['Gender', grades_column]]
elif attribute == 'age':
    data = students_df[['Age', grades_column]]
elif attribute == 'name':
    data = students_df[['Name', grades_column]]

if attribute == 'name':
    fig = px.histogram(data, x=grades_column, title=f'Distribution of {grades_column} for Each Student Name')

else:

    if attribute == 'gender':
        aggregated_data = data.groupby('Gender').mean().reset_index()
        fig = px.bar(aggregated_data, x='Gender', y=grades_column,
                     title=f'Average {grades_column} by Gender',
                     labels={grades_column: 'Average Grade'})
    elif attribute == 'age':
        aggregated_data = data.groupby('Age').mean().reset_index()
        fig = px.line(aggregated_data, x='Age', y=grades_column,
                      title=f'Average {grades_column} by Age',
                      labels={grades_column: 'Average Grade'})

fig.show()