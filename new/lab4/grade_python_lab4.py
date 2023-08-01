import unittest
import answer_key.example_python_lab4 as expected
import python_lab4 as actual

INFILE = "sample_logs.log"

class Lab4UnitTests(unittest.TestCase):
    def test_lab4(self):
        expected_string_list = expected.ingest_logs(INFILE)
        actual_string_list = actual.ingest_logs(INFILE)

        expected_output = expected.format_logs(expected_string_list)
        actual_output = actual.format_logs(actual_string_list)

        equals = True
        if len(expected_output) != len(actual_output):
            equals = False
        
        if equals:
            for index, line in enumerate(expected_output):
                if line != actual_output[index]:
                    equals = False
        
        self.assertTrue(equals)


if __name__ == "__main__":
    unittest.main()