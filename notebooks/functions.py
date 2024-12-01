import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # for Plotly Express, which is easy-to-use for quick visualizations
import plotly.graph_objects as go 


# function for concatenation of the data from eurostat
def concatenate_eurostat_countries():
    housing = pd.read_excel("../data/raw/week_3_project_data.xlsx", sheet_name=0)
    rental = pd.read_excel("../data/raw/week_3_project_data.xlsx", sheet_name=1)
    income = pd.read_excel("../data/raw/week_3_project_data.xlsx", sheet_name=2)
    eurostat_df = pd.concat([housing, rental, income], ignore_index=True)
    index_labels = ['Housing'] * len(housing) + ['Rental'] * len(rental) + ['Income'] * len(income)
    eurostat_df.index = index_labels
    eurostat_df.rename(columns={"Unnamed: 0": "Country"}, inplace=True)    
    
    return eurostat_df


#function to retrieve differenet dataframes from eurostat to prepare the data for visualization by melting
def cleaning_eurostat_data_for_viz(eurostat_df):
    income_df = eurostat_df[eurostat_df.index == 'Income']
    housing_df = eurostat_df[eurostat_df.index == "Housing"]
    rental_df = eurostat_df[eurostat_df.index == "Rental"]

    income_tidy = income_df.melt(id_vars="Country", var_name="Year", value_name="Income")
    housing_tidy = housing_df.melt(id_vars="Country", var_name="Year", value_name="Housing")
    rental_tidy = rental_df.melt(id_vars="Country", var_name="Year", value_name="Rental")

    return income_tidy, housing_tidy, rental_tidy, income_df, housing_df, rental_df

#income_tidy, housing_tidy, rental_tidy, income_df, housing_df, rental_df = cleaning_eurostat_data_for_viz()
#income_df (getting the income for each country per years)

#displaying countries data from numbeo, assigning a value to indicies and converting to float
def clean_countries_numbeo():
    countries = pd.read_excel("../data/raw/numbeo_stats.xlsx", sheet_name=1)
    countries.columns = countries.columns.str.strip()
    countries.rename(columns={"Unnamed: 0": "Type"}, inplace = True)

    countries.loc[[1,2],"Type"] = '1 bed apartment (rent)'
    countries.loc[[4,5], 'Type'] = '3 bed apartment (rent)'
    countries.loc[[6,7,8], 'Type'] = 'Buy apartment (per m2 in city center)'
    countries.loc[[10,11], 'Type'] = 'Av salary (after tax)'
    countries.loc[[13,14], 'Type'] = 'Min wage (after tax)'

    columns_to_clean = ['2019', '2020', '2021', '2022', '2023', '2024']
    # Remove spaces and convert to float for each column
    for col in columns_to_clean:
        countries[col] = countries[col].astype(str).str.replace(" ", "").str.replace("\xa0", "").astype(float)
        
    return countries

#countries = clean_countries()
#one_bed_apt = countries[countries["Type"] == "1 bed apartment (rent)"]
#one_bed_apt_melted = one_bed_apt.melt(id_vars=["Type", "Country"], var_name="Year", value_name="Value")
#one_bed_apt_melted["Year"] = one_bed_apt_melted["Year"].astype(int)


#displaying city data from numbeo, assigning a value to indicies and converting to float
def clean_cities():
    cities = pd.read_excel("../data/raw/numbeo_stats.xlsx", sheet_name=0)
    cities.columns = cities.columns.str.strip()
    cities.rename(columns={"Unnamed: 0": "Type"}, inplace = True)

    cities.loc[[1,2],"Type"] = '1 bed apartment (rent)'
    cities.loc[[4,5], 'Type'] = '3 bed apartment (rent)'
    cities.loc[[6,7,8], 'Type'] = 'Buy apartment (per m2 in city center)'
    cities.loc[[10,11], 'Type'] = 'Av salary (after tax)'

    columns_to_clean = ['2019', '2020', '2021', '2022', '2023', '2024']
    # Remove spaces and convert to float for each column
    for col in columns_to_clean:
        cities[col] = cities[col].astype(str).str.replace(" ", "").str.replace("\xa0", "").astype(float)
    
    return cities
    
#df_lisbon = cities[cities['City'] == 'Lisbon']
#df_lisbon
#melt for further work with charts 
#lisbon_melted = df_lisbon.melt(id_vars=["Type", "City"], var_name="Year", value_name="Value")
#lisbon_melted["Year"] = lisbon_melted["Year"].astype(int)

#add minimum wage and multiply by 12 to get the yearly min_wage per country to eurostat data
def adding_minimum_wage(eurostat_df):
    min_wage = pd.read_excel("../data/raw/week_3_project_data.xlsx", sheet_name=3)
    min_wage.index = ["Min Wage"] * len(min_wage)
    min_wage_yr = min_wage.select_dtypes(include='number')

    # Multiply only numeric columns by 12
    min_wage_yr = min_wage_yr * 12

    min_wage_yr['Unnamed: 0'] = min_wage['Unnamed: 0']

    # Reorder columns to have 'Country' as the first column
    min_wage_yr = min_wage_yr[['Unnamed: 0'] + [col for col in min_wage_yr.columns if col != 'Unnamed: 0']]
    min_wage_yr.rename(columns={"Unnamed: 0": "Country"}, inplace=True) 
    eurostat_df = pd.concat([eurostat_df, min_wage_yr])
    return eurostat_df
    
eurostat_df = adding_minimum_wage(eurostat_df)