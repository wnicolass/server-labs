################################
#
#           PYTHON
#
###############################

# concat('abc', 'def') => 'abcdef'
# concat('abc', 23, True, ['alberto', 19]) => "abc23True['alberto', 19]"
# concat('abc', 'def', sep='/', end='.') => 'abc/def.'

# concat
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
