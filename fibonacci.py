#
# Fibonacci Numbers Test Change
#
# 0, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
#
import q
import unittest

@q
def fib(n):
    ''' Fibonacci numbers.
    Examples
    ========
    >>> fib(10)
    89
    >>> fib(11)
    144
    >>> fib(50)
    20365011074
    '''
    if type(n) != int:
        raise TypeError('n must be of type int.')
    a, b = 0, 1
    for _ in range(1, n + 1):
        a, b = b, a + b
    return b

class TestFib(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(fib(10), 89)
        self.assertEqual(fib(11), 144)
    def test_true(self):
        self.assertTrue(fib(50) == 20365011074)
    def test_type_error(self):
        with self.assertRaises(TypeError):
            fib('string')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #unittest.main()
    #print(fib(10))
    #print(fib(11))
    #print(fib(50))
