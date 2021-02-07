def cubeVol(length):
    if length > 0:
        return length ** 3
    else:
        raise Exception("Enter non-negative side length.")