import pandas as pd

df = pd.read_csv('students_mental_health_survey.csv')

df.to_html('students_mental_health_survey.html')