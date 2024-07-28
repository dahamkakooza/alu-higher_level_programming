from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_initialization(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str_method(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        # Test display method implementation here

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 89)
        self.assertEqual(r.to_dictionary(), {'id': 89, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(width=1, height=2, x=3, y=4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
