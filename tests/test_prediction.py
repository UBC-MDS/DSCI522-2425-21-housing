import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.prediction import make_predictions

class TestMakePredictions(unittest.TestCase):

    @patch('builtins.open', create=True)  # Mock the open function
    @patch('pickle.load')  # Mock pickle.load to return a mock model
    def test_make_predictions(self, mock_load, mock_open):
        # Mock the predict method of the model
        mock_model = MagicMock()
        mock_model.predict.return_value = [100000, 200000, 300000, 400000, 500000]
        
        # Simulate loading the model using pickle
        mock_load.return_value = mock_model

        # Sample input data for predictions
        input_data = {
            'meters': [174.23, 132.76, 90.82, 68.54, 221.30],
            'garage': ['Y', 'Y', 'Y', 'N', 'Y'],
            'firepl': ['Y', 'N', 'N', 'N', 'Y'],
            'bsmt': ['Y', 'Y', 'N', 'N', 'Y'],
            'bdevl': ['N', 'Y', 'Y', 'N', 'Y']
        }

        # Call the make_predictions function
        model_file = 'fake_model.pkl'  # The model file is not actually loaded because we are mocking it
        result_df = make_predictions(model_file, input_data)

        # Assertions
        self.assertIsInstance(result_df, pd.DataFrame, "Output should be a DataFrame")
        self.assertEqual(result_df.shape[0], 5, "Number of rows in the result should be 5")
        self.assertIn('Predicted_Values', result_df.columns, "'Predicted_Values' column should exist")
        
        # Check the first few predicted values
        self.assertEqual(result_df['Predicted_Values'].iloc[0], 100000, "First prediction should be 100000")
        self.assertEqual(result_df['Predicted_Values'].iloc[1], 200000, "Second prediction should be 200000")

if __name__ == '__main__':
    unittest.main()
