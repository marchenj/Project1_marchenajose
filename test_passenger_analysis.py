# Task 7: Implement unit tests for functions from passenger_analysis.py 

import unittest
import pandas as pd
from datetime import datetime
import logging
from passenger_analysis import load_data, clean_data, calculate_average_age, find_loyalty_members, get_class_statistics

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestPassengerAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up a sample dataframe for testing.
        This method is called once for the test class.
        """
        logging.info("Setting up sample data for testing...")
        
        # Sample data for testing
        cls.sample_data = {
            'PassengerID': [3321, 3322, 3323, 3324, 3325],
            'Name': ['Jose Abel', 'Chris Smith', 'Pat Wong', 'Denisse Johnson', 'Sully Tam'],
            'Birthdate': ['1902-12-23', '1980-11-12', '1991-03-08', '1984-07-19', '1982-08-30'],
            'TravelClass': ['FIRST_CLASS', 'BUSINESS', 'ECONOMY', 'ECONOMY', 'FIRST_CLASS'],
            'LoyaltyMember': [True, False, True, False, True],
            'FlightNumber': ['LA249', 'UA100', 'BA255', 'AA110', 'BA249']
        }
        
        # Print sample data for verification
        print('\nSample data for testing:')
        print(cls.sample_data)
        
        # Convert sample data to DataFrame
        cls.df = pd.DataFrame(cls.sample_data)
        
        # Convert 'Birthdate' to datetime
        cls.df['Birthdate'] = pd.to_datetime(cls.df['Birthdate'])
        logging.info("Sample data setup complete.")

    def test_load_data(self):
        """
        Test the load_data function.
        Since load_data reads from a file, this test simulates its effect by checking the columns.
        """
        logging.info("Testing load_data function...")
        # Expected column names after loading data
        expected_columns = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
        # Verify if the dataframe columns match the expected columns
        self.assertListEqual(list(self.df.columns), expected_columns)
        logging.info("load_data function test passed.")

    def test_clean_data(self):
        """
        Test the clean_data function to ensure it handles missing values and data types correctly.
        """
        logging.info("Testing clean_data function...")
        # Clean the sample dataframe
        cleaned_df = clean_data(self.df)
        
        # Check if there are no missing values
        self.assertFalse(cleaned_df.isnull().values.any())
        
        # Check if 'Birthdate' is of datetime type
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned_df['Birthdate']))
        
        # Check if 'LoyaltyMember' is of boolean type
        self.assertTrue(pd.api.types.is_bool_dtype(cleaned_df['LoyaltyMember']))
        logging.info("clean_data function test passed.")

    def test_calculate_average_age(self):
        """
        Test the calculate_average_age function to ensure it calculates the correct average age for a travel class.
        """
        logging.info("Testing calculate_average_age function for 'ECONOMY' class...")
        
        # Calculate the current year
        current_year = datetime.now().year
        
        # Calculate the expected average age for the 'ECONOMY' travel class
        expected_avg_age = (current_year - self.df[self.df['TravelClass'] == 'ECONOMY']['Birthdate'].dt.year).mean()
       
        # Calculate the actual average age using the function
        actual_avg_age = calculate_average_age(self.df, 'ECONOMY')
       
        # Verify if the actual average age matches the expected average age
        self.assertEqual(actual_avg_age, expected_avg_age)
        logging.info("calculate_average_age function test passed.")

    def test_find_loyalty_members(self):
        """
        Test the find_loyalty_members function to ensure it returns the correct list of loyalty members.
        """
        logging.info("Testing find_loyalty_members function...")
        
        # Expected list of loyalty member names
        expected_loyalty_members = self.df[self.df['LoyaltyMember']]['Name'].tolist()
       
        # Actual list of loyalty member names using the function
        actual_loyalty_members = find_loyalty_members(self.df)
       
        # Verify if the actual list matches the expected list
        self.assertListEqual(actual_loyalty_members, expected_loyalty_members)
        logging.info("find_loyalty_members function test passed.")

    def test_get_class_statistics(self):
        """
        Test the get_class_statistics function to ensure it returns correct statistics for each travel class.
        """
        logging.info("Testing get_class_statistics function...")
        
        # Calculate the current year
        current_year = datetime.now().year
        
        # Calculate the expected average age for each travel class
        avg_age_first_class = (current_year - self.df[self.df['TravelClass'] == 'FIRST_CLASS']['Birthdate'].dt.year).mean()
        avg_age_business = (current_year - self.df[self.df['TravelClass'] == 'BUSINESS']['Birthdate'].dt.year).mean()
        avg_age_economy = (current_year - self.df[self.df['TravelClass'] == 'ECONOMY']['Birthdate'].dt.year).mean()
        
        # Get the statistics using the function
        stats = get_class_statistics(self.df)
        
        # Verify if the actual statistics match the expected statistics
        self.assertEqual(stats['FIRST_CLASS']['Average Age'], avg_age_first_class)
        self.assertEqual(stats['BUSINESS']['Average Age'], avg_age_business)
        self.assertEqual(stats['ECONOMY']['Average Age'], avg_age_economy)
        self.assertEqual(stats['FIRST_CLASS']['Loyalty Members'], 2)
        self.assertEqual(stats['BUSINESS']['Loyalty Members'], 0)
        self.assertEqual(stats['ECONOMY']['Loyalty Members'], 1)
        logging.info("get_class_statistics function test passed.")

if __name__ == '__main__':
    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPassengerAnalysis)
    result = test_runner.run(test_suite)

    # Print explanation of the output
    print("\nExplanation of the Output:")
    print("1. Log Messages: These provide detailed information about the progress and results of each test.")
    print("2. Dot Characters ('.'): Each dot represents a single test that has run. Since there are five tests, you see five dots.")
    print("3. 'OK' Message: This indicates that all tests were successful. If any test were to fail, additional information about the failure would be provided.")
    print("4. Summary: Shows the total number of tests run and the total time taken, followed by 'OK' to indicate all tests passed.")
    
    
    
    
        
        
        