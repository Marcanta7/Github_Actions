import unittest


from main import add


class TestCalculadoraFunctions(unittest.TestCase):
    def test_sumar(self):
        """Test de la función sumar"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(2.5, 3.5), 6.0)


if __name__ == '_main_':
    unittest.main()