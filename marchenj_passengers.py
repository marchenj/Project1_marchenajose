# 3.3: Import this module into your main script and call the functions as needed.

import pandas as pd
from passenger_analysis import load_data, clean_data, calculate_average_age, find_loyalty_members, get_class_statistics, plot_age_distribution, plot_average_age_by_class, plot_age_vs_loyalty, plot_age_distribution_by_class, plot_travel_class_distribution, plot_loyalty_members_by_class, plot_correlation_heatmap, plot_class_age_heatmap, plot_class_flight_heatmap

# Main Execution

# File path to the original CSV file
file_path = '/Users/josemarchena/Python/Project1_marchenajose/passengers.csv'

# Task 1: Data Loadong Cleaning 

# Load the dataset
df = load_data(file_path)

print('\nTask 1: Data Loadong Cleaning ')
# Display the first few rows to inspect column names
print("\nOriginal Data:")
print(df.head())

# Print column names to debug
print("Column names:", df.columns)

# Clean the dataset
cleaned_df = clean_data(df)

print("\nCleaned Data:")
print(cleaned_df.head())

# Try to use ace_tools to display the cleaned dataset
try:
   import ace_tools as tools
   tools.display_dataframe_to_user(name="Cleaned Passenger Data", dataframe=cleaned_df)
except ImportError:
   # If ace_tools is not available, fall back to displaying the data using pandas
   print("ace_tools is not available. Displaying cleaned data using pandas:")
   print(cleaned_df)
   # Optionally, save the cleaned data to a CSV file
   cleaned_df.to_csv('/Users/josemarchena/Python/Project1_marchenajose/cleaned_passengers.csv', index=False)
   print("Cleaned data saved to 'cleaned_passengers.csv'")


# File path to the cleaned CSV file
cleaned_file_path = '/Users/josemarchena/Python/Project1_marchenajose/cleaned_passengers.csv'

# Load the cleaned dataset
cleaned_df = pd.read_csv(cleaned_file_path, parse_dates=['Birthdate'])

# Task 2: Decision Making and Loops

# Call the fn for the task 2.1
print("\nTask 2.1: Calculate the average age for a specific travel class")
average_age_economy = calculate_average_age(cleaned_df, 'ECONOMY')
print(f"Average age of ECONOMY class passengers: {average_age_economy}")

# Find loyalty members
# Call the fn for the task 2.2
print("\nTask 2.2: Find loyalty members")
loyalty_members = find_loyalty_members(cleaned_df)
print(f"Loyalty Members: {loyalty_members}")

# Task 3.1: Get Class Statistics
print("\nTask 3.1: Get Class Statistics")
class_statistics = get_class_statistics(cleaned_df)

print(f"\nClass Statistics: {class_statistics}")

# Task 4: Data Visualization with Matplotlib

# Task 4.1: Plot Age Distribution
print("\nTask 4.1: Plot Age Distribution")
plot_age_distribution(cleaned_df)

# Task 4.3: Plot Average Age by Class
print("\nTask 4.3: Plot Average Age by Class")
plot_average_age_by_class(cleaned_df)

# Task 5: Data Visualization with Seaborn and Plotly

# Task 5.1: Plot Age vs. Loyalty Membership
print("\nTask 5.1: Plot Age vs. Loyalty Membership")
plot_age_vs_loyalty(cleaned_df)

# Task 5.3: Plot Age Distribution by Class
print("\nTask 5.3: Plot Age Distribution by Class")
plot_age_distribution_by_class(cleaned_df)

#####

# Task 6: Additional Visualizations

# Task 6.1: Plot Travel Class Distribution as a Pie Chart
print("\nTask 6.1: Plot Travel Class Distribution as a Pie Chart")
plot_travel_class_distribution(cleaned_df)

# Task 6.2: Plot Number of Loyalty Members by Travel Class
print("\nTask 6.2: Plot Number of Loyalty Members by Travel Class")
plot_loyalty_members_by_class(cleaned_df)

# Task 7: Heatmap Visualizations

# Option 1: Correlation Heatmap
print("\nTask 7.1: Plot Correlation Heatmap")
plot_correlation_heatmap(cleaned_df)

# Option 2: Travel Class vs. Age Heatmap
print("\nTask 7.2: Plot Travel Class vs. Age Heatmap")
plot_class_age_heatmap(cleaned_df)

# Option 3: Travel Class vs. Flight Number Heatmap
print("\nTask 7.3: Plot Travel Class vs. Flight Number Heatmap")
plot_class_flight_heatmap(cleaned_df)

