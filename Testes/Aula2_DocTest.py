def soma(x, y):
    '''Soma x e y

    >>> soma(10,20)
    30
    >>> soma(-10,20)
    10
    >>> soma(5,-5)
    0
    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser inteiro ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser inteiro ou float'
    assert isinstance(y, (int, float)), 'y precisa ser inteiro ou float'
    return x + y


def subtrai(x, y):
    '''Subtração x - y
    >>> subtrai(10,5)
    5
    >>> subtrai('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser inteiro ou float
    '''
    assert isinstance(x, (int, float)), 'x precisa ser inteiro ou float'
    assert isinstance(y, (int, float)), 'y precisa ser inteiro ou float'
    return x - y


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)