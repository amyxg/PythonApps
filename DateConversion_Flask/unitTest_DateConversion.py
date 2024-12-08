import unittest
from dateConversion import app, dateToLabel

class TestDateConverter(unittest.TestCase):
    def setUp(self):
        """
        Set up test for user(s), making sure it can connect to server

        Parameters
        ----------
        self

        Returns
        -------
        none
        
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_dateToLabel(self):
        """
        Test test_dateToLabel functionality

        Parameters
        ----------
        self

        Returns
        -------
        none
        
        """
        # Test valid dates
        self.assertEqual(dateToLabel("09/08/2024"), "September 08, 2024")
        self.assertEqual(dateToLabel("01/01/2024"), "January 01, 2024")
        self.assertEqual(dateToLabel("12/31/2024"), "December 31, 2024")
        
        # Test invalid month
        self.assertEqual(
            dateToLabel("13/01/2024"), 
            "Error: 13 (mm) was not a valid month. Month should between 1 and 12."
        )
        
        # Test invalid format
        self.assertEqual(
            dateToLabel("9/8/2024"),
            "Error: Incorrect format for date. Must be in mm/dd/yyyy format"
        )
        
        # Test invalid numbers
        self.assertEqual(
            dateToLabel("aa/01/2024"),
            "Error: month (mm), day (dd), and year (yyyy) must be numbers"
        )

    def testHomeRoute(self):
        """
        Test the homepage route (/)

        Parameters
        ----------
        self

        Returns
        -------
        none
        
        """
        # Test GET request to home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check if page loads
        self.assertIn(b'Enter a date:', response.data)  # Check if form exists
        
        # Test POST request to dateToLabel route
        response = self.app.post('/dateToLabel', data={'userDate': '09/08/2024'})
        self.assertEqual(response.status_code, 200)  # Check if response is successful
        self.assertIn(b'September', response.data)  # Check if conversion appears
        
        # Test invalid date POST request
        response = self.app.post('/dateToLabel', data={'userDate': '13/01/2024'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)  # Check if error message appears

if __name__ == '__main__':
    unittest.main()