import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = './heart.csv'
df = pd.read_csv(file_path)

target_counts = df['target'].value_counts()
labels = ['No Heart Disease', 'Heart Disease']
colors = ['skyblue', 'lightcoral']

plt.figure(figsize=(8, 8))
plt.pie(target_counts, labels=labels, autopct='%1.1f%%',
        startangle=90, colors=colors, wedgeprops=dict(width=0.4))
plt.title('Distribution of Heart Disease in the Dataset')
plt.show()

plt.figure(figsize=(12, 6))

# Scatter points with 'target' value 0
plt.scatter(df[df['target'] == 0]['age'], df[df['target'] == 0]
            ['thalach'], label='No Heart Disease', color='skyblue', alpha=0.7)

# Scatter points with 'target' value 1
plt.scatter(df[df['target'] == 1]['age'], df[df['target'] == 1]
            ['thalach'], label='Heart Disease', color='lightcoral', alpha=0.7)

plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate (thalach)')
plt.title('Relationship between Age and Maximum Heart Rate')
plt.legend()
plt.show()
