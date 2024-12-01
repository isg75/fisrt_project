# utils/display.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(df, x, y, hue, title):
    sns.lineplot(data=df, x=x, y=y, hue=hue)
    plt.title(title)
    plt.show()