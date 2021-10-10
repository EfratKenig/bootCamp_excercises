import json
import math
import unittest

from ex1 import combine_lines
from ex2 import generate_psd, validate_password
from ex4 import my_reduce
from ex5 import EquilateralTriangle, Square, Rectangle, Circle


class MyTestCase(unittest.TestCase):
    def test_combine_lines(self):
        with open("file_A.txt", 'w') as a:
            a.write("Hello girls!\nToday is Tuesday\nGood luck!!!")
        with open("file_B.txt", 'w') as b:
            b.write("We are learning python\nThe best language!!:)")

        combine_lines('file_A.txt', 'file_B.txt', 'combination.json', [0, 1, 2], [0, 1])
        with open("combination.json", 'r') as j:
            res = json.load(j)

        self.assertEqual(res, {
            "line1": ["Hello girls!", "We are learning python"],
            "line2": ["Today is Tuesday", "The best language!!:)"],
            "line3": ["Good luck!!!"],
        }
                         )

    def test_validate_password(self):
        # tests both functions, one as the other's input
        compare = [True for _ in range(300)]
        res = []
        for i in range(300):
            res.append(validate_password(generate_psd()))
        self.assertEqual(res, compare)

    def test_deck(self):
        from deck import Deck
        cards = []
        compare = []
        deck = Deck()
        for card in deck:
            cards.append(card)
        after_iter = deck.cards
        self.assertEqual(after_iter, compare)

    def test_my_reduce(self):
        def multiple(a, b):
            return a * b
        res = my_reduce(multiple, [1, 2, 3, 4, 5, 6])
        self.assertEqual(res, 720)

    def test_ex5(self):
        res = []
        compare = []

        triangle = EquilateralTriangle(6)
        res.append(triangle.calculate_area())
        compare.append(round(6 * math.sqrt(3) / 2, 3))
        res.append(triangle.calculate_perimeter())
        compare.append(6 * 3)

        circle = Circle(6)
        res.append(circle.calculate_area())
        compare.append(round((6 ** 2) * math.pi, 3))
        res.append(circle.calculate_perimeter())
        compare.append(round((6 * 2) * math.pi, 3))

        square = Square(6)
        res.append(square.calculate_area())
        compare.append(6 * 6)
        res.append(square.calculate_perimeter())
        compare.append(6 * 4)

        rectangle = Rectangle(6, 7)
        res.append(rectangle.calculate_area())
        compare.append(6 * 7)
        res.append(rectangle.calculate_perimeter())
        compare.append((6 + 7) * 2)
        self.assertEqual(res, compare)


if __name__ == '__main__':
    unittest.main()
