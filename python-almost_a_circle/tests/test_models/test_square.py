from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_initialization(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)

    def test_invalid_square_types(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_invalid_square_values(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_method_square(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")

    def test_to_dictionary_square(self):
        s = Square(10, 2, 1, 89)
        self.assertEqual(s.to_dictionary(), {'id': 89, 'size': 10, 'x': 2, 'y': 1})

    def test_update_square(self):
        s = Square(10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(size=1, x=2, y=3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
