def fullName(first, last):
    if len(first) > 0 and len(last) > 0:
        return first + " " + last
    else:
        raise Exception("Enter both first and last names.")