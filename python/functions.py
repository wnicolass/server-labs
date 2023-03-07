################################
#
#           PYTHON
#
###############################

# concat('abc', 'def') => 'abcdef'
# concat('abc', 23, True, ['alberto', 19]) => "abc23True['alberto', 19]"
# concat('abc', 'def', sep='/', end='.') => 'abc/def.'

# concat
from typing import Iterable


def concat(*args, sep="", end="") -> str:
    items_str = []
    for arg in args:
        items_str.append(str(arg))
    items_str.append(end)
    return sep.join(items_str)

# concat(['abc', 'def'])
# concat(('abc', 'def'))

# args
def fun1(a, b, *args, c):
    print(a)
    print(b)
    print(args)
    print(c)

# fun1(2, 3)
# fun1(2, 3, 4, 5, c = 6)

def fun3(a, b, *args, c = 78, d = 90, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

# fun3(1, 2, 3, 4, 5, d = 12, e = 900, xpto = 'alberto')

# function that can be used between two other functions
def fun4(*args, **kargs):
    print(args)
    print(kargs)

############################################
#
#    FUNÇÕES DE PRIMEIRA ORDEM
# funções parametrizadas com outras funções
#
############################################
nums = [100, -2, -1, 59, 44, 46, 77]
names = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

# lists, tuples, dicts -> iterable
def filter_positives(items: Iterable) -> list:
    selected = []
    for item in items:
        if item > 0:
            selected.append(item)
    return selected
#:

def filter_even(items: Iterable) -> list:
    selected = []
    for item in items:
        if item % 2 == 0:
            selected.append(item)
    return selected
#:

def filter_gt_fifty(items: Iterable) -> list:
    selected = []
    for item in items:
        if item > 50:
            selected.append(item)
    return selected
#:

def filter_len_gt_6(items: Iterable) -> list:
    selected = []
    for item in items:
        if len(item) > 6:
            selected.append(item)
    return selected
#:

def filter_generic(items: Iterable, criteria) -> list:
    selected = []
    for item in items:
        if criteria(item):
            selected.append(item)
    return selected
#:

def is_positive(num: int) -> bool:
    return num > 0
#:

def is_even(num: int) -> bool:
    return num % 2 == 0
#:

def len_gt_six(elem) -> bool:
    return len(elem) > 6
#:

filter_generic(nums, is_even)
filter_generic(names, len_gt_six)
filter_generic(nums, is_positive)
filter_generic(nums, lambda num: num % 2 == 0)

dim = int(input("Length?: "))
filter_generic(names, lambda name: len(name) > dim)

# MAP

def mapp(items: Iterable, mapping) -> list:
    changed = []
    for item in items:
        changed.append(mapping(item))
    #:
    return changed
#:

def double(num: int | float) -> float:
    return 2.0 * num
#:

mapp(nums, double)
mapp(nums, lambda num: num * 2)
mapp(names, lambda name: name[0]) # first char
mapp(names, lambda name: name[-1]) # last char
mapp(names, len)

# built-in functions: map, filter, sorted

list(filter(lambda num: num > 0, nums))
tuple(map(lambda num: num * 2, nums))

# 3 first letters of the names with more than 6 chars
map(lambda name: name[:3], filter(lambda name: len(name) > 6, names))

more_than_six = filter(lambda name: len(name) > 6, names)
map(lambda name: name[:3], more_than_six)

# SORTED

nums = [100, -2, -1, 59, 44, 46, 77, 1000000, 10, 440, -7003]

# order by asc, with < operator
sorted(nums)
sorted(nums, key = lambda num: str(abs(num))[0])

# order by asc, through a string last character
sorted(names, key = lambda name: name[-1])

# order by desc
sorted(names, reverse=True)

############################################
#
#    LIST EXPRESSIONS
# Alternativa mais idiomática a MAP & FILTER
#
############################################

# list(map(lambda x: 2 * x, nums))
# list(filter(lambda x: x > 0, nums))
# list(map(lambda x: 2 * x, filter(lambda x: x > 0, nums)))

[2 * num for num in nums]
[x for x in nums if x > 0]
[2 * num for num in nums if num > 0]
