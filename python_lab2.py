# -*- coding: utf-8 -*-
import doctest


def minutes_in_weeks(weeks):
    """ 1: (Task 0.5.1) Minutes in a Week

    >>> minutes_in_weeks(1)
    10080

    >>> minutes_in_weeks(2)
    20160
    """
    return weeks * 10080


def remainder_without_mod(numerator, divisor):
    """
    2: (Task 0.5.2) Remainder
    >>> remainder_without_mod(28,7)
    0
    >>> remainder_without_mod(30,7)
    2
    """
    # if(numerator<divisor):
    #     return numerator
    # else:
    #     return remainder_without_mod((numerator-divisor),divisor)

    return numerator if numerator < divisor else remainder_without_mod(numerator - divisor, divisor)


def divisable_by_3(num):
    """
    3: (Task 0.5.3) Divisibility
    >>> divisable_by_3(9)
    True
    >>> divisable_by_3(7)
    False
    """

    return (num % 3) == 0


def predict_expression(x, y, prediction):
    """
    4: (Task 0.5.4) Conditional Expression
    Try to predict the value of 2**(y+1/2) if x+10<0 else 2**(y-1/2)
    >>> predict_expression(-9, 1/2, 1)
    1
    """
    # if((x + 10) < 0):
    #     return 2 ** (y + 1/2)
    # else:
    #     return 2 ** (y - 1/2)
    return 2 ** (y + 1 / 2) if x + 10 < 0 else 2 ** (y - 1 / 2)


def squares_set(numbers):
    """
    5: (Task 0.5.5) Squares Set Comprehension
    Given a set of numbers return a set of the numbers squared
    >>> squares_set({1,2,3,4,5,5,5})
    set([16, 1, 4, 25, 9])
    """
    # num_Set = set(numbers)
    # new_Set = set()
    # for num in num_Set:
    #     new_Set.add(num ** 2)
    # return new_Set
    return set(
        x ** 2
        for x in numbers
    )


def pows_two(numbers):
    """
    6: (Task 0.5.6) Powers-of-2 Set Comprehension
    Given a set of numbers return the powers of two of those numbers
    >>> pows_two({0,1,2,3,4})
    set([8, 1, 2, 4, 16])
    """
    # new_Set =set()
    # for num in numbers:
    #     new_Set.add(2 ** num)
    # return new_Set
    return set([
        2 ** x
        for x in numbers
    ])


def set_product57(xs, ys):
    """
    7: (Task 0.5.7) Double comprehension evaluating to nine-element set
    Return a set containing the multiplication of every element in a set multiplied by the other
    >>> set_product57({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 9, 10, 12, 15])
    """
    #new_Set = set()
    # for numXs in xs:
    #     for numYs in ys:
    #         new_Set.add(numXs * numYs)

    # return new_Set
    return set([
        numXs * numYs
        for numYs in ys
        for numXs in xs
    ])


def set_product58(xs, ys):
    """
    8: (Task 0.5.8) Double comprehension evaluating to five-element set
    Return a set containing the multiplicacion of every elment in a set multiplied by the other
    where elements dont repeat
    >>> set_product58({1,2,3},{3,4,5})
    set([3, 4, 5, 6, 8, 10, 12, 15])
    """
    # new_Set = set()
    # for numXs in xs:
    #     for numYs in ys :
    #         if(numXs != numYs):
    #             new_Set.add(numXs * numYs)

    # return new_Set
    return set([
        numXs * numYs
        for numYs in ys
        for numXs in xs
        if numXs != numYs
    ])

#////////


def intersection(Ss, Ts):
    """
    9: (Task 0.5.9) Set intersection as a comprehension
    >>> intersection({1, 2, 3, 4},{3, 4, 5, 6})
    set([3, 4])
    """
    return Ss & Ts


def list_average(list_of_numbers):
    """
    10: (Task 0.5.10) Average
    A one-line expression that evaluates to the average of list_of_numbers.
    Your expression should refer to the variable list_of_numbers, and should work
    for a list of any length greater than zero.

    >>> list_average([20, 10, 15, 75])
    30
    """
    return sum(list_of_numbers) / len(list_of_numbers)


def cartesian_product(Xs, Ys):
    """
    11: (Task 0.5.11) Cartesian-product comprehension
    a double list comprehension over {'A','B','C'} and {1,2,3}
    >>> cartesian_product(['A','B','C'],[1,2,3])
    [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
    """
    return [
        [x, y]
        for x in Xs
        for y in Ys
    ]


def LofL_sum(list_of_lists):
    """
    12: (Task 0.5.12) Sum of numbers in list of list of numbers
    a one-line expression of the form sum([sum(...) ... ]) that
    includes a comprehension and evaluates to the sum of all numbers in all the lists.

    >>> LofL_sum([[.25, .75, .1], [-1, 0], [4, 4, 4, 4]])
    16.1

    """
    return sum([
        sum(x)
        for x in list_of_lists
    ])


def zero_sum_list(list_of_numbers):
    """
    13: (Task 0.5.14) Three-element tuples summing to zero
    >>> zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2), (-2, 1, 1), (-2, 2, 0), (-2, 0, 2), (1, -2, 1), (1, 1, -2), (2, -4, 2), (2, -2, 0), (2, 2, -4), (2, 0, -2), (0, -2, 2), (0, 2, -2), (0, 0, 0)]
    """
    return [
        (x, y, z)
        for x in list_of_numbers
        for y in list_of_numbers
        for z in list_of_numbers
        if (x + y + z) == 0
    ]


def non_zero_sum_list(list_of_numbers):
    """
    Task 0.5.15: Modify the comprehension of the previous task so that the resulting list does
    not include (0, 0, 0). Hint: add a filter.
    >>> non_zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2), (-2, 1, 1), (-2, 2, 0), (-2, 0, 2), (1, -2, 1), (1, 1, -2), (2, -4, 2), (2, -2, 0), (2, 2, -4), (2, 0, -2), (0, -2, 2), (0, 2, -2)]
    """
    #ls = [(x, y, z) for x in list_of_numbers for y in list_of_numbers for z in list_of_numbers if (x + y + z) == 0]
    return filter(
        lambda (x, y, z): (x, y, z) != (0, 0, 0), [
            (x, y, z)
            for x in list_of_numbers
            for y in list_of_numbers
            for z in list_of_numbers
            if (x + y + z) == 0
        ])


def first_zero_sum_list(list_of_numbers):
    """
    16: (Task 0.5.16) first nontrivial three-element tuple summing to zero
    >>> first_zero_sum_list([-4, -2, 1, 2, 5, 0])
    [(-4, 2, 2)]
    """
    return [
        (x, y, z)
        for x in list_of_numbers
        for y in list_of_numbers
        for z in list_of_numbers
        if (x + y + z) == 0
    ][:1]


def is_element_repeated(things):
    """
    17: Task 0.5.17: Find an example of a list L such that len(L) and len(list(set(L))) are diferent."
    >>> is_element_repeated([1,1,2,3])
    True
    >>> is_element_repeated([1,2,3,4])
    False
    """
    return len(things) != len(list(set(things)))


def odd_num_list(n):
    """
    Task 0.5.18: Write a comprehension over a range of the form range(n) such that the
    value of the comprehension is the set of odd numbers from 1 to n.
    >>> odd_num_list(17)
    [1, 3, 5, 7, 9, 11, 13, 15]
    """
    return [
        x
        for x in range(17)
        if x % 2 != 0
    ]


def range_and_zip(letters):
    """
    (Task 0.5.19) Using range and zip
    >>> range_and_zip("ABCDE")
    [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

    Do not use a list comprehension use range and zip
    """
    return zip(range(len(letters)), letters)


def list_sum_zip(A, B):
    """
    (Task 0.5.20) Using zip to find elementwise sums
    A one-line comprehension that uses zip together with the variables A and B.
    The comprehension should evaluate to a list whose ith element is the ith element of
    A plus the ith element of B.
    >>> list_sum_zip([10,20,30],[1,2,3])
    [11, 22, 33]
    """
    return [
        i + j
        for i, j in zip(A, B)
    ]


def value_list(k, dlist):
    """
    (Task 0.5.21) Extracting the value corresponding to key k from each dictionary in a list
    >>> value_list('James',[{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}])
    ['Sean', 'Roger', 'Pierce']
    """
    return [
        dlist[x][k]
        for x in xrange(len(dlist))
    ]


def value_list_m(k, dlist):
    """
    Task 0.5.22: Modify the comprehension in Task 0.5.21 to handle the case
                 in which k might not appear in all the dictionaries.
                 The comprehension evaluates to the list whose ith element is
                 the value corresponding to key k in the i
    th dictionary in dlist if that dictionary
    contains that key, and 'NOT PRESENT' otherwise.
    >>> value_list_m('Bilbo',[{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Rich'}])
    ['Ian', 'Martin']
    >>> value_list_m('Frodo',[{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Rich'}])
    ['Elijah', 'NOT PRESENT']
    """
    return [
        'NOT PRESENT'
        for x in xrange(len(dlist))
        if (dlist[x].get(k) is None)
        else dlist[x][k]
    ]


def square_dict(n):
    """
    (Task 0.5.23) A dictionary mapping integers to their squares
    Replace {...} with a one-line dictionary comprehension
    >>> square_dict(10)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    """
    return {x: x ** 2 for x in xrange(n)}


# def dictionary_mapping(names, id2salaries):
    """
    (Task 0.5.26) A dictionary mapping names to salaries
    >>> dictionary_mapping(['Larry', 'Curly', 'Moe'],{0:100.0, 1:120.50, 2:99})
    {'Larry': 100.0, 'Moe': 99, 'Curly': 120.5}
    """
    return {map({names: id2salaries}, names, id2salaries)}


def nextInts(L):
    """
    Task 0.5.28: #Define a one-line procedure nextInts(L) specified as follows:
      input: list L of integers
      output: list of integers whose ith element is one more than the i
      th element of L
    >>> nextInts([1, 5, 7])
    [2, 6, 8]
    """
    return [
        x + 1
        for x in L
    ]


def cubes(L):
    """
    Task 0.5.29: #Define a one-line procedure cubes(L) specified as follows:
    - input: list L of numbers
    - output: list of numbers whose ith element is the cube
              of the ith element of L
    >>> cubes([1, 2, 3])
    [1, 8, 27]
    """
    return [
        x ** 3
        for x in L]


def dict2list(dct, keylist):
    """
    Task 0.5.30: #Define a one-line procedure
                 dict2list(dct,keylist) with this spec:
      input: dictionary dct, list keylist consisting of the keys of dct
      output: list L such that L[i] = dct[keylist[i]]
              for i = 0, 1, 2,..., len(keylist) % 1
    >>> dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a'])
    ['B', 'C', 'A']
    """
    return [
        dct.get(keylist[i])
        for i in range(len(keylist))]


def list2dict(L, keylist):
    """
    Task 0.5.31: #Define a one-line procedure list2dict(L, keylist)
                 specified as follows:
      input: list L, list keylist of immutable items
      output: dictionary that maps keylist[i] to L[i]
              for i = 0, 1, 2,..., len(L) % 1
    >>> list2dict(['A','B','C'],keylist=['a','b','c'])
    {'a':'A', 'b':'B', 'c':'C'}
    """
    return{
        keylist[i]: L[i]
        for i in xrange(len(keylist))
    }


if __name__ == '__main__':
    doctest.testmod()
