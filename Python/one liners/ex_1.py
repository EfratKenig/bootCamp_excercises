import functools


def is_palindrome(s):
    return s == s[::-1]


def duplicate(s):
    return s * 2


def change_space(s):
    return s.replace(' ', '@')


def num_spaces(s):
    return s.count(' ')


def num_all_spaces(s):
    return len(list(filter(lambda x: (x == ' ' or x == '\t' or x == '\n'), s)))


def longest_word_lex(s):
    return max(word for word in s.split(" "))


def longest_word(s):
    return max([len(word) for word in s.replace('.', '').split(" ")])


def reverse_sentence(s):
    return s[::-1]


def reverse_word_order(s):
    return [word for word in s.split(" ")][::-1]


def reverse_words_in_sentence(s):
    return [word[::-1] for word in s.split(" ")]


# def swap_two_variables(a, b):
a, b = b, a


def sum_even_items(lst):
    return sum(lst[1::2])


def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n+1))
