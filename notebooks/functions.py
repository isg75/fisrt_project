import pandas as pd

#Clean Rows and Columns
def clean_row_column(df: pd.DataFrame,url):
    # Use the second row as actual column names
    df.columns = df.iloc[1]  # Set first row as column headers
    df = df[1:].reset_index(drop=True)  # Drop the redundant first row
    df = pd.read_csv(url, header=1)
    df = df.drop(df.columns[0], axis=1) #Drop first column
    df.rename(columns={'Unnamed: 1':'Region/Country/Area'},inplace=True)
    return df

#Insert column to concat
def insert_column(df: pd.DataFrame, col,value):
    df.insert(3, col, [value]*len(df))
    return df


# Create the dictionary for continents and countries (as defined earlier)
continents={
    "Africa": [
        'Egypt', 'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde',
        'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Djibouti', 'Equatorial Guinea',
        'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast',
        'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique',
        'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles',
        'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Togo', 'Uganda', 'Zambia', 'Zimbabwe',
        'Eswatini', 'United Rep. of Tanzania','Madagascar', 'Malawi','Morocco','Côte d’Ivoire','Réunion','Tunisia',
        'Africa', 'Northern Africa', 'Sub-Saharan Africa'
    ],
    "Americas": [
        'Argentina', 'Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Bolivia (Plurin. State of)',
        'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic',
        'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica',
        'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'Saint Kitts and Nevis',
        'Saint Lucia', 'Saint Vincent & Grenadines', 'Suriname', 'Trinidad and Tobago', 'United States of America',
        'Uruguay', 'Venezuela (Boliv. Rep. of)', 'Aruba', 'Curaçao', 'French Guiana', 'French Polynesia',
        'New Caledonia', 'Niue', 'Northern Mariana Islands', 'United States Virgin Islands', 'Turks and Caicos Islands',
        'Montserrat','Anguilla', 'Bermuda', 'Bonaire','Saba','Sint Eustatius', 'Sint Maarten (Dutch part)',
       'British Virgin Islands', 'Cayman Islands', 'Guadeloupe','Martinique', 'Americas',
       'Northern America', 'Latin America & the Caribbean','Eastern Africa', 'Middle Africa',
       'Southern Africa', 'Western Africa','Caribbean',
       'Central America', 'South America'
    ],
    "Asia": [
        'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei Darussalam',
        'Cambodia', 'China', 'Georgia', 'India', 'Indonesia', 'Iran (Islamic Republic of)', 'Iraq', 'Israel',
        'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Lao People\'s Dem. Rep.', 'Lebanon', 'Malaysia',
        'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar',
        'Republic of Korea', 'Saudi Arabia', 'Singapore', 'Sri Lanka', 'Syrian Arab Republic', 'Tajikistan',
        'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam','Asia',
        'Yemen', 'China, Hong Kong SAR', 'China, Macao SAR', 'Dem. Rep. of the Congo', 'Korea, North (Dem. People\'s Republic of)',
        'Viet Nam', 'Caucasus', 'Central Asia', 'Eastern Asia', 'South-eastern Asia', 'Southern Asia', 'Western Asia','State of Palestine'
    ],
    "Europe": [
        'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina',
        'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia',
        'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania',
        'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway',
        'Poland', 'Portugal', 'Republic of Moldova', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia',
        'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Eastern Europe', 'Northern Europe',
        'Southern Europe', 'Western Europe', 'European Union (EU)', 'Kosovo', 'Gibraltar', 'Channel Islands',
        'Netherlands (Kingdom of the)', 'Russian Federation', 'Türkiye','Europe'
    ],
    "Oceania": [
        'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia (Fed. States of)', 'Nauru',
        'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu',
        'Australia and New Zealand', 'Melanesia', 'Micronesia', 'Polynesia', 'Falkland Islands (Malvinas)','Oceania',
        'Faroe Islands', 'Netherlands Antilles [former]', 'Greenland', 'Isle of Man', 'Holy See', 'Cook Islands','American Samoa','Guam'
    ],
    "Other": [
        'Total, all countries or areas', 'Other non-specified areas', 'LLDCs', 'LDC§', 'SIDS', 'Falkland Islands (Malvinas)',
        'Western Sahara', 'European Union (EU)', 'Mayotte', 'Saint Helena', 'Saint Martin (French part)',
        'Saint Pierre and Miquelon', 'Dem. People\'s Rep. Korea', 'Western Sahara', 'Gibraltar', 'Holy See', 'Isle of Man'
    ]
}

# Create a reverse mapping from country to continent
country_to_continent = {country: continent for continent, countries in continents.items() for country in countries}


# Function to map country to continent
def get_continent(country):
    return country_to_continent.get(country, 'Unknown')