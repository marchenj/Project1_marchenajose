Flight Management Syst
/Users/josemarchena/Python/Project1_marchenajose/

│
├── inspect_csv.py
├── passenger_analysis.py
├── test_passenger_analysis.py
├── marchenj_passengers.py
├── passengers.csv
├── cleaned_passengers.csv
└── README.md


Files and Their Functions
1. inspect_csv.py
	Objective: This script is used to inspect the content of the CSV file to ensure it is read correctly.
	Usage: Run this script to view the first lines of the passengers.csv file and check the formatting.

2. passenger_analysis.py
	Objective: This module contains all the functions for data loading, cleaning, analysis, and visualization.
	Functions:
	- load_data(file_path): Loads the CSV file into a pandas DataFrame.
	- clean_data(df): Cleans the DataFrame by handling missing values and ensuring appropriate data types.
	- calculate_average_age(df, travel_class): Calculates the average age of passengers in the specified travel class.
	- find_loyalty_members(df): Finds names of passengers who are loyalty program members.
	- get_class_statistics(df): Returns a dictionary with travel classes as keys and their respective average ages and number of loyalty members as values.
	- plot_age_distribution(df): Plots the distribution of ages using a histogram.
	- plot_average_age_by_class(df): Plots the average age by travel class  using a bar chart.
	- plot_age_vs_loyalty(df): Plots a scatter plot of age vs. loyalty membership using Seaborn.
	- plot_age_distribution_by_class(df): Plots the distribution of ages for each travel class using a box plot with Plotly.

3. test_passenger_analysis.py
	Objective: This script contains unit tests for the functions in passenger_analysis.py.
	Usage: Run this script to execute the tests and ensure the functions in passenger_analysis.py are working correctly.
		Tests:
	- test_load_data(): Tests the load_data function.
	- test_clean_data(): Tests the clean_data function.
	- test_calculate_average_age(): Tests the calculate_average_age function.
	- test_find_loyalty_members(): Tests the find_loyalty_members function.
	- test_get_class_statistics(): Tests the get_class_statistics function.

4. marchenj_passengers.py
	Objective: This is the main script that integrates all the functions and executes the overall analysis and visualization.
	Workflow:
	Step1: Loads the original data from passengers.csv.
	Step2: Cleans the data.
	Step3: Performs various analyses and visualizations, including calculating average age, finding loyalty members, and plotting different charts.
	Usage: Run this script to see the complete workflow and outputs of the project.

5. passengers.csv
	Objective: This is the original dataset containing passenger information.
	Columns:
	PassengerID: Unique identifier for each passenger.
	Name: Full name of the passenger.
	Birthdate: Birthdate of the passenger.
	TravelClass: Class of travel (e.g., Economy, Business, First).
	LoyaltyMember: Whether the passenger is a loyalty program member (True/False).
	FlightNumber: Flight number.

6. cleaned_passengers.csv
	Objective: This file is generated after cleaning the original dataset. It is used for further analysis and visualization.

How to Run the Project
Step1: Inspect the CSV File:
python inspect_csv.py

Step2: Run the Main Script:
python marchenj_passengers.py


Step3: Run the Unit Tests:
python test_passenger_analysis.py

Dependencies
- Python 3.x
- pandas
- matplotlib
- seaborn
- plotly
- unittest
- kaleido

Installation
Install the required packages using pip:
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly 
pip install kaleido

Summary
This project provides an analysis of flight passengers, utilizing various data visualization techniques to derive meaningful insights. The unit tests ensure the reliability of each function.


