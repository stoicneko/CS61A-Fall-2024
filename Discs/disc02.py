def is_even(x):  # Even numbers have remainder 0 when divided by 2.
    return x % 2 == 0


def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"

    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
        # return cond
        return

    # 这里不能返回keeper
    # 根据doctest可知该函数的操作只有print
    # 最后不返回任何值，若返回 keeper则原函数返回一个函数，这不是我们想要的
    # 错了错了 是不能返回cond 若keeper返回cond，后面又返回keeper 相当于返回cond函数
    return keeper


def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"

    # def digit(n):
    #     if k > 1:
    #         return n % pow(10, k) // pow(10, k - 1)
    #     else:
    #         return n % pow(10, k)
    #
    # return digit
    # 既然k-1 有可能等于0，那么如何规避这个问题呢
    # 使用k+1和k，但是这样原本的第k位就变成了第k+1位，怎么办呢
    # 让原本的x *  10就可以了,这样整体向左移一位
    # return lambda x: x * 10 % pow(10, k + 1) // pow(10, k)
    return lambda x: x * 10 % 10 ** (k + 1) // 10**k


def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """

    def check(x):
        while x // (10**k) > 0:
            if x % 10 != x % 10 ** (k + 1) // 10**k:
                return False
            x //= 10
        return True

    return check
