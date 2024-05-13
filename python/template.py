def implementation():
    return False


def test():
    expected = True
    actual = implementation()
    assert expected == actual, \
           f'expected {expected} but {actual} was received.'

if __name__ == '__main__':
    test()

