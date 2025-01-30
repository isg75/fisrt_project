import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt

# geo factors
# host country
def plot_ridgeline_chart(df2, noc_of_interest, colors, hosting_info):
    plot_data = []
    
    for noc in noc_of_interest:
        noc_data = df2[df2['NOC'] == noc]
        years = noc_data['Year'].values
        gold = noc_data['Gold'].values
        silver = noc_data['Silver'].values
        bronze = noc_data['Bronze'].values
        
        # Stack data: Gold, Silver, and Bronze (no smoothing)
        plot_data.append(np.stack([gold, silver, bronze], axis=0))
        
    # Plot the ridgeline chart
    fig, axes = plt.subplots(len(noc_of_interest), 1, figsize=(12, 10), sharex=True, sharey=False)
    fig.suptitle('Olympic Medal Trends by Host Country', fontsize=16, fontweight='bold')

    # Adjust the spacing around subplots (if needed)
    fig.subplots_adjust(hspace=0.3)  # Increase space between subplots if necessary
    
    for i, (ax, noc, data) in enumerate(zip(axes, noc_of_interest, plot_data)):
        years = df2[df2['NOC'] == noc]['Year'].values
        
        ax.stackplot(years, data, labels=['Gold', 'Silver', 'Bronze'], colors=colors, alpha=0.8)
        
        # Add a vertical line for the hosting year and label medal counts within the stacked areas
        for year in years:
            if str(year) in hosting_info and hosting_info[str(year)] == noc:
                ax.axvline(x=year, color='grey', linestyle='--', label=f'Hosting Year ({year})')
                
                # Find the index for the hosting year and add the text labels
                year_index = np.where(years == year)[0][0]
                ax.text(year, data[0, year_index] / 2, f'Gold: {int(data[0, year_index])}', ha='center', fontsize=10, color='black',fontweight='bold')
                ax.text(year, data[0, year_index] + data[1, year_index] / 2, f'Silver: {int(data[1, year_index])}', ha='center', fontsize=10, color='black')
                ax.text(year, data[0, year_index] + data[1, year_index] + data[2, year_index] / 2, f'Bronze: {int(data[2, year_index])}', ha='center', fontsize=10, color='black')
        
        # Remove the frame and y-axis
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_yticks([])

        # Use annotate to place Region text to the left of the chart
        ax.annotate(
            f'{df2[df2["NOC"] == noc]["Region"].values[0]}',
            xy=(0.0, 0.5),  # Position at the middle vertically
            xycoords='axes fraction',  # Relative to the axes' coordinates
            ha='right',  # Align the text to the right
            va='center',  # Vertically center it
            fontsize=12,
            color='black',
            fontweight='bold'
        )

    # Set the x-axis label
    ax.set_xlabel('Year', fontsize=12)
    # Adjust layout to ensure titles and labels fit
    plt.tight_layout()
    plt.show()

# Time zone
def create_range_time(time):
    if time <= 2.0:
        return "[0-2.0]"
    elif time <=4:
        return "(2.0-4.0]"
    elif time <=6:
        return "(4.0-6.0]"
    elif time <=8:
        return "(6.0-8.0]"
    elif time <=10:
        return "(8.0-10.0]"
    elif time <=12:
        return "(10.0-12.0]"
    else:
        return "(12.0-13.00]"

# Economic factors
def clean_numeric_values(gdp_per_capita):
    gdp_per_capita = gdp_per_capita.copy()
    for col in gdp_per_capita.columns[2:]:  
        gdp_per_capita[col] = (
            gdp_per_capita[col]
            .astype(str)
            .str.replace('.', '', regex=False)  
            .str.replace(',', '.', regex=False)  
            .astype(float))
    return gdp_per_capita

# Sport factors
# Function to calculate repeat medalists for a group
def calculate_repeat_medalists(group, olympic_data2):
    # Find athletes from the group in the next Olympics
    next_olympics = pd.merge(
        group,
        olympic_data2,
        left_on=['Name', 'region'],
        right_on=['Name', 'region'],
        suffixes=('_current', '_next')
    )
    next_olympics = next_olympics[next_olympics['Year_next'] == next_olympics['Year_current'] + 4]

    # Calculate repeat medalists
    next_olympics['Won_Medal_Next'] = next_olympics['Medal_next'] != 'No Medal'
    repeat_medalists = next_olympics['Won_Medal_Next'].sum()
    total_athletes = len(group)
    percentage_repeat_medalists = (repeat_medalists / total_athletes) * 100 if total_athletes > 0 else 0
    return total_athletes, repeat_medalists, percentage_repeat_medalists


