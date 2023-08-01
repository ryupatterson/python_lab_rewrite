import unittest
import answer_key.example_python_lab4 as expected
import python_lab4 as actual
import os, json

pwd = os.getcwd()

INFILE = "sample_logs.log"
for root, dirs, files in os.walk(pwd):
    for file in files:
        if file == INFILE:
            INFILE = os.path.join(pwd, root, file)

class Lab4UnitTests(unittest.TestCase):
    def test_lab4(self):
        expected_string_list = expected.ingest_logs(INFILE)
        actual_string_list = actual.ingest_logs(INFILE)

        expected_output = expected.format_logs(expected_string_list) # jsonified strings
        actual_output = actual.format_logs(actual_string_list) # jsonified strings

        expected_parsed = json.loads(expected_output)
        actual_parsed = json.loads(actual_output)

        equals = True
        if len(expected_parsed) != len(actual_parsed):
            equals = False
        
        if equals:
            for index, line in enumerate(expected_parsed):
                if line != actual_parsed[index]:
                    equals = False
        
        self.assertTrue(equals)


if __name__ == "__main__":
    unittest.main()