import unittest
import example_python_lab2
import inspect, re

class Lab2UnitTests(unittest.TestCase):
    def test_withdrawal(self):
        balance = 1000.0
        
        with self.subTest("Successful withdrawal test"):
            withdrawal = 250.2
            expected = str('%.2f' % (balance - withdrawal))
            actual = example_python_lab2.withdrawal(balance, withdrawal)
            self.assertEqual(expected, actual)

        with self.subTest("Withdrawal full balance test"):
            withdrawal = 1000.0
            expected = "This is all your money!"
            actual = example_python_lab2.withdrawal(balance, withdrawal)
            self.assertEqual(expected, actual)

        with self.subTest("Withdrawal fail test"):
            withdrawal = 1000.5
            expected = "Insufficient funds."
            actual = example_python_lab2.withdrawal(balance, withdrawal)
            self.assertEqual(expected, actual)
    
    def test_product_is_even(self):
        with self.subTest("Product is even"):
            expected = True
            actual = example_python_lab2.product_is_even(7, 2)
            self.assertEqual(expected, actual)
        
        with self.subTest("Product is odd"):
            expected = False
            actual = example_python_lab2.product_is_even(7, 3)
            self.assertEqual(expected, actual)

        with self.subTest("Product is zero"):
            expected = True
            actual = example_python_lab2.product_is_even(7, 0)
            self.assertEqual(expected, actual)

    def test_reverse_squared(self):
        with self.subTest("Does not contain .reverse()"):
            code = inspect.getsource(example_python_lab2.reverse_squared)
            actual = re.search(r'[a-zA-Z]+\.reverse()', code)
            self.assertFalse(actual)
        
        with self.subTest("Generic list reversal test"):
            example_input = ["hello", "yes", "goodbyes"]
            expected = ["seybdoog", "sey", "olleh"]
            actual = example_python_lab2.reverse_squared(example_input)
            self.assertListEqual(expected, actual)
        
        with self.subTest("Empty list reversal test"):
            example_input = []
            actual = example_python_lab2.reverse_squared(example_input)
            self.assertFalse(actual)

    def test_times_tables(self):
        x = 3
        y = 5
        actual = example_python_lab2.times_tables(x, y)
        for i in range(1, x+1):
            for k in range(1, y+1):
                with self.subTest(i*k):
                    self.assertEqual(i*k, actual[i-1][k-1])

    def test_remove_vowels(self):
        input = "hello"
        expected = "hll"
        actual = example_python_lab2.remove_vowels(input)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()