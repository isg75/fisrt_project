# Week 3 | Project: Olympic Dataset

### **Project Overview*
...

# Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/repository_name.git
```

2. **Install UV**

If you're a MacOS/Linux user type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a Windows user open an Anaconda Powershell Prompt and type :

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv 
```

3. **Activate the environment**

If you're a MacOS/Linux user type (if you're using a bash shell):

```bash
source ./venv/bin/activate
```

If you're a MacOS/Linux user type (if you're using a csh/tcsh shell):

```bash
source ./venv/bin/activate.csh
```

If you're a Windows user type:

```bash
.\venv\Scripts\activate
```

4. **Install dependencies**:

```bash
uv pip install -r requirements.txt
```
### **Dataset and Hypothesis**
# Dataset 
...
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/data
# Hypothesis 
...
**Economic Factors**
Effect of GDP/per capita on medal's performance
Effect of GDP/per capita on medal's performance by female athletes
Effect of GDP/per capita on total athletes sent
**Geo Factors**
Effect of Host Country on medal's performance
Effect of Differences on Timezone between home country and host country on medal's performance
**Sport Factors**
Effect of strong younger players (under 25 years old)
Effect of historic performance in these sports



## **Data Wrangling and Cleaning**  
## Main dataset issues

- **ID**: Duplicates exist but this is intentional, as one athlete can participate in more than one event/olympics.
ID numbering is consistent throughout years - e.g. same ID for athlete in different olympic games.
ID is based on alphabetical order of last name
No major issues with ID column
- **Team**: Issues with Sports teams being mixed with countries (e.g. Toronto Argonauts)
Issues with Countries entering multiple teams for a single event using numbers following (e.g. Ukraine-2, Belarus-1)
Inconsistencies with number of countries participating due to geopolitical factors (like splitting up of Soviet Union)
- **Year**: 1906 invalid year as it was not an oficial Olympic
No data registred for year between World Wars
- **Season**: Winter olympics are also registred in out dataframe
- **City**: Non-English spelling city names
- **Sport**: Some sports may have very few instances (e.g., "Basque Pelota" or "Aeronautics"), which are edge cases and are no longer part of the modern Olympic Games.
- **Events**: Duplicated medals by event as the dateframe counts de number os metals won by athletes
- **Medal**: Null values refer to athletes who have not won any medals
Another point to consider is the discrepancy between the number of gold, silver, and bronze medals. On one hand, duplicates need to be accounted for as they can distort the overall picture. Additionally, the fact that certain team sports do not have the same number of athletes across all teams also contributes to this difference. Lastly, isolated cases, such as ties, can also impact the total medal count.

## Solutions for the dataset issues

- **Team**: Recommend using National Olympic Committee (NOC) code instead for country indicator
Only look at Olympics since 1992 (since splitting up of Soviet Union
- **Medal**: For null values, we updated and labeled as “No Medal”.
- **City**: Standardised all the city names to English
- **Events**: Create a new dataframe (olympic_data_results) which only registred the events and which country has won each medal by year.

## **Exploratory Data Analysis**  
### **Methods Used:**  
**Economic Factors**
**Geo Factors**
**Sport Factors**
### **Key Insights:** 
**Economic Factors**
**Geo Factors**
**Sport Factors**
## **Major Obstacle**  

## **Conclusion and Insights**  
### **Hypothesis Outcome:**   

### **Surprising Insights:**  

### **Next Step:** 
...
