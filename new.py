# ---------------------------------------------
# UNDP People's Climate Vote 2024 - Age Gap Analysis
# Person 1: Data Acquisition & Preprocessing
# ---------------------------------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("/content/Peoples_Climate_Vote_Database_2024.xlsx")

# Quick look at dataset
print(df.shape)

# Filter to the question of interest
question_text = "How quickly should your country replace coal, oil, and gas with renewable energy, such as power from the wind or sun?"
df_question = df[df['Question Text'] == question_text]
df_question = df_question[['Country', 'Age', 'Question Text', 'Response', 'Weighted Mean']]
df_question = df_question[~df_question['Age'].isin(['All Ages'])]
df_question = df_question[df_question['Response'] == "Very quickly"]
df_question['Weighted Mean'] = df_question['Weighted Mean'].replace('NA', np.nan)
df_question = df_question.dropna(subset=['Weighted Mean'])
df_question.shape

