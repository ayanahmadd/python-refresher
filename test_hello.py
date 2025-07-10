import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)

    def test_add(self):
        self.assertEqual(hello.add(3, 7), 10)
        self.assertEqual(hello.add(6, 5), 11)

    def test_sub(self):
        self.assertEqual(hello.sub(5, 3), 2)
        self.assertEqual(hello.sub(6, 5), 1)

    def test_mul(self):
        self.assertEqual(hello.mul(5, 3), 15)
        self.assertEqual(hello.mul(6, 5), 30)

    def test_div(self):
        self.assertEqual(hello.div(6, 3), 2)
        self.assertEqual(hello.div(21, 7), 3)

    def test_div(self):
        self.assertEqual(hello.div(6, 3), 2)
        self.assertEqual(hello.div(21, 7), 3)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(36), 6)
        self.assertEqual(hello.sqrt(49), 7)

    def test_power(self):
        self.assertEqual(hello.power(2, 3), 8)
        self.assertEqual(hello.power(3, 3), 27)

    def test_log(self):
        self.assertEqual(hello.log(100), 4.605170185988092)
        self.assertEqual(hello.log(1000), 6.907755278982137)

    def test_exp(self):
        self.assertEqual(hello.exp(100), 2.6881171418161356e43)
        self.assertEqual(hello.exp(25), 72004899337.38588)


if __name__ == "__main__":
    unittest.main()
