import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files for Heart Disease and No Heart Disease
heart_disease_data = pd.read_csv('heart_disease_data.csv').head(5)
no_heart_disease_data = pd.read_csv('no_heart_disease_data.csv').head(5)

# Function to create bar charts for a given DataFrame and factors


def create_bar_charts(data, factors, title):
    num_factors = len(factors)
    fig, axes = plt.subplots(nrows=1, ncols=num_factors, figsize=(15, 5))

    for i, factor in enumerate(factors):
        factor_counts = data[factor].value_counts().sort_index()
        axes[i].bar(factor_counts.index, factor_counts.values, color='skyblue')
        axes[i].set_xlabel(factor)
        axes[i].set_ylabel('Count')
        axes[i].set_title(f'{title} - {factor}')

    plt.tight_layout()
    plt.show()


# List of factors to include in the bar charts
factors_to_plot = ['cp', 'slope', 'sex',
                   'fbs', 'restecg', 'exang', 'ca', 'thal']

# Factors of Heart Disease
create_bar_charts(heart_disease_data, factors_to_plot, 'Heart Disease')

# Factors of No Heart Disease
create_bar_charts(no_heart_disease_data, factors_to_plot, 'No Heart Disease')
