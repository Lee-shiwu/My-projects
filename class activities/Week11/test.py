
import argparse
import math
import sys
import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def root(x, n=2):
    if x < 0 and n % 2 == 0:
        raise ValueError("Even root of negative number")
    return x ** (1 / n)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


def main_cli():
    parser = argparse.ArgumentParser(
        description="Engineering calculator: +, -, *, /, pow, root, sin, cos, tan"
    )
    parser.add_argument("op", choices=[
        "add","sub","mul","div",
        "pow","root",
        "sin","cos","tan"
    ], help="operation")
    parser.add_argument("args", nargs="+", type=float, help="operands")
    args = parser.parse_args()

    ops = {
        "add": add, "sub": sub, "mul": mul, "div": div,
        "pow": power, "root": root,
        "sin": sin, "cos": cos, "tan": tan
    }
    func = ops[args.op]
    try:
        result = func(*args.args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    print(result)


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(2.5, 0.1), 2.6)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(mul(4, 2), 8)
        self.assertEqual(mul(3, 0), 0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


class TestPowerRoot(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertAlmostEqual(power(9, 0.5), 3.0)

    def test_root(self):
        self.assertEqual(root(16, 2), 4)
        self.assertAlmostEqual(root(27, 3), 3.0)
        with self.assertRaises(ValueError):
            root(-8, 2)


class TestTrigonometry(unittest.TestCase):
    def test_sin_cos(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(math.pi/2), 1)
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(math.pi), -1)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(math.pi/4), 1)


if __name__ == "__main__":
    unittest.main()
