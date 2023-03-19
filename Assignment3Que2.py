def string(str1):

    qwrd1 = ''
    index = len(str1)
    while index > 0:
        qwrd1 += str1[ index - 1 ]
        index = index - 1
    return qwrd1
print(string('1234abcd'))
