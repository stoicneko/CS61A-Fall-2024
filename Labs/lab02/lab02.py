def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"

    def compose(f, g):
        return lambda x: f(g(x))

    F = compose(f, g)
    G = compose(g, f)

    def identity(x):
        if F(x) == G(x):
            return True
        else:
            return False

    return identity


def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total


def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"

    def wrapped_condition(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count

    return wrapped_condition


def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"

    def fd_common_factor(a, b):
        n = min(a, b)
        i = 2
        while i <= n:
            if a % i == 0 and b % i == 0:
                return True
            i += 1
        return False

    if not fd_common_factor(a, b):
        return a * b
    else:
        n = max(a, b)
        while True:
            n += 1
            if n % a == 0 and n % b == 0:
                return n


# 这道题的官方解法更暴力，根本不用找什么公因数
# 找公因数和直接一个一个试最小公倍数时间复杂度一样的?


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    """
    my_cycle(n)(x)

    if n == 3 f3(x)
    if n == 2 f2(x)
    """
    # def make_repeater(f, n):
    #     if n > 0:
    #         def compose(f, g):
    #             return lambda x: f(g(x))
    #         return compose(f, make_repeater(f, n-1))
    #     else:
    #         return f
    #
    #

    # def my_cycle(n):
    # def f(x):
    #     if x == 1:
    #         return lambda y: f1(y)
    #     elif x == 2:
    #         return lambda y: f2(y)
    #     else:
    #         return lambda y: f3(y)
    #
    # def solution_1(x):
    #     k = 1
    #     while k <= n:  # 当n==0时不执行这个循环语句直接return x
    #         if k % 3 == 1:
    #             x, k = (lambda y: f1(y))(x), k + 1
    #         elif k % 3 == 2:
    #             x, k = (lambda y: f2(y))(x), k + 1
    #         else:
    #             x, k = (lambda y: f3(y))(x), k + 1
    #     return x
    # return solution_1
    # 看了一下官方解法似乎逻辑不太一样
    # 一样的一样的，只是官方解法k/i 是从0开始的
    # solution 2
    # def solution_2(x):
    #     k = 1
    #     while k <= n:  # 当n==0时不执行这个循环语句直接return x
    #         if k % 3 == 1:
    #             x = (lambda y: f1(y))(x)
    #         if k % 3 == 2:
    #             x = (lambda y: f2(y))(x)
    #         if k % 3 == 3:
    #             x = (lambda y: f3(y))(x)
    #         k += 1
    #     return x
    # return solution_2

    # 这里还是只判断一次更好，即用if-elif-else
    # 三个if 会让这个数判断三次，虽然这道题3个if条件互斥，但其他题可就不一定。根据逻辑来这个数只判断一次
    # def solution_3(n):
    #     def h(x):  # 定义一个新的h(x)函数，返回f1(x)....
    #         i = 0
    #         while i < n:
    #             if i % 3 == 0:
    #                 x = f1(x)
    #             elif i % 3 == 1:
    #                 x = f2(x)
    #             else:
    #                 x = f3(x)
    #             i += 1
    #         return x
    #
    #     return h
    #
    def recuisive_solv(n):
        def h(x):
            if n == 0:
                return x
            return cycle(f2, f3, f1)(n - 1)(f1(x))

        # 为什么是n -1 呢，
        return h

    return recuisive_solv
