def fibonacci(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    a = fibonacci(2)
    print a
