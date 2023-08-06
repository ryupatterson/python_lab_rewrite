import unittest
import python_lab1

class Lab1UnitTests(unittest.TestCase):
    def test_question_1(self):
        expected = 5
        actual = python_lab1.question_1()
        self.assertEqual(expected, actual)
    
    def test_question_2(self):
        expected = ["3.2", 'python', 9.8]
        actual = python_lab1.question_2()
        self.assertListEqual(expected, actual)
    
    def test_question_3(self):
        expected = 25
        actual = python_lab1.question_3()
        self.assertEqual(expected, actual)
    
    def test_question_4(self):
        expected = "python rocks"
        actual = python_lab1.question_4()
        self.assertEqual(expected, actual)
    
    def test_question_5(self):
        expected = 5.2
        actual = python_lab1.question_5()
        self.assertEqual(expected, actual)
    
    def test_question_6(self):
        expected = "9.825"
        actual = python_lab1.question_6()
        self.assertEqual(expected, actual)

    def test_question_7(self):
        expected = str
        actual = python_lab1.question_7()
        self.assertEqual(expected, actual)
    
    def test_question_8(self):
        expected = 3.2
        actual = python_lab1.question_8()
        self.assertEqual(expected, actual)
    
    def test_question_9(self):
        expected = "The Earth is ROUND"
        actual = python_lab1.question_9()
        self.assertEqual(expected, actual)

    def test_question_10(self):
        expected = "hello"
        actual = python_lab1.question_10()
        self.assertEqual(expected, actual)
    
    def test_question_11(self):
        expected = "This PC costs $1999.00"
        actual = python_lab1.question_11()
        self.assertEqual(expected, actual)
    
    def test_question_12(self):
        e1, e2, e3 = (
            [600, 'laptop', 1999, 'PC', 450, 'console'], 
            [600, 'laptop', 1999, 'PC', 450, 'console'], 
            [580, 'laptop', 1999, 'PC', 450, 'console']
        )

        a1, a2, a3 = python_lab1.question_12()
        self.assertTrue(e1 == a1 and e2 == a2 and e3 == a3)
    
    def test_question_13(self):
        binary_expected, hex_expected = "0b10001100", "0x8c"
        binary_actual, hex_actual = python_lab1.question_13()
        self.assertTrue(binary_actual == binary_expected and hex_expected == hex_actual)
    
    def test_question_14(self):
        expected = ["attack_box", "redirector", "target"]
        actual = list(python_lab1.question_14())
        self.assertEqual(expected, actual)
    
    def test_question_15(self):
        expected = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris', "network_ips": ['10.10.10.1', '10.10.10.254']}
        actual = python_lab1.question_15()
        self.assertDictEqual(expected, actual)

    def test_question_16(self):
        expected = {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'Windows 7'}
        actual = python_lab1.question_16()
        self.assertDictEqual(expected, actual)
    
    def test_question_17(self):
        e1, e2, e3 = (
            {'attack_box': 'kali', 'redirector': 'freeBSD', 'target': 'solaris'},
            {'attack_box': 'kali', 'redirector': 'freeBSD', 'target': 'solaris'},
            {'attack_box': 'kali', 'redirector': 'centOS', 'target': 'solaris'}
        )

        a1, a2, a3 = python_lab1.question_17()
        with self.subTest(e1=a1):
            self.assertEqual(e1, a1)
        
        with self.subTest(e2=a2):
            self.assertEqual(e2, a2)
        
        with self.subTest(e3=a3):
            self.assertEqual(e3, a3)

    def test_question_18(self):
        expected = 10
        actual = python_lab1.question_18()
        self.assertEqual(expected, actual)
    
    def test_question_19(self):
        e1, e2, e3 = 5, 8, 11
        a1, a2, a3 = python_lab1.question_19()
        
        with self.subTest(e1=a1):
            self.assertEqual(e1, a1)
        
        with self.subTest(e2=a2):
            self.assertEqual(e2, a2)
        
        with self.subTest(e3=a3):
            self.assertEqual(e3, a3)
    
    def test_question_20(self):
        expected = 13
        actual = python_lab1.question_20()
        self.assertEqual(expected, actual)
    
    def test_question_21(self):
        expected = "192.168.1.15"
        actual = python_lab1.question_21(python_lab1.HEXDUMP_IP)
        self.assertEqual(expected, actual)
    
    def test_question_22(self):
        expected = {'src_ip': '192.168.1.15', 'dst_ip': '192.168.1.1', 'src_port': 63612, 'dst_port': 443}
        actual = python_lab1.question_22(python_lab1.HEXDUMP)
        self.assertDictEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
