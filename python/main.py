
def flawed(A):
    my_max = 0
    for v in A:
        if my_max < v:
            my_max = v
    return my_max


