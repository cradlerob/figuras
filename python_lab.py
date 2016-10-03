# -*- coding: utf-8 -*-


def minutes_in_weeks(weeks):
    """ 1: (Task 0.5.1) Minutes in a Week
    >>> minutes_in_weeks(1)
    10080
    >>> minutes_in_weeks(2)
    20160
    """
    return weeks * 7 * 24 * 60


def remainder_without_mod(numerator, divisor):
    """2: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    return numerator - ((numerator / divisor) * divisor)


def divisible_by_3(num):
    """3: (Task 0.5.3) Divisibility
    >>> divisible_by_3(9)
    True
    >>> divisible_by_3(7)
    False
    """

    return num % 3 == 0


def predict_expression(x, y, prediction):
    """4: (Task 0.5.4) Conditional Expression
    Try to predict the value of 2**(y+1/2) if x+10<0 else 2**(y-1/2)
    >>> predict_expression(-9, 1/2, 1)
    1

    >>> predict_expression(-9, 2, 4)
    4
    """
    return 2 ** (y + 1 / 2) if x + 10 < 0 else 2 ** (y - 1 / 2)


def squares_set(numbers):
    """5: (Task 0.5.5) Squares Set Comprehension
    Given a set of numbers return a set of the numbers squared
    >>> squares_set({1,2,3,4,5,5,5})
    set([16, 1, 4, 25, 9])
    """

    return set([x**2 for x in numbers])


def pows_two(numbers):
    """6: (Task 0.5.6) Powers-of-2 Set Comprehension
    Given a set of numbers return the powers of two of those numbers
    >>> pows_two({0,1,2,3,4})
    set([8, 1, 2, 4, 16])"""
    return set([2**x for x in numbers])


def set_product57(xs, ys):
    """7: (Task 0.5.7) Double comprehension evaluating to nine-element set
    Return a set containing the multiplication of every element in a set multiplied by the other
    >>> set_product57({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 9, 10, 12, 15])
    """
    return set([i * j for i in xs for j in ys])


def set_product58(xs, ys):
    """8: (Task 0.5.8) Double comprehension evaluating to five-element set
    Return a set containing the multiplicacion of every elment in a set multiplied by the other
    where elements dont repeat
    >>> set_product58({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 10, 12, 15])
    """
    return set([i * j for i in xs for j in ys if i != j])


def intersection(Ss, Ts):
    """
    9: (Task 0.5.9) Set intersection as a comprehension
    >>> intersection({1, 2, 3, 4},{3, 4, 5, 6})
    set([3, 4])
    """
    return Ss & Ts
