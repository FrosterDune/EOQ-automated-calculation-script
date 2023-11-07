import unittest
import pandas as pd

from QoptEN import Qopt

class QoptTest(unittest.TestCase):

    df_firstresults = pd.read_csv(
        filepath_or_buffer="test_results1.csv", encoding="UTF-8", delimiter=",", index_col=0)
    df_secondresults = pd.read_csv(
        filepath_or_buffer="test_results2.csv", encoding="UTF-8", delimiter=",", index_col=0)
    qopt_test = Qopt()

    # Generate the result DataFrame and compare the results of df dataframe and results from the results file
    def test_qopt_firstsample(self):
        result_df = self.qopt_test.calculations_qopt(4000, 1200, 300, 0.2, 1, 1)
        self.assertTrue(result_df.equals(self.df_firstresults.round(1)))

    def test_qopt_secondsample(self):
        result_df = self.qopt_test.calculations_qopt(10000, 5000, 1, 400, 1, 0.25)
        self.assertTrue(result_df.equals(self.df_secondresults.round(1)))

if __name__ == '__main__':
    unittest.main()