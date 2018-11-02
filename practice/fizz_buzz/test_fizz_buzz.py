"""

Z - zero
O - one
M - many
B - boundaries
I - interface
E - exceptions
S - simple

ZI
fizz_buzz(0)
-> ""

O
fizz_buzz(1)
-> 1

M
fizz_buzz(2)
-> 1, 2

B
fizz_buzz(3)
-> 1, 2, fizz

You can’t write any production code until you have first written a failing unit test.
You can’t write more of a unit test than is sufficient to fail, and not compiling is failing.
You can’t write more production code than is sufficient to pass the currently failing unit test.

"""

# this is a comment

from practice.fizz_buzz.fizz_buzz import fizz_buzz


def test_fizz_buzz_zero():
    expected = []

    actual = fizz_buzz(0)

    assert expected == actual


def test_fizz_buzz_one():
    expected = [1]

    actual = fizz_buzz(1)

    assert expected == actual


def test_fizz_buzz_three():
    expected = [1, 2, 'fizz']

    actual = fizz_buzz(3)

    print(actual)
    assert expected == actual


def test_fizz_buzz_five():
    expected = [1, 2, 'fizz', 4, 'buzz']

    actual = fizz_buzz(5)

    print(actual)
    assert expected == actual


def test_fizz_buzz_six():
    expected = [1, 2, 'fizz', 4, 'buzz', 'fizz']

    actual = fizz_buzz(6)

    print(actual)
    assert expected == actual


def test_fizz_buzz_ten():
    expected = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']

    actual = fizz_buzz(10)

    print(actual)
    assert expected == actual


def test_fizz_buzz_fifteen():
    expected = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']

    actual = fizz_buzz(15)

    print(actual)
    assert expected == actual


def test_fizz_buzz_thirty():
    expected = [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz',
                16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizzbuzz'
                ]

    actual = fizz_buzz(30)

    print(actual)
    assert expected == actual
