# Task 3.2: Write a module named passenger_analysis.py and

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Task 1.1: Load the Data
def load_data(file_path):
    """
    Load the CSV file into a pandas DataFrame with explicit column names.
    
    :param file_path: str, path to the CSV file
    :return: pandas DataFrame
    """
    column_names = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
    return pd.read_csv(file_path, names=column_names, header=0)

# Task 1.2: Clean the Data (Checks for and handles any missing values and ensures data types are appropriate for analysis)
def clean_data(df):
    """
    Clean the DataFrame by handling missing values and ensuring appropriate data types.
    
    :param df: pandas DataFrame
    :return: cleaned pandas DataFrame
    """
    # Handle missing values
    df = df.dropna()  # Dropping rows with any missing values
    
    # Convert 'Birthdate' to datetime
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    
    # Convert 'LoyaltyMember' to string and then to boolean
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(str).str.upper() == 'TRUE'
    
    # Drop any rows where 'Birthdate' conversion failed
    df = df.dropna(subset=['Birthdate'])
    
    # Ensure 'PassengerID' is an integer
    df['PassengerID'] = df['PassengerID'].astype(int)
    
    return df

# Task 2.1: Calculate Average Age
def calculate_average_age(df, travel_class):
    """
    Calculate the average age of passengers in the specified travel class.
    
    :param df: pandas DataFrame
    :param travel_class: str, the travel class to filter by (e.g., 'ECONOMY', 'BUSINESS', 'FIRST_CLASS')
    :return: float, the average age of passengers in the specified travel class
    """
    # Filter the DataFrame by the specified travel class
    class_df = df[df['TravelClass'] == travel_class].copy()
    
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    
    # Calculate ages
    class_df.loc[:, 'Age'] = current_year - class_df['Birthdate'].dt.year
    
    # Calculate and return the average age
    return class_df['Age'].mean()

# Task 2.2: Find Loyalty Members
def find_loyalty_members(df):
    """
    Find names of passengers who are loyalty program members.
    
    :param df: pandas DataFrame
    :return: list, names of loyalty program members
    """
    # Filter the DataFrame by loyalty members
    loyalty_df = df[df['LoyaltyMember']]
    
    # Return the list of names of loyalty program members
    return loyalty_df['Name'].tolist()

# Task 3.1: Get Class Statistics
def get_class_statistics(df):
    """
    Get statistics for each travel class.
    
    :param df: pandas DataFrame
    :return: dict, statistics for each travel class
    """
    class_statistics = {}
    travel_classes = df['TravelClass'].unique()
    
    for travel_class in travel_classes:
        avg_age = calculate_average_age(df, travel_class)
        loyalty_members = df[(df['TravelClass'] == travel_class) & (df['LoyaltyMember'])].shape[0]
        
        class_statistics[travel_class] = {
            
            'Average Age': avg_age,
            'Loyalty Members': loyalty_members
        }

    return class_statistics

# Task 4.1: Plot Age Distribution
def plot_age_distribution(df):
    """
    Plot the distribution of ages using a histogram.
    
    :param df: pandas DataFrame
    """
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=20, edgecolor='black', alpha=0.7)
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/age_distribution.png')
    plt.show()

# Task 4.3: Plot Average Age by Class
def plot_average_age_by_class(df):
    """
    Plot the average age by travel class using a bar chart.
    
    :param df: pandas DataFrame
    """
    # Calculate average age by travel class
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    avg_age_by_class = df.groupby('TravelClass')['Age'].mean()
    
    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    avg_age_by_class.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/average_age_by_class.png')
    plt.show()

# Task 5.1: Plot Age vs. Loyalty
def plot_age_vs_loyalty(df):
    """
    Plot a scatter plot of age vs. loyalty membership using Seaborn.
    
    :param df: pandas DataFrame
    """
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Plot the scatter plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='LoyaltyMember', hue='TravelClass', alpha=0.7)
    plt.title('Age vs. Loyalty Membership')
    plt.xlabel('Age')
    plt.ylabel('Loyalty Member')
    plt.grid(True)
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/age_vs_loyalty.png')
    plt.show()

# Task 5.3: Plot Age Distribution by Class
def plot_age_distribution_by_class(df):
    """
    Plot the distribution of ages for each travel class using a box plot with Plotly.
    
    :param df: pandas DataFrame
    """
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Plot the box plot using Plotly
    fig = px.box(df, x='TravelClass', y='Age', color='TravelClass', title='Age Distribution by Travel Class')
    fig.update_layout(xaxis_title='Travel Class', yaxis_title='Age')
    fig.write_image('/Users/josemarchena/Python/Project1_marchenajose/age_distribution_by_class.png')
    fig.show()
    
    ########### Bonus part
    
    # Task 6.1: Plot Travel Class Distribution as a Pie Chart
def plot_travel_class_distribution(df):
    """
    Plot the distribution of passengers across different travel classes using a pie chart.
    
    :param df: pandas DataFrame
    """
    travel_class_counts = df['TravelClass'].value_counts()
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(travel_class_counts, labels=travel_class_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Passengers by Travel Class')
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/travel_class_distribution.png')
    plt.show()

# Task 6.2: Plot Number of Loyalty Members by Travel Class
def plot_loyalty_members_by_class(df):
    """
    Plot the number of loyalty members in each travel class using a bar chart.
    
    :param df: pandas DataFrame
    """
    loyalty_counts = df[df['LoyaltyMember']].groupby('TravelClass')['LoyaltyMember'].count()
    
    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    loyalty_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Number of Loyalty Members by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Number of Loyalty Members')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/loyalty_members_by_class.png')
    plt.show()
    
# Task 6.3: Creating Heatmaps
   
# Option 1: Correlation Heatmap
def plot_correlation_heatmap(df):
    """
    Plot a heatmap of the correlation between different numerical variables in the dataset.
    
    :param df: pandas DataFrame
    """
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Select numerical columns for correlation
    numerical_df = df[['Age', 'LoyaltyMember']]
    
    # Calculate the correlation matrix
    correlation_matrix = numerical_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/correlation_heatmap.png')
    plt.show()

# Option 2: Travel Class vs. Age Heatmap
def plot_class_age_heatmap(df):
    """
    Plot a heatmap of the density of different age groups within each travel class.
    
    :param df: pandas DataFrame
    """
    # Calculate the current year to determine the age of passengers
    current_year = datetime.now().year
    df['Age'] = current_year - df['Birthdate'].dt.year
    
    # Create a pivot table for the heatmap
    age_bins = pd.cut(df['Age'], bins=range(0, 101, 10))
    class_age_pivot = df.pivot_table(index=age_bins, columns='TravelClass', aggfunc='size', fill_value=0)
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(class_age_pivot, annot=True, cmap='YlGnBu')
    plt.title('Travel Class vs. Age Heatmap')
    plt.xlabel('Travel Class')
    plt.ylabel('Age Group')
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/class_age_heatmap.png')
    plt.show()

# Option 3: Travel Class vs. Flight Number Heatmap
def plot_class_flight_heatmap(df):
    """
    Plot a heatmap of the density or count of passengers within each travel class for each flight number.
    
    :param df: pandas DataFrame
    """
    # Create a pivot table for the heatmap
    class_flight_pivot = df.pivot_table(index='FlightNumber', columns='TravelClass', aggfunc='size', fill_value=0)
    
    # Plot the heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(class_flight_pivot, annot=True, cmap='Blues')
    plt.title('Travel Class vs. Flight Number Heatmap')
    plt.xlabel('Travel Class')
    plt.ylabel('Flight Number')
    plt.savefig('/Users/josemarchena/Python/Project1_marchenajose/class_flight_heatmap.png')
    plt.show()
    
    