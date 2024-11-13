import unittest
from datetime import datetime

class TestStockVisualizerInputs(unittest.TestCase):
    
    def test_symbol(self):
        # Arrange
        valid_symbol = "IBM"
        invalid_symbols = ["ibm", "IBM11", "IBMIBMIBM"]
        
        # Act and Assert for valid symbol
        result = self.is_valid_symbol(valid_symbol)
        self.assertTrue(result)

        # Act and Assert for invalid symbols
        for symbol in invalid_symbols:
            result = self.is_valid_symbol(symbol)
            self.assertFalse(result)

    def test_chart_type(self):
        # Arrange
        valid_chart_types = ["1", "2"]
        invalid_chart_types = ["3", "a"]
        
        # Act and Assert for valid chart types
        for chart_type in valid_chart_types:
            result = self.is_valid_chart_type(chart_type)
            self.assertTrue(result)

        # Act and Assert for invalid chart types
        for chart_type in invalid_chart_types:
            result = self.is_valid_chart_type(chart_type)
            self.assertFalse(result)

    def test_time_series(self):
        # Arrange
        valid_time_series = ["1", "2", "3", "4"]
        invalid_time_series = ["0", "abc"]
        
        # Act and Assert for valid time series options
        for time_series in valid_time_series:
            result = self.is_valid_time_series(time_series)
            self.assertTrue(result)

        # Act and Assert for invalid time series options
        for time_series in invalid_time_series:
            result = self.is_valid_time_series(time_series)
            self.assertFalse(result)

    def test_start_date(self):
        # Arrange
        valid_dates = ["2022-01-01", "1999-12-31"]
        invalid_dates = ["2022-13-01", "22-01-01"]

        # Act and Assert for valid dates
        for date_str in valid_dates:
            result = self.is_valid_date(date_str)
            self.assertTrue(result)

        # Act and Assert for invalid dates
        for date_str in invalid_dates:
            result = self.is_valid_date(date_str)
            self.assertFalse(result)

    def test_end_date(self):
        # Arrange
        valid_dates = ["2022-01-01", "1999-12-31"]
        invalid_dates = ["2022-13-01", "22-01-01"]

        # Act and Assert for valid dates
        for date_str in valid_dates:
            result = self.is_valid_date(date_str)
            self.assertTrue(result)

        # Act and Assert for invalid dates
        for date_str in invalid_dates:
            result = self.is_valid_date(date_str)
            self.assertFalse(result)

    # Helper methods
    def is_valid_symbol(self, symbol):
        return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

    def is_valid_chart_type(self, chart_type):
        return chart_type in {"1", "2"}

    def is_valid_time_series(self, time_series):
        return time_series in {"1", "2", "3", "4"}

    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    unittest.main()